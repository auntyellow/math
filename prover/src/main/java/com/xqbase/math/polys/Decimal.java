package com.xqbase.math.polys;

import java.math.BigDecimal;
import java.math.MathContext;

public class Decimal extends MutableNumber<Decimal> {
	private static final long serialVersionUID = 1L;

	private static final Decimal[] cache =
			new Decimal[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new Decimal(BigDecimal.valueOf(i));
		}
	}

	public static Decimal valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new Decimal(BigDecimal.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	private BigDecimal n;

	public Decimal(BigDecimal n) {
		this.n = n;
	}

	public Decimal(String s) {
		this(new BigDecimal(s));
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
		if (!(o instanceof Decimal)) {
			return false;
		}
		return n.equals(((Decimal) o).n);
	}

	@Override
	public int compareTo(Decimal o) {
		return n.compareTo(o.n);
	}

	@Override
	public Decimal negate() {
		return new Decimal(n.negate());
	}

	@Override
	public int signum() {
		return n.signum();
	}

	@Override
	public void add(Decimal n1) {
		n = n.add(n1.n);
	}

	@Override
	public void addMul(Decimal n1, Decimal n2) {
		n = n.add(n1.n.multiply(n2.n));
	}

	@Override
	public void addMul(Decimal n1, Decimal n2, Decimal n3) {
		n = n.add(n1.n.multiply(n2.n).multiply(n3.n));
	}

	@Override
	public Decimal div(Decimal n1) {
		return new Decimal(n.divide(n1.n, MathContext.DECIMAL128));
	}

	@Override
	public Decimal gcd(Decimal n1) {
		return Decimal.valueOf(1);
	}
}