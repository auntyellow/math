package com.xqbase.math.inequality;

import java.util.List;
import java.util.Set;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.Poly;

public class SDS {
	public static class SDSResult {
		private boolean nonNegative;
		private Set<List<Long>> zeroAt;
		private List<Long> negativeAt;

		private SDSResult(boolean nonNegative, Set<List<Long>> zeroAt, List<Long> negativeAt) {
			this.nonNegative = nonNegative;
			this.zeroAt = zeroAt;
			this.negativeAt = negativeAt;
		}

		public boolean isNonNegative() {
			return nonNegative;
		}

		public Set<List<Long>> getZeroAt() {
			return zeroAt;
		}

		public List<Long> getNegativeAt() {
			return negativeAt;
		}
	}

	/** @param tsds unused */
	public static SDSResult sds(Poly f, boolean tsds) {
		// check homogeneous
		int deg = 0;
		for (Mono m : f.keySet()) {
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

		// TODO permutations of vars
		return null;
	}
}