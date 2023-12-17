package com.xqbase.math.geometry;

import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.MutableLong;
import com.xqbase.math.polys.Poly;

public class Circle {
	private static final MutableLong _1 = new MutableLong(1);
	private static final MutableLong __1 =new MutableLong(-1);
	private static final MutableLong __2 =new MutableLong(-2);

	private LongPoly a, d, e, f;

	public Circle(LongPoly a, LongPoly d, LongPoly e, LongPoly f) {
		this.a = a;
		this.d = d;
		this.e = e;
		this.f = f;
	}

	public Circle(Point p1, Point p2, Point p3) {
		LongPoly[] r1 = row(p1);
		LongPoly[] r2 = row(p2);
		LongPoly[] r3 = row(p3);
		a = Poly.det(r1[1], r1[2], r1[3], r2[1], r2[2], r2[3], r3[1], r3[2], r3[3]);
		d = (LongPoly) new LongPoly().add(__1, Poly.det(r1[0], r1[2], r1[3], r2[0], r2[2], r2[3], r3[0], r3[2], r3[3]));
		e = Poly.det(r1[0], r1[1], r1[3], r2[0], r2[1], r2[3], r3[0], r3[1], r3[3]);
		f = (LongPoly) new LongPoly().add(__1, Poly.det(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]));
	}

	public Point getCenter() {
		return new Point(d, e, (LongPoly) new LongPoly().add(__2, a));
	}

	public boolean passesThrough(Point p) {
		LongPoly[] r = row(p);
		return new LongPoly().addMul(_1, a, r[0]).addMul(_1, d, r[1]).addMul(_1, e, r[2]).addMul(_1, f, r[3]).isEmpty();
	}

	/** pick the other point P1 lies on this circle, such that PP1's direction is (x, y) */
	public Point pickPoint(Point p, LongPoly x, LongPoly y) {
		return p.reflect(new Point(new Line(p, x, y), new Line(getCenter(), y, (LongPoly) new LongPoly().add(__1, x))));
	}

	@Override
	public String toString() {
		return "(" + a + ")*(x**2 + y**2) + (" + d + ")*x*z + (" + e + ")*y*z + (" + f + ")*z**2 = 0";
	}

	private static LongPoly[] row(Point p) {
		LongPoly x = p.getX();
		LongPoly y = p.getY();
		LongPoly z = p.getZ();
		return new LongPoly[] {
			(LongPoly) new LongPoly().addMul(_1, x, x).addMul(_1, y, y),
			(LongPoly) new LongPoly().addMul(_1, x, z),
			(LongPoly) new LongPoly().addMul(_1, y, z),
			(LongPoly) new LongPoly().addMul(_1, z, z),
		};
	}

	public static boolean concyclic(Point p1, Point p2, Point p3, Point p4) {
		LongPoly[] r1 = row(p1);
		LongPoly[] r2 = row(p2);
		LongPoly[] r3 = row(p3);
		LongPoly[] r4 = row(p4);
		return Poly.det(
				r1[0], r1[1], r1[2], r1[3],
				r2[0], r2[1], r2[2], r2[3],
				r3[0], r3[1], r3[2], r3[3],
				r4[0], r4[1], r4[2], r4[3]).isEmpty();
	}
}