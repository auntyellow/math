package com.xqbase.math.polys;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.geometry.Circle;
import com.xqbase.math.geometry.Line;
import com.xqbase.math.geometry.Point;
import com.xqbase.math.polys.Poly;

public class PolyTest {
	private static final String VARS_7 = "abcdefg";
	private static final String VARS_16 = VARS_7 + "hijklmnop";
	private static final String VARS_19 = VARS_16 + "qrs";

	// Results from pentagon.py, A3B1A4 and C4
	private static final String A = "b**2*d*e*g**2 - b**2*e**2*f*g - b*c*d**2*g**2 + b*c*e**2*f**2 + c**2*d**2*f*g - c**2*d*e*f**2";
	private static final String D = "-b**2*d*e*f + b**2*d*f*g - b**2*e**2*g + b**2*e*g**2 + b*c*d**2*f - b*c*d*f**2 - b*c*d*g**2 + b*c*e**2*f - b*d**2*f*g + b*d*e*f**2 + b*d*e*g**2 - b*e**2*f*g + c**2*d**2*g - c**2*d*e*f + c**2*d*f*g - c**2*e*f**2 - c*d**2*g**2 + c*e**2*f**2";
	private static final String E = "b**2*d*e*g + b**2*d*g**2 - b**2*e**2*f - b**2*e*f*g - b*c*d**2*g - b*c*e**2*g + b*c*e*f**2 + b*c*e*g**2 - b*d**2*g**2 + b*e**2*f**2 + c**2*d**2*f + c**2*d*e*g - c**2*d*f**2 - c**2*e*f*g + c*d**2*f*g - c*d*e*f**2 - c*d*e*g**2 + c*e**2*f*g";
	private static final String F = "b**2*d*g - b**2*e*f - b*d**2*g - b*e**2*g + b*e*f**2 + b*e*g**2 + c**2*d*g - c**2*e*f + c*d**2*f - c*d*f**2 - c*d*g**2 + c*e**2*f";
	private static final String X = "b**2*c**2*d*e**2*g**2 - b**2*c**2*d*e*g**3 - b**2*c**2*e**3*f*g + b**2*c**2*e**2*f*g**2 - b**2*c*d*e**3*g**2 + b**2*c*d*e*g**4 + b**2*c*e**4*f*g - b**2*c*e**2*f*g**3 + b**2*d*e**3*g**3 - b**2*d*e**2*g**4 - b**2*e**4*f*g**2 + b**2*e**3*f*g**3 - b*c**3*d**2*e*g**2 + b*c**3*d**2*g**3 + b*c**3*e**3*f**2 - b*c**3*e**2*f**2*g + b*c**2*d**2*e**2*g**2 - b*c**2*d**2*g**4 - b*c**2*e**4*f**2 + b*c**2*e**2*f**2*g**2 - b*c*d**2*e**2*g**3 + b*c*d**2*e*g**4 + b*c*e**4*f**2*g - b*c*e**3*f**2*g**2 + c**4*d**2*e*f*g - c**4*d**2*f*g**2 - c**4*d*e**2*f**2 + c**4*d*e*f**2*g - c**3*d**2*e**2*f*g + c**3*d**2*f*g**3 + c**3*d*e**3*f**2 - c**3*d*e*f**2*g**2 + c**2*d**2*e**2*f*g**2 - c**2*d**2*e*f*g**3 - c**2*d*e**3*f**2*g + c**2*d*e**2*f**2*g**2";
	private static final String Y = "-b**2*c**2*d**2*g**3 + b**2*c**2*d*e**2*f*g + b**2*c**2*d*e*f*g**2 - b**2*c**2*e**3*f**2 + 2*b**2*c*d**2*e*g**3 - b**2*c*d*e**3*f*g - 2*b**2*c*d*e**2*f*g**2 - b**2*c*d*e*f*g**3 - b**2*c*e**4*g**2 + 2*b**2*c*e**3*f**2*g + 2*b**2*c*e**3*g**3 - b**2*c*e**2*g**4 - b**2*d**2*e**2*g**3 + b**2*d*e**3*f*g**2 + b**2*d*e**2*f*g**3 - b**2*e**3*f**2*g**2 - b*c**3*d**2*e*f*g + b*c**3*d**2*f*g**2 + b*c**3*d*e**2*f**2 + b*c**3*d*e**2*g**2 - b*c**3*d*e*f**2*g - b*c**3*d*e*g**3 - b*c**3*e**3*f*g + b*c**3*e**2*f*g**2 + b*c**2*d**2*e**2*f*g - 2*b*c**2*d**2*e*f*g**2 + b*c**2*d**2*f*g**3 + b*c**2*d*e**3*f**2 + b*c**2*d*e**3*g**2 - 2*b*c**2*d*e**2*f**2*g - 2*b*c**2*d*e**2*g**3 + b*c**2*d*e*f**2*g**2 + b*c**2*d*e*g**4 + b*c**2*e**4*f*g - 2*b*c**2*e**3*f*g**2 + b*c**2*e**2*f*g**3 + b*c*d**2*e**2*f*g**2 - b*c*d**2*e*f*g**3 - b*c*d*e**3*f**2*g - b*c*d*e**3*g**3 + b*c*d*e**2*f**2*g**2 + b*c*d*e**2*g**4 + b*c*e**4*f*g**2 - b*c*e**3*f*g**3 - c**4*d**2*e*g**2 + c**4*d*e**2*f*g + c**4*d*e*f*g**2 - c**4*e**2*f**2*g - c**3*d**2*e**2*f**2 + 2*c**3*d**2*e*f**2*g + 2*c**3*d**2*e*g**3 - c**3*d**2*f**2*g**2 - c**3*d*e**3*f*g - 2*c**3*d*e**2*f*g**2 - c**3*d*e*f*g**3 + 2*c**3*e**3*f**2*g - c**2*d**2*e*g**4 + c**2*d*e**3*f*g**2 + c**2*d*e**2*f*g**3 - c**2*e**4*f**2*g";
	private static final String Z = "b**2*c**2*d**2*g**4 - 2*b**2*c**2*d*e**2*f*g**2 + b**2*c**2*e**4*f**2 + b**2*c**2*e**4*g**2 - 2*b**2*c**2*e**3*g**3 + b**2*c**2*e**2*g**4 - 2*b**2*c*d**2*e*g**4 + 2*b**2*c*d*e**3*f*g**2 + 2*b**2*c*d*e**2*f*g**3 - 2*b**2*c*e**4*f**2*g + b**2*d**2*e**2*g**4 - 2*b**2*d*e**3*f*g**3 + b**2*e**4*f**2*g**2 + 2*b*c**3*d**2*e*f*g**2 - 2*b*c**3*d**2*f*g**3 - 2*b*c**3*d*e**3*f**2 - 2*b*c**3*d*e**3*g**2 + 2*b*c**3*d*e**2*f**2*g + 2*b*c**3*d*e**2*g**3 + 2*b*c**3*e**3*f*g**2 - 2*b*c**3*e**2*f*g**3 - 2*b*c**2*d**2*e**2*f*g**2 + 2*b*c**2*d**2*e*f*g**3 + 2*b*c**2*d*e**3*f**2*g + 2*b*c**2*d*e**3*g**3 - 2*b*c**2*d*e**2*f**2*g**2 - 2*b*c**2*d*e**2*g**4 - 2*b*c**2*e**4*f*g**2 + 2*b*c**2*e**3*f*g**3 + c**4*d**2*e**2*f**2 + c**4*d**2*e**2*g**2 - 2*c**4*d**2*e*f**2*g + c**4*d**2*f**2*g**2 - 2*c**4*d*e**2*f*g**2 + c**4*e**2*f**2*g**2 - 2*c**3*d**2*e**2*g**3 + 2*c**3*d*e**3*f*g**2 + 2*c**3*d*e**2*f*g**3 - 2*c**3*e**3*f**2*g**2 + c**2*d**2*e**2*g**4 - 2*c**2*d*e**3*f*g**3 + c**2*e**4*f**2*g**2";

