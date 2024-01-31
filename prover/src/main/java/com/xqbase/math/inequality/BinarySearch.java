package com.xqbase.math.inequality;

import java.math.BigInteger;
import java.util.ArrayList;

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

	/**
	 * @param n a positive number
	 * @return s that s^2 >= n
	 */
	private static Rational sqrt(Rational n) {
		Rational n1;
		// initial estimate, see BigInteger.sqrt() (jdk 9+) for more accurate approach:
		// https://github.com/openjdk/jdk/blob/jdk-11-ga/src/java.base/share/classes/java/math/MutableBigInteger.java#L1869
		if (n.compareTo(_1) <= 0) {
			// t = q/p
			// quick estimate: 1-3:1; 4-15:2; 16-63:4; 64-255:8; ...
			// e = (t.bit_length - 1)/2
			// s = 2^e <= sqrt(t)
			BigInteger t = n.getQ().divide(n.getP());
			int e = (t.bitLength() - 1)/2;
			n1 = new Rational(__1, __1.shiftLeft(e));
		} else {
			// t = (p + q - 1)/q >= p/q
			// quick estimate: 2-4:2; 5-16:4; 17-64:8; 65-256:16; ...
			// e = ((t - 1).bit_length + 1)/2
			// s = 2^e >= sqrt(t)
			BigInteger t = n.getP().add(n.getQ()).subtract(__1).divide(n.getQ());
			int e = (t.subtract(__1).bitLength() + 1)/2;
			n1 = new Rational(__1.shiftLeft(e));
		}
		// 3 iterations are enough
		for (int i = 0; i < 3; i ++) {
			// x1 = (x0 + a/x0)/2
			n1.add(n.div(n1));
			Rational n2 = newZero();
			n2.addMul(HALF, n1);
			n1 = n2;
		}
		return n1;
	}

	/**
	 * binary search negative for all x_i >= 0
	 *
	 * @param f shouldn't be homogeneous because it hardly works when x_i are near zero.<p>
	 * For homogeneous polynomials, try {@link SDS}.
	 * @return [x_i, f(x_i)] if negative found, or [] if f is proved non-negative for all x_i >= 0
	 */
	public static Rational[] binarySearch(RationalPoly f) {
		int deg = 0;
		String vars = "";
		for (Mono m : f.keySet()) {
			int exps = 0;
			for (int exp : m.getExps()) {
				exps += exp;
			}
			if (exps > deg) {
				deg = exps;
				vars = m.getVars();
			}
		}
		if (deg == 0) {
			return EMPTY_RESULT;
		}

		int len = vars.length();
		ArrayList<RationalPoly> fs = new ArrayList<>();
		Rational[] range01 = new Rational[len*2];
		for (int i = 0; i < len; i ++) {
			range01[i*2] = _0;
			range01[i*2 + 1] = _1;
			ArrayList<RationalPoly> fs1 = new ArrayList<>(fs);
			for (RationalPoly fj : fs.toArray(EMPTY_POLYS)) {
				// TODO inverse fj at var_i
				fs1.add(fj);
			}
			fs = fs1;
		}
		for (RationalPoly fj : fs) {
			// TODO calculate sum of square coefficients
			log.info("Search " + fj + " within ([0, 1], ..., [0, 1])");
			Rational coeff = f.newZero();
			Rational[] result = binarySearch(fj, vars, coeff, range01);
			if (result.length > 0) {
				return result;
			}
		}
		return EMPTY_RESULT;
	}

	/**
	 * @param f
	 * @param vars
	 * @param coeff
	 * @param ranges
	 */
	private static Rational[] binarySearch(RationalPoly f, String vars, Rational coeff, Rational[] ranges) {
		return EMPTY_RESULT;
	}

	public static void main(String[] args) {
		BigInteger maxQ = BigInteger.valueOf(1000000000);
		Rational a = new Rational(BigInteger.valueOf(100), BigInteger.valueOf(101));
		Rational b = _1;
		Rational minus = new Rational("-1");
		for (int i = 0; i < 2000; i ++) {
			Rational s = sqrt(b);
			Rational t = newZero();
			t.addMul(s, s);
			t.addMul(minus, b);
			System.out.println(s + "^2 - " + b + " = " + t.doubleValue());
			Rational b1 = newZero();
			b1.addMul(b, a);
			BigInteger p = b1.getP();
			BigInteger q = b1.getQ();
			BigInteger divisor = q.divide(maxQ);
			if (divisor.compareTo(__1) > 0) {
				b = new Rational(p.divide(divisor), q.divide(divisor));
			} else {
				b = b1;
			}
		}
	}
}