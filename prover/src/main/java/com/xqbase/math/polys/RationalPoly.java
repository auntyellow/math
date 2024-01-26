package com.xqbase.math.polys;

import java.math.BigInteger;

public class RationalPoly extends Poly<Rational, RationalPoly> {
	private static final long serialVersionUID = 1L;
	private static final Rational[] cache =
			new Rational[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new Rational(BigInteger.valueOf(i));
		}
	}

	public RationalPoly() {/**/}

	public RationalPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public Rational valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new Rational(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
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