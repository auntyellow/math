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
	private static final Rational HALF = new Rational(BigInteger.valueOf(1), BigInteger.valueOf(2));
	private static final Rational[] EMPTY_RESULT = new Rational[0];

	private static Rational __() {
		return new Rational(BigInteger.ZERO);
	}

	/**
	 * binary search negative for all x_i >= 0
	 *
	 * @param f shouldn't be homogeneous because it hardly works when x_i are near zero.<p>
	 * For homogeneous polynomials, try {@link SDS}.
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all x_i >= 0
	 */
	public static Rational[] binarySearch(RationalPoly f) {
		String vars = null;
		for (Mono m : f.keySet()) {
			vars = m.getVars();
			break;
		}
		if (vars == null) {
			return EMPTY_RESULT;
		}

		int len = vars.length();
		int[] degrees = new int[len];
		Arrays.fill(degrees, 0);
		for (Mono m : f.keySet()) {
			short[] exps = m.getExps();
			for (int i = 0; i < len; i ++) {
				if (exps[i] > degrees[i]) {
					degrees[i] = exps[i];
				}
			}
		}

		// m0 helps to find f0 (constant) directly
		short[] exps0 = new short[len];
		Arrays.fill(exps0, (short) 0);
		Mono m0 = new Mono(vars, exps0);
		// subs helps to generate new f
		RationalPoly[] subsLower = new RationalPoly[len];
		RationalPoly[] subsUpper = new RationalPoly[len];
		// fs and inverses: only one original f and no inverse
		ArrayList<RationalPoly> fs = new ArrayList<>();
		fs.add(f);
		ArrayList<boolean[]> inverses = new ArrayList<>();
		boolean[] inverse0 = new boolean[len];
		Arrays.fill(inverse0, false);
		inverses.add(inverse0);
		// after each iteration, one var is inverse, fs and inverses doubled
		for (int i = 0; i < len; i ++) {
			// prepare subs {{
			short[] exps_ = exps0.clone();
			exps_[i] = 1;
			Mono m = new Mono(vars, exps_);
			RationalPoly subs = new RationalPoly();
			subs.put(m, HALF);
			subsLower[i] = subs;
			subs = new RationalPoly();
			subs.put(m, HALF);
			subs.put(m0, HALF);
			subsUpper[i] = subs;
			// }}
			RationalPoly[] fs_ = new RationalPoly[fs.size()];
			fs.toArray(fs_);
			for (int j = 0; j < fs_.length; j ++) {
				// fj1 = fj.subs(vi, 1/vi)
				RationalPoly fj = fs_[j];
				RationalPoly fj1 = new RationalPoly();
				for (Map.Entry<Mono, Rational> entry : fj.entrySet()) {
					short[] exps = entry.getKey().getExps();
					short[] exps1 = exps.clone();
					exps1[i] = (short) (degrees[i] - exps[i]);
					fj1.put(new Mono(vars, exps1), entry.getValue());
				}
				fs.add(fj1);
				boolean[] inverse = inverses.get(j).clone();
				inverse[i] = true;
				inverses.add(inverse);
			}
		}

		Rational[] coords = new Rational[len];
		Arrays.fill(coords, _0);
		Rational[] lengths = new Rational[len];
		Arrays.fill(lengths, _1);

		int lenFs = fs.size();
		for (int i = 0; i < lenFs; i ++) {
			RationalPoly fi = fs.get(i);
			log.info("Searching " + fi + " ...");
			Rational[] result = binarySearch(fi, vars, m0, coords, lengths, subsLower, subsUpper);
			if (result.length == 0) {
				continue;
			}
			boolean[] inverse = inverses.get(i);
			for (int j = 0; j < len; j ++) {
				if (inverse[j]) {
					result[j] = _1.div(result[j]);
				}
			}
			return result;
		}
		return EMPTY_RESULT;
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