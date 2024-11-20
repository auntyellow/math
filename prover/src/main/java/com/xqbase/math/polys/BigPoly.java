package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigPoly extends Poly<MutableBig, BigPoly> {
	private static final long serialVersionUID = 1L;

	public BigPoly(String[] vars) {
		super(vars);
	}

	public BigPoly(String expr, String... vars) {
		super(expr, vars);
	}

	@Override
	public MutableBig valueOf(long n) {
		return MutableBig.valueOf(n);
	}

	@Override
	public MutableBig valueOf(String s) throws NumberFormatException {
		return new MutableBig(s);
	}

	@Override
	public MutableBig newZero() {
		return new MutableBig(BigInteger.ZERO);
	}

	@Override
	public MutableBig[] newVector(int n) {
		return new MutableBig[n];
	}

	@Override
	public MutableBig[][] newMatrix(int n1, int n2) {
		return new MutableBig[n1][n2];
	}
}