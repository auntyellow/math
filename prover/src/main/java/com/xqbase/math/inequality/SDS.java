package com.xqbase.math.inequality;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.Poly;

public class SDS {
	private static Logger log = LoggerFactory.getLogger(Poly.class);

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

	public static SDSResult sds(Poly f) {
		return sds(f, false);
	}

	public static SDSResult tsds(Poly f) {
		return sds(f, true);
	}

	/** @param tsds unused */
	public static SDSResult sds(Poly f, boolean tsds) {
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

		Set<Integer> varSeq = new TreeSet<>();
		for (int i = 0; i < vars.length(); i ++) {
			varSeq.add(Integer.valueOf(i));
		}
		List<List<Integer>> perms = permutations(varSeq);

		HashMap<Poly, List<int[][]>> polyTransList = new HashMap<>();
		polyTransList.put(f, Collections.singletonList(new int[0][0]));

		SDSResult result = new SDSResult();
		for (int depth = 0; depth <= 100; depth ++) {
			log.debug("depth = " + depth + ", polynomials = " + polyTransList.size());
			Iterator<Map.Entry<Poly, List<int[][]>>> it = polyTransList.entrySet().iterator();
			while (it.hasNext()) {
				Map.Entry<Poly, List<int[][]>> entry = it.next();
				Poly f0 = entry.getKey();
				// List<int[][]> transList = entry.getValue();
				// TODO find negative or zero: try 0/1 for each var
				// substitute and iterate if there are negative terms
				boolean neg = false;
				for (long[] coeff : f0.values()) {
					if (coeff[0] < 0) {
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
			for (Map.Entry<Poly, List<int[][]>> entry : polyTransList.entrySet()) {
				Poly f0 = entry.getKey();
				// List<int[][]> transList = entry.getValue();
				for (List<Integer> perm : perms) {
					// f1 = perm(f0)
					Poly f1 = new Poly();
					for (Map.Entry<Mono, long[]> term : f0.entrySet()) {
						byte[] exps = term.getKey().getExps();
						byte[] exps1 = new byte[vars.length()];
						for (int i = 0; i < exps.length; i ++) {
							exps1[perm.get(i).intValue()] = exps[i];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// TODO trans
					// TODO subs
					// TODO update next poly_trans_list
				}
			}
		}
		return null;
	}
}