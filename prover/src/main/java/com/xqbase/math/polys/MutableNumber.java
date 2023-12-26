package com.xqbase.math.polys;

public abstract class MutableNumber<T> extends Number implements Comparable<T> {
	private static final long serialVersionUID = 1L;

	public abstract T negate();
	public abstract int signum();
	public abstract void add(T n1);
	public abstract void addMul(T n1, T n2);
	public abstract void addMul(T n1, T n2, T n3);
	public abstract T div(T n1);
	public abstract T gcd(T n1);
}