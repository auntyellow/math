package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigPoly extends Poly<MutableBigInteger> {
	private static final long serialVersionUID = 1L;
	private static final MutableBigInteger ZERO = new MutableBigInteger(BigInteger.ZERO);
	private static final MutableBigInteger ONE = new MutableBigInteger(BigInteger.ONE);
	private static final MutableBigInteger MINUS_ONE = ONE.negate();

	public BigPoly() {/**/}

	public BigPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	protected MutableBigInteger zero() {
		return ZERO;
	}

	@Override
	protected MutableBigInteger one() {
		return ONE;
	}

	@Override
	protected MutableBigInteger minusOne() {
		return MINUS_ONE;
	}

	@Override
	protected MutableBigInteger newZero() {
		return new MutableBigInteger(BigInteger.ZERO);
	}

	@Override
	protected MutableBigInteger parse(String s) {
		return new MutableBigInteger(s);
	}

	@Override
	protected BigPoly newPoly() {
		return new BigPoly();
	}
}