	@BeforeClass
	public static void startup() {
		// https://stackoverflow.com/a/6308286/4260959
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
	}

	@Test
	public void testParse() {
		Assert.assertEquals("0", new Poly().toString());
		Assert.assertTrue(new Poly("", "0").isEmpty());
		for (int i = -100; i <= 100; i ++) {
			String expr = "" + i;
			Assert.assertEquals(expr, "" + new Poly(VARS_7, expr));
		}
		Assert.assertEquals(A, "" + new Poly(VARS_7, A));
		Assert.assertEquals(D, "" + new Poly(VARS_7, D));
		Assert.assertEquals(E, "" + new Poly(VARS_7, E));
		Assert.assertEquals(F, "" + new Poly(VARS_7, F));
		Assert.assertEquals(X, "" + new Poly(VARS_7, X));
		Assert.assertEquals(Y, "" + new Poly(VARS_7, Y));
		Assert.assertEquals(Z, "" + new Poly(VARS_7, Z));
	}

	private static Point P(String x, String y, String z) {
		return new Point(new Poly(VARS_7, x), new Poly(VARS_7, y), new Poly(VARS_7, z));
	}

	@Test
	public void testOnCircle() {
		Point p = P(X, Y, Z);
		Circle c = new Circle(new Poly(VARS_7, A), new Poly(VARS_7, D), new Poly(VARS_7, E), new Poly(VARS_7, F));
		Assert.assertTrue(c.passesThrough(p));
	}

