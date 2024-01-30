package com.xqbase.math.polys;

import java.math.BigInteger;

public class MutableLong extends MutableNumber<MutableLong> {
	private static final long serialVersionUID = 1L;

	private static final MutableLong[] cache =
			new MutableLong[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new MutableLong(i);
		}
	}

	public static MutableLong valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new MutableLong(n);
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	private long n;

	public MutableLong(long n) {
		this.n = n;
	}

	public MutableLong(String s) {
		this(Long.parseLong(s));
	}

	@Override
	public int intValue() {
		return (int) n;
	}

	@Override
	public long longValue() {
		return n;
	}

	@Override
	public float floatValue() {
		return n;
	}

	@Override
	public double doubleValue() {
		return n;
	}

	@Override
	public String toString() {
		return Long.toString(n);
	}

	@Override
	public int hashCode() {
		return Long.hashCode(n);
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof MutableLong)) {
			return false;
		}
		return n == ((MutableLong) o).n;
	}

	@Override
	public int compareTo(MutableLong o) {
		return Long.compare(n, o.n);
	}

	@Override
	public MutableLong negate() {
		return new MutableLong(-n);
	}

	@Override
	public int signum() {
		return Long.signum(n);
	}

	@Override
	public void add(MutableLong n1) {
		n = Math.addExact(n, n1.n);
	}

	@Override
	public void addMul(MutableLong n1, MutableLong n2) {
		n = Math.addExact(n, Math.multiplyExact(n1.n, n2.n));
	}

	@Override
	public void addMul(MutableLong n1, MutableLong n2, MutableLong n3) {
		n = Math.addExact(n, Math.multiplyExact(Math.multiplyExact(n1.n, n2.n), n3.n));
	}

	@Override
	public MutableLong div(MutableLong n1) {
		return new MutableLong(n / n1.n);
	}

	@Override
	public MutableLong gcd(MutableLong n1) {
		return new MutableLong(BigInteger.valueOf(n).gcd(BigInteger.valueOf(n1.n)).longValue());
	}
}