package com.xqbase.math.polys;

import java.util.List;

public class LongPoly extends Poly<MutableLong, LongPoly> {
	private static final long serialVersionUID = 1L;

	public LongPoly(List<String> vars) {
		super(vars);
	}

	public LongPoly(List<String> vars, String expr) {
		super(vars, expr);
	}

	public LongPoly(String expr, String... vars) {
		super(expr, vars);
	}

	@Override
	public MutableLong valueOf(long n) {
		return MutableLong.valueOf(n);
	}

	@Override
	public MutableLong valueOf(String s) throws NumberFormatException {
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