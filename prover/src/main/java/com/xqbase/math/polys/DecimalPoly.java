package com.xqbase.math.polys;

import java.math.BigDecimal;

public class DecimalPoly extends Poly<Decimal, DecimalPoly> {
	private static final long serialVersionUID = 1L;

	public DecimalPoly(String vars) {
		super(vars);
	}

	public DecimalPoly(String vars, String expr) {
		super(vars, expr);
	}

	@Override
	public Decimal valueOf(long n) {
		return Decimal.valueOf(n);
	}

	@Override
	public Decimal valueOf(String s) {
		return new Decimal(s);
	}

	@Override
	public Decimal newZero() {
		return new Decimal(BigDecimal.ZERO);
	}

	@Override
	public Decimal[] newVector(int n) {
		return new Decimal[n];
	}

	@Override
	public Decimal[][] newMatrix(int n1, int n2) {
		return new Decimal[n1][n2];
	}
}