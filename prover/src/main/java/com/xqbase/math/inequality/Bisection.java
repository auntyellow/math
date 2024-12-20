package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.Rational2;
import com.xqbase.math.polys.Rational2Poly;
import com.xqbase.math.polys.RationalPoly;

public class Bisection {
	private static Logger log = LoggerFactory.getLogger(Bisection.class);

	private static final int MAX_DEPTH = 100;
	private static final Rational2 _0 = Rational2.valueOf(0);
	private static final Rational _0_R = _0.toRational();
	private static final Rational2 HALF = new Rational2(BigInteger.ONE, 1);
	private static final Rational HALF_R = HALF.toRational();
	private static final Rational INFINITY = Rational.valueOf(Long.MAX_VALUE);
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational newZero() {
		return new Rational(BigInteger.ZERO);
	}

	private static Rational mul(Rational n1, Rational n2) {
		Rational r = newZero();
		r.addMul(n1, n2);
		return r;
	}

	private String[] vars;
	private int len, depth;
	/** monopoly for constant term, helps to get f(0, 0, ..., 0) */
	private Monom m0;
	/** helps to generate new f for lower half: x -> x/2 */
	private Rational2Poly[] subsLower;
	/** helps to generate new f for upper half: x -> (x + 1)/2 */
	private Rational2Poly[] subsUpper;
	/** helps to call {@link #search1} */
	private Rational2[] bounds1;
	/** helps to call {@link #negativeResult(Rational)} */
	private Rational2[] coords0;

	private Bisection(String... vars) {
		this.vars = vars;
		len = vars.length;
		depth = 0;
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		m0 = new Monom(exps0);
		subsLower = new Rational2Poly[len];
		subsUpper = new Rational2Poly[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = exps0.clone();
			exps[i] = 1;
			Monom m = new Monom(exps);
			Rational2Poly subs = new Rational2Poly(vars);
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new Rational2Poly(vars);
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
		}
		bounds1 = new Rational2[len];
		Arrays.fill(bounds1, Rational2.valueOf(1));
		coords0 = new Rational2[len];
		Arrays.fill(coords0, _0);
	}

