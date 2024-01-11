package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigPoly extends Poly<MutableBig, BigPoly> {
	private static final long serialVersionUID = 1L;
	private static final MutableBig[] cache =
			new MutableBig[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new MutableBig(BigInteger.valueOf(i));
		}
	}

	public BigPoly() {/**/}

	public BigPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public MutableBig valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new MutableBig(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	@Override
	public MutableBig valueOf(String s) {
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