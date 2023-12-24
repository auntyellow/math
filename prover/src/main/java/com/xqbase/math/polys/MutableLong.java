package com.xqbase.math.polys;

public class MutableLong extends MutableNumber<MutableLong> {
	private static final long serialVersionUID = 1L;

	private long[] n;

	public MutableLong(long n) {
		this.n = new long[] {n};
	}

	public MutableLong(String s) {
		this(Long.parseLong(s));
	}

	@Override
	public int intValue() {
		return (int) n[0];
	}

	@Override
	public long longValue() {
		return n[0];
	}

	@Override
	public float floatValue() {
		return n[0];
	}

	@Override
	public double doubleValue() {
		return n[0];
	}

	@Override
	public String toString() {
		return Long.toString(n[0]);
	}

	@Override
	public int hashCode() {
		return Long.hashCode(n[0]);
	}

	@Override
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (!(o instanceof MutableLong)) {
			return false;
		}
		return n[0] == ((MutableLong) o).n[0];
	}

	@Override
	public int compareTo(MutableLong o) {
		return Long.compare(n[0], o.n[0]);
	}

	@Override
	public MutableLong negate() {
		return new MutableLong(-n[0]);
	}

	@Override
	public int signum() {
		return Long.signum(n[0]);
	}

	@Override
	public void add(MutableLong n1) {
		n[0] = Math.addExact(n[0], n1.n[0]);
	}

	@Override
	public void addMul(MutableLong n1, MutableLong n2) {
		n[0] = Math.addExact(n[0], Math.multiplyExact(n1.n[0], n2.n[0]));
	}

	@Override
	public void addMul(MutableLong n1, MutableLong n2, MutableLong n3) {
		n[0] = Math.addExact(n[0], Math.multiplyExact(Math.multiplyExact(n1.n[0], n2.n[0]), n3.n[0]));
	}
}