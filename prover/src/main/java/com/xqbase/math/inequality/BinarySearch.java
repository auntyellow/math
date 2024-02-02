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
	private static final Rational _2 = Rational.valueOf(2);
	private static final Rational HALF = _1.div(_2);
	private static final Rational MAX_UPPER = new Rational(BigInteger.ONE.shiftLeft(100));
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational __() {
		return new Rational(BigInteger.ZERO);
	}

	private static boolean nonNegative(RationalPoly f) {
		for (Rational v : f.values()) {
			if (v.signum() < 0) {
				return false;
			}
		}
		return true;
	}

	/**
	 * binary search negative for all x_i >= 0
	 *
	 * @param f shouldn't be homogeneous because it hardly works when x_i are near zero.<p>
	 * For homogeneous polynomials, try {@link SDS}.
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all x_i >= 0
	 */
	public static Rational[] binarySearch(RationalPoly f) {
		if (nonNegative(f)) {
			return EMPTY_RESULT;
		}
		String vars = null;
		for (Mono m : f.keySet()) {
			vars = m.getVars();
			break;
		}
		if (vars == null) {
			return EMPTY_RESULT;
		}
		int len = vars.length();

		// m0 helps to find f0 (constant) directly
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		Mono m0 = new Mono(vars, exps0);
		Mono[] ms = new Mono[len];
		// subs helps to generate new f
		RationalPoly[] subsLower = new RationalPoly[len];
		RationalPoly[] subsUpper = new RationalPoly[len];
		for (int i = 0; i < len; i ++) {
			short[] exps = exps0.clone();
			exps[i] = 1;
			Mono m = new Mono(vars, exps);
			ms[i] = m;
			RationalPoly subs = new RationalPoly();
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new RationalPoly();
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
		}

		// f1 = f.subs(vi, vi + upper), double upper until f1 trivially non-negative
		Rational upper = _1;
		while (true) {
			RationalPoly f1 = f;
			for (int i = 0; i < len; i ++) {
				RationalPoly sub = new RationalPoly();
				sub.put(ms[i], _1);
				sub.put(m0, upper);
				f1 = f1.subs(vars.charAt(i), sub);
			}
			if (nonNegative(f1)) {
				break;
			}
			if (upper.equals(MAX_UPPER)) {
				throw new ArithmeticException("Polynomial may be negative for large variables: " + f);
			}
			Rational newUpper = __();
			newUpper.addMul(_2, upper);
			upper = newUpper;
		}

		Rational[] coords = new Rational[len];
		Arrays.fill(coords, _0);
		Rational[] lengths = new Rational[len];
		Arrays.fill(lengths, upper);
		RationalPoly f1 = f;
		upper = _1.div(upper);
		for (int i = 0; i < len; i ++) {
			RationalPoly sub = new RationalPoly();
			sub.put(ms[i], upper);
			f1 = f1.subs(vars.charAt(i), sub);
		}
		return binarySearch(f1, vars, m0, coords, lengths, subsLower, subsUpper);
	}

	private static Rational[] binarySearch(RationalPoly f, String vars, Mono m0,
			Rational[] coords, Rational[] lengths, RationalPoly[] subsLower, RationalPoly[] subsUpper) {
		int len = vars.length();
		Rational grad2 = __();
		Rational absMax = _0;
		int iMax = -1;
		for (int i = 0; i < len; i ++) {
			Rational abs = __();
			for (Map.Entry<Mono, Rational> entry : f.entrySet()) {
				Rational c = entry.getValue();
				abs.addMul(Rational.valueOf(entry.getKey().getExps()[i]),
						c.signum() < 0 ? c.negate() : c);
				if (abs.compareTo(absMax) > 0) {
					absMax = abs;
					iMax = i;
				}
			}
			grad2.addMul(abs, abs);
		}
		// value at lower bound
		Rational f0 = f.getOrDefault(m0, _0);
		if (f0.signum() < 0) {
			Rational[] result = new Rational[len + 1];
			System.arraycopy(coords, 0, result, 0, len);
			result[len] = f0;
			return result;
		}
		// f_min = f_0 - |grad f|d
		Rational min = __();
		min.addMul(f0, f0);
		min.addMul(grad2, Rational.valueOf(len).negate());
		if (min.signum() >= 0) {
			if (log.isDebugEnabled()) {
				log.debug("non_negative: " + Arrays.toString(coords) + ", " + Arrays.toString(lengths));
			}
			return EMPTY_RESULT;
		}
		// not positive-semidefinite, divide at i_max
		if (log.isDebugEnabled()) {
			log.debug("try_dividing: " + Arrays.toString(coords) + ", " + Arrays.toString(lengths) +
					", f = " + f0.doubleValue() + ", |grad f| = " + Math.sqrt(grad2.doubleValue()));
		}
		// set new lengths, used in upper and lower half
		Rational[] newLengths = lengths.clone();
		Rational length = __();
		length.addMul(HALF, lengths[iMax]);
		newLengths[iMax] = length;
		// set new coords, used in upper half only
		Rational[] newCoords = coords.clone();
		Rational coord = __();
		coord.add(coords[iMax]);
		coord.addMul(_1, length);
		newCoords[iMax] = coord;
		char x = vars.charAt(iMax);
		// search upper half: f.subs(x, (x + 1)/2)
		Rational[] result = binarySearch(f.subs(x, subsUpper[iMax]), vars, m0,
				newCoords, newLengths, subsLower, subsUpper);
		if (result.length > 0) {
			return result;
		}
		// search lower half: f.subs(x, x/2)
		return binarySearch(f.subs(x, subsLower[iMax]), vars, m0,
				coords, newLengths, subsLower, subsUpper);
	}
}