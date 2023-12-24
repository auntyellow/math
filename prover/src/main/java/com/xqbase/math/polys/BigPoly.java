package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigPoly extends Poly<MutableBigInteger> {
	private static final long serialVersionUID = 1L;
	private static final MutableBigInteger[] cache =
			new MutableBigInteger[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new MutableBigInteger(BigInteger.valueOf(i));
		}
	}

	public BigPoly() {/**/}

	public BigPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public MutableBigInteger valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new MutableBigInteger(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	@Override
	public MutableBigInteger valueOf(String s) {
		return new MutableBigInteger(s);
	}

	@Override
	public MutableBigInteger newZero() {
		return new MutableBigInteger(BigInteger.ZERO);
	}

	@Override
	public MutableBigInteger[] newVector(int n) {
		return new MutableBigInteger[n];
	}

	@Override
	public MutableBigInteger[][] newMatrix(int n1, int n2) {
		return new MutableBigInteger[n1][n2];
	}
}