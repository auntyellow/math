package com.xqbase.math.geometry;

import com.xqbase.math.polys.Poly;

public class Line {
	private Poly u, v, w;

	public Line(Poly u, Poly v, Poly w) {
		this.u = u;
		this.v = v;
		this.w = w;
	}

	/** a line passing through p1 and p2 */
	public Line(Point p1, Point p2) {
		u = Poly.det(p1.getY(), p1.getZ(), p2.getY(), p2.getZ());
		v = Poly.det(p1.getZ(), p1.getX(), p2.getZ(), p2.getX());
		w = Poly.det(p1.getX(), p1.getY(), p2.getX(), p2.getY());
	}

	/** a line passing through p and parallel to direction (x, y) */
	public Line(Point p, Poly x, Poly y) {
		u = new Poly().addMul(1, p.getZ(), y);
		v = new Poly().addMul(-1, p.getZ(), x);
		w = new Poly().addMul(1, p.getY(), x).addMul(-1, p.getX(), y);
	}

	public Poly getU() {
		return u;
	}

	public Poly getV() {
		return v;
	}

	public Poly getW() {
		return w;
	}

	public boolean passesThrough(Point p) {
		Poly g = new Poly();
		g.addMul(1, u, p.getX());
		g.addMul(1, v, p.getY());
		g.addMul(1, w, p.getZ());
		return g.isEmpty();
	}

	@Override
	public String toString() {
		return "[" + u + ", " + v + ", " + w + "]";
	}

	public static boolean concurrent(Line l1, Line l2, Line l3) {
		return Poly.det(
				l1.getU(), l1.getV(), l1.getW(),
				l2.getU(), l2.getV(), l2.getW(),
				l3.getU(), l3.getV(), l3.getW()).isEmpty();
	}
}