	private Rational[] negativeResult(Rational2 f0) {
		Rational[] result = new Rational[len + 1];
		for (int i = 0; i < len; i ++) {
			result[i] = _0_R;
		}
		if (f0 != null) {
			result[len] = f0.toRational();
		}
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
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	private Rational[] search1(Rational2Poly f, Rational2 f0_, Rational2[] bounds, Rational2[] coords) {
		Rational2 f0 = f0_;
		if (f0 == null) {
			f0 = f.getOrDefault(m0, _0);
			int s = f0.signum();
			if (s < 0) {
				return negativeResult(f0);
			}
			if (s == 0 || depth > MAX_DEPTH) {
				return negativeResult(null);
			}
		}
		Rational2 f1 = f.newZero();
		f1.add(f0);
		Rational2 fxMin = _0;
		int iMin = -1;
		for (int i = 0; i < len; i ++) {
			// f(x1, y0) = f(x0, y0) + intg_x0x1(f_x(y = y0))
			// f = sum_j(c_j*x**a_j*y**b_j), 0 <= x0, x1, y0, y1 <= 1:
			// f_x = sum_j(c_j*a_j*x**(a_j - 1)y**b_i) >= sum_j(c_j*a_j) (c_j < 0)
			// f(x_i1) >= f(x_i0) + sum_i(sum_j(c_j*a_ij)) (c_j < 0)
			int i_ = i;
			Rational2 fx = f.newZero();
			// TODO move outside for better performance
			f.forEach((m, c) -> {
				if (c.signum() < 0) {
					fx.addMul(c, Rational2.valueOf(m.getExps()[i_]));
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
		Rational2[] newBounds = bounds;
		Rational2[] newCoords = coords;
		String x = vars[iMin];
		if (log.isDebugEnabled()) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < bounds.length; i ++) {
				sb.append(coords[i].doubleValue() + "(" + bounds[i].doubleValue() + "), ");
			}
			log.debug(indent() + "divide [" + sb.substring(0, sb.length() - 2) + "], f = " +
					f0.doubleValue() + ", f_" + vars[iMin] + " = " + fxMin.doubleValue());
			// set new bounds for upper and lower half
			newBounds = bounds.clone();
			Rational2 bound = f.newZero();
			bound.addMul(HALF, bounds[iMin]);
			newBounds[iMin] = bound;
			// set new coords for upper half
			newCoords = coords.clone();
			Rational2 coord = f.newZero();
			coord.add(coords[iMin]);
			coord.add(bound);
			newCoords[iMin] = coord;
		}
		// search upper half: f.subs(x, (x + 1)/2)
		depth ++;
		Rational[] result = search1(f.subs(x, subsUpper[iMin]), null, newBounds, newCoords);
		depth --;
		if (result.length > 0) {
			result[iMin] = mul(HALF_R, result[iMin]);
			result[iMin].add(HALF_R);
			return result;
		}
		// search lower half: f.subs(x, x/2)
		depth ++;
		result = search1(f.subs(x, subsLower[iMin]), f0, newBounds, coords);
		depth --;
		if (result.length > 0) {
			result[iMin] = mul(HALF_R, result[iMin]);
		}
		return result;
	}

	/**
	 * search negative for f and 0 <= x_i <= 1, where f(0) may be positive, zero or negative
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	private Rational[] search0(Rational2Poly f) {
		Rational2 f0 = f.getOrDefault(m0, _0);
		int s = f0.signum();
		if (s < 0) {
			return negativeResult(f0);
		}
		if (s > 0) {
			// test if max-subs works
			// return EMPTY_RESULT;
			return search1(f, f0, bounds1, coords0);
		}

		// convert Monon to Rational[]
		ArrayList<Rational[]> monoms = new ArrayList<>();
		// calculate minDeg and minMonoms
		int minDeg0 = Integer.MAX_VALUE;
		ArrayList<Rational[]> minMonoms = new ArrayList<>();
		for (Monom monom : f.keySet()) {
			short[] exps = monom.getExps();
			int degree = 0;
			Rational[] m = new Rational[len];
			for (int i = 0; i < len; i ++) {
				int exp = exps[i];
				degree += exp;
				m[i] = Rational.valueOf(exp);
			}
			monoms.add(m);
			if (degree < minDeg0) {
				minDeg0 = degree;
				minMonoms = new ArrayList<>();
			}
			if (degree == minDeg0) {
				minMonoms.add(m);
			}
		}
		Rational minDeg_ = Rational.valueOf(minDeg0);

		// whether minMonoms has x_i:
		boolean[] hasVar = new boolean[len];
		Arrays.fill(hasVar, false);
		for (Rational[] m : minMonoms) {
			for (int i = 0; i < len; i ++) {
				if (m[i].signum() > 0) {
					hasVar[i] = true;
				}
			}
		}

		// 0 = no need to substitute; 1 = no need to shrink
		Rational[] shrinks = new Rational[len];
		for (int i = 0; i < len; i ++) {
			if (hasVar[i]) {
				shrinks[i] = Rational.valueOf(1);
				continue;
			}
			Rational shrink = _0_R;
			for (Rational[] m : monoms) {
				// exp_i
				Rational exp = m[i];
				if (exp.signum() == 0) {
					continue;
				}
				// sum(exp_j), j != i
				Rational exps = newZero();
				for (int j = 0; j < len; j ++) {
					if (j != i) {
						exps.add(m[j]);
					}
				}
				Rational gap = newZero();
				gap.add(minDeg_);
				gap.add(exps.negate());
				if (gap.signum() <= 0) {
					continue;
				}
				gap = gap.div(exp);
				if (gap.compareTo(shrink) > 0) {
					shrink = gap;
				}
			}
			shrinks[i] = shrink;
			// make at least one deg(has x_i) = minDeg and other deg > minDeg
			for (Rational[] m : monoms) {
				m[i] = mul(m[i], shrink);
			}
		}

		// denominators' lcm
		int lcm = 1;
		for (int i = 0; i < len; i ++) {
			Rational shrink = shrinks[i];
			if (shrink.signum() > 0) {
				BigInteger q = shrink.getQ();
				lcm = lcm/BigInteger.valueOf(lcm).gcd(q).intValue()*q.intValue();
			}
		}
		// numerators when all denominators = lcm, 0 = no need to substitute
		int[] pows = new int[len];
		for (int i = 0; i < len; i ++) {
			Rational shrink = shrinks[i];
			if (shrink.signum() > 0) {
				pows[i] = lcm/shrink.getQ().intValue()*shrink.getP().intValue();
			} else {
				pows[i] = 0;
			}
		}
		// x_i -> x_i**pow_i (A)
		Rational2Poly f1 = new Rational2Poly(vars);
		f.forEach((m, c) -> {
			short[] exps = m.getExps().clone();
			for (int i = 0; i < len; i ++) {
				int pow = pows[i];
				if (pow > 0) {
					exps[i] *= pow;
				}
			}
			f1.put(new Monom(exps), c);
		});
		// final minDeg
		minDeg_ = newZero();
		Rational[] minMonom = minMonoms.get(0);
		for (int i = 0; i < len; i ++) {
			minDeg_.addMul(minMonom[i], Rational.valueOf(pows[i]));
		}
		int minDeg = minDeg_.intValue();
		log.info(indent() + "vars = " + vars + ", shrinks = " + Arrays.toString(shrinks) +
				", pows = " + Arrays.toString(pows) + ", minDeg = " + minDeg + ", f = " + f1);

		for (int i = 0; i < len; i ++) {
			if (pows[i] == 0) {
				continue;
			}
			// x_i = max(x), x_j = k_j*x_i, f /= x_i**minDeg (B)
			StringBuilder sb = new StringBuilder();
			for (int j = 0; j < len; j ++) {
				if (pows[j] > 0) {
					sb.append(vars[j]);
				}
			}
			Rational2Poly f2 = new Rational2Poly(vars);
			int i_ = i;
			f1.forEach((m, c) -> {
				short[] exps2 = m.getExps().clone();
				for (int j = 0; j < len; j ++) {
					if (j != i_ && pows[j] > 0) {
						exps2[i_] += exps2[j];
					}
				}
				if (exps2[i_] < minDeg) {
					throw new AssertionError(m.toString(vars) + " after " +
							sb + " substitutions can't be divided by " +
							vars[i_] + "**" + minDeg + ", f = " + f1);
				}
				exps2[i_] -= minDeg;
				f2.put(new Monom(exps2), c);
			});
			log.info(indent() + "search f(" + vars[i] + " = max(" + sb + ")) = " + f2);
			depth ++;
			// test if max-subs works
			// Rational[] result = EMPTY_RESULT;
			Rational[] result = search0(f2);
			depth --;
			if (result.length == 0) {
				continue;
			}
			// restore (B)
			Rational xi = result[i];
			if (xi.signum() == 0) {
				// there should be negative near 0
				Arrays.fill(result, 0, len, _0_R);
				if (result[len] != null) {
					result[len] = _0_R;
				}
				return result;
			}
			for (int j = 0; j < len; j ++) {
				if (j != i) {
					result[j] = mul(result[j], xi);
				}
			}
			for (int j = 0; j < minDeg; j ++) {
				if (result[len] != null) {
					result[len] = result[len].div(xi);
				}
			}
			// restore (A)
			for (int j = 0; j < len; j ++) {
				int pow = pows[j];
				if (pow <= 1) {
					continue;
				}
				Rational xj = result[j];
				Rational x = xj;
				for (int k = 1; k < pow; k ++) {
					x = mul(x, xj);
				}
				result[j] = x;
			}
			return result;
		}
		return EMPTY_RESULT;
	}

	private Rational[] search0(RationalPoly f) {
		BigInteger[] lcm_ = {null};
		Rational[] result = search0(Rational2Poly.fromRationalPoly(f, lcm_));
		if (result.length > 0 && result[len] != null) {
			result[len] = result[len].div(new Rational(lcm_[0]));
		}
		return result;
	}

	/**
	 * search negative for f and 0 <= x_i <= 1, where f(0) may be positive, zero or negative
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	public static Rational[] search01(RationalPoly f) {
		return new Bisection(f.getVars()).search0(f);
	}

	/**
	 * search negative for f and 0 <= x_i <= 1, where f(0) may be positive, zero or negative
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	public static Rational[] search01(Rational2Poly f) {
		return new Bisection(f.getVars()).search0(f);
	}

	/**
	 * search negative for all x_i >= 0
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	public static Rational[] search(RationalPoly f) {
		Bisection bs = new Bisection(f.getVars());
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
			RationalPoly[] fs_ = new RationalPoly[fs.size()];
			fs.toArray(fs_);
			for (int j = 0; j < fs_.length; j ++) {
				// x_i -> 1/x_i, f *= x_i**degree_i (*)
				fs.add(fs_[j].reciprocal(i, degrees[i]));
				boolean[] reciprocal = reciprocals.get(j).clone();
				reciprocal[i] = true;
				reciprocals.add(reciprocal);
			}
		}
		// bisect each polynomial
		for (int i = 0; i < fs.size(); i ++) {
			boolean[] reciprocal = reciprocals.get(i);
			StringBuilder sb = new StringBuilder();
			for (boolean b : reciprocal) {
				sb.append(b ? '+' : '-');
			}
			RationalPoly fi = fs.get(i);
			log.info("search f(" + sb + ") = " + fi);
			Rational[] result = bs.search0(fi);
			if (result.length == 0) {
				continue;
			}
			// restore (*)
			Rational f0 = result[bs.len];
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
				result[j] = Rational.valueOf(1).div(result[j]);
				if (f0 == null || reeval) {
					continue;
				}
				f0 = result[bs.len];
				for (int k = 0; k < degrees[j]; k ++) {
					f0 = mul(f0, result[j]);
				}
				result[bs.len] = f0;
			}
			if (f0 == null || !reeval) {
				return result;
			}
			RationalPoly f1 = f;
			for (int j = 0; j < bs.len; j ++) {
				f1 = f1.subs(j, result[j]);
			}
			result[bs.len] = f1.remove(bs.m0);
			if (!f1.isEmpty()) {
				throw new AssertionError("Should be empty after substitutions: " + f1 + ", f = " +
						f + ", result = " + Arrays.toString(result));
			}
			if (result[bs.len] == null) {
				result[bs.len] = null;
			}
			return result;
		}
		return EMPTY_RESULT;
	}
}