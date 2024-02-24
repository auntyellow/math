package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class BinarySearch {
	private static Logger log = LoggerFactory.getLogger(BinarySearch.class);

	private static final Rational _0 = Rational.valueOf(0);
	private static final Rational _1 = Rational.valueOf(1);
	private static final Rational HALF = _1.div(Rational.valueOf(2));
	private static final Rational INFINITY = Rational.valueOf(Long.MAX_VALUE);
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational __() {
		return new Rational(BigInteger.ZERO);
	}

	private static Rational __(Rational n1) {
		return new Rational(n1.getP(), n1.getQ());
	}

	private static Rational __(Rational n1, Rational n2) {
		Rational n = __();
		n.addMul(n1, n2);
		return n;
	}

	private String vars;
	private int len, depth;
	/** monopoly for constant term, helps to get f(0, 0, ..., 0) */
	private Mono m0;
	/** helps to generate new f for lower half: x -> x/2 */
	private RationalPoly[] subsLower;
	/** helps to generate new f for upper half: x -> (x + 1)/2 */
	private RationalPoly[] subsUpper;
	/** helps to call {@link #search0(RationalPoly) */
	private Rational[] bounds1;
	/** helps to call {@link #negativeResult(Rational)} */
	private Rational[] coords0;
	/** helps to generate f' in {@link #search0(RationalPoly)} */
	private RationalPoly[][] subsDiff;

	private BinarySearch(String vars) {
		this.vars = vars;
		len = vars.length();
		depth = 0;
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		m0 = new Mono(exps0);
		subsLower = new RationalPoly[len];
		subsUpper = new RationalPoly[len];
		subsDiff = new RationalPoly[len][len];
		for (int i = 0; i < len; i ++) {
			short[] exps = exps0.clone();
			exps[i] = 1;
			Mono m = new Mono(exps);
			RationalPoly subs = new RationalPoly(vars);
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new RationalPoly(vars);
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
			for (int j = 0; j < len; j ++) {
				// x_j -> x_i*x_j
				short[] eij = exps0.clone();
				eij[i] = 1;
				eij[j] = 1;
				subs = new RationalPoly(vars);
				subs.put(new Mono(eij), _1);
				// i = j is useless
				subsDiff[i][j] = subs;
			}
		}
		bounds1 = new Rational[len];
		Arrays.fill(bounds1, _1);
		coords0 = new Rational[len];
		Arrays.fill(coords0, _0);
	}

	private Rational[] negativeResult(Rational f0) {
		Rational[] result = Arrays.copyOf(coords0, len + 1);
		result[len] = f0;
		return result;		
	}

	private String indent() {
		// can use String.repeat() in Java 11
		return String.join("", Collections.nCopies(depth, "--")) + "> ";
	}

	/**
	 * search negative for f(0) > 0 and all 0 <= x_i <= 1
	 * @param bounds just for log
	 * @param coords just for log
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative
	 */
	private Rational[] search1(RationalPoly f, Rational f0_, Rational[] bounds, Rational[] coords) {
		Rational f0 = f0_;
		if (f0 == null) {
			f0 = f.getOrDefault(m0, _0);
			if (f0.signum() <= 0) {
				return negativeResult(f0);
			}
		}
		Rational f1 = __(f0);
		Rational fxMin = _0;
		int iMin = -1;
		for (int i = 0; i < len; i ++) {
			// f(x1, y0) = f(x0, y0) + intg_x0x1(f_x(y = y0))
			// f = sum_j(c_j*x**a_j*y**b_j), 0 <= x0, x1, y0, y1 <= 1:
			// f_x = sum_j(c_j*a_j*x**(a_j - 1)y**b_i) >= sum_j(c_j*a_j) (c_j < 0)
			// f(x_i1) >= f(x_i0) + sum_i(sum_j(c_j*a_ij)) (c_j < 0)
			int i_ = i;
			Rational fx = __();
			// TODO move outside for better performance
			f.forEach((m, c) -> {
				if (c.signum() < 0) {
					fx.addMul(c, Rational.valueOf(m.getExps()[i_]));
				}
			});
			f1.add(fx);
			if (fx.compareTo(fxMin) < 0) {
				fxMin = fx;
				iMin = i;
			}
		}
		if (f1.signum() >= 0) {
			return EMPTY_RESULT;
		}
		// not positive-semidefinite, divide at i_min
		Rational[] newBounds = bounds;
		Rational[] newCoords = coords;
		char x = vars.charAt(iMin);
		if (log.isDebugEnabled()) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < bounds.length; i ++) {
				sb.append(coords[i].doubleValue() + "(" + bounds[i].doubleValue() + "), ");
			}
			log.debug(indent() + "divide [" + sb.substring(0, sb.length() - 2) + "] at " + x +
					", f = " + f0.doubleValue() + ", f_" + vars.charAt(iMin) + " = " + fxMin.doubleValue());
			// set new bounds for upper and lower half
			newBounds = bounds.clone();
			Rational bound = __(HALF, bounds[iMin]);
			newBounds[iMin] = bound;
			// set new coords for upper half
			newCoords = coords.clone();
			Rational coord = __(coords[iMin]);
			coord.add(bound);
			newCoords[iMin] = coord;
		}
		// search upper half: f.subs(x, (x + 1)/2)
		depth ++;
		Rational[] result = search1(f.subs(x, subsUpper[iMin]), null, newBounds, newCoords);
		depth --;
		if (result.length > 0) {
			result[iMin] = __(HALF, result[iMin]);
			result[iMin].add(HALF);
			return result;
		}
		// search lower half: f.subs(x, x/2)
		depth ++;
		result = search1(f.subs(x, subsLower[iMin]), f0, newBounds, coords);
		depth --;
		if (result.length > 0) {
			result[iMin] = __(HALF, result[iMin]);
		}
		return result;
	}

	/**
	 * search negative for f and 0 <= x_i <= 1, where f(0) may be positive, zero or negative
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative
	 */
	private Rational[] search01(RationalPoly f) {
		Rational f0 = f.getOrDefault(m0, _0);
		int s = f0.signum();
		if (s < 0) {
			return negativeResult(f0);
		}
		if (s > 0) {
			return search1(f, f0, bounds1, coords0);
		}

		int minDeg = Integer.MAX_VALUE;
		for (Mono m : f.keySet()) {
			int degree = 0;
			for (short exp : m.getExps()) {
				degree += exp;
			}
			if (degree < minDeg) {
				minDeg = degree;
			}
		}

		for (int i = 0; i < len; i ++) {
			// x_i = max(x), x_j = k_j*x_i, f /= x_i**minDeg (*)
			RationalPoly f1 = f;
			for (int j = 0; j < len; j ++) {
				if (j != i) {
					f1 = f1.subs(vars.charAt(j), subsDiff[i][j]);
				}
			}
			RationalPoly f2 = new RationalPoly(vars);
			int i_ = i;
			int lowestDegree_ = minDeg;
			f1.forEach((m, c) -> {
				short[] exps2 = m.getExps().clone();
				exps2[i_] -= lowestDegree_;
				if (exps2[i_] < 0) {
					throw new RuntimeException();
				}
				f2.put(new Mono(exps2), c);
			});
			char x = vars.charAt(i);
			log.info("search f(" + x + " = max(" + vars + ")) = " + f2);
			depth ++;
			Rational[] result = search01(f2);
			depth --;
			if (result.length == 0) {
				continue;
			}
			// restore (*)
			Rational xi = result[i];
			if (xi.signum() == 0) {
				// there should be negative near 0
				Arrays.fill(result, _0);
				return result;
			}
			for (int j = 0; j < len; j ++) {
				if (j != i) {
					result[j] = __(result[j], xi);
				}
			}
			for (int j = 0; j < minDeg; j ++) {
				result[len] = result[len].div(xi);
			}
			return result;
		}
		return EMPTY_RESULT;
	}

	/**
	 * search negative for all x_i >= 0
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative
	 */
	public static Rational[] search(RationalPoly f) {
		BinarySearch bs = new BinarySearch(f.getVars());
		// initial fs and reciprocals: only one original f and no reciprocal
		List<RationalPoly> fs = new ArrayList<>();
		fs.add(f);
		List<boolean[]> reciprocals = new ArrayList<>();
		boolean[] reciprocal0 = new boolean[bs.len];
		Arrays.fill(reciprocal0, false);
		reciprocals.add(reciprocal0);
		// degrees[i] = 0 when f hasn't x_i
		int[] degrees = f.degrees();
		// after each iteration, one var is reciprocated, fs and reciprocals doubled
		for (int i = 0; i < bs.len; i ++) {
			char var = bs.vars.charAt(i);
			RationalPoly[] fs_ = new RationalPoly[fs.size()];
			fs.toArray(fs_);
			for (int j = 0; j < fs_.length; j ++) {
				// x_i -> 1/x_i, f *= x_i**degree_i (*)
				fs.add(fs_[j].reciprocal(var, degrees[i]));
				boolean[] reciprocal = reciprocals.get(j).clone();
				reciprocal[i] = true;
				reciprocals.add(reciprocal);
			}
		}
		// binary search each polynomial
		for (int i = 0; i < fs.size(); i ++) {
			boolean[] reciprocal = reciprocals.get(i);
			StringBuilder sb = new StringBuilder();
			for (boolean b : reciprocal) {
				sb.append(b ? '+' : '-');
			}
			RationalPoly fi = fs.get(i);
			log.info("search f(" + sb + ") = " + fi);
			Rational[] result = bs.search01(fi);
			if (result.length == 0) {
				continue;
			}
			// restore (*)
			boolean reeval = false;
			for (int j = 0; j < bs.len; j ++) {
				if (!reciprocal[j]) {
					continue;
				}
				if (result[j].signum() == 0) {
					// make 1/0 = +inf and re-evaluate
					result[j] = INFINITY;
					reeval = true;
					continue;
				}
				result[j] = _1.div(result[j]);
				if (reeval) {
					continue;
				}
				Rational f0 = result[bs.len];
				for (int k = 0; k < degrees[j]; k ++) {
					f0 = __(f0, result[j]);
				}
				result[bs.len] = f0;
			}
			if (!reeval) {
				return result;
			}
			RationalPoly f1 = f;
			for (int j = 0; j < bs.len; j ++) {
				f1 = f1.subs(bs.vars.charAt(j), result[j]);
			}
			result[bs.len] = f1.remove(bs.m0);
			if (!f1.isEmpty()) {
				throw new AssertionError("Should be empty after substitutions: " + f1 + ", f = " +
						f + ", result = " + Arrays.toString(result));
			}
			if (result[bs.len] == null) {
				result[bs.len] = _0;
			}
			return result;
		}
		return EMPTY_RESULT;
	}
}