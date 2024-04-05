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
}