package com.xqbase.math.inequality;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.MutableNumber;
import com.xqbase.math.polys.Poly;

/**
 * Successive Difference Substitution<p>
 * {@link #sds(Poly f)} or sds(f, false) uses upper triangular matrix (A_n)<p>
 * {@link #tsds(Poly f)} or sds(f, true) uses column stochastic matrix (T_n)<p> 
 * @see https://arxiv.org/pdf/0904.4030v3.pdf
 */
public class SDS {
	private static Logger log = LoggerFactory.getLogger(SDS.class);

	public static class SDSResult<T extends MutableNumber<T>> {
		Set<List<T>> zeroAt;
		List<T> negativeAt = null;
		int depth = 0;

		SDSResult(int len) {
			zeroAt = new TreeSet<>(listComparator(len));
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

	private static <T extends MutableNumber<T>> T[][] matMul(T[][] m1, T[][] m2, Poly<T> p) {
		int n = m1.length;
		T[][] m = p.newMatrix(n, n);
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				T mij = p.newZero();
				for (int k = 0; k < n; k ++) {
					mij.addMul(m1[i][k], m2[k][j]);
				}
				m[i][j] = mij;
			}
		}
		return m;
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

	private static <T extends MutableNumber<T>> List<T> matMulReduce(T[][] trans, List<T> key, Poly<T> p) {
		int n = key.size();
		T[] v = p.newVector(n);
		for (int i = 0; i < n; i ++) {
			v[i] = key.get(i);
		}
		v = matMul(trans, v, p);
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

	// for debug only
	/*
	private static <T> String toString(T[][] m) {
		return Stream.of(m).map(Arrays::asList).collect(Collectors.toList()).toString();
	}
	*/

	private static <T extends MutableNumber<T>> Map<List<T>, T> subs(Poly<T> f, String vars) {
		int len = vars.length();
		if (len == 0) {
			T value = f.valueOf(0);
			// at most one term, and must be a constant if there is
			for (T t : f.values()) {
				value = t;
			}
			return Collections.singletonMap(Collections.emptyList(), value);
		}
		String subVars = vars.substring(0, len - 1);
		char from = vars.charAt(len - 1);
		Map<List<T>, T> result = new HashMap<>();
		for (long i = 0; i <= 1; i ++) {
			// substitute the last variable with 0 and 1
			T to = f.valueOf(i);
			subs(f.subs(from, to), subVars).forEach((k, v) -> {
				List<T> key = new ArrayList<>(k);
				key.add(to);
				result.put(key, v);
			});
		}
		return result;
	}

	static <T extends Comparable<T>> Comparator<List<T>> listComparator(int len) {
		return (Comparator<List<T>>) (p1, p2) -> {
			for (int i = 0; i < len; i ++) {
				int c = p1.get(i).compareTo(p2.get(i));
				if (c != 0) {
					return c;
				}
			}
			return 0;
		};
	}

	/**
	 * find negative and zeros, then return if trivially non-negative
	 *
	 * @param transList skip finding negative if empty
	 */
	private static <T extends MutableNumber<T>> boolean trivial(Poly<T> f,
			List<T[][]> transList, String vars, SDSResult<T> result) {
		if (!transList.isEmpty()) {
			// find negative and zeros: try 0/1 for each var
			for (Map.Entry<List<T>, T> subsEntry : subs(f, vars).entrySet()) {
				int c = subsEntry.getValue().compareTo(f.valueOf(0));
				if (c < 0) {
					result.negativeAt = matMulReduce(transList.get(0), subsEntry.getKey(), f);
					return false;
				}
				if (c == 0) {
					// remove trivial zero
					boolean zero = true;
					for (T v : subsEntry.getKey()) {
						if (!v.equals(f.valueOf(0))) {
							zero = false;
							break;
						}
					}
					if (!zero) {
						for (T[][] trans : transList) {
							result.zeroAt.add(matMulReduce(trans, subsEntry.getKey(), f));
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

	public static <T extends MutableNumber<T>> SDSResult<T> sds(Poly<T> f) {
		return sds(f, false, false);
	}

	public static <T extends MutableNumber<T>> SDSResult<T> tsds(Poly<T> f) {
		return sds(f, true, false);
	}

	/** 
	 * @param tsds
	 * <code>false</code> to uses upper triangular matrix (A_n) and
	 * <code>true</code> to uses column stochastic matrix (T_n)
	 */
	public static <T extends MutableNumber<T>> SDSResult<T> sds(Poly<T> f, boolean tsds, boolean skipNegative) {
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
			return new SDSResult<>(0);
		}

		int len = vars.length();
		// sds: [1, ..., 1], tsds: [lcm, lcm/2, ..., lcm/n]
		T[] column = f.newVector(len);
		if (tsds) {
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

		T[][] oneMat = f.newMatrix(len, len);
		T[][] upperMat = f.newMatrix(len, len);
		for (int i = 0; i < len; i ++) {
			for (int j = 0; j < len; j ++) {
				oneMat[i][j] = f.valueOf(i == j ? 1 : 0);
				upperMat[i][j] = i <= j ? column[j] : f.valueOf(0);
			}
		}
		Set<Integer> varSeq = new TreeSet<>();
		for (int i = 0; i < len; i ++) {
			varSeq.add(Integer.valueOf(i));
		}
		TreeMap<List<Integer>, T[][]> permMat = new TreeMap<>(listComparator(len));
		for (List<Integer> perm : permutations(varSeq)) {
			T[][] m = f.newMatrix(len, len);
			for (int i = 0; i < len; i ++) {
				// permute
				m[i] = upperMat[perm.get(i).intValue()].clone();
				// m[perm.get(i).intValue()] = upperMat[i].clone();
			}
			permMat.put(perm, m);
		}

		@SuppressWarnings("unchecked")
		Poly<T>[] subs = new Poly[tsds ? len : len - 1];
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
		if (tsds) {
			Poly<T> sub = f.newPoly();
			sub.put(monos[len - 1], column[len - 1]);
			subs[len - 1] = sub;
		}

		// depth = 0
		SDSResult<T> result = new SDSResult<>(len);
		// transList is always empty if skipNegative
		List<T[][]> initTransList = skipNegative ? Collections.emptyList() : Collections.singletonList(oneMat);
		if (trivial(f, initTransList, vars, result) || result.negativeAt != null) {
			return result;
		}

		Map<Poly<T>, List<T[][]>> polyTransList = Collections.singletonMap(f, initTransList);
		while (!polyTransList.isEmpty()) {
			result.depth ++;
			log.debug("depth = " + result.depth + ", polynomials = " + polyTransList.size());
			int traceCurr = 0, traceTrans = 0;
			HashMap<Poly<T>, List<T[][]>> polyTransList1 = new HashMap<>();
			for (Map.Entry<Poly<T>, List<T[][]>> transEntry : polyTransList.entrySet()) {
				traceCurr ++;
				log.trace("depth = " + result.depth + ", polynomial: " + traceCurr + "/" + polyTransList.size());

				Poly<T> f0 = transEntry.getKey();
				List<T[][]> transList = transEntry.getValue();
				for (Map.Entry<List<Integer>, T[][]> permEntry : permMat.entrySet()) {
					// f1 = f0's permutation and substitution (transformation)
					List<Integer> perm = permEntry.getKey();
					T[][] permValue = permEntry.getValue();
					Poly<T> f1 = f.newPoly();
					for (Map.Entry<Mono, T> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = new short[vars.length()];
						for (int i = 0; i < exps.length; i ++) {
							// permute
							exps1[perm.get(i).intValue()] = exps[i];
							// exps1[i] = exps[perm.get(i).intValue()];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// sds: x0 += x1, x1 += x2, ... , x_n-2 += x_n-1
					// tsds: x_i = x_i/(i + 1) + x_i+1, x_n-1 = x_i/n
					for (int i = 0; i < subs.length; i ++) {
						f1 = f1.subs(vars.charAt(i), subs[i]);
					}
					List<T[][]> transList1 = new ArrayList<>();
					for (T[][] transMat : transList) {
						transList1.add(matMul(transMat, permValue, f));
					}
					// find negative and zeros, then skip trivial
					if (trivial(f1, transList1, vars, result)) {
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
			polyTransList = polyTransList1;
		}
		return result;
	}
}