package com.xqbase.math.polys;

import java.math.BigInteger;

public class MutableBig extends MutableNumber<MutableBig> {
	private static final long serialVersionUID = 1L;

	private static final MutableBig[] cache =
			new MutableBig[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new MutableBig(BigInteger.valueOf(i));
		}
	}

	public static MutableBig valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new MutableBig(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	private BigInteger n;

	public MutableBig(BigInteger n) {
		this.n = n;
	}

	public MutableBig(String s) throws NumberFormatException {
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
		if (!(o instanceof MutableBig)) {
			return false;
		}
		return n.equals(((MutableBig) o).n);
	}

	@Override
	public int compareTo(MutableBig o) {
		return n.compareTo(o.n);
	}

	@Override
	public MutableBig negate() {
		return new MutableBig(n.negate());
	}

	@Override
	public int signum() {
		return n.signum();
	}

	@Override
	public void add(MutableBig n1) {
		n = n.add(n1.n);
	}

	@Override
	public void addMul(MutableBig n1, MutableBig n2) {
		n = n.add(n1.n.multiply(n2.n));
	}

	@Override
	public void addMul(MutableBig n1, MutableBig n2, MutableBig n3) {
		n = n.add(n1.n.multiply(n2.n).multiply(n3.n));
	}

	@Override
	public MutableBig div(MutableBig n1) {
		return new MutableBig(n.divide(n1.n));
	}

	@Override
	public MutableBig gcd(MutableBig n1) {
		return new MutableBig(n.gcd(n1.n));
	}
}