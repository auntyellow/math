package com.xqbase.math.inequality;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Decimal;
import com.xqbase.math.polys.DecimalPoly;
import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.Rational;

public class DecimalBisection {
	private static Logger log = LoggerFactory.getLogger(DecimalBisection.class);

	private static final int MAX_DEPTH = 100;
	private static final Decimal _0 = Decimal.valueOf(0);
	private static final Decimal _1 = Decimal.valueOf(1);
	private static final Decimal HALF = _1.div(Decimal.valueOf(2));
	private static final Decimal INFINITY = Decimal.valueOf(Long.MAX_VALUE);
	private static final Decimal[] EMPTY_RESULT = new Decimal[0];

	private static Decimal __() {
		return new Decimal(BigDecimal.ZERO);
	}

	private static Decimal __(Decimal n1) {
		Decimal ret = __();
		ret.add(n1);
		return ret;
	}

	/** @return n1*n2 */
	private static Decimal __(Decimal n1, Decimal n2) {
		Decimal ret = __();
		ret.addMul(n1, n2);
		return ret;
	}

	private String vars;
	private int len, depth;
	/** monopoly for constant term, helps to get f(0, 0, ..., 0) */
	private Monom m0;
	/** helps to generate new f for lower half: x -> x/2 */
	private DecimalPoly[] subsLower;
	/** helps to generate new f for upper half: x -> (x + 1)/2 */
	private DecimalPoly[] subsUpper;
	/** helps to call {@link #search1(DecimalPoly, Decimal, Decimal[], Decimal[])} */
	private Decimal[] bounds1;
	/** helps to call {@link #negativeResult(Decimal)} */
	private Decimal[] coords0;

	private DecimalBisection(String vars) {
		this.vars = vars;
		len = vars.length();
		depth = 0;
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		m0 = new Monom(exps0);
		subsLower = new DecimalPoly[len];
		subsUpper = new DecimalPoly[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = exps0.clone();
			exps[i] = 1;
			Monom m = new Monom(exps);
			DecimalPoly subs = new DecimalPoly(vars);
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new DecimalPoly(vars);
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
		}
		bounds1 = new Decimal[len];
		Arrays.fill(bounds1, _1);
		coords0 = new Decimal[len];
		Arrays.fill(coords0, _0);
	}

