package com.xqbase.math.polys;

import java.math.BigInteger;

public class Rational extends MutableNumber<Rational> {
	private static final long serialVersionUID = 1L;
	private static final BigInteger _0 = BigInteger.ZERO;
	private static final BigInteger _1 = BigInteger.ONE;

	private static final Rational[] cache =
			new Rational[Byte.MAX_VALUE - Byte.MIN_VALUE + 1];

	static {
		for (int i = Byte.MIN_VALUE; i <= Byte.MAX_VALUE; i ++) {
			cache[i - Byte.MIN_VALUE] = new Rational(BigInteger.valueOf(i));
		}
	}

	public static Rational valueOf(long n) {
		if (n < Byte.MIN_VALUE || n > Byte.MAX_VALUE) {
			return new Rational(BigInteger.valueOf(n));
		}
		return cache[(int) n - Byte.MIN_VALUE];
	}

	private BigInteger p;
	/** q > 0 */
	private BigInteger q;

	public BigInteger getP() {
		return p;
	}

	public BigInteger getQ() {
		return q;
	}

	private void reduce() {
		if (p.equals(_0)) {
			q = _1;
			return;
		}
		BigInteger gcd = p.gcd(q);
		if (gcd.equals(_1)) {
			return;
		}
		p = p.divide(gcd);
		q = q.divide(gcd);
	}

	private void posQ() {
		int sign = q.signum();
		if (sign == 0) {
			throw new ArithmeticException("/ by zero");
		}
		if (sign < 0) {
			this.p = p.negate();
			this.q = q.negate();
		}
	}

	public Rational(BigInteger p) {
		this.p = p;
		q = _1;
	}

	public Rational(BigInteger p, BigInteger q) {
		this.p = p;
		this.q = q;
		posQ();
		reduce();
	}

	public Rational(String s) {
		int slash = s.indexOf('/');
		if (slash < 0) {
			p = new BigInteger(s);
			q = _1;
		} else {
			p = new BigInteger(s.substring(0, slash));
			q = new BigInteger(s.substring(slash + 1));
			posQ();
			reduce();
		}
	}

	@Override
	public int intValue() {
		return p.divide(q).intValue();
	}

	@Override
	public long longValue() {
		return p.divide(q).longValue();
	}

	@Override
	public float floatValue() {
		return (float) doubleValue();
	}

	@Override
	public double doubleValue() {
		double q_ = q.doubleValue();
		return Double.isInfinite(q_) ? 1/q.divide(p).doubleValue() : p.doubleValue()/q_;
	}

	@Override
	public String toString() {
		return p + (q.equals(_1) ? "" : "/" + q);
	}

	@Override
	public int hashCode() {
		return p.hashCode()*31 + q.hashCode();
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof Rational)) {
			return false;
		}
		Rational o1 = (Rational) o;
		return p.multiply(o1.q).equals(q.multiply(o1.p));
	}

	@Override
	public int compareTo(Rational o) {
		return p.multiply(o.q).compareTo(q.multiply(o.p));
	}

	@Override
	public Rational negate() {
		return new Rational(p.negate(), q);
	}

	@Override
	public int signum() {
		return p.signum();
	}

	@Override
	public void add(Rational n1) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		p = p0.multiply(n1.q).add(q0.multiply(n1.p));
		q = q0.multiply(n1.q);
		reduce();
	}

	@Override
	public void addMul(Rational n1, Rational n2) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		BigInteger p1 = n1.p.multiply(n2.p);
		BigInteger q1 = n1.q.multiply(n2.q);
		p = p0.multiply(q1).add(q0.multiply(p1));
		q = q0.multiply(q1);
		reduce();
	}

	@Override
	public void addMul(Rational n1, Rational n2, Rational n3) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		BigInteger p1 = n1.p.multiply(n2.p).multiply(n3.p);
		BigInteger q1 = n1.q.multiply(n2.q).multiply(n3.q);
		p = p0.multiply(q1).add(q0.multiply(p1));
		q = q0.multiply(q1);
		reduce();
	}

	@Override
	public Rational div(Rational n1) {
		return new Rational(p.multiply(n1.q), q.multiply(n1.p));
	}

	@Override
	public Rational gcd(Rational n1) {
		return new Rational(p.gcd(n1.p).multiply(q.gcd(n1.q)), q.multiply(n1.q));
	}

	/*
	private static final Rational __0 = Rational.valueOf(0);
	private static final Rational __1 = Rational.valueOf(1);
	private static final Rational HALF = new Rational(_1, BigInteger.valueOf(2));
	private static final Rational SQRT_ERROR = new Rational(_1, BigInteger.valueOf(1639));

	// @return s that s^2 >= this
	public Rational sqrt() {
		if (signum() <= 0) {
			return __0;
		}
		Rational s;
		// initial estimate, see BigInteger.sqrt() (jdk 9+) for more accurate approach:
		// https://github.com/openjdk/jdk/blob/jdk-11-ga/src/java.base/share/classes/java/math/MutableBigInteger.java#L1869
		if (compareTo(__1) <= 0) {
			// t = q/p <= 1/this
			// quick estimate: 1 <= sqrt(1~3), 2 <= sqrt(4~15), 4 <= sqrt(16~63); ...
			// e = (t.bit_length - 1)/2
			// s = 1/2^e >= 1/sqrt(t) >= sqrt(this)
			BigInteger t = q.divide(p);
			int e = (t.bitLength() - 1)/2;
			s = new Rational(_1, _1.shiftLeft(e));
		} else {
			// t = (p + q - 1)/q >= r
			// quick estimate: 2 >= sqrt(2~4), 4 >= sqrt(5~16), 8 >= sqrt(17-64); ...
			// e = ((t - 1).bit_length + 1)/2
			// s = 2^e >= sqrt(t) >= sqrt(r)
			BigInteger t = p.add(q).subtract(_1).divide(q);
			int e = (t.subtract(_1).bitLength() + 1)/2;
			s = new Rational(_1.shiftLeft(e));
		}
		// 3 iterations are enough
		for (int i = 0; i < 3; i ++) {
			// x1 = (x0 + a/x0)/2
			s.add(div(s));
			Rational n2 = new Rational(BigInteger.ZERO);
			n2.addMul(HALF, s);
			s = n2;
		}
		// in the worst case s = 2*sqrt(r), so after 3 iterations:
		// s = 3281*sqrt(r)/3280, error = (s^2 - r)/r < 1/1639, see sqrt-heron-error.py
		Rational e = new Rational(BigInteger.ZERO);
		e.addMul(s, s);
		e.add(negate());
		if (e.signum() < 0) {
			throw new ArithmeticException("Unexpected: (" + s + ")^2 < " + this);
		}
		if (e.div(this).compareTo(SQRT_ERROR) >= 0) {
			throw new ArithmeticException("Unexpected: ((" + s + ")^2 - "
					+ this + ")/(" + this + ") >= " + SQRT_ERROR);
		}
		return s;
	}
	*/
}