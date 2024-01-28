package com.xqbase.math.polys;

import java.math.BigInteger;

public class Rational extends MutableNumber<Rational> {
	private static final long serialVersionUID = 1L;
	private static final BigInteger _0 = BigInteger.ZERO;
	private static final BigInteger _1 = BigInteger.ONE;
	private static final Rational __0 = new Rational(_0);
	private static final Rational __1 = new Rational(_1);

	private BigInteger p, q;

	public BigInteger getP() {
		return p;
	}

	public BigInteger getQ() {
		return q;
	}

	public Rational(BigInteger p) {
		this.p = p;
		q = _1;
	}

	public Rational(BigInteger p, BigInteger q) {
		if (q.equals(_0)) {
			throw new ArithmeticException("/ by zero");
		}
		this.p = p;
		this.q = q;
	}

	public Rational(String s) {
		int slash = s.indexOf(s);
		if (slash < 0) {
			p = new BigInteger(s);
			q = _1;
		} else {
			p = new BigInteger(s.substring(0, slash));
			q = new BigInteger(s.substring(slash + 1));
			if (q.equals(_0)) {
				throw new ArithmeticException("/ by zero");
			}
		}
	}

	public Rational reduced() {
		if (p.equals(_0)) {
			return __0;
		}
		BigInteger gcd = p.gcd(q);
		if (gcd.equals(_1)) {
			if (q.signum() > 0) {
				return this;
			}
			return new Rational(p.negate(), q.negate());
		}
		if (q.signum() > 0) {
			return new Rational(p.divide(gcd), q.divide(gcd));
		}
		return new Rational(p.divide(gcd).negate(), q.divide(gcd).negate());
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
		return p.floatValue()/q.floatValue();
	}

	@Override
	public double doubleValue() {
		return p.doubleValue()/q.doubleValue();
	}

	@Override
	public String toString() {
		Rational r = reduced();
		return r.p + (r.q.equals(_1) ? "" : "/" + r.q);
	}

	@Override
	public int hashCode() {
		Rational r = reduced();
		return r.p.hashCode()*31 + r.q.hashCode();
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
		return p.signum()*q.signum();
	}

	@Override
	public void add(Rational n1) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		p = p0.multiply(n1.q).add(q0.multiply(n1.p));
		q = q0.multiply(n1.q);
	}

	@Override
	public void addMul(Rational n1, Rational n2) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		BigInteger p1 = n1.p.multiply(n2.p);
		BigInteger q1 = n1.q.multiply(n2.q);
		p = p0.multiply(q1).add(q0.multiply(p1));
		q = q0.multiply(q1);
	}

	@Override
	public void addMul(Rational n1, Rational n2, Rational n3) {
		BigInteger p0 = p;
		BigInteger q0 = q;
		BigInteger p1 = n1.p.multiply(n2.p).multiply(n3.p);
		BigInteger q1 = n1.q.multiply(n2.q).multiply(n3.q);
		p = p0.multiply(q1).add(q0.multiply(p1));
		q = q0.multiply(q1);
	}

	@Override
	public Rational div(Rational n1) {
		return new Rational(p.multiply(n1.q), q.multiply(n1.p));
	}

	@Override
	public Rational gcd(Rational n1) {
		return __1;
	}
}