package com.xqbase.math.geometry;

import com.xqbase.math.polys.Poly;

public class Pascal {
	private static final int VARS = 7;

	private static Point P(String x, String y, String z) {
		return new Point(new Poly(VARS, x), new Poly(VARS, y), new Poly(VARS, z));
	}

	public static void main(String[] args) {
		Point a = P("0", "0", "1");
		Point b = P("1", "0", "1");
		Point c = P("a", "b", "1");
		System.out.println(new Circle(a, b, c).getCenter());
	}
}