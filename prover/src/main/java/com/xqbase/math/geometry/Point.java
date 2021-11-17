package com.xqbase.math.geometry;

import com.xqbase.math.polys.Poly;

public class Point {
	private Poly x, y, z;

	public Point(Poly x, Poly y, Poly z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public Point(Line l1, Line l2) {
		x = Poly.det(l1.getV(), l1.getW(), l2.getV(), l2.getW());
		y = Poly.det(l1.getW(), l1.getU(), l2.getW(), l2.getU());
		z = Poly.det(l1.getU(), l1.getV(), l2.getU(), l2.getV());
	}

	public Poly getX() {
		return x;
	}

	public Poly getY() {
		return y;
	}

	public Poly getZ() {
		return z;
	}

	public boolean liesOn(Line l) {
		return new Poly().addMul(1, x, l.getU()).addMul(1, y, l.getV()).addMul(1, z, l.getW()).isEmpty();
	}

	/** reflect this about p */
	public Point reflect(Point p) {
		return new Point(
				new Poly().addMul(2, z, p.getX()).addMul(-1, x, p.getZ()),
				new Poly().addMul(2, z, p.getY()).addMul(-1, y, p.getZ()),
				new Poly().addMul(1, z, p.getZ()));
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ", " + z + ")";
	}

	public static Point midpoint(Point p1, Point p2) {
		return new Point(
				new Poly().addMul(1, p1.getX(), p2.getZ()).addMul(1, p1.getZ(), p2.getX()),
				new Poly().addMul(1, p1.getY(), p2.getZ()).addMul(1, p1.getZ(), p2.getY()),
				new Poly().addMul(2, p1.getZ(), p2.getZ()));
	}

	public static boolean collinear(Point p1, Point p2, Point p3) {
		return Poly.det(
				p1.getX(), p1.getY(), p1.getZ(),
				p2.getX(), p2.getY(), p2.getZ(),
				p3.getX(), p3.getY(), p3.getZ()).isEmpty();
	}
}