package com.xqbase.math.polys;

import java.math.BigInteger;

public class MutableBigInteger extends MutableNumber<MutableBigInteger> {
	private static final long serialVersionUID = 1L;

	private BigInteger[] n;

	public MutableBigInteger(BigInteger n) {
		this.n = new BigInteger[] {n};
	}

	public MutableBigInteger(String s) {
		this(new BigInteger(s));
	}

	@Override
	public int intValue() {
		return n[0].intValue();
	}

	@Override
	public long longValue() {
		return n[0].longValue();
	}

	@Override
	public float floatValue() {
		return n[0].floatValue();
	}

	@Override
	public double doubleValue() {
		return n[0].doubleValue();
	}

	@Override
	public String toString() {
		return n[0].toString();
	}

	@Override
	public int hashCode() {
		return n[0].hashCode();
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof MutableBigInteger)) {
			return false;
		}
		return n[0].equals(((MutableBigInteger) o).n[0]);
	}

	@Override
	public int compareTo(MutableBigInteger o) {
		return n[0].compareTo(o.n[0]);
	}

	@Override
	public MutableBigInteger negate() {
		return new MutableBigInteger(n[0].negate());
	}

	@Override
	public int signum() {
		return n[0].signum();
	}

	@Override
	protected void add(MutableBigInteger n1) {
		n[0] = n[0].add(n1.n[0]);
	}

	@Override
	protected MutableBigInteger multiply(MutableBigInteger n1) {
		return new MutableBigInteger(n[0].multiply(n1.n[0]));
	}

	@Override
	protected MutableBigInteger multiply(MutableBigInteger n1, MutableBigInteger n2) {
		return new MutableBigInteger(n[0].multiply(n1.n[0]).multiply(n2.n[0]));
	}
}