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
		d = Poly.det(r1[0], r1[2], r1[3], r2[0], r2[2], r2[3], r3[0], r3[2], r3[3]);
		d.mul(-1);
		e = Poly.det(r1[0], r1[1], r1[3], r2[0], r2[1], r2[3], r3[0], r3[1], r3[3]);
		f = Poly.det(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]);
		f.mul(-1);
	}

	public Point getCenter() {
		Poly x = new Poly();
		Poly y = new Poly();
		Poly z = new Poly();
		x.add(-1, d);
		y.add(-1, e);
		z.add(2, a);
		return new Point(x, y, z);
	}

	public boolean passesThrough(Point p) {
		Poly g = new Poly();
		Poly[] r = row(p);
		g.addMul(1, a, r[0]);
		g.addMul(1, d, r[1]);
		g.addMul(1, e, r[2]);
		g.addMul(1, f, r[3]);
		return g.isEmpty();
	}

	private static Poly[] row(Point p) {
		Poly x = p.getX();
		Poly y = p.getY();
		Poly z = p.getZ();
		Poly[] r = {new Poly(), new Poly(), new Poly(), new Poly()};
		r[0].addMul(1, x, x);
		r[0].addMul(1, y, y);
		r[1].addMul(1, x, z);
		r[2].addMul(1, y, z);
		r[3].addMul(1, z, z);
		return r;
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