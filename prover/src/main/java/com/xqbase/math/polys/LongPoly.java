package com.xqbase.math.polys;

public class LongPoly extends Poly<MutableLong> {
	private static final long serialVersionUID = 1L;
	private static final MutableLong ZERO = new MutableLong(0);
	private static final MutableLong ONE = new MutableLong(1);
	private static final MutableLong MINUS_ONE = ONE.negate();

	public LongPoly() {/**/}

	public LongPoly(String var, String expr) {
		super(var, expr);
	}

	@Override
	protected MutableLong zero() {
		return ZERO;
	}

	@Override
	protected MutableLong one() {
		return ONE;
	}

	@Override
	protected MutableLong minusOne() {
		return MINUS_ONE;
	}

	@Override
	protected MutableLong newZero() {
		return new MutableLong(0);
	}

	@Override
	protected MutableLong parse(String s) {
		return new MutableLong(s);
	}

	@Override
	protected LongPoly newPoly() {
		return new LongPoly();
	}
}