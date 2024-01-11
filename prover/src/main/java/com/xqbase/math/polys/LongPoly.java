package com.xqbase.math.polys;

public class LongPoly extends Poly<MutableLong, LongPoly> {
	private static final long serialVersionUID = 1L;
	private static final MutableLong[] cache =
			new MutableLong[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new MutableLong(i);
		}
	}

	public LongPoly() {/**/}

	public LongPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public MutableLong valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new MutableLong(n);
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	@Override
	public MutableLong valueOf(String s) {
		return new MutableLong(s);
	}

	@Override
	public MutableLong newZero() {
		return new MutableLong(0);
	}

	@Override
	public MutableLong[] newVector(int n) {
		return new MutableLong[n];
	}

	@Override
	public MutableLong[][] newMatrix(int n1, int n2) {
		return new MutableLong[n1][n2];
	}
}