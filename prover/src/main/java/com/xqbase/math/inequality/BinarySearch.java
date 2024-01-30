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

	private static final Rational _0 = Rational.valueOf(0);
	private static final Rational _1 = Rational.valueOf(1);
	private static final Rational HALF = new Rational(BigInteger.ONE, BigInteger.valueOf(2));
	private static final Rational[] EMPTY_RESULT = new Rational[0];
	private static final RationalPoly[] EMPTY_POLYS = new RationalPoly[0];

	private static Rational newZero() {
		return new Rational(BigInteger.ZERO);
	}

	private static Rational sqrt(Rational n) {
		if (n.compareTo(_1) < 0) {
			// TODO set result >= sqrt(n)
			return _1.div(sqrt(_1.div(n)));
		}
		// TODO initial estimate
		BigInteger p = n.getP().divide(n.getQ());
		Rational n1 = new Rational(p.shiftRight(p.bitLength()/2));
		// TODO how many iterations?
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
		for (int i = 1; i <= 1000; i ++) {
			Rational n = Rational.valueOf(i);
			System.out.println(n + " -> " + sqrt(n));
			Rational n1 = _1.div(n);
			System.out.println(n1 + " -> " + sqrt(n1));
		}
	}
}