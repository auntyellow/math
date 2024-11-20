package com.xqbase.math.geometry;

import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.Poly;

public class Point {
	private LongPoly x, y, z;

	public Point(LongPoly x, LongPoly y, LongPoly z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public Point(Line l1, Line l2) {
		x = Poly.det(l1.getV(), l1.getW(), l2.getV(), l2.getW());
		y = Poly.det(l1.getW(), l1.getU(), l2.getW(), l2.getU());
		z = Poly.det(l1.getU(), l1.getV(), l2.getU(), l2.getV());
	}

	public LongPoly getX() {
		return x;
	}

	public LongPoly getY() {
		return y;
	}

	public LongPoly getZ() {
		return z;
	}

	public boolean liesOn(Line l) {
		return x.newPoly().addMul(x, l.getU()).addMul(y, l.getV()).addMul(z, l.getW()).isEmpty();
	}

	/** reflect this about p */
	public Point reflect(Point p) {
		return new Point(
				x.newPoly().addMul(2, z, p.getX()).subMul(x, p.getZ()),
				x.newPoly().addMul(2, z, p.getY()).subMul(y, p.getZ()),
				x.newPoly().addMul(z, p.getZ()));
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ", " + z + ")";
	}

	public static Point midpoint(Point p1, Point p2) {
		LongPoly x = p1.getX();
		return new Point(
				x.newPoly().addMul(p1.getX(), p2.getZ()).addMul(p1.getZ(), p2.getX()),
				x.newPoly().addMul(p1.getY(), p2.getZ()).addMul(p1.getZ(), p2.getY()),
				x.newPoly().addMul(2, p1.getZ(), p2.getZ()));
	}

	public static boolean collinear(Point p1, Point p2, Point p3) {
		return Poly.det(
				p1.getX(), p1.getY(), p1.getZ(),
				p2.getX(), p2.getY(), p2.getZ(),
				p3.getX(), p3.getY(), p3.getZ()).isEmpty();
	}
}