	@Test
	public void testDet() {
		// Matrix([[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]).det()
		String expected = "a*f*k*p - a*f*l*o - a*g*j*p + a*g*l*n + a*h*j*o - a*h*k*n - b*e*k*p + b*e*l*o + b*g*i*p - b*g*l*m - b*h*i*o + b*h*k*m + c*e*j*p - c*e*l*n - c*f*i*p + c*f*l*m + c*h*i*n - c*h*j*m - d*e*j*o + d*e*k*n + d*f*i*o - d*f*k*m - d*g*i*n + d*g*j*m";
		Poly[][] m = new Poly[4][4];
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				m[i][j] = new Poly(VARS_16, "" + (char) ('a' + i * 4 + j));
			}
		}
		Assert.assertEquals(expected, Poly.det(
				m[0][0], m[0][1], m[0][2], m[0][3],
				m[1][0], m[1][1], m[1][2], m[1][3],
				m[2][0], m[2][1], m[2][2], m[2][3],
				m[3][0], m[3][1], m[3][2], m[3][3]).toString());
		// Results from pappus-h.py
		Poly x_G = new Poly(VARS_19, "-a**2*h*n*p + a**2*j*m*p + a*b*g*n*p - a*b*j*k*p - a*c*g*m*p + a*c*h*k*p - a*d*h*n*q + a*d*j*m*q - a*e*j*k*q + a*f*h*k*q + b*d*g*n*q - b*f*g*k*q - c*d*g*m*q + c*e*g*k*q");
		Poly y_G = new Poly(VARS_19, "-a*b*h*n*p + a*b*j*m*p - a*e*h*n*q + a*f*h*m*q + b**2*g*n*p - b**2*j*k*p - b*c*g*m*p + b*c*h*k*p + b*d*j*m*q + b*e*g*n*q - b*e*j*k*q - b*f*g*m*q - c*d*h*m*q + c*e*h*k*q");
		Poly z_G = new Poly(VARS_19, "-a*c*h*n*p + a*c*j*m*p - a*e*j*n*q + a*f*j*m*q + b*c*g*n*p - b*c*j*k*p + b*d*j*n*q - b*f*j*k*q - c**2*g*m*p + c**2*h*k*p - c*d*h*n*q + c*e*g*n*q - c*f*g*m*q + c*f*h*k*q");
		Poly x_H = new Poly(VARS_19, "-a*d*h*n*p*s + a*d*j*m*p*s + a*e*g*j*p*r + a*e*g*n*p*s - a*f*g*h*p*r - a*f*g*m*p*s - b*d*g*j*p*r - b*d*j*k*p*s + b*f*g**2*p*r + b*f*g*k*p*s + c*d*g*h*p*r + c*d*h*k*p*s - c*e*g**2*p*r - c*e*g*k*p*s - d**2*h*n*q*s + d**2*j*m*q*s + d*e*g*n*q*s - d*e*j*k*q*s - d*f*g*m*q*s + d*f*h*k*q*s");
		Poly y_H = new Poly(VARS_19, "a*e*h*j*p*r + a*e*j*m*p*s - a*f*h**2*p*r - a*f*h*m*p*s - b*d*h*j*p*r - b*d*h*n*p*s + b*e*g*n*p*s - b*e*j*k*p*s + b*f*g*h*p*r + b*f*h*k*p*s + c*d*h**2*p*r + c*d*h*m*p*s - c*e*g*h*p*r - c*e*g*m*p*s - d*e*h*n*q*s + d*e*j*m*q*s + e**2*g*n*q*s - e**2*j*k*q*s - e*f*g*m*q*s + e*f*h*k*q*s");
		Poly z_H = new Poly(VARS_19, "a*e*j**2*p*r + a*e*j*n*p*s - a*f*h*j*p*r - a*f*h*n*p*s - b*d*j**2*p*r - b*d*j*n*p*s + b*f*g*j*p*r + b*f*g*n*p*s + c*d*h*j*p*r + c*d*j*m*p*s - c*e*g*j*p*r - c*e*j*k*p*s - c*f*g*m*p*s + c*f*h*k*p*s - d*f*h*n*q*s + d*f*j*m*q*s + e*f*g*n*q*s - e*f*j*k*q*s - f**2*g*m*q*s + f**2*h*k*q*s");
		Poly x_J = new Poly(VARS_19, "a*d*h*n*r - a*d*j*m*r + a*e*j*k*r + a*e*k*n*s - a*f*h*k*r - a*f*k*m*s - b*d*g*n*r - b*d*k*n*s + b*f*g*k*r + b*f*k**2*s + c*d*g*m*r + c*d*k*m*s - c*e*g*k*r - c*e*k**2*s");
		Poly y_J = new Poly(VARS_19, "a*e*h*n*r + a*e*m*n*s - a*f*h*m*r - a*f*m**2*s - b*d*j*m*r - b*d*m*n*s - b*e*g*n*r + b*e*j*k*r + b*f*g*m*r + b*f*k*m*s + c*d*h*m*r + c*d*m**2*s - c*e*h*k*r - c*e*k*m*s");
		Poly z_J = new Poly(VARS_19, "a*e*j*n*r + a*e*n**2*s - a*f*j*m*r - a*f*m*n*s - b*d*j*n*r - b*d*n**2*s + b*f*j*k*r + b*f*k*n*s + c*d*h*n*r + c*d*m*n*s - c*e*g*n*r - c*e*k*n*s + c*f*g*m*r - c*f*h*k*r");
		Assert.assertTrue(Poly.det(x_G, y_G, z_G, x_H, y_H, z_H, x_J, y_J, z_J).isEmpty());
		Point pg = new Point(x_G, y_G, z_G);
		Point ph = new Point(x_H, y_H, z_H);
		Point pj = new Point(x_J, y_J, z_J);
		Assert.assertTrue(Point.collinear(pg, ph, pj));
		Assert.assertTrue(new Line(pg, ph).passesThrough(pj));
		Line lg = new Line(x_G, y_G, z_G);
		Line lh = new Line(x_H, y_H, z_H);
		Line lj = new Line(x_J, y_J, z_J);
		Assert.assertTrue(Line.concurrent(lg, lh, lj));
		Assert.assertTrue(new Point(lg, lh).liesOn(lj));
		// Results from pentagon.py
		Point c4 = P(X, Y, Z);
		Point a4 = P("e - g", "-d + f", "d*g - e*f");
		Point a3 = P("c - e", "-b + d", "b*e - c*d");
		Point b1 = P("c - g", "-b + f", "b*g - c*f");
		Assert.assertTrue(Circle.concyclic(c4, a4, a3, b1));
	}
}