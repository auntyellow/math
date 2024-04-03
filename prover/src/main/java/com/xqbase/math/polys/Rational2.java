package com.xqbase.math.polys;

import java.math.BigInteger;

public class Rational2 extends MutableNumber<Rational2> {
	private static final long serialVersionUID = 1L;
	private static final BigInteger _1 = BigInteger.ONE;

	private static final Rational2[] cache =
			new Rational2[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new Rational2(BigInteger.valueOf(i));
		}
	}

	public static Rational2 valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new Rational2(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	private static int scale(BigInteger q) {
		int lowest = q.getLowestSetBit();
		if (q.bitLength() > lowest + 1) {
			throw new ArithmeticException(q + " != 2^n");
		}
		return lowest;
	}

	private BigInteger p;
	/** value = p*2^-scale */
	private int scale;

	private void reduce() {
		if (p.signum() == 0) {
			scale = 0;
			return;
		}
		int lowest = p.getLowestSetBit();
		if (lowest > 0) {
			p = p.shiftRight(lowest);
			scale -= lowest;
		}
	}

	public Rational toRational() {
		return scale > 0 ?
				new Rational(p, _1.shiftLeft(scale)) :
				new Rational(p.shiftLeft(scale));
	}

	public Rational2(BigInteger p) {
		this(p, 0);
	}

	public Rational2(Rational r) {
		this(r.getP(), scale(r.getQ()));
	}

	public Rational2(BigInteger p, int scale) {
		this(p, scale, true);
	}

	private Rational2(BigInteger p, int scale, boolean reduce) {
		this.p = p;
		this.scale = scale;
		if (reduce) {
			reduce();
		}
	}

	public Rational2(String s) {
		this(new Rational(s));
	}

	@Override
	public int intValue() {
		return toRational().intValue();
	}

	@Override
	public long longValue() {
		return toRational().longValue();
	}

	@Override
	public float floatValue() {
		return toRational().floatValue();
	}

	@Override
	public double doubleValue() {
		return toRational().doubleValue();
	}

	@Override
	public String toString() {
		return toRational().toString();
	}

	@Override
	public int hashCode() {
		return p.hashCode()*31 + scale;
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof Rational2)) {
			return false;
		}
		Rational2 o1 = (Rational2) o;
		return p.equals(o1.p) && scale == o1.scale;
	}

	@Override
	public int compareTo(Rational2 o) {
		int scale1 = o.scale;
		return scale > scale1 ?
				p.compareTo(o.p.shiftLeft(scale - scale1)) :
				p.shiftLeft(scale1 - scale).compareTo(o.p);
	}

	@Override
	public Rational2 negate() {
		return new Rational2(p.negate(), scale);
	}

	@Override
	public int signum() {
		return p.signum();
	}

	@Override
	public void add(Rational2 n1) {
		BigInteger p1 = n1.p;
		int scale1 = n1.scale;
		if (scale > scale1) {
			p1 = p1.shiftLeft(scale - scale1);
			scale1 = scale;
		} else {
			p = p.shiftLeft(scale1 - scale);
			scale = scale1;
		}
		p = p.add(p1);
		reduce();
	}

	@Override
	public void addMul(Rational2 n1, Rational2 n2) {
		add(new Rational2(n1.p.multiply(n2.p), n1.scale + n2.scale, false));
	}

	@Override
	public void addMul(Rational2 n1, Rational2 n2, Rational2 n3) {
		add(new Rational2(n1.p.multiply(n2.p).multiply(n3.p), n1.scale + n2.scale + n3.scale, false));
	}

	@Override
	public Rational2 div(Rational2 n1) {
		return new Rational2(toRational().div(n1.toRational()));
	}

	@Override
	public Rational2 gcd(Rational2 n1) {
		return new Rational2(toRational().gcd(n1.toRational()));
	}
}