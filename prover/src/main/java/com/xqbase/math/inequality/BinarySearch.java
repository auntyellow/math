package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.ArrayList;
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

	private static void fillResult(Rational[] result, boolean[] key, Rational upper) {
		for (int i = 0; i < key.length; i ++) {
			result[i] = key[i] ? upper : _0;
		}
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

		// product([false, true], repeat = len)
		boolean[] key0 = new boolean[len];
		Arrays.fill(key0, false);
		ArrayList<boolean[]> keys = new ArrayList<>();
		keys.add(key0);
		for (int i = 0; i < len; i ++) {
			boolean[][] keys_ = new boolean[keys.size()][];
			keys.toArray(keys_);
			for (boolean[] key : keys_) {
				boolean[] key1 = key.clone();
				key1[i] = true;
				keys.add(key1);
			}
		}
		// remove first trivial zeros
		keys.remove(0);

		// f1 = f.subs(vi, vi + upper), double upper until f1 trivially non-negative
		Rational upper = __();
		upper.add(_1);
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
			// negative test
			for (boolean[] key : keys) {
				RationalPoly f0 = f;
				for (int i = 0; i < len; i ++) {
					f0 = f0.subs(vars.charAt(i), key[i] ? upper : _0);
				}
				Rational c0 = f0.remove(m0);
				if (!f0.isEmpty()) {
					Rational[] result = new Rational[len];
					fillResult(result, key, upper);
					throw new ArithmeticException("Unexpected substitution result: " + f + " =" +
							Arrays.toString(result) + "=> " + f0);
				}
				if (c0 == null || c0.signum() >= 0) {
					continue;
				}
				Rational[] result = new Rational[len + 1];
				fillResult(result, key, upper);
				result[len] = c0;
				return result;
			}
			upper.add(upper);
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
		// value at (0, ..., 0)
		int len = vars.length();
		Rational f0 = f.getOrDefault(m0, _0);
		if (f0.signum() < 0) {
			Rational[] result = Arrays.copyOf(coords, len + 1);
			result[len] = f0;
			return result;
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
				log.debug("non_negative: " + Arrays.toString(coords) + ", " + Arrays.toString(lengths));
			}
			return EMPTY_RESULT;
		}
		// not positive-semidefinite, divide at i_min
		if (log.isDebugEnabled()) {
			log.debug("try_dividing: " + Arrays.toString(coords) + ", " + Arrays.toString(lengths) +
					", f = " + f0.doubleValue() + ", f_" + vars.charAt(iMin) + " = " + fxMin.doubleValue());
		}
		// set new lengths, used in upper and lower half
		Rational[] newLengths = lengths.clone();
		Rational length = __();
		length.addMul(HALF, lengths[iMin]);
		newLengths[iMin] = length;
		// set new coords, used in upper half only
		Rational[] newCoords = coords.clone();
		Rational coord = __();
		coord.add(coords[iMin]);
		coord.addMul(_1, length);
		newCoords[iMin] = coord;
		char x = vars.charAt(iMin);
		// search upper half: f.subs(x, (x + 1)/2)
		Rational[] result = binarySearch(f.subs(x, subsUpper[iMin]), vars, m0,
				newCoords, newLengths, subsLower, subsUpper);
		if (result.length > 0) {
			return result;
		}
		// search lower half: f.subs(x, x/2)
		return binarySearch(f.subs(x, subsLower[iMin]), vars, m0,
				coords, newLengths, subsLower, subsUpper);
	}
}