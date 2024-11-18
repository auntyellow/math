package com.xqbase.math.polys;

import java.math.BigInteger;
import java.util.List;

public class RationalPoly extends Poly<Rational, RationalPoly> {
	private static final long serialVersionUID = 1L;

	public RationalPoly(List<String> vars) {
		super(vars);
	}

	public RationalPoly(List<String> vars, String expr) {
		super(vars, expr);
	}

	public RationalPoly(String expr, String... vars) {
		super(expr, vars);
	}

	@Override
	public Rational valueOf(long n) {
		return Rational.valueOf(n);
	}

	@Override
	public Rational valueOf(String s) throws NumberFormatException {
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