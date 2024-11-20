package com.xqbase.math.geometry;

import java.util.Arrays;
import java.util.List;

import com.xqbase.math.polys.LongPoly;

public class Pascal {
	private static final List<String> VARS = Arrays.asList("a", "b", "c", "d", "e", "f");

	private static Point P(String x, String y, String z) {
		return new Point(new LongPoly(VARS, x), new LongPoly(VARS, y), new LongPoly(VARS, z));
	}

	public static void main(String[] args) {
		Point a = P("0", "0", "1");
		Point b = P("1", "0", "1");
		Point c = P("a", "b", "1");
		Circle circle = new Circle(a, b, c);
		System.out.println("Circle: " + circle);
		LongPoly one = new LongPoly(VARS, "1");
		Point d = circle.pickPoint(a, one, new LongPoly(VARS, "d"));
		System.out.println("D: " + d);
		System.out.println("Is D on circle? " + circle.passesThrough(d));
		Point e = circle.pickPoint(a, one, new LongPoly(VARS, "e"));
		System.out.println("E: " + e);
		System.out.println("Is E on circle? " + circle.passesThrough(e));
		Point f = circle.pickPoint(a, one, new LongPoly(VARS, "f"));
		System.out.println("F: " + f);
		System.out.println("Is F on circle? " + circle.passesThrough(f));
		Line ab = new Line(a, b);
		System.out.println("AB: " + ab);
		Line bc = new Line(b, c);
		System.out.println("BC: " + bc);
		Line cd = new Line(c, d);
		System.out.println("CD: " + cd);
		Line de = new Line(d, e);
		System.out.println("DE: " + de);
		Line ef = new Line(e, f);
		System.out.println("EF: " + ef);
		Line fa = new Line(f, a);
		System.out.println("FA: " + fa);
		Point g = new Point(ab, de);
		System.out.println("G: " + g);
		Point h = new Point(bc, ef);
		System.out.println("H: " + h);
		Point j = new Point(cd, fa);
		System.out.println("J: " + j);
		System.out.println("Are G, H and J collinear? " + Point.collinear(g, h, j));
	}
}