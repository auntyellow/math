package com.xqbase.math.polys;

public abstract class MutableNumber<T> extends Number implements Comparable<T> {
	private static final long serialVersionUID = 1L;

	public abstract T negate();
	public abstract int signum();
	protected abstract void add(T n1);
	protected abstract T multiply(T n1);
	protected abstract T multiply(T n1, T n2);
}