	private Decimal[] negativeResult(Decimal f0) {
		Decimal[] result = Arrays.copyOf(coords0, len + 1);
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
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	private Decimal[] search1(DecimalPoly f, Decimal f0_, Decimal[] bounds, Decimal[] coords) {
		Decimal f0 = f0_;
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
		Decimal f1 = __(f0);
		Decimal fxMin = _0;
		int iMin = -1;
		for (int i = 0; i < len; i ++) {
			// f(x1, y0) = f(x0, y0) + intg_x0x1(f_x(y = y0))
			// f = sum_j(c_j*x**a_j*y**b_j), 0 <= x0, x1, y0, y1 <= 1:
			// f_x = sum_j(c_j*a_j*x**(a_j - 1)y**b_i) >= sum_j(c_j*a_j) (c_j < 0)
			// f(x_i1) >= f(x_i0) + sum_i(sum_j(c_j*a_ij)) (c_j < 0)
			int i_ = i;
			Decimal fx = __();
			// TODO move outside for better performance
			f.forEach((m, c) -> {
				if (c.signum() < 0) {
					fx.addMul(c, Decimal.valueOf(m.getExps()[i_]));
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
		Decimal[] newBounds = bounds;
		Decimal[] newCoords = coords;
		char x = vars.charAt(iMin);
		if (log.isDebugEnabled()) {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < bounds.length; i ++) {
				sb.append(coords[i].doubleValue() + "(" + bounds[i].doubleValue() + "), ");
			}
			log.debug(indent() + "divide [" + sb.substring(0, sb.length() - 2) + "], f = " +
					f0.doubleValue() + ", f_" + vars.charAt(iMin) + " = " + fxMin.doubleValue());
			// set new bounds for upper and lower half
			newBounds = bounds.clone();
			Decimal bound = __(HALF, bounds[iMin]);
			newBounds[iMin] = bound;
			// set new coords for upper half
			newCoords = coords.clone();
			Decimal coord = __(coords[iMin]);
			coord.add(bound);
			newCoords[iMin] = coord;
		}
		// search upper half: f.subs(x, (x + 1)/2)
		depth ++;
		Decimal[] result = search1(f.subs(x, subsUpper[iMin]), null, newBounds, newCoords);
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
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	private Decimal[] search0(DecimalPoly f) {
		Decimal f0 = f.getOrDefault(m0, _0);
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
			Rational shrink = Rational.valueOf(0);
			for (Rational[] m : monoms) {
				// exp_i
				Rational exp = m[i];
				if (exp.signum() == 0) {
					continue;
				}
				// sum(exp_j), j != i
				Rational exps = new Rational(BigInteger.ZERO);
				for (int j = 0; j < len; j ++) {
					if (j != i) {
						exps.add(m[j]);
					}
				}
				Rational gap = new Rational(BigInteger.ZERO);
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
				Rational mi = new Rational(BigInteger.ZERO);
				mi.addMul(m[i], shrink);
				m[i] = mi;
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
		DecimalPoly f1 = new DecimalPoly(vars);
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
		minDeg_ = new Rational(BigInteger.ZERO);
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
					sb.append(vars.charAt(j));
				}
			}
			DecimalPoly f2 = new DecimalPoly(vars);
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
							vars.charAt(i_) + "**" + minDeg + ", f = " + f1);
				}
				exps2[i_] -= minDeg;
				f2.put(new Monom(exps2), c);
			});
			log.info(indent() + "search f(" + vars.charAt(i) + " = max(" + sb + ")) = " + f2);
			depth ++;
			// test if max-subs works
			// Rational[] result = EMPTY_RESULT;
			Decimal[] result = search0(f2);
			depth --;
			if (result.length == 0) {
				continue;
			}
			// restore (B)
			Decimal xi = result[i];
			if (xi.signum() == 0) {
				// there should be negative near 0
				Arrays.fill(result, 0, len, _0);
				if (result[len] != null) {
					result[len] = _0;
				}
				return result;
			}
			for (int j = 0; j < len; j ++) {
				if (j != i) {
					result[j] = __(result[j], xi);
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
				Decimal xj = result[j];
				Decimal x = xj;
				for (int k = 1; k < pow; k ++) {
					x = __(x, xj);
				}
				result[j] = x;
			}
			return result;
		}
		return EMPTY_RESULT;
	}

	/**
	 * search negative for f and 0 <= x_i <= 1, where f(0) may be positive, zero or negative
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	public static Decimal[] search01(DecimalPoly f) {
		return new DecimalBisection(f.getVars()).search0(f);
	}

	/**
	 * search negative for all x_i >= 0
	 * @return [] if f is proved non-negative, or<br>
	 * [x_i, f(x_i)] if negative found, or<br>
	 * [x_i, null] if unable to prove and x_i is the critical point 
	 */
	public static Decimal[] search(DecimalPoly f) {
		DecimalBisection bs = new DecimalBisection(f.getVars());
		// initial fs and reciprocals: only one original f and no reciprocal
		List<DecimalPoly> fs = new ArrayList<>();
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
			DecimalPoly[] fs_ = new DecimalPoly[fs.size()];
			fs.toArray(fs_);
			for (int j = 0; j < fs_.length; j ++) {
				// x_i -> 1/x_i, f *= x_i**degree_i (*)
				fs.add(fs_[j].reciprocal(var, degrees[i]));
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
			DecimalPoly fi = fs.get(i);
			log.info("search f(" + sb + ") = " + fi);
			Decimal[] result = bs.search0(fi);
			if (result.length == 0) {
				continue;
			}
			// restore (*)
			Decimal f0 = result[bs.len];
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
				if (f0 == null || reeval) {
					continue;
				}
				f0 = result[bs.len];
				for (int k = 0; k < degrees[j]; k ++) {
					f0 = __(f0, result[j]);
				}
				result[bs.len] = f0;
			}
			if (f0 == null || !reeval) {
				return result;
			}
			DecimalPoly f1 = f;
			for (int j = 0; j < bs.len; j ++) {
				f1 = f1.subs(bs.vars.charAt(j), result[j]);
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