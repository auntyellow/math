package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class BinarySearch {
	private static Logger log = LoggerFactory.getLogger(BinarySearch.class);

	private static final BigInteger __1 = BigInteger.ONE;
	private static final Rational _0 = Rational.valueOf(0);
	private static final Rational _1 = Rational.valueOf(1);
	private static final Rational HALF = new Rational(__1, BigInteger.valueOf(2));
	private static final Rational[] EMPTY_RESULT = new Rational[0];
	private static final RationalPoly[] EMPTY_POLYS = new RationalPoly[0];

	private static Rational newZero() {
		return new Rational(BigInteger.ZERO);
	}

	private static final Rational SQRT_ERROR = new Rational(__1, BigInteger.valueOf(1639));

	/** @return s that s^2 >= r */
	private static Rational sqrt(Rational r) {
		if (r.signum() <= 0) {
			return _0;
		}
		Rational s;
		// initial estimate, see BigInteger.sqrt() (jdk 9+) for more accurate approach:
		// https://github.com/openjdk/jdk/blob/jdk-11-ga/src/java.base/share/classes/java/math/MutableBigInteger.java#L1869
		if (r.compareTo(_1) <= 0) {
			// t = q/p <= 1/r
			// quick estimate: 1 <= sqrt(1~3), 2 <= sqrt(4~15), 4 <= sqrt(16~63); ...
			// e = (t.bit_length - 1)/2
			// s = 1/2^e >= 1/sqrt(t) >= sqrt(r)
			BigInteger t = r.getQ().divide(r.getP());
			int e = (t.bitLength() - 1)/2;
			s = new Rational(__1, __1.shiftLeft(e));
		} else {
			// t = (p + q - 1)/q >= r
			// quick estimate: 2 >= sqrt(2~4), 4 >= sqrt(5~16), 8 >= sqrt(17-64); ...
			// e = ((t - 1).bit_length + 1)/2
			// s = 2^e >= sqrt(t) >= sqrt(r)
			BigInteger t = r.getP().add(r.getQ()).subtract(__1).divide(r.getQ());
			int e = (t.subtract(__1).bitLength() + 1)/2;
			s = new Rational(__1.shiftLeft(e));
		}
		// 3 iterations are enough
		for (int i = 0; i < 3; i ++) {
			// x1 = (x0 + a/x0)/2
			s.add(r.div(s));
			Rational n2 = newZero();
			n2.addMul(HALF, s);
			s = n2;
		}
		// in the worst case s = 2*sqrt(r), so after 3 iterations:
		// s = 3281*sqrt(r)/3280, error = (s^2 - r)/r < 1/1639
		Rational e = newZero();
		e.addMul(s, s);
		e.add(r.negate());
		if (e.signum() < 0) {
			throw new ArithmeticException("Unexpected: (" + s + ")^2 < " + r);
		}
		if (e.div(r).compareTo(SQRT_ERROR) >= 0) {
			throw new ArithmeticException("Unexpected: ((" + s + ")^2 - "
					+ r + ")/(" + r + ") >= " + SQRT_ERROR);
		}
		return s;
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

		// f -> |grad f|^2 = sum_i(sum_j(|a_i*c_j|)^2)
		HashMap<RationalPoly, Rational> grad2Map = new HashMap<>();
		Rational[] range01 = new Rational[len*2];
		for (int i = 0; i < len; i ++) {
			range01[i*2] = _0;
			range01[i*2 + 1] = _1;
			for (RationalPoly fj : grad2Map.keySet().toArray(EMPTY_POLYS)) {
				// fj1 = fj.subs(vi, 1/vi)
				RationalPoly fj1 = new RationalPoly();
				for (Map.Entry<Mono, Rational> entry : fj.entrySet()) {
					short[] exps = entry.getKey().getExps();
					short[] exps1 = exps.clone();
					exps1[i] = (short) (degrees[i] - exps[i]);
					fj1.put(new Mono(vars, exps1), entry.getValue());
				}
				grad2Map.computeIfAbsent(fj1, key -> {
					Rational grad2 = newZero();
					for (int k = 0; k < len; k ++) {
						Rational abs = newZero();
						for (Map.Entry<Mono, Rational> entry : fj1.entrySet()) {
							Rational c = entry.getValue();
							abs.addMul(Rational.valueOf(entry.getKey().getExps()[k]),
									c.signum() < 0 ? c.negate() : c);
						}
						grad2.addMul(abs, abs);
					}
					return grad2;
				});
			}
		}
		for (Map.Entry<RationalPoly, Rational> entry : grad2Map.entrySet()) {
			RationalPoly fj = entry.getKey();
			log.info("Search " + fj + " within ([0, 1], ..., [0, 1])");
			Rational[] result = binarySearch(fj, vars, entry.getValue(), range01);
			if (result.length > 0) {
				return result;
			}
		}
		return EMPTY_RESULT;
	}

	/**
	 * @param f
	 * @param vars
	 * @param grad2
	 * @param ranges
	 */
	private static Rational[] binarySearch(RationalPoly f, String vars, Rational grad2, Rational[] ranges) {
		return EMPTY_RESULT;
	}
}