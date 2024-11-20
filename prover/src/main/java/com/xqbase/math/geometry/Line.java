package com.xqbase.math.geometry;

import java.util.List;

import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.Poly;

public class Line {
	private static LongPoly __(List<String> vars) {
		return new LongPoly(vars);
	}

	private LongPoly u, v, w;

	public Line(LongPoly u, LongPoly v, LongPoly w) {
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
	public Line(Point p, LongPoly x, LongPoly y) {
		List<String> vars = p.getX().getVars();
		u = __(vars).addMul(p.getZ(), y);
		v = __(vars).subMul(p.getZ(), x);
		w = __(vars).addMul(p.getY(), x).subMul(p.getX(), y);
	}

	public LongPoly getU() {
		return u;
	}

	public LongPoly getV() {
		return v;
	}

	public LongPoly getW() {
		return w;
	}

	public boolean passesThrough(Point p) {
		LongPoly g = __(p.getX().getVars());
		g.addMul(u, p.getX());
		g.addMul(v, p.getY());
		g.addMul(w, p.getZ());
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