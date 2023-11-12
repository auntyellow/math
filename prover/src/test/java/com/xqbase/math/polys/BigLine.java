package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigLine {
	private static final BigInteger _1 = BigInteger.ONE;
	private static final BigInteger __1 = _1.negate();

	private BigPoly u, v, w;

	public BigLine(BigPoly u, BigPoly v, BigPoly w) {
		this.u = u;
		this.v = v;
		this.w = w;
	}

	/** a line passing through p1 and p2 */
	public BigLine(BigPoint p1, BigPoint p2) {
		u = BigPoly.det(p1.getY(), p1.getZ(), p2.getY(), p2.getZ());
		v = BigPoly.det(p1.getZ(), p1.getX(), p2.getZ(), p2.getX());
		w = BigPoly.det(p1.getX(), p1.getY(), p2.getX(), p2.getY());
	}

	/** a line passing through p and parallel to direction (x, y) */
	public BigLine(BigPoint p, BigPoly x, BigPoly y) {
		u = new BigPoly().addMul(_1, p.getZ(), y);
		v = new BigPoly().addMul(__1, p.getZ(), x);
		w = new BigPoly().addMul(_1, p.getY(), x).addMul(__1, p.getX(), y);
	}

	public BigPoly getU() {
		return u;
	}

	public BigPoly getV() {
		return v;
	}

	public BigPoly getW() {
		return w;
	}

	public boolean passesThrough(BigPoint p) {
		BigPoly g = new BigPoly();
		g.addMul(_1, u, p.getX());
		g.addMul(_1, v, p.getY());
		g.addMul(_1, w, p.getZ());
		return g.isEmpty();
	}

	@Override
	public String toString() {
		return "[" + u + ", " + v + ", " + w + "]";
	}

	public static boolean concurrent(BigLine l1, BigLine l2, BigLine l3) {
		return BigPoly.det(
				l1.getU(), l1.getV(), l1.getW(),
				l2.getU(), l2.getV(), l2.getW(),
				l3.getU(), l3.getV(), l3.getW()).isEmpty();
	}
}