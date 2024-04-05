package com.xqbase.math.polys;

import java.math.BigInteger;

public class Rational2Poly extends Poly<Rational2, Rational2Poly> {
	private static final long serialVersionUID = 1L;

	public Rational2Poly(String vars) {
		super(vars);
	}

	public Rational2Poly(String vars, String expr) {
		super(vars, expr);
	}

	@Override
	public Rational2 valueOf(long n) {
		return Rational2.valueOf(n);
	}

	@Override
	public Rational2 valueOf(String s) {
		return new Rational2(s);
	}

	@Override
	public Rational2 newZero() {
		return new Rational2(BigInteger.ZERO);
	}

	@Override
	public Rational2[] newVector(int n) {
		return new Rational2[n];
	}

	@Override
	public Rational2[][] newMatrix(int n1, int n2) {
		return new Rational2[n1][n2];
	}

	public static Rational2Poly fromRationalPoly(RationalPoly f, BigInteger[] lcm_) {
		BigInteger lcm = BigInteger.ONE;
		for (Rational c : f.values()) {
			BigInteger q = c.getQ();
			lcm = lcm.divide(lcm.gcd(q)).multiply(q);
		}
		Rational2Poly f2 = new Rational2Poly(f.getVars());
		BigInteger lcm__ = lcm;
		f.forEach((m, c) -> {
			f2.put(m, new Rational2(c.getP().multiply(lcm__.divide(c.getQ()))));
		});
		if (lcm_ != null && lcm_.length > 0) {
			lcm_[0] = lcm;
		}
		return f2;
	}
}