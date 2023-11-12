package com.xqbase.math.polys;

public class BigPascal {
	private static final String VARS = "abcdef";

	private static BigPoint P(String x, String y, String z) {
		return new BigPoint(new BigPoly(VARS, x), new BigPoly(VARS, y), new BigPoly(VARS, z));
	}

	public static void main(String[] args) {
		BigPoint a = P("0", "0", "1");
		BigPoint b = P("1", "0", "1");
		BigPoint c = P("a", "b", "1");
		BigCircle circle = new BigCircle(a, b, c);
		System.out.println("Circle: " + circle);
		BigPoly one = new BigPoly(VARS, "1");
		BigPoint d = circle.pickPoint(a, one, new BigPoly(VARS, "d"));
		System.out.println("D: " + d);
		System.out.println("Is D on circle? " + circle.passesThrough(d));
		BigPoint e = circle.pickPoint(a, one, new BigPoly(VARS, "e"));
		System.out.println("E: " + e);
		System.out.println("Is E on circle? " + circle.passesThrough(e));
		BigPoint f = circle.pickPoint(a, one, new BigPoly(VARS, "f"));
		System.out.println("F: " + f);
		System.out.println("Is F on circle? " + circle.passesThrough(f));
		BigLine ab = new BigLine(a, b);
		System.out.println("AB: " + ab);
		BigLine bc = new BigLine(b, c);
		System.out.println("BC: " + bc);
		BigLine cd = new BigLine(c, d);
		System.out.println("CD: " + cd);
		BigLine de = new BigLine(d, e);
		System.out.println("DE: " + de);
		BigLine ef = new BigLine(e, f);
		System.out.println("EF: " + ef);
		BigLine fa = new BigLine(f, a);
		System.out.println("FA: " + fa);
		BigPoint g = new BigPoint(ab, de);
		System.out.println("G: " + g);
		BigPoint h = new BigPoint(bc, ef);
		System.out.println("H: " + h);
		BigPoint j = new BigPoint(cd, fa);
		System.out.println("J: " + j);
		System.out.println("Are G, H and J collinear? " + BigPoint.collinear(g, h, j));
	}
}