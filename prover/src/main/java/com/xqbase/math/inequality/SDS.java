package com.xqbase.math.inequality;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
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

public class SDS {
	private static Logger log = LoggerFactory.getLogger(SDS.class);

	public static class SDSResult<T extends MutableNumber<T>> {
		Set<List<T>> zeroAt = new HashSet<>();
		List<T> negativeAt = null;
		int depth = 0;

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
				T m_ij = p.newZero();
				for (int k = 0; k < n; k ++) {
					m_ij.addMul(m1[i][k], m2[k][j]);
				}
				m[i][j] = m_ij;
			}
		}
		return m;
	}

	public static <T extends MutableNumber<T>> SDSResult<T> sds(Poly<T> f) {
		return sds(f, false);
	}

	public static <T extends MutableNumber<T>> SDSResult<T> tsds(Poly<T> f) {
		return sds(f, true);
	}

	/** @param tsds unused */
	public static <T extends MutableNumber<T>> SDSResult<T> sds(Poly<T> f, boolean tsds) {
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

		int len = vars.length();
		T[][] oneMat = f.newMatrix(len, len);
		T[][] upperMat = f.newMatrix(len, len);
		for (int i = 0; i < len; i ++) {
			for (int j = 0; j < len; j ++) {
				oneMat[i][j] = f.valueOf(i <= j ? 1 : 0);
				upperMat[i][j] = f.valueOf(i == j ? 1 : 0);
			}
		}
		Set<Integer> varSeq = new TreeSet<>();
		for (int i = 0; i < len; i ++) {
			varSeq.add(Integer.valueOf(i));
		}
		TreeMap<List<Integer>, T[][]> permMat = new TreeMap<>((p1, p2) -> {
			for (int i = 0; i < len; i ++) {
				int c = p1.get(i).compareTo(p2.get(i));
				if (c != 0) {
					return c;
				}
			}
			return 0;
		});
		for (List<Integer> perm : permutations(varSeq)) {
			T[][] m = f.newMatrix(len, len);
			for (int i = 0; i < len; i ++) {
				m[perm.get(i).intValue()] = upperMat[i].clone();
			}
			permMat.put(perm, m);
		}

		// TODO tsds: subs[i] = subs[i]/len + subs[i + 1]
		@SuppressWarnings("unchecked")
		Poly<T>[] subs = new Poly[len - 1];
		Mono[] monos = new Mono[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = new short[len];
			Arrays.fill(exps, (short) 0);
			exps[i] = 1;
			monos[i] = new Mono(vars, exps);
		}
		for (int i = 0; i < len - 1; i ++) {
			Poly<T> sub = f.newPoly();
			sub.put(monos[i], f.valueOf(1));
			sub.put(monos[i + 1], f.valueOf(1));
			subs[i] = sub;
		}

		HashMap<Poly<T>, List<T[][]>> polyTransList = new HashMap<>();
		polyTransList.put(f, Collections.singletonList(oneMat));

		SDSResult<T> result = new SDSResult<>();
		for (int depth = 0; depth <= 100; depth ++) {
			log.debug("depth = " + depth + ", polynomials = " + polyTransList.size());
			result.depth = depth;
			Iterator<Map.Entry<Poly<T>, List<T[][]>>> it = polyTransList.entrySet().iterator();
			while (it.hasNext()) {
				Map.Entry<Poly<T>, List<T[][]>> entry = it.next();
				Poly<T> f0 = entry.getKey();
				// List<int[][]> transList = entry.getValue();
				// TODO find negative or zero: try 0/1 for each var
				// substitute and iterate if there are negative terms
				boolean neg = false;
				for (T coeff : f0.values()) {
					if (coeff.signum() < 0) {
						neg = true;
						break;
					}
				}
				if (!neg) {
					it.remove();
				}
			}
			if (polyTransList.isEmpty()) {
				return result;
			}

			// substitution takes much time, so do it after negative check
			HashMap<Poly<T>, List<T[][]>> polyTransList1 = new HashMap<>();
			for (Map.Entry<Poly<T>, List<T[][]>> transEntry : polyTransList.entrySet()) {
				Poly<T> f0 = transEntry.getKey();
				List<T[][]> transList = transEntry.getValue();
				// List<int[][]> transList = transEntry.getValue();
				for (Map.Entry<List<Integer>, T[][]> permEntry : permMat.entrySet()) {
					// f1 = perm(f0)
					List<Integer> perm = permEntry.getKey();
					Poly<T> f1 = f.newPoly();
					for (Map.Entry<Mono, T> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = new short[vars.length()];
						for (int i = 0; i < exps.length; i ++) {
							exps1[perm.get(i).intValue()] = exps[i];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// subs: x0 += x1; x1 += x2; ... ; x_n-2 += x_n-1
					for (int i = 0; i < len - 1; i ++) {
						f1 = f1.subs(vars.charAt(i), subs[i]);
					}
					// TODO tsds: x_i = x_i/len + x_i+1
					// update next polyTransList
					List<T[][]> transList1 = polyTransList1.computeIfAbsent(f1, k -> new ArrayList<>());
					for (T[][] transMat : transList) {
						transList1.add(matMul(transMat, permEntry.getValue(), f));
					}
				}
			}
			polyTransList = polyTransList1;
		}
		return null;
	}
}