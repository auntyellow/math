package com.xqbase.math.inequality;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.MutableNumber;
import com.xqbase.math.polys.Poly;

/**
 * Successive Difference Substitution<p>
 * {@link #sds(Poly f)} or sds(f, {@link Transform#A_n}) uses upper triangular matrix (A_n)<p>
 * {@link #tsds(Poly f)} or sds(f, {@link Transform#T_n}) uses column stochastic matrix (T_n)<p> 
 * @see https://arxiv.org/pdf/0904.4030v3.pdf
 */
public class SDS {
	private static Logger log = LoggerFactory.getLogger(SDS.class);

	public static enum Find {
		SKIP, FAST, FULL, DUMP_LATTICE
	}

	/** @see http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545 */
	public static enum Transform {
		A_n, T_n, H_n, J_n, Z_n
	}

	public static class Result<T extends MutableNumber<T>> {
		Set<List<T>> zeroAt;
		List<T> negativeAt = null;
		int depth = 0;

		Result(int len) {
			zeroAt = new TreeSet<>((p1, p2) -> {
				for (int i = 0; i < len; i ++) {
					int c = p1.get(i).compareTo(p2.get(i));
					if (c != 0) {
						return c;
					}
				}
				return 0;
			});
		}

		public boolean isNonNegative() {
			return negativeAt == null;
		}

		public Set<List<T>> getZeroAt() {
			return zeroAt;
		}

		public List<T> getNegativeAt() {
			return negativeAt;
		}

		public int getDepth() {
			return depth;
		}

		@Override
		public String toString() {
			return "SDSResult [nonNegative=" + isNonNegative() + ", zeroAt=" + zeroAt +
					", negativeAt=" + negativeAt + ", depth = " + depth + "]";
		}
	}

	static class PermSubs<T extends MutableNumber<T>> {
		List<Integer> perm;
		Poly<T>[] subs;
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

