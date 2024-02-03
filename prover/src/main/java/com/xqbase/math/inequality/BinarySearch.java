package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Map;

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
	// private static final Rational MAX_UPPER = new Rational(BigInteger.ONE.shiftLeft(100));
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational __() {
		return new Rational(BigInteger.ZERO);
	}

	private String vars;
	private int len;
	/** monopoly for constant term, helps to get f(0, 0, ..., 0) */
	private Mono m0;
	/** helps to generate new f for lower half */
	private RationalPoly[] subsLower;
	/** helps to generate new f for upper half */
	private RationalPoly[] subsUpper;
	/** helps to call binarySearch1 in binarySearch0 */
	private Rational[] coords0;

	private BinarySearch(String vars) {
		this.vars = vars;
		len = vars.length();
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		m0 = new Mono(exps0);
		Mono[] ms = new Mono[len];
		subsLower = new RationalPoly[len];
		subsUpper = new RationalPoly[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = exps0.clone();
			exps[i] = 1;
			Mono m = new Mono(exps);
			ms[i] = m;
			RationalPoly subs = new RationalPoly(vars);
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new RationalPoly(vars);
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
		}
		coords0 = new Rational[len];
		Arrays.fill(coords0, _0);
	}

	/**
	 * binary search negative for all 0 <= x_i <= 1
	 * @param f shouldn't be homogeneous because it hardly works when f == 0 at x_i == k*x_j.<p>
	 * For homogeneous polynomials, try {@link SDS}.
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all 0 <= x_i <= 1
	 */
	public static Rational[] binarySearch(RationalPoly f) {
		BinarySearch bs = new BinarySearch(f.getVars());
		Rational[] bounds = new Rational[bs.len];
		Arrays.fill(bounds, _1);
		Rational f0 = f.getOrDefault(bs.m0, _0);
		if (f0.signum() <= 0) {
			Rational[] result = Arrays.copyOf(bs.coords0, bs.len + 1);
			result[bs.len] = f0;
			return result;
		}
		return bs.binarySearch(f, bs.coords0, bounds, f0);
	}

	/** @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all 0 <= x_i <= b */
	private Rational[] binarySearch(RationalPoly f, Rational[] coords, Rational[] bounds, Rational f0_) {
		Rational f0 = f0_;
		if (f0 == null) {
			f0 = f.getOrDefault(m0, _0);
			if (f0.signum() <= 0) {
				Rational[] result = Arrays.copyOf(coords, len + 1);
				result[len] = f0;
				return result;
			}
		}
		Rational f1 = __();
		f1.add(f0);
		Rational fxMin = _0;
		int iMin = -1;
		for (int i = 0; i < len; i ++) {
			// f(x1, y0) = f(x0, y0) + intg_x0x1(f_x(y = y0))
			// f = sum_j(c_j*x**a_j*y**b_j), 0 <= x0, x1, y0, y1 <= 1:
			// f_x = sum_j(c_j*a_j*x**(a_j - 1)y**b_i) >= sum_j(c_j*a_j) (c_j < 0)
			// f(x_i1) >= f(x_i0) + sum_i(sum_j(c_j*a_ij)) (c_j < 0)
			Rational fx = __();
			for (Map.Entry<Mono, Rational> entry : f.entrySet()) {
				Rational c = entry.getValue();
				if (c.signum() >= 0) {
					continue;
				}
				fx.addMul(c, Rational.valueOf(entry.getKey().getExps()[i]));
			}
			f1.add(fx);
			if (fx.compareTo(fxMin) < 0) {
				fxMin = fx;
				iMin = i;
			}
		}
		if (f1.signum() >= 0) {
			if (log.isDebugEnabled()) {
				log.debug("non_negative: " + Arrays.toString(coords) + ", " + Arrays.toString(bounds));
			}
			return EMPTY_RESULT;
		}
		// not positive-semidefinite, divide at i_min
		if (log.isDebugEnabled()) {
			log.debug("try_dividing: " + Arrays.toString(coords) + ", " + Arrays.toString(bounds) +
					", f = " + f0.doubleValue() + ", f_" + vars.charAt(iMin) + " = " + fxMin.doubleValue());
		}
		// set new bounds, used in upper and lower half
		Rational[] newBounds = bounds.clone();
		Rational bound = __();
		bound.addMul(HALF, bounds[iMin]);
		newBounds[iMin] = bound;
		// set new coords, used in upper half only
		Rational[] newCoords = coords.clone();
		Rational coord = __();
		coord.add(coords[iMin]);
		coord.addMul(_1, bound);
		newCoords[iMin] = coord;
		char x = vars.charAt(iMin);
		// search upper half: f.subs(x, (x + 1)/2)
		Rational[] result = binarySearch(f.subs(x, subsUpper[iMin]), newCoords, newBounds, null);
		if (result.length > 0) {
			return result;
		}
		// search lower half: f.subs(x, x/2)
		return binarySearch(f.subs(x, subsLower[iMin]), coords, newBounds, f0);
	}
}