package com.xqbase.math.geometry;

import com.xqbase.math.polys.Poly;

public class Circle {
	private Poly a, d, e, f;

	public Circle(Poly a, Poly d, Poly e, Poly f) {
		this.a = a;
		this.d = d;
		this.e = e;
		this.f = f;
	}

	public Circle(Point p1, Point p2, Point p3) {
		Poly[] r1 = row(p1);
		Poly[] r2 = row(p2);
		Poly[] r3 = row(p3);
		a = Poly.det(r1[1], r1[2], r1[3], r2[1], r2[2], r2[3], r3[1], r3[2], r3[3]);
		d = new Poly().add(-1, Poly.det(r1[0], r1[2], r1[3], r2[0], r2[2], r2[3], r3[0], r3[2], r3[3]));
		e = Poly.det(r1[0], r1[1], r1[3], r2[0], r2[1], r2[3], r3[0], r3[1], r3[3]);
		f = new Poly().add(-1, Poly.det(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]));
	}

	public Point getCenter() {
		return new Point(d, e, new Poly().add(-2, a));
	}

	public boolean passesThrough(Point p) {
		Poly[] r = row(p);
		return new Poly().addMul(1, a, r[0]).addMul(1, d, r[1]).addMul(1, e, r[2]).addMul(1, f, r[3]).isEmpty();
	}

	/** pick the other point P1 lies on this circle, such that PP1's direction is (x, y) */
	public Point pickPoint(Point p, Poly x, Poly y) {
		return p.reflect(new Point(new Line(p, x, y), new Line(getCenter(), y, new Poly().add(-1, x))));
	}

	@Override
	public String toString() {
		return "(" + a + ")*(x**2 + y**2) + (" + d + ")*x*z + (" + e + ")*y*z + (" + f + ")*z**2 = 0";
	}

	private static Poly[] row(Point p) {
		Poly x = p.getX();
		Poly y = p.getY();
		Poly z = p.getZ();
		return new Poly[] {
			new Poly().addMul(1, x, x).addMul(1, y, y),
			new Poly().addMul(1, x, z),
			new Poly().addMul(1, y, z),
			new Poly().addMul(1, z, z),
		};
	}

	public static boolean concyclic(Point p1, Point p2, Point p3, Point p4) {
		Poly[] r1 = row(p1);
		Poly[] r2 = row(p2);
		Poly[] r3 = row(p3);
		Poly[] r4 = row(p4);
		return Poly.det(
				r1[0], r1[1], r1[2], r1[3],
				r2[0], r2[1], r2[2], r2[3],
				r3[0], r3[1], r3[2], r3[3],
				r4[0], r4[1], r4[2], r4[3]).isEmpty();
	}
}