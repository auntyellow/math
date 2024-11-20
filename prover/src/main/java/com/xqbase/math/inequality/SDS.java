package com.xqbase.math.inequality;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.MutableNumber;
import com.xqbase.math.polys.Poly;

/**
 * Successive Difference Substitution<p>
 * @see https://arxiv.org/pdf/0904.4030v3.pdf
 */
public class SDS {
	private static Logger log = LoggerFactory.getLogger(SDS.class);

	private static final int[][] MATRIX_H = {{2, 1, 1}, {0, 1, 0}, {0, 0, 1}};
	private static final int[][] MATRIX_H4 = {{1, 1, 0}, {0, 1, 1}, {1, 0, 1}};
	// this also works with tempVars
	// private static final int[][] MATRIX_H4 = {{0, 1, 1}, {1, 0, 1}, {1, 1, 0}};
	private static final int[][][] MATRIX_J = {
		{{2, 1, 1, 1}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}},
		{{1, 1, 1, 0}, {1, 0, 0, 1}, {0, 1, 0, 1}, {0, 0, 1, 0}},
	};

	/** @see http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 */
	public static enum Transform {
		A_n, T_n, H_3, J_4, Z_n,
		/** n vertex + 1 center, less overlapped than {@link #Z_n} */
		Y_n
	}

	public static enum Find {
		SKIP, FAST, FULL, DUMP_LATTICE
	}

	private static <T> List<T> asList(Collection<T> c) {
		return c instanceof List ? (List<T>) c : new ArrayList<>(c);
	}

	static final <T> Comparator<Collection<T>> listComparator(Comparator<T> comparator) {
		return (o1, o2) -> {
			int len1 = o1.size();
			int len2 = o2.size();
			int len = Integer.min(len1, len2);
			List<T> list1 = asList(o1);
			List<T> list2 = asList(o2);
			for (int i = 0; i < len; i ++) {
				int c = comparator.compare(list1.get(i), list2.get(i));
				if (c != 0) {
					return c;
				}
			}
			return Integer.compare(len1, len2);
		};
	}

	public static class Result<T extends MutableNumber<T>> {
		List<T> negativeAt = null;
		TreeSet<List<T>> zeroAt;
		List<Set<Set<List<T>>>> simplices;
		int depth = 0;

		Result() {
			zeroAt = new TreeSet<>(listComparator(Comparator.<T>naturalOrder()));
			simplices = new ArrayList<>();
		}

		public boolean isNonNegative() {
			return negativeAt == null;
		}

		public List<T> getNegativeAt() {
			return negativeAt;
		}

		public Set<List<T>> getZeroAt() {
			return zeroAt;
		}

		public List<Set<Set<List<T>>>> getSimplices() {
			return simplices;
		}

		public int getDepth() {
			return depth;
		}

		@Override
		public String toString() {
			return "SDSResult [nonNegative=" + isNonNegative() + ", negativeAt=" + negativeAt +
					", zeroAt=" + zeroAt + ", simplices=" + simplices + ", depth=" + depth + "]";
		}
	}

	static class PermSubs<T extends MutableNumber<T>, U extends Poly<T, U>> {
		int[] perm;
		U[] subs;
		boolean tempVars = false;
		boolean reverse = false;
		int index;
	}

	private static final Integer[] EMPTY_INTS = new Integer[0];

	private static List<List<Integer>> permutations(Set<Integer> nums) {
		List<List<Integer>> result = new ArrayList<>();
		if (nums.size() == 1) {
			for (Integer i : nums) {
				result.add(Collections.singletonList(i));
			}
			return result;
		}
		for (Integer num : nums.toArray(EMPTY_INTS)) {
			nums.remove(num);
			List<List<Integer>> subResult = permutations(nums);
			nums.add(num);
			for (List<Integer> subList : subResult) {
				List<Integer> list = new ArrayList<>();
				list.add(num);
				list.addAll(subList);
				result.add(list);
			}
		}
		return result;
	}

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> T[] matMul(T[][] m, T[] v, P p) {
		int n = m.length;
		T[] v1 = p.newVector(n);
		for (int i = 0; i < n; i ++) {
			T vi = p.newZero();
			for (int j = 0; j < n; j ++) {
				vi.addMul(m[i][j], v[j]);
			}
			v1[i] = vi;
		}
		return v1;
	}

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> List<T>
			matMulReduce(List<Integer> trans, List<T[][]> transMat, boolean[] key, P f) {
		int n = key.length;
		T[] v = f.newVector(n);
		for (int i = 0; i < n; i ++) {
			v[i] = f.valueOf(key[i] ? 1 : 0);
		}
		for (int i = trans.size() - 1; i >= 0; i --) {
			v = matMul(transMat.get(trans.get(i).intValue()), v, f);
		}
		T gcd = f.valueOf(0);
		for (int i = 0; i < n; i ++) {
			gcd = gcd.gcd(v[i]);
		}
		List<T> value = new ArrayList<>();
		for (int i = 0; i < n; i ++) {
			value.add(v[i].div(gcd));
		}
		return value;
	}

	/**
	 * find negative and zeros, then return if trivially non-negative
	 *
	 * @param transList skip finding negative if empty
	 */
	private static <T extends MutableNumber<T>, P extends Poly<T, P>> boolean trivial(P f,
			List<List<Integer>> transList, List<T[][]> transMat, List<boolean[]> keys, Result<T> result, boolean dumpLattice) {
		if (!transList.isEmpty()) {
			int numKeys = keys.size();
			if (dumpLattice) {
				Set<Set<List<T>>> simplices = result.simplices.get(result.depth);
				for (List<Integer> trans : transList) {
					Set<List<T>> simplex = new TreeSet<>(result.zeroAt.comparator());
					for (int i = 0; i < numKeys; i ++) {
						List<T> lattice = matMulReduce(trans, transMat, keys.get(i), f);
						result.zeroAt.add(lattice);
						simplex.add(lattice);
					}
					simplices.add(simplex);
				}
			} else {
				// find negative and zeros: try 0(false)/1(true)s in keys
				List<T> values = new ArrayList<>();
				for (int i = 0; i < numKeys; i ++) {
					values.add(f.newZero());
				}
				for (Map.Entry<Monom, T> entry : f.entrySet()) {
					short[] exps = entry.getKey().getExps();
					T coeff = entry.getValue();
					for (int i = 0; i < numKeys; i ++) {
						T value = values.get(i);
						boolean[] key = keys.get(i);
						boolean zero = false;
						for (int j = 0; j < key.length; j ++) {
							if (!key[j] && exps[j] > 0) {
								zero = true;
								break;
							}
						}
						if (!zero) {
							value.add(coeff);
						}
					}
				}
				for (int i = 0; i < numKeys; i ++) {
					T value = values.get(i);
					int c = value.signum();
					if (c < 0) {
						result.negativeAt = matMulReduce(transList.get(0), transMat, keys.get(i), f);
						return false;
					}
					if (c == 0) {
						for (List<Integer> trans : transList) {
							result.zeroAt.add(matMulReduce(trans, transMat, keys.get(i), f));
						}
					}
				}
			}
		}
		for (T coeff : f.values()) {
			if (coeff.signum() < 0) {
				return false;
			}
		}
		return true;
	}

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> void copy(int[] src, T[] dst, P f) {
		for (int i = 0; i < src.length; i ++) {
			dst[i] = f.valueOf(src[i]);
		}
	}

	@SuppressWarnings("unchecked")
	private static <T extends MutableNumber<T>, P extends Poly<T, P>> P[]
			unchecked(@SuppressWarnings("rawtypes") Poly[] polys) {
		return (P[]) polys;
	}

	private static Monom getMonom(int len, int i) {
		short[] exps = new short[len];
		Arrays.fill(exps, (short) 0);
		exps[i] = 1;
		return new Monom(exps);
	}

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> P[]
			getSubsPoly(int[][] mat, P f) {
		int len = mat.length;
		// build substitution polynomials from transformation matrix
		P[] subs = unchecked(new Poly[len]);
		Monom[] monoms = new Monom[len];
		for (int i = 0; i < len; i ++) {
			monoms[i] = getMonom(len*2, len + i);
		}
		for (int i = 0; i < len; i ++) {
			P p = f.newPoly();
			for (int j = 0; j < len; j ++) {
				long c = mat[i][j];
				if (c != 0) {
					p.put(monoms[j], f.valueOf(c));
				}
			}
			subs[i] = p;
		}
		return subs;
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> Result<T> sds(P f) {
		return sds(f, Transform.A_n);
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> Result<T> sds(P f,
			Transform transform) {
		return sds(f, transform, Find.FULL);
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> Result<T> sds(P f,
			Transform transform, Find find) {
		return sds(f, transform, find, Integer.MAX_VALUE);
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> Result<T> sds(P f,
			Transform transform, Find find, int maxDepth) {
		// check homogeneous
		int deg = 0;
		for (Monom m : f.keySet()) {
			int exps = 0;
			for (int exp : m.getExps()) {
				exps += exp;
			}
			if (deg == 0) {
				deg = exps;
			} else if (deg != exps) {
				throw new IllegalArgumentException(f + " is not homogeneous");
			}
		}
		if (deg == 0) {
			return new Result<>();
		}
		int len = f.getVars().size();
		Monom[] monoms = new Monom[len];
		for (int i = 0; i < len; i ++) {
			monoms[i] = getMonom(len, i);
		}

		// product([false, true], repeat = len)
		List<boolean[]> keys;
		if (find == Find.DUMP_LATTICE) {
			keys = new ArrayList<>();
			for (int i = 0; i < len; i ++) {
				boolean[] key = new boolean[len];
				for (int j = 0; j < len; j ++) {
					key[j] = i == j;
				}
				keys.add(key);
			}
		} else {
			keys = Collections.singletonList(new boolean[len]);
			for (int i = 0; i < len; i ++) {
				List<boolean[]> keys1 = new ArrayList<>();
				if (find == Find.FULL) {
					for (boolean[] key : keys) {
						boolean[] key1 = key.clone();
						key1[i] = false;
						keys1.add(key1);
					}
				}
				for (boolean[] key : keys) {
					boolean[] key1 = key.clone();
					key1[i] = true;
					keys1.add(key1);
				}
				keys = keys1;
			}
			if (find == Find.FULL) {
				// remove first trivial zeros
				keys.remove(0);
			}
		}

		// depth = 0
		Result<T> result = new Result<>();
		@SuppressWarnings("unchecked")
		Comparator<Collection<List<T>>> comparator =
				listComparator((Comparator<List<T>>) result.zeroAt.comparator());
		result.simplices.add(new TreeSet<>(comparator));
		// transList is always empty if skipNegative
		List<List<Integer>> initTransList = find == Find.SKIP ? Collections.emptyList() :
				Collections.singletonList(Collections.emptyList());
		if (trivial(f, initTransList, Collections.emptyList(), keys, result,
				find == Find.DUMP_LATTICE) || result.negativeAt != null) {
			return result;
		}

		ArrayList<PermSubs<T, P>> permSubsList = new ArrayList<>();
		ArrayList<T[][]> transMat = new ArrayList<>();
		T zero = f.valueOf(0);
		T one = f.valueOf(1);
		switch (transform) {
		case A_n:
		case T_n:
		default:
			// A_n: [1, ..., 1], T_n: [lcm, lcm/2, ..., lcm/n]
			T[] column = f.newVector(len);
			if (transform == Transform.T_n) {
				T lcm = one;
				for (int i = 1; i <= len; i ++) {
					T i_ = f.valueOf(i);
					T t = f.newZero();
					t.addMul(lcm, i_);
					lcm = t.div(lcm.gcd(i_));
				}
				for (int i = 0; i < len; i ++) {
					column[i] = lcm.div(f.valueOf(i + 1));
				}
			} else {
				for (int i = 0; i < len; i ++) {
					column[i] = one;
				}
			}

			T[][] upperMat = f.newMatrix(len, len);
			for (int i = 0; i < len; i ++) {
				for (int j = 0; j < len; j ++) {
					upperMat[i][j] = i <= j ? column[j] : zero;
				}
			}

			P[] subs = unchecked(new Poly[transform == Transform.T_n ? len : len - 1]);
			for (int i = 0; i < len - 1; i ++) {
				P sub = f.newPoly();
				sub.put(monoms[i], column[i]);
				sub.put(monoms[i + 1], one);
				subs[i] = sub;
			}
			if (transform == Transform.T_n) {
				P sub = f.newPoly();
				sub.put(monoms[len - 1], column[len - 1]);
				subs[len - 1] = sub;
			}

			Set<Integer> varSeq = new TreeSet<>();
			for (int i = 0; i < len; i ++) {
				varSeq.add(Integer.valueOf(i));
			}
			for (List<Integer> perm : permutations(varSeq)) {
				T[][] m = f.newMatrix(len, len);
				for (int i = 0; i < len; i ++) {
					// permute
					m[i] = upperMat[perm.get(i).intValue()].clone();
					// m[perm.get(i).intValue()] = upperMat[i].clone();
				}
				PermSubs<T, P> permSubs = new PermSubs<>();
				permSubs.perm = perm.stream().mapToInt(Integer::intValue).toArray();
				permSubs.subs = subs;
				permSubs.index = transMat.size();
				transMat.add(m);
				permSubsList.add(permSubs);
			}
			break;

		case H_3:
			if (len != 3) {
				throw new IllegalArgumentException("H_3 only works on 3-var polynomials");
			}
			List<String> xyz = Arrays.asList("x", "y", "z");
			subs = unchecked(new Poly[] {f.newPoly(xyz, "2*x + y + z")});
			for (int i = 0; i < 3; i ++) {
				PermSubs<T, P> permSubs = new PermSubs<>();
				permSubs.perm = new int[] {i, (i + 1)%3, (i + 2)%3};
				permSubs.subs = subs;
				permSubs.index = transMat.size();
				T[][] m = f.newMatrix(3, 3);
				for (int j = 0; j < 3; j ++) {
					// permute
					copy(MATRIX_H[(i + j)%3], m[j], f);
					// copy(MATRIX_H[j], m[(i + j)%3], f);
				}
				transMat.add(m);
				permSubsList.add(permSubs);
			}
			PermSubs<T, P> permSubsH = new PermSubs<>();
			permSubsH.perm = new int[] {0, 1, 2};
			// x' = x + y, y' = y + z, z' = x + z
			// doesn't work for MATRIX_H4 = {{0, 1, 1}, {1, 0, 1}, {1, 1, 0}}
			permSubsH.subs = unchecked(new Poly[] {
				f.newPoly(xyz, "2*x + y - z"),
				f.newPoly(xyz, "y + z - x"),
				f.newPoly(xyz, "z + x"),
			});
			// also works for MATRIX_H4 = {{0, 1, 1}, {1, 0, 1}, {1, 1, 0}}
			// permSubsH.subs = getSubsPoly(MATRIX_H4, f);
			permSubsH.index = transMat.size();
			T[][] m = f.newMatrix(3, 3);
			for (int i = 0; i < 3; i ++) {
				copy(MATRIX_H4[i], m[i], f);
			}
			transMat.add(m);
			permSubsList.add(permSubsH);
			break;

		case J_4:
			if (len != 4) {
				throw new IllegalArgumentException("J_4 only works on 4-var polynomials");
			}
			@SuppressWarnings("unchecked")
			P[][] subsJ = (P[][]) new Poly[][] {
				{ f.newPoly("2*x + y + z + w", "x", "y", "z", "w") },
				// Unable to substitute by x_i = p1(x_i, y_i, z_i, w), y = p2(x, y, z, w) ...
				// so use tempVars for J[1]
				getSubsPoly(MATRIX_J[1], f),
			};
			for (int i = 0; i < 2; i ++) {
				for (int j = 0; j < 4; j ++) {
					PermSubs<T, P> permSubs = new PermSubs<>();
					permSubs.perm = new int[] {j, (j + 1)%4, (j + 2)%4, (j + 3)%4};
					permSubs.subs = subsJ[i];
					permSubs.tempVars = i > 0;
					permSubs.index = transMat.size();
					m = f.newMatrix(4, 4);
					for (int k = 0; k < 4; k ++) {
						// permute
						copy(MATRIX_J[i][(j + k)%4], m[k], f);
						// copy(MATRIX_J[i][k], m[(j + k)%4], f);
					}
					transMat.add(m);
					permSubsList.add(permSubs);
				}
			}
			break;

		case Z_n:
		case Y_n:
			/*
			int[][] MATRIX_Z = {
				{n,   1,   1, ...,   1},
				{0, n-1,   0, ...,   0},
				{0,   0, n-1, ...,   0},
				...
				{0,   0,   0, ..., n-1},
			};

			int[][] MATRIX_Y = {
				{n-1, 1, 1, ..., 1},
				{0, n-2, 0, ..., 0},
				{0, 0, n-2, ..., 0},
				...
				{0, 0, 0, ..., n-2},
			};
			*/
			T[][] zMat = f.newMatrix(len, len);
			int lead_ = transform == Transform.Z_n ? len : len - 1;
			T lead = f.valueOf(lead_);
			T diag = f.valueOf(lead_ - 1);
			zMat[0][0] = lead;
			for (int i = 1; i < len; i ++) {
				zMat[0][i] = one;
				for (int j = 0; j < len; j ++) {
					zMat[i][j] = i == j ? diag : zero;
				}
			}

			subs = unchecked(new Poly[len]);
			P sub0 = f.newPoly();
			sub0.put(monoms[0], lead);
			for (int i = 1; i < len; i ++) {
				sub0.put(monoms[i], one);
				P sub = f.newPoly();
				sub.put(monoms[i], diag);
				subs[i] = sub;
			}
			subs[0] = sub0;

			for (int i = 0; i < len; i ++) {
				PermSubs<T, P> permSubs = new PermSubs<>();
				permSubs.perm = new int[len];
				for (int j = 0; j < len; j ++) {
					permSubs.perm[j] = (i + j)%len;
				}
				permSubs.subs = subs;
				permSubs.reverse = true;
				permSubs.index = transMat.size();
				m = f.newMatrix(len, len);
				for (int j = 0; j < len; j ++) {
					// permute
					m[j] = zMat[(i + j)%len].clone();
					// m[(i + j)%len] = zMat[j].clone();
				}
				transMat.add(m);
				permSubsList.add(permSubs);
			}
			if (transform == Transform.Z_n) {
				break;
			}

			/*
			int[][] MATRIX_Y2 = {
				{0, 1, 1, ..., 1},
				{1, 0, 1, ..., 1},
				{1, 1, 0, ..., 1},
				...
				{1, 1, 1, ..., 0},
			};
			*/
			int[][] yMat = new int[len][len];
			for (int i = 0; i < len; i ++) {
				for (int j = 0; j < len; j ++) {
					yMat[i][j] = i == j ? 0 : 1;
				}
			}
			PermSubs<T, P> permSubs = new PermSubs<>();
			permSubs.perm = new int[len];
			for (int i = 0; i < len; i ++) {
				permSubs.perm[i] = i;
			}
			permSubs.subs = getSubsPoly(yMat, f);
			permSubs.tempVars = true;
			permSubs.index = transMat.size();
			m = f.newMatrix(len, len);
			for (int i = 0; i < len; i ++) {
				copy(yMat[i], m[i], f);
			}
			transMat.add(m);
			permSubsList.add(permSubs);
			break;
		}

		Map<P, List<List<Integer>>> polyTransList = Collections.singletonMap(f, initTransList);
		for (result.depth = 1; result.depth < maxDepth; result.depth ++) {
			log.debug("depth = " + result.depth + ", polynomials = " + polyTransList.size());
			result.simplices.add(new TreeSet<>(comparator));
			int traceCurr = 0, traceTrans = 0;
			HashMap<P, List<List<Integer>>> polyTransList1 = new HashMap<>();
			for (Map.Entry<P, List<List<Integer>>> transEntry : polyTransList.entrySet()) {
				traceCurr ++;
				log.trace("depth = " + result.depth + ", polynomial: " + traceCurr + "/" + polyTransList.size());

				P f0 = transEntry.getKey();
				List<List<Integer>> transList = transEntry.getValue();
				for (PermSubs<T, P> permSubs : permSubsList) {
					// f1 = f0's permutation and substitution (transformation)
					P f1 = f.newPoly();
					if (permSubs.tempVars) {
						int len2 = len*2;
						// temp poly (2n-vars)
						P f2 = f.newPoly();
						// copy 0..n-1
						for (Map.Entry<Monom, T> term : f0.entrySet()) {
							short[] exps = term.getKey().getExps();
							short[] exps1 = new short[len2];
							Arrays.fill(exps1, len, len2, (short) 0);
							for (int i = 0; i < len; i ++) {
								// permute
								exps1[permSubs.perm[i]] = exps[i];
								// exps1[i] = exps[permSubs.perm[i]];
							}
							f2.put(new Monom(exps1), term.getValue());
						}
						// substitute 0..n-1 with n..2n-1
						for (int i = 0; i < permSubs.subs.length; i ++) {
							f2 = f2.subs(i, permSubs.subs[i]);
						}
						// copy and truncate n..2n-1
						for (Map.Entry<Monom, T> term : f2.entrySet()) {
							f1.put(new Monom(Arrays.copyOfRange(term.getKey().getExps(), len, len2)),
									term.getValue());
						}
					} else {
						for (Map.Entry<Monom, T> term : f0.entrySet()) {
							short[] exps = term.getKey().getExps();
							short[] exps1 = new short[len];
							for (int i = 0; i < len; i ++) {
								// permute
								exps1[permSubs.perm[i]] = exps[i];
								// exps1[i] = exps[permSubs.perm[i]];
							}
							f1.put(new Monom(exps1), term.getValue());
						}
						if (permSubs.reverse) {
							// Z_n
							for (int i = permSubs.subs.length - 1; i >= 0; i --) {
								f1 = f1.subs(i, permSubs.subs[i]);
							}
						} else {
							// A_n: x0 += x1, x1 += x2, ... , x_n-2 += x_n-1
							// T_n: x_i = x_i/(i + 1) + x_i+1, x_n-1 = x_i/n
							for (int i = 0; i < permSubs.subs.length; i ++) {
								f1 = f1.subs(i, permSubs.subs[i]);
							}
						}
					}
					List<List<Integer>> transList1 = new ArrayList<>();
					for (List<Integer> trans : transList) {
						List<Integer> trans1 = new ArrayList<>(trans);
						trans1.add(Integer.valueOf(permSubs.index));
						transList1.add(trans1);
					}
					// find negative and zeros, then skip trivial
					if (trivial(f1, transList1, transMat, keys, result, find == Find.DUMP_LATTICE)) {
						continue;
					}
					// terminate if find negative
					if (result.negativeAt != null) {
						return result;
					}
					// update next polyTransList
					polyTransList1.computeIfAbsent(f1, k -> new ArrayList<>()).addAll(transList1);

					traceTrans += transList1.size();
					log.trace("after depth = " + result.depth + ": polynomials = " +
							polyTransList1.size() + ", tranformations = " + traceTrans);
				}
			}
			if (polyTransList1.isEmpty()) {
				return result;
			}
			polyTransList = polyTransList1;
		}
		return result;
	}
}