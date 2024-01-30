package com.xqbase.math.polys;

public class LongPoly extends Poly<MutableLong, LongPoly> {
	private static final long serialVersionUID = 1L;

	public LongPoly() {/**/}

	public LongPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	public MutableLong valueOf(long n) {
		return MutableLong.valueOf(n);
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