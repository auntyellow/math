package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.Arrays;

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
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational __() {
		return new Rational(BigInteger.ZERO);
	}

	private static Rational __(Rational n1) {
		return new Rational(n1.getP(), n1.getQ());
	}

	private static Rational __(Rational n1, Rational n2) {
		return new Rational(n1.getP().multiply(n2.getP()), n1.getQ().multiply(n2.getQ()));
	}

	private String vars;
	private int len;
	/** monopoly for constant term, helps to get f(0, 0, ..., 0) */
	private Mono m0;
	/** helps to generate new f for lower half */
	private RationalPoly[] subsLower;
	/** helps to generate new f for upper half */
	private RationalPoly[] subsUpper;
	/** helps to call negativeResult */
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

	private Rational[] negativeResult(Rational f0) {
		Rational[] result = Arrays.copyOf(coords0, len + 1);
		result[len] = f0;
		return result;		
	}

	private static String toString(Rational[] bounds, Rational[] coords) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < bounds.length; i ++) {
			sb.append(coords[i].doubleValue() + "(" + bounds[i].doubleValue() + "), ");
		}
		return sb.substring(0, sb.length() - 2);
	}

	/**
	 * @param coords just for log
	 * @param bounds just for log
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all 0 <= x_i <= b
	 */
	private Rational[] binarySearch(RationalPoly f, Rational f0_, Rational[] bounds, Rational[] coords) {
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
			if (log.isDebugEnabled()) {
				log.debug("non_negative: [" + toString(bounds, coords) + "]");
			}
			return EMPTY_RESULT;
		}
		// not positive-semidefinite, divide at i_min
		Rational[] newBounds = bounds;
		Rational[] newCoords = coords;
		if (log.isDebugEnabled()) {
			log.debug("try_dividing: [" + toString(bounds, coords) + "], f = " +
					f0.doubleValue() + ", f_" + vars.charAt(iMin) + " = " + fxMin.doubleValue());
			// set new bounds, used in upper and lower half
			newBounds = bounds.clone();
			Rational bound = __(HALF, bounds[iMin]);
			newBounds[iMin] = bound;
			// set new coords, used in upper half only
			newCoords = coords.clone();
			Rational coord = __(coords[iMin]);
			coord.add(bound);
			newCoords[iMin] = coord;
		}
		char x = vars.charAt(iMin);
		// search upper half: f.subs(x, (x + 1)/2)
		Rational[] result = binarySearch(f.subs(x, subsUpper[iMin]), null, newBounds, newCoords);
		if (result.length > 0) {
			result[iMin] = __(HALF, result[iMin]);
			result[iMin].add(HALF);
			return result;
		}
		// search lower half: f.subs(x, x/2)
		result = binarySearch(f.subs(x, subsLower[iMin]), f0, newBounds, coords);
		if (result.length > 0) {
			result[iMin] = __(HALF, result[iMin]);
		}
		return result;
	}

	/**
	 * binary search negative for all 0 <= x_i <= 1
	 * @param f shouldn't be homogeneous because it hardly works when f == 0 at x_i == k*x_j.<p>
	 * For homogeneous polynomials, try {@link SDS}.
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all 0 <= x_i <= 1
	 */
	public static Rational[] binarySearch(RationalPoly f) {
		BinarySearch bs = new BinarySearch(f.getVars());
		Rational f0 = f.getOrDefault(bs.m0, _0);
		if (f0.signum() <= 0) {
			return bs.negativeResult(f0);
		}
		Rational[] bounds = new Rational[bs.len];
		Arrays.fill(bounds, _1);
		return bs.binarySearch(f, f0, bounds, bs.coords0);
	}
}