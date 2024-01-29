package com.xqbase.math.polys;

import java.math.BigInteger;

public class Rational extends MutableNumber<Rational> {
	private static final long serialVersionUID = 1L;
	private static final BigInteger _0 = BigInteger.ZERO;
	private static final BigInteger _1 = BigInteger.ONE;
	private static final Rational __1 = new Rational(_1);

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
		return p.floatValue()/q.floatValue();
	}

	@Override
	public double doubleValue() {
		return p.doubleValue()/q.doubleValue();
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
		return __1;
	}
}