	private static <T extends MutableNumber<T>> T[] matMul(T[][] m, T[] v, Poly<T> p) {
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

	private static <T extends MutableNumber<T>> List<T> matMulReduce(List<Integer> trans,
			List<T[][]> transMat, boolean[] key, Poly<T> p) {
		int n = key.length;
		T[] v = p.newVector(n);
		for (int i = 0; i < n; i ++) {
			v[i] = p.valueOf(key[i] ? 1 : 0);
		}
		for (int i = trans.size() - 1; i >= 0; i --) {
			v = matMul(transMat.get(trans.get(i).intValue()), v, p);
		}
		T gcd = p.valueOf(0);
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
	private static <T extends MutableNumber<T>> boolean trivial(Poly<T> f, List<List<Integer>> transList,
			List<T[][]> transMat, List<boolean[]> keys, Result<T> result, boolean dumpLattice) {
		if (!transList.isEmpty()) {
			// find negative and zeros: try 0(false)/1(true)s in keys
			int numKeys = keys.size();
			List<T> values = new ArrayList<>();
			for (int i = 0; i < numKeys; i ++) {
				values.add(f.newZero());
			}
			for (Map.Entry<Mono, T> entry: f.entrySet()) {
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
				if (!dumpLattice && c < 0) {
					result.negativeAt = matMulReduce(transList.get(0), transMat, keys.get(i), f);
					return false;
				}
				if (dumpLattice || c == 0) {
					for (List<Integer> trans : transList) {
						result.zeroAt.add(matMulReduce(trans, transMat, keys.get(i), f));
					}
				}
			}
		}
		if (dumpLattice) {
			return false;
		}
		for (T coeff : f.values()) {
			if (coeff.signum() < 0) {
				return false;
			}
		}
		return true;
	}

	private static List<Integer> makePerm(int... values) {
		return IntStream.of(values).boxed().collect(Collectors.toList());
	}

	private static <T extends MutableNumber<T>> void copy(T[] src, long[] dst, Poly<T> p) {
		for (int i = 0; i < src.length; i ++) {
			src[i] = p.valueOf(dst[i]);
		}
	}

	public static <T extends MutableNumber<T>> Result<T> sds(Poly<T> f) {
		return sds(f, Transform.A_n, Find.FULL, Integer.MAX_VALUE);
	}

	public static <T extends MutableNumber<T>> Result<T> tsds(Poly<T> f) {
		return sds(f, Transform.T_n, Find.FULL, Integer.MAX_VALUE);
	}

	public static <T extends MutableNumber<T>> Result<T> sds(Poly<T> f,
			Transform transform, Find find, int maxDepth) {
		// check homogeneous
		int deg = 0;
		String vars = "";
		for (Mono m : f.keySet()) {
			int exps = 0;
			for (int exp : m.getExps()) {
				exps += exp;
			}
			if (deg == 0) {
				deg = exps;
				vars = m.getVars();
			} else if (deg != exps) {
				throw new IllegalArgumentException(f + " is not homogeneous");
			}
		}
		if (deg == 0) {
			return new Result<>(0);
		}
		int len = vars.length();

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
		Result<T> result = new Result<>(len);
		// transList is always empty if skipNegative
		List<List<Integer>> initTransList = find == Find.SKIP ? Collections.emptyList() :
				Collections.singletonList(Collections.emptyList());
		if (trivial(f, initTransList, Collections.emptyList(), keys, result,
				find == Find.DUMP_LATTICE) || result.negativeAt != null) {
			return result;
		}

		ArrayList<PermSubs<T>> permSubsList = new ArrayList<>();
		ArrayList<T[][]> transMat = new ArrayList<>();
		if (transform == Transform.H_n) {
			if (len != 3) {
				throw new IllegalArgumentException("H_n only works on 3-var polynomials");
			}
			// H1 = [[2,1,1],[0,1,0],[0,0,1]]
			// H2 = [[1,0,0],[1,2,1],[0,0,1]]
			// H3 = [[1,0,0],[0,1,0],[1,1,2]]
			@SuppressWarnings("unchecked")
			Poly<T>[] subsPoly = new Poly[] {f.newPoly("xyz", "2*x + y + z")};
			long[][] h123 = {{2, 1, 1}, {0, 1, 0}, {0, 0, 1}};
			for (int i = 0; i < 3; i ++) {
				PermSubs<T> permSubs = new PermSubs<>();
				permSubs.perm = makePerm(i, (i + 1)%3, (i + 2)%3);
				permSubs.subs = subsPoly;
				permSubs.index = transMat.size();
				T[][] m = f.newMatrix(3, 3);
				copy(m[0], h123[i], f);
				copy(m[1], h123[(i + 1)%3], f);
				copy(m[2], h123[(i + 2)%3], f);
				transMat.add(m);
				permSubsList.add(permSubs);
			}
			// H4 = [[1,1,0],[0,1,1],[1,0,1]]
			PermSubs<T> permSubs = new PermSubs<>();
			permSubs.perm = makePerm(0, 1, 2);
			@SuppressWarnings("unchecked")
			// x' = x + y, y' = y + z, z' = x + z
			Poly<T>[] subsPoly3 = new Poly[] {
				f.newPoly("xyz", "2*x + y - z"),
				f.newPoly("xyz", "y + z - x"),
				f.newPoly("xyz", "z + x"),
			};
			permSubs.subs = subsPoly3;
			permSubs.index = transMat.size();
			T[][] m = f.newMatrix(3, 3);
			long[][] h4 = {{1, 1, 0}, {0, 1, 1}, {1, 0, 1}};
			for (int i = 0; i < 3; i ++) {
				copy(m[i], h4[i], f);
			}
			transMat.add(m);
			permSubsList.add(permSubs);

		} else {
			// sds: [1, ..., 1], tsds: [lcm, lcm/2, ..., lcm/n]
			T[] column = f.newVector(len);
			if (transform == Transform.T_n) {
				T lcm = f.valueOf(1);
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
					column[i] = f.valueOf(1);
				}
			}

			T[][] upperMat = f.newMatrix(len, len);
			for (int i = 0; i < len; i ++) {
				for (int j = 0; j < len; j ++) {
					upperMat[i][j] = i <= j ? column[j] : f.valueOf(0);
				}
			}

			@SuppressWarnings("unchecked")
			Poly<T>[] subs = new Poly[transform == Transform.T_n ? len : len - 1];
			Mono[] monos = new Mono[len];
			for (int i = 0; i < len; i ++) {
				short[] exps = new short[len];
				Arrays.fill(exps, (short) 0);
				exps[i] = 1;
				monos[i] = new Mono(vars, exps);
			}
			for (int i = 0; i < len - 1; i ++) {
				Poly<T> sub = f.newPoly();
				sub.put(monos[i], column[i]);
				sub.put(monos[i + 1], f.valueOf(1));
				subs[i] = sub;
			}
			if (transform == Transform.T_n) {
				Poly<T> sub = f.newPoly();
				sub.put(monos[len - 1], column[len - 1]);
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
				PermSubs<T> permSubs = new PermSubs<>();
				permSubs.perm = perm;
				permSubs.subs = subs;
				permSubs.index = transMat.size();
				transMat.add(m);
				permSubsList.add(permSubs);
			}
		}

		Map<Poly<T>, List<List<Integer>>> polyTransList = Collections.singletonMap(f, initTransList);
		for (result.depth = 1; result.depth < maxDepth; result.depth ++) {
			log.debug("depth = " + result.depth + ", polynomials = " + polyTransList.size());
			int traceCurr = 0, traceTrans = 0;
			HashMap<Poly<T>, List<List<Integer>>> polyTransList1 = new HashMap<>();
			for (Map.Entry<Poly<T>, List<List<Integer>>> transEntry : polyTransList.entrySet()) {
				traceCurr ++;
				log.trace("depth = " + result.depth + ", polynomial: " + traceCurr + "/" + polyTransList.size());

				Poly<T> f0 = transEntry.getKey();
				List<List<Integer>> transList = transEntry.getValue();
				for (PermSubs<T> permSubs : permSubsList) {
					// f1 = f0's permutation and substitution (transformation)
					Poly<T> f1 = f.newPoly();
					for (Map.Entry<Mono, T> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = new short[vars.length()];
						for (int i = 0; i < exps.length; i ++) {
							// permute
							exps1[permSubs.perm.get(i).intValue()] = exps[i];
							// exps1[i] = exps[permSubs.perm.get(i).intValue()];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// sds: x0 += x1, x1 += x2, ... , x_n-2 += x_n-1
					// tsds: x_i = x_i/(i + 1) + x_i+1, x_n-1 = x_i/n
					for (int i = 0; i < permSubs.subs.length; i ++) {
						f1 = f1.subs(vars.charAt(i), permSubs.subs[i]);
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