package com.xqbase.math.polys;

import java.math.BigInteger;

public class RationalPoly extends Poly<Rational, RationalPoly> {
	private static final long serialVersionUID = 1L;

	public RationalPoly() {/**/}

	public RationalPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public Rational valueOf(long n) {
		return Rational.valueOf(n);
	}

	@Override
	public Rational valueOf(String s) {
		return new Rational(s);
	}

	@Override
	public Rational newZero() {
		return new Rational(BigInteger.ZERO);
	}

	@Override
	public Rational[] newVector(int n) {
		return new Rational[n];
	}

	@Override
	public Rational[][] newMatrix(int n1, int n2) {
		return new Rational[n1][n2];
	}
}