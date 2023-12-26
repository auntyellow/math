package com.xqbase.math.polys;

import java.math.BigInteger;

public class MutableBigInteger extends MutableNumber<MutableBigInteger> {
	private static final long serialVersionUID = 1L;

	private BigInteger n;

	public MutableBigInteger(BigInteger n) {
		this.n = n;
	}

	public MutableBigInteger(String s) {
		this(new BigInteger(s));
	}

	@Override
	public int intValue() {
		return n.intValue();
	}

	@Override
	public long longValue() {
		return n.longValue();
	}

	@Override
	public float floatValue() {
		return n.floatValue();
	}

	@Override
	public double doubleValue() {
		return n.doubleValue();
	}

	@Override
	public String toString() {
		return n.toString();
	}

	@Override
	public int hashCode() {
		return n.hashCode();
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof MutableBigInteger)) {
			return false;
		}
		return n.equals(((MutableBigInteger) o).n);
	}

	@Override
	public int compareTo(MutableBigInteger o) {
		return n.compareTo(o.n);
	}

	@Override
	public MutableBigInteger negate() {
		return new MutableBigInteger(n.negate());
	}

	@Override
	public int signum() {
		return n.signum();
	}

	@Override
	public void add(MutableBigInteger n1) {
		n = n.add(n1.n);
	}

	@Override
	public void addMul(MutableBigInteger n1, MutableBigInteger n2) {
		n = n.add(n1.n.multiply(n2.n));
	}

	@Override
	public void addMul(MutableBigInteger n1, MutableBigInteger n2, MutableBigInteger n3) {
		n = n.add(n1.n.multiply(n2.n).multiply(n3.n));
	}

	@Override
	public MutableBigInteger div(MutableBigInteger n1) {
		return new MutableBigInteger(n.divide(n1.n));
	}

	@Override
	public MutableBigInteger gcd(MutableBigInteger n1) {
		return new MutableBigInteger(n.gcd(n1.n));
	}
}