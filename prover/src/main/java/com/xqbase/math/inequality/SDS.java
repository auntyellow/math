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
import com.xqbase.math.polys.MutableLong;
import com.xqbase.math.polys.LongPoly;

public class SDS {
	private static Logger log = LoggerFactory.getLogger(LongPoly.class);
	private static final MutableLong _1 = new MutableLong(1);

	public static class SDSResult {
		private Set<List<Long>> zeroAt = new HashSet<>();
		private List<Long> negativeAt = null;

		public boolean isNonNegative() {
			return negativeAt == null;
		}

		public Set<List<Long>> getZeroAt() {
			return zeroAt;
		}

		public List<Long> getNegativeAt() {
			return negativeAt;
		}

		@Override
		public String toString() {
			return "SDSResult [nonNegative=" + isNonNegative() +
					", zeroAt=" + zeroAt + ", negativeAt=" + negativeAt + "]";
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

	private static long[][] matMul(long[][] m1, long[][] m2) {
		int n = m1.length;
		long[][] m = new long[n][n];
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < n; j ++) {
				long m_ij = 0;
				for (int k = 0; k < n; k ++) {
					m_ij += m1[i][k]*m2[k][j];
				}
				m[i][j] = m_ij;
			}
		}
		return m;
	}

	public static SDSResult sds(LongPoly f) {
		return sds(f, false);
	}

	public static SDSResult tsds(LongPoly f) {
		return sds(f, true);
	}

	/** @param tsds unused */
	public static SDSResult sds(LongPoly f, boolean tsds) {
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
		long[][] oneMat = new long[len][len];
		long[][] upperMat = new long[len][len];
		for (int i = 0; i < len; i ++) {
			for (int j = 0; j < len; j ++) {
				oneMat[i][j] = (i <= j ? 1 : 0);
				upperMat[i][j] = (i == j ? 1 : 0);
			}
		}
		Set<Integer> varSeq = new TreeSet<>();
		for (int i = 0; i < len; i ++) {
			varSeq.add(Integer.valueOf(i));
		}
		TreeMap<List<Integer>, long[][]> permMat = new TreeMap<>((p1, p2) -> {
			for (int i = 0; i < len; i ++) {
				int c = p1.get(i).compareTo(p2.get(i));
				if (c != 0) {
					return c;
				}
			}
			return 0;
		});
		for (List<Integer> perm : permutations(varSeq)) {
			long[][] m = new long[len][len];
			for (int i = 0; i < len; i ++) {
				m[perm.get(i).intValue()] = upperMat[i].clone();
			}
			permMat.put(perm, m);
		}

		// TODO tsds: subs[i] = subs[i]/len + subs[i + 1]
		LongPoly[] subs = new LongPoly[len - 1];
		Mono[] monos = new Mono[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = new short[len];
			Arrays.fill(exps, (short) 0);
			exps[i] = 1;
			monos[i] = new Mono(vars, exps);
		}
		for (int i = 0; i < len - 1; i ++) {
			LongPoly sub = new LongPoly();
			sub.put(monos[i], _1);
			sub.put(monos[i + 1], _1);
			subs[i] = sub;
		}

		HashMap<LongPoly, List<long[][]>> polyTransList = new HashMap<>();
		polyTransList.put(f, Collections.singletonList(oneMat));

		SDSResult result = new SDSResult();
		for (int depth = 0; depth <= 100; depth ++) {
			log.debug("depth = " + depth + ", polynomials = " + polyTransList.size());
			Iterator<Map.Entry<LongPoly, List<long[][]>>> it = polyTransList.entrySet().iterator();
			while (it.hasNext()) {
				Map.Entry<LongPoly, List<long[][]>> entry = it.next();
				LongPoly f0 = entry.getKey();
				// List<int[][]> transList = entry.getValue();
				// TODO find negative or zero: try 0/1 for each var
				// substitute and iterate if there are negative terms
				boolean neg = false;
				for (MutableLong coeff : f0.values()) {
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
			HashMap<LongPoly, List<long[][]>> polyTransList1 = new HashMap<>();
			for (Map.Entry<LongPoly, List<long[][]>> transEntry : polyTransList.entrySet()) {
				LongPoly f0 = transEntry.getKey();
				List<long[][]> transList = transEntry.getValue();
				// List<int[][]> transList = transEntry.getValue();
				for (Map.Entry<List<Integer>, long[][]> permEntry : permMat.entrySet()) {
					// f1 = perm(f0)
					List<Integer> perm = permEntry.getKey();
					LongPoly f1 = new LongPoly();
					for (Map.Entry<Mono, MutableLong> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = new short[vars.length()];
						for (int i = 0; i < exps.length; i ++) {
							exps1[perm.get(i).intValue()] = exps[i];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// subs: x0 += x1; x1 += x2; ... ; x_n-2 += x_n-1
					for (int i = 0; i < len - 1; i ++) {
						f1 = (LongPoly) f1.subs(vars.charAt(i), subs[i]);
					}
					// TODO tsds: x_i = x_i/len + x_i+1
					// update next polyTransList
					List<long[][]> transList1 = polyTransList1.computeIfAbsent(f1, k -> new ArrayList<>());
					for (long[][] transMat : transList) {
						transList1.add(matMul(transMat, permEntry.getValue()));
					}
				}
			}
			polyTransList = polyTransList1;
		}
		return null;
	}
}