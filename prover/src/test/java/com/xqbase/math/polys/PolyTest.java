package com.xqbase.math.polys;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.geometry.Circle;
import com.xqbase.math.geometry.Line;
import com.xqbase.math.geometry.Point;

public class PolyTest {
	private static final String VARS_7 = "abcdefg";
	private static final String VARS_16 = VARS_7 + "hijklmnop";
	private static final String VARS_19 = VARS_16 + "qrs";
	private static final String VARS_PQUV = "pquv";

	// Results from pentagon.py, A3B1A4 and C4
	private static final String A = "b**2*d*e*g**2 - b**2*e**2*f*g - b*c*d**2*g**2 + b*c*e**2*f**2 + c**2*d**2*f*g - c**2*d*e*f**2";
	private static final String D = "-b**2*d*e*f + b**2*d*f*g - b**2*e**2*g + b**2*e*g**2 + b*c*d**2*f - b*c*d*f**2 - b*c*d*g**2 + b*c*e**2*f - b*d**2*f*g + b*d*e*f**2 + b*d*e*g**2 - b*e**2*f*g + c**2*d**2*g - c**2*d*e*f + c**2*d*f*g - c**2*e*f**2 - c*d**2*g**2 + c*e**2*f**2";
	private static final String E = "b**2*d*e*g + b**2*d*g**2 - b**2*e**2*f - b**2*e*f*g - b*c*d**2*g - b*c*e**2*g + b*c*e*f**2 + b*c*e*g**2 - b*d**2*g**2 + b*e**2*f**2 + c**2*d**2*f + c**2*d*e*g - c**2*d*f**2 - c**2*e*f*g + c*d**2*f*g - c*d*e*f**2 - c*d*e*g**2 + c*e**2*f*g";
	private static final String F = "b**2*d*g - b**2*e*f - b*d**2*g - b*e**2*g + b*e*f**2 + b*e*g**2 + c**2*d*g - c**2*e*f + c*d**2*f - c*d*f**2 - c*d*g**2 + c*e**2*f";
	private static final String X = "b**2*c**2*d*e**2*g**2 - b**2*c**2*d*e*g**3 - b**2*c**2*e**3*f*g + b**2*c**2*e**2*f*g**2 - b**2*c*d*e**3*g**2 + b**2*c*d*e*g**4 + b**2*c*e**4*f*g - b**2*c*e**2*f*g**3 + b**2*d*e**3*g**3 - b**2*d*e**2*g**4 - b**2*e**4*f*g**2 + b**2*e**3*f*g**3 - b*c**3*d**2*e*g**2 + b*c**3*d**2*g**3 + b*c**3*e**3*f**2 - b*c**3*e**2*f**2*g + b*c**2*d**2*e**2*g**2 - b*c**2*d**2*g**4 - b*c**2*e**4*f**2 + b*c**2*e**2*f**2*g**2 - b*c*d**2*e**2*g**3 + b*c*d**2*e*g**4 + b*c*e**4*f**2*g - b*c*e**3*f**2*g**2 + c**4*d**2*e*f*g - c**4*d**2*f*g**2 - c**4*d*e**2*f**2 + c**4*d*e*f**2*g - c**3*d**2*e**2*f*g + c**3*d**2*f*g**3 + c**3*d*e**3*f**2 - c**3*d*e*f**2*g**2 + c**2*d**2*e**2*f*g**2 - c**2*d**2*e*f*g**3 - c**2*d*e**3*f**2*g + c**2*d*e**2*f**2*g**2";
	private static final String Y = "-b**2*c**2*d**2*g**3 + b**2*c**2*d*e**2*f*g + b**2*c**2*d*e*f*g**2 - b**2*c**2*e**3*f**2 + 2*b**2*c*d**2*e*g**3 - b**2*c*d*e**3*f*g - 2*b**2*c*d*e**2*f*g**2 - b**2*c*d*e*f*g**3 - b**2*c*e**4*g**2 + 2*b**2*c*e**3*f**2*g + 2*b**2*c*e**3*g**3 - b**2*c*e**2*g**4 - b**2*d**2*e**2*g**3 + b**2*d*e**3*f*g**2 + b**2*d*e**2*f*g**3 - b**2*e**3*f**2*g**2 - b*c**3*d**2*e*f*g + b*c**3*d**2*f*g**2 + b*c**3*d*e**2*f**2 + b*c**3*d*e**2*g**2 - b*c**3*d*e*f**2*g - b*c**3*d*e*g**3 - b*c**3*e**3*f*g + b*c**3*e**2*f*g**2 + b*c**2*d**2*e**2*f*g - 2*b*c**2*d**2*e*f*g**2 + b*c**2*d**2*f*g**3 + b*c**2*d*e**3*f**2 + b*c**2*d*e**3*g**2 - 2*b*c**2*d*e**2*f**2*g - 2*b*c**2*d*e**2*g**3 + b*c**2*d*e*f**2*g**2 + b*c**2*d*e*g**4 + b*c**2*e**4*f*g - 2*b*c**2*e**3*f*g**2 + b*c**2*e**2*f*g**3 + b*c*d**2*e**2*f*g**2 - b*c*d**2*e*f*g**3 - b*c*d*e**3*f**2*g - b*c*d*e**3*g**3 + b*c*d*e**2*f**2*g**2 + b*c*d*e**2*g**4 + b*c*e**4*f*g**2 - b*c*e**3*f*g**3 - c**4*d**2*e*g**2 + c**4*d*e**2*f*g + c**4*d*e*f*g**2 - c**4*e**2*f**2*g - c**3*d**2*e**2*f**2 + 2*c**3*d**2*e*f**2*g + 2*c**3*d**2*e*g**3 - c**3*d**2*f**2*g**2 - c**3*d*e**3*f*g - 2*c**3*d*e**2*f*g**2 - c**3*d*e*f*g**3 + 2*c**3*e**3*f**2*g - c**2*d**2*e*g**4 + c**2*d*e**3*f*g**2 + c**2*d*e**2*f*g**3 - c**2*e**4*f**2*g";
	private static final String Z = "b**2*c**2*d**2*g**4 - 2*b**2*c**2*d*e**2*f*g**2 + b**2*c**2*e**4*f**2 + b**2*c**2*e**4*g**2 - 2*b**2*c**2*e**3*g**3 + b**2*c**2*e**2*g**4 - 2*b**2*c*d**2*e*g**4 + 2*b**2*c*d*e**3*f*g**2 + 2*b**2*c*d*e**2*f*g**3 - 2*b**2*c*e**4*f**2*g + b**2*d**2*e**2*g**4 - 2*b**2*d*e**3*f*g**3 + b**2*e**4*f**2*g**2 + 2*b*c**3*d**2*e*f*g**2 - 2*b*c**3*d**2*f*g**3 - 2*b*c**3*d*e**3*f**2 - 2*b*c**3*d*e**3*g**2 + 2*b*c**3*d*e**2*f**2*g + 2*b*c**3*d*e**2*g**3 + 2*b*c**3*e**3*f*g**2 - 2*b*c**3*e**2*f*g**3 - 2*b*c**2*d**2*e**2*f*g**2 + 2*b*c**2*d**2*e*f*g**3 + 2*b*c**2*d*e**3*f**2*g + 2*b*c**2*d*e**3*g**3 - 2*b*c**2*d*e**2*f**2*g**2 - 2*b*c**2*d*e**2*g**4 - 2*b*c**2*e**4*f*g**2 + 2*b*c**2*e**3*f*g**3 + c**4*d**2*e**2*f**2 + c**4*d**2*e**2*g**2 - 2*c**4*d**2*e*f**2*g + c**4*d**2*f**2*g**2 - 2*c**4*d*e**2*f*g**2 + c**4*e**2*f**2*g**2 - 2*c**3*d**2*e**2*g**3 + 2*c**3*d*e**3*f*g**2 + 2*c**3*d*e**2*f*g**3 - 2*c**3*e**3*f**2*g**2 + c**2*d**2*e**2*g**4 - 2*c**2*d*e**3*f*g**3 + c**2*e**4*f**2*g**2";
	// Result from isolated-fudging/imo-2001-2.py
	private static final String K2 = "17*p**2*u**6 + 158*p**2*u**5*v + 106*p**2*u**5 + 557*p**2*u**4*v**2 + 818*p**2*u**4*v - 579*p**2*u**4 + 868*p**2*u**3*v**3 + 2816*p**2*u**3*v**2 - 1620*p**2*u**3*v - 1208*p**2*u**3 + 512*p**2*u**2*v**4 + 4592*p**2*u**2*v**3 - 864*p**2*u**2*v**2 - 3792*p**2*u**2*v - 540*p**2*u**2 - 40*p**2*u*v**5 + 3208*p**2*u*v**4 + 2280*p**2*u*v**3 - 4560*p**2*u*v**2 - 1512*p**2*u*v - 100*p**2*v**6 + 520*p**2*v**5 + 1908*p**2*v**4 - 1024*p**2*v**3 - 1512*p**2*v**2 + 98*p*q*u**6 + 448*p*q*u**5*v + 756*p*q*u**5 + 770*p*q*u**4*v**2 + 4900*p*q*u**4*v - 98*p*q*u**4 + 532*p*q*u**3*v**3 + 10696*p*q*u**3*v**2 + 7980*p*q*u**3*v - 1512*p*q*u**3 - 224*p*q*u**2*v**4 + 9912*p*q*u**2*v**3 + 17276*p*q*u**2*v**2 + 5040*p*q*u**2*v - 756*p*q*u**2 - 616*p*q*u*v**5 + 4368*p*q*u*v**4 + 12544*p*q*u*v**3 + 9072*p*q*u*v**2 + 1512*p*q*u*v - 280*p*q*v**6 + 448*p*q*v**5 + 3248*p*q*v**4 + 4032*p*q*v**3 + 1512*p*q*v**2 - 288*p*u**6 - 776*p*u**5*v - 3008*p*u**5 + 204*p*u**4*v**2 - 8248*p*u**4*v - 6828*p*u**4 + 2408*p*u**3*v**3 - 6968*p*u**3*v**2 - 14552*p*u**3*v - 5944*p*u**3 + 2900*p*u**2*v**4 - 784*p*u**2*v**3 - 11416*p*u**2*v**2 - 8592*p*u**2*v - 1836*p*u**2 + 1544*p*u*v**5 + 1712*p*u*v**4 - 4288*p*u*v**3 - 6096*p*u*v**2 - 1512*p*u*v + 360*p*v**6 + 928*p*v**5 - 608*p*v**4 - 2048*p*v**3 - 1512*p*v**2 - 147*q**2*u**6 - 686*q**2*u**5*v + 98*q**2*u**5 - 1519*q**2*u**4*v**2 - 1078*q**2*u**4*v + 245*q**2*u**4 - 1960*q**2*u**3*v**3 - 1960*q**2*u**3*v**2 - 392*q**2*u**3*v - 1568*q**2*u**2*v**4 - 1960*q**2*u**2*v**3 - 588*q**2*u**2*v**2 - 784*q**2*u*v**5 - 1176*q**2*u*v**4 - 392*q**2*u*v**3 - 196*q**2*v**6 - 392*q**2*v**5 - 196*q**2*v**4 + 784*q*u**6 + 3192*q*u**5*v + 1344*q*u**5 + 6356*q*u**4*v**2 + 7448*q*u**4*v - 196*q*u**4 + 7784*q*u**3*v**3 + 16184*q*u**3*v**2 + 7784*q*u**3*v - 1512*q*u**3 + 5852*q*u**2*v**4 + 17360*q*u**2*v**3 + 17864*q*u**2*v**2 + 5040*q*u**2*v - 756*q*u**2 + 2520*q*u*v**5 + 9072*q*u*v**4 + 14112*q*u*v**3 + 9072*q*u*v**2 + 1512*q*u*v + 504*q*v**6 + 2016*q*v**5 + 4032*q*v**4 + 4032*q*v**3 + 1512*q*v**2 - 1040*u**6 - 3776*u**5*v - 4192*u**5 - 5792*u**4*v**2 - 11712*u**4*v - 6592*u**4 - 4928*u**3*v**3 - 13312*u**3*v**2 - 12736*u**3*v - 4736*u**3 - 2512*u**2*v**4 - 8512*u**2*v**3 - 9376*u**2*v**2 - 4800*u**2*v - 1296*u**2 - 768*u*v**5 - 3456*u*v**4 - 4608*u*v**3 - 1536*u*v**2 - 128*v**6 - 768*v**5 - 1536*v**4 - 1024*v**3";
	private static final String P2 = "(17*p**2 + 98*p*q - 288*p - 147*q**2 + 784*q - 1040)*u**6 + (158*p**2 + 448*p*q - 776*p - 686*q**2 + 3192*q - 3776)*u**5*v + (106*p**2 + 756*p*q - 3008*p + 98*q**2 + 1344*q - 4192)*u**5 + (557*p**2 + 770*p*q + 204*p - 1519*q**2 + 6356*q - 5792)*u**4*v**2 + (818*p**2 + 4900*p*q - 8248*p - 1078*q**2 + 7448*q - 11712)*u**4*v + (-579*p**2 - 98*p*q - 6828*p + 245*q**2 - 196*q - 6592)*u**4 + (868*p**2 + 532*p*q + 2408*p - 1960*q**2 + 7784*q - 4928)*u**3*v**3 + (2816*p**2 + 10696*p*q - 6968*p - 1960*q**2 + 16184*q - 13312)*u**3*v**2 + (-1620*p**2 + 7980*p*q - 14552*p - 392*q**2 + 7784*q - 12736)*u**3*v + (-1208*p**2 - 1512*p*q - 5944*p - 1512*q - 4736)*u**3 + (512*p**2 - 224*p*q + 2900*p - 1568*q**2 + 5852*q - 2512)*u**2*v**4 + (4592*p**2 + 9912*p*q - 784*p - 1960*q**2 + 17360*q - 8512)*u**2*v**3 + (-864*p**2 + 17276*p*q - 11416*p - 588*q**2 + 17864*q - 9376)*u**2*v**2 + (-3792*p**2 + 5040*p*q - 8592*p + 5040*q - 4800)*u**2*v + (-540*p**2 - 756*p*q - 1836*p - 756*q - 1296)*u**2 + (-40*p**2 - 616*p*q + 1544*p - 784*q**2 + 2520*q - 768)*u*v**5 + (3208*p**2 + 4368*p*q + 1712*p - 1176*q**2 + 9072*q - 3456)*u*v**4 + (2280*p**2 + 12544*p*q - 4288*p - 392*q**2 + 14112*q - 4608)*u*v**3 + (-4560*p**2 + 9072*p*q - 6096*p + 9072*q - 1536)*u*v**2 + (-1512*p**2 + 1512*p*q - 1512*p + 1512*q)*u*v + (-100*p**2 - 280*p*q + 360*p - 196*q**2 + 504*q - 128)*v**6 + (520*p**2 + 448*p*q + 928*p - 392*q**2 + 2016*q - 768)*v**5 + (1908*p**2 + 3248*p*q - 608*p - 196*q**2 + 4032*q - 1536)*v**4 + (-1024*p**2 + 4032*p*q - 2048*p + 4032*q - 1024)*v**3 + (-1512*p**2 + 1512*p*q - 1512*p + 1512*q)*v**2";

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
		assertEquals("0", new LongPoly(VARS_7).toString());
		assertTrue(new LongPoly("", "0").isEmpty());
		for (int i = -100; i <= 100; i ++) {
			String expr = "" + i;
			assertEquals(expr, "" + new LongPoly(VARS_7, expr));
		}
		assertEquals(A, "" + new LongPoly(VARS_7, A));
		assertEquals(D, "" + new LongPoly(VARS_7, D));
		assertEquals(E, "" + new LongPoly(VARS_7, E));
		assertEquals(F, "" + new LongPoly(VARS_7, F));
		assertEquals(X, "" + new LongPoly(VARS_7, X));
		assertEquals(Y, "" + new LongPoly(VARS_7, Y));
		assertEquals(Z, "" + new LongPoly(VARS_7, Z));
	}

	private static Point P(String x, String y, String z) {
		return new Point(new LongPoly(VARS_7, x), new LongPoly(VARS_7, y), new LongPoly(VARS_7, z));
	}

	@Test
	public void testOnCircle() {
		Point p = P(X, Y, Z);
		Circle c = new Circle(new LongPoly(VARS_7, A), new LongPoly(VARS_7, D), new LongPoly(VARS_7, E), new LongPoly(VARS_7, F));
		assertTrue(c.passesThrough(p));
	}

	@Test
	public void testDet() {
		// Matrix([[a, b, c, d], [e, f, g, h], [i, j, k, l], [m, n, o, p]]).det()
		String expected = "a*f*k*p - a*f*l*o - a*g*j*p + a*g*l*n + a*h*j*o - a*h*k*n - b*e*k*p + b*e*l*o + b*g*i*p - b*g*l*m - b*h*i*o + b*h*k*m + c*e*j*p - c*e*l*n - c*f*i*p + c*f*l*m + c*h*i*n - c*h*j*m - d*e*j*o + d*e*k*n + d*f*i*o - d*f*k*m - d*g*i*n + d*g*j*m";
		LongPoly[][] m = new LongPoly[4][4];
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				m[i][j] = new LongPoly(VARS_16, "" + (char) ('a' + i * 4 + j));
			}
		}
		assertEquals(expected, Poly.det(
				m[0][0], m[0][1], m[0][2], m[0][3],
				m[1][0], m[1][1], m[1][2], m[1][3],
				m[2][0], m[2][1], m[2][2], m[2][3],
				m[3][0], m[3][1], m[3][2], m[3][3]).toString());
		// Results from pappus-h.py
		LongPoly x_G = new LongPoly(VARS_19, "-a**2*h*n*p + a**2*j*m*p + a*b*g*n*p - a*b*j*k*p - a*c*g*m*p + a*c*h*k*p - a*d*h*n*q + a*d*j*m*q - a*e*j*k*q + a*f*h*k*q + b*d*g*n*q - b*f*g*k*q - c*d*g*m*q + c*e*g*k*q");
		LongPoly y_G = new LongPoly(VARS_19, "-a*b*h*n*p + a*b*j*m*p - a*e*h*n*q + a*f*h*m*q + b**2*g*n*p - b**2*j*k*p - b*c*g*m*p + b*c*h*k*p + b*d*j*m*q + b*e*g*n*q - b*e*j*k*q - b*f*g*m*q - c*d*h*m*q + c*e*h*k*q");
		LongPoly z_G = new LongPoly(VARS_19, "-a*c*h*n*p + a*c*j*m*p - a*e*j*n*q + a*f*j*m*q + b*c*g*n*p - b*c*j*k*p + b*d*j*n*q - b*f*j*k*q - c**2*g*m*p + c**2*h*k*p - c*d*h*n*q + c*e*g*n*q - c*f*g*m*q + c*f*h*k*q");
		LongPoly x_H = new LongPoly(VARS_19, "-a*d*h*n*p*s + a*d*j*m*p*s + a*e*g*j*p*r + a*e*g*n*p*s - a*f*g*h*p*r - a*f*g*m*p*s - b*d*g*j*p*r - b*d*j*k*p*s + b*f*g**2*p*r + b*f*g*k*p*s + c*d*g*h*p*r + c*d*h*k*p*s - c*e*g**2*p*r - c*e*g*k*p*s - d**2*h*n*q*s + d**2*j*m*q*s + d*e*g*n*q*s - d*e*j*k*q*s - d*f*g*m*q*s + d*f*h*k*q*s");
		LongPoly y_H = new LongPoly(VARS_19, "a*e*h*j*p*r + a*e*j*m*p*s - a*f*h**2*p*r - a*f*h*m*p*s - b*d*h*j*p*r - b*d*h*n*p*s + b*e*g*n*p*s - b*e*j*k*p*s + b*f*g*h*p*r + b*f*h*k*p*s + c*d*h**2*p*r + c*d*h*m*p*s - c*e*g*h*p*r - c*e*g*m*p*s - d*e*h*n*q*s + d*e*j*m*q*s + e**2*g*n*q*s - e**2*j*k*q*s - e*f*g*m*q*s + e*f*h*k*q*s");
		LongPoly z_H = new LongPoly(VARS_19, "a*e*j**2*p*r + a*e*j*n*p*s - a*f*h*j*p*r - a*f*h*n*p*s - b*d*j**2*p*r - b*d*j*n*p*s + b*f*g*j*p*r + b*f*g*n*p*s + c*d*h*j*p*r + c*d*j*m*p*s - c*e*g*j*p*r - c*e*j*k*p*s - c*f*g*m*p*s + c*f*h*k*p*s - d*f*h*n*q*s + d*f*j*m*q*s + e*f*g*n*q*s - e*f*j*k*q*s - f**2*g*m*q*s + f**2*h*k*q*s");
		LongPoly x_J = new LongPoly(VARS_19, "a*d*h*n*r - a*d*j*m*r + a*e*j*k*r + a*e*k*n*s - a*f*h*k*r - a*f*k*m*s - b*d*g*n*r - b*d*k*n*s + b*f*g*k*r + b*f*k**2*s + c*d*g*m*r + c*d*k*m*s - c*e*g*k*r - c*e*k**2*s");
		LongPoly y_J = new LongPoly(VARS_19, "a*e*h*n*r + a*e*m*n*s - a*f*h*m*r - a*f*m**2*s - b*d*j*m*r - b*d*m*n*s - b*e*g*n*r + b*e*j*k*r + b*f*g*m*r + b*f*k*m*s + c*d*h*m*r + c*d*m**2*s - c*e*h*k*r - c*e*k*m*s");
		LongPoly z_J = new LongPoly(VARS_19, "a*e*j*n*r + a*e*n**2*s - a*f*j*m*r - a*f*m*n*s - b*d*j*n*r - b*d*n**2*s + b*f*j*k*r + b*f*k*n*s + c*d*h*n*r + c*d*m*n*s - c*e*g*n*r - c*e*k*n*s + c*f*g*m*r - c*f*h*k*r");
		assertTrue(Poly.det(x_G, y_G, z_G, x_H, y_H, z_H, x_J, y_J, z_J).isEmpty());
		Point pg = new Point(x_G, y_G, z_G);
		Point ph = new Point(x_H, y_H, z_H);
		Point pj = new Point(x_J, y_J, z_J);
		assertTrue(Point.collinear(pg, ph, pj));
		assertTrue(new Line(pg, ph).passesThrough(pj));
		Line lg = new Line(x_G, y_G, z_G);
		Line lh = new Line(x_H, y_H, z_H);
		Line lj = new Line(x_J, y_J, z_J);
		assertTrue(Line.concurrent(lg, lh, lj));
		assertTrue(new Point(lg, lh).liesOn(lj));
		// Results from pentagon.py
		Point c4 = P(X, Y, Z);
		Point a4 = P("e - g", "-d + f", "d*g - e*f");
		Point a3 = P("c - e", "-b + d", "b*e - c*d");
		Point b1 = P("c - g", "-b + f", "b*g - c*f");
		assertTrue(Circle.concyclic(c4, a4, a3, b1));
	}

	@Test
	public void testCoeffsOf() {
		StringBuilder sb = new StringBuilder();
		new LongPoly(VARS_PQUV, K2).coeffsOf("uv").forEach((mono, coeff) -> {
			sb.append("(" + coeff + ")*" + mono + " + ");
		});
		assertEquals(P2, sb.substring(0, sb.length() - 3));
	}

	@Test
	public void testHomogenize() {
		// Result from han23-p341u.py
		String nonHomo = "a**5*b*u**2*v**2 + a**5*b*u**2*v + a**5*b*u*v**2 + a**5*b*u*v + a**5*c*u**2*v**2 + a**5*c*u**2*v + a**5*c*u*v**2 + a**5*c*u*v + a**4*b**2*u**3*v**2 + a**4*b**2*u**3*v + a**4*b**2*u**2*v**3 + 2*a**4*b**2*u**2*v**2 + a**4*b**2*u**2*v + a**4*b**2*u*v**3 + a**4*b**2*u*v**2 - 9*a**4*b**2*u*v + a**4*b*c*u**3*v**2 + a**4*b*c*u**3*v + a**4*b*c*u**2*v**3 + 3*a**4*b*c*u**2*v**2 - 6*a**4*b*c*u**2*v + a**4*b*c*u**2 + a**4*b*c*u*v**3 - 6*a**4*b*c*u*v**2 + 3*a**4*b*c*u*v + a**4*b*c*u + a**4*b*c*v**2 + a**4*b*c*v - 9*a**4*c**2*u**2*v**2 + a**4*c**2*u**2*v + a**4*c**2*u**2 + a**4*c**2*u*v**2 + 2*a**4*c**2*u*v + a**4*c**2*u + a**4*c**2*v**2 + a**4*c**2*v + a**3*b**3*u**3*v**3 + a**3*b**3*u**3*v**2 + a**3*b**3*u**2*v**3 + 2*a**3*b**3*u**2*v**2 - 8*a**3*b**3*u**2*v - 8*a**3*b**3*u*v**2 + 2*a**3*b**3*u*v + a**3*b**3*u + a**3*b**3*v + a**3*b**3 + a**3*b**2*c*u**3*v**3 + 3*a**3*b**2*c*u**3*v**2 - 6*a**3*b**2*c*u**3*v + a**3*b**2*c*u**3 + 3*a**3*b**2*c*u**2*v**3 - 10*a**3*b**2*c*u**2*v**2 + 7*a**3*b**2*c*u**2*v + 2*a**3*b**2*c*u**2 - 6*a**3*b**2*c*u*v**3 + 7*a**3*b**2*c*u*v**2 + 6*a**3*b**2*c*u*v - 7*a**3*b**2*c*u + a**3*b**2*c*v**3 + 2*a**3*b**2*c*v**2 - 7*a**3*b**2*c*v + a**3*b**2*c + a**3*b*c**2*u**3*v**3 - 7*a**3*b*c**2*u**3*v**2 + 2*a**3*b*c**2*u**3*v + a**3*b*c**2*u**3 - 7*a**3*b*c**2*u**2*v**3 + 6*a**3*b*c**2*u**2*v**2 + 7*a**3*b*c**2*u**2*v - 6*a**3*b*c**2*u**2 + 2*a**3*b*c**2*u*v**3 + 7*a**3*b*c**2*u*v**2 - 10*a**3*b*c**2*u*v + 3*a**3*b*c**2*u + a**3*b*c**2*v**3 - 6*a**3*b*c**2*v**2 + 3*a**3*b*c**2*v + a**3*b*c**2 + a**3*c**3*u**3*v**3 + a**3*c**3*u**3*v**2 + a**3*c**3*u**2*v**3 + 2*a**3*c**3*u**2*v**2 - 8*a**3*c**3*u**2*v - 8*a**3*c**3*u*v**2 + 2*a**3*c**3*u*v + a**3*c**3*u + a**3*c**3*v + a**3*c**3 - 9*a**2*b**4*u**2*v**2 + a**2*b**4*u**2*v + a**2*b**4*u**2 + a**2*b**4*u*v**2 + 2*a**2*b**4*u*v + a**2*b**4*u + a**2*b**4*v**2 + a**2*b**4*v + a**2*b**3*c*u**3*v**3 - 7*a**2*b**3*c*u**3*v**2 + 2*a**2*b**3*c*u**3*v + a**2*b**3*c*u**3 - 7*a**2*b**3*c*u**2*v**3 + 6*a**2*b**3*c*u**2*v**2 + 7*a**2*b**3*c*u**2*v - 6*a**2*b**3*c*u**2 + 2*a**2*b**3*c*u*v**3 + 7*a**2*b**3*c*u*v**2 - 10*a**2*b**3*c*u*v + 3*a**2*b**3*c*u + a**2*b**3*c*v**3 - 6*a**2*b**3*c*v**2 + 3*a**2*b**3*c*v + a**2*b**3*c - 9*a**2*b**2*c**2*u**3*v**3 + 3*a**2*b**2*c**2*u**3*v**2 + 6*a**2*b**2*c**2*u**3*v - 6*a**2*b**2*c**2*u**3 + 3*a**2*b**2*c**2*u**2*v**3 + 12*a**2*b**2*c**2*u**2*v**2 - 12*a**2*b**2*c**2*u**2*v + 6*a**2*b**2*c**2*u**2 + 6*a**2*b**2*c**2*u*v**3 - 12*a**2*b**2*c**2*u*v**2 + 12*a**2*b**2*c**2*u*v + 3*a**2*b**2*c**2*u - 6*a**2*b**2*c**2*v**3 + 6*a**2*b**2*c**2*v**2 + 3*a**2*b**2*c**2*v - 9*a**2*b**2*c**2 + a**2*b*c**3*u**3*v**3 + 3*a**2*b*c**3*u**3*v**2 - 6*a**2*b*c**3*u**3*v + a**2*b*c**3*u**3 + 3*a**2*b*c**3*u**2*v**3 - 10*a**2*b*c**3*u**2*v**2 + 7*a**2*b*c**3*u**2*v + 2*a**2*b*c**3*u**2 - 6*a**2*b*c**3*u*v**3 + 7*a**2*b*c**3*u*v**2 + 6*a**2*b*c**3*u*v - 7*a**2*b*c**3*u + a**2*b*c**3*v**3 + 2*a**2*b*c**3*v**2 - 7*a**2*b*c**3*v + a**2*b*c**3 + a**2*c**4*u**3*v**2 + a**2*c**4*u**3*v + a**2*c**4*u**2*v**3 + 2*a**2*c**4*u**2*v**2 + a**2*c**4*u**2*v + a**2*c**4*u*v**3 + a**2*c**4*u*v**2 - 9*a**2*c**4*u*v + a*b**5*u**2*v**2 + a*b**5*u**2*v + a*b**5*u*v**2 + a*b**5*u*v + a*b**4*c*u**3*v**2 + a*b**4*c*u**3*v + a*b**4*c*u**2*v**3 + 3*a*b**4*c*u**2*v**2 - 6*a*b**4*c*u**2*v + a*b**4*c*u**2 + a*b**4*c*u*v**3 - 6*a*b**4*c*u*v**2 + 3*a*b**4*c*u*v + a*b**4*c*u + a*b**4*c*v**2 + a*b**4*c*v + a*b**3*c**2*u**3*v**3 + 3*a*b**3*c**2*u**3*v**2 - 6*a*b**3*c**2*u**3*v + a*b**3*c**2*u**3 + 3*a*b**3*c**2*u**2*v**3 - 10*a*b**3*c**2*u**2*v**2 + 7*a*b**3*c**2*u**2*v + 2*a*b**3*c**2*u**2 - 6*a*b**3*c**2*u*v**3 + 7*a*b**3*c**2*u*v**2 + 6*a*b**3*c**2*u*v - 7*a*b**3*c**2*u + a*b**3*c**2*v**3 + 2*a*b**3*c**2*v**2 - 7*a*b**3*c**2*v + a*b**3*c**2 + a*b**2*c**3*u**3*v**3 - 7*a*b**2*c**3*u**3*v**2 + 2*a*b**2*c**3*u**3*v + a*b**2*c**3*u**3 - 7*a*b**2*c**3*u**2*v**3 + 6*a*b**2*c**3*u**2*v**2 + 7*a*b**2*c**3*u**2*v - 6*a*b**2*c**3*u**2 + 2*a*b**2*c**3*u*v**3 + 7*a*b**2*c**3*u*v**2 - 10*a*b**2*c**3*u*v + 3*a*b**2*c**3*u + a*b**2*c**3*v**3 - 6*a*b**2*c**3*v**2 + 3*a*b**2*c**3*v + a*b**2*c**3 + a*b*c**4*u**3*v**2 + a*b*c**4*u**3*v + a*b*c**4*u**2*v**3 + 3*a*b*c**4*u**2*v**2 - 6*a*b*c**4*u**2*v + a*b*c**4*u**2 + a*b*c**4*u*v**3 - 6*a*b*c**4*u*v**2 + 3*a*b*c**4*u*v + a*b*c**4*u + a*b*c**4*v**2 + a*b*c**4*v + a*c**5*u**2*v**2 + a*c**5*u**2*v + a*c**5*u*v**2 + a*c**5*u*v + b**5*c*u**2*v**2 + b**5*c*u**2*v + b**5*c*u*v**2 + b**5*c*u*v + b**4*c**2*u**3*v**2 + b**4*c**2*u**3*v + b**4*c**2*u**2*v**3 + 2*b**4*c**2*u**2*v**2 + b**4*c**2*u**2*v + b**4*c**2*u*v**3 + b**4*c**2*u*v**2 - 9*b**4*c**2*u*v + b**3*c**3*u**3*v**3 + b**3*c**3*u**3*v**2 + b**3*c**3*u**2*v**3 + 2*b**3*c**3*u**2*v**2 - 8*b**3*c**3*u**2*v - 8*b**3*c**3*u*v**2 + 2*b**3*c**3*u*v + b**3*c**3*u + b**3*c**3*v + b**3*c**3 - 9*b**2*c**4*u**2*v**2 + b**2*c**4*u**2*v + b**2*c**4*u**2 + b**2*c**4*u*v**2 + 2*b**2*c**4*u*v + b**2*c**4*u + b**2*c**4*v**2 + b**2*c**4*v + b*c**5*u**2*v**2 + b*c**5*u**2*v + b*c**5*u*v**2 + b*c**5*u*v";
		String homo = "a**5*b*u**2*v**2*w**2 + a**5*b*u**2*v*w**3 + a**5*b*u*v**2*w**3 + a**5*b*u*v*w**4 + a**5*c*u**2*v**2*w**2 + a**5*c*u**2*v*w**3 + a**5*c*u*v**2*w**3 + a**5*c*u*v*w**4 + a**4*b**2*u**3*v**2*w + a**4*b**2*u**3*v*w**2 + a**4*b**2*u**2*v**3*w + 2*a**4*b**2*u**2*v**2*w**2 + a**4*b**2*u**2*v*w**3 + a**4*b**2*u*v**3*w**2 + a**4*b**2*u*v**2*w**3 - 9*a**4*b**2*u*v*w**4 + a**4*b*c*u**3*v**2*w + a**4*b*c*u**3*v*w**2 + a**4*b*c*u**2*v**3*w + 3*a**4*b*c*u**2*v**2*w**2 - 6*a**4*b*c*u**2*v*w**3 + a**4*b*c*u**2*w**4 + a**4*b*c*u*v**3*w**2 - 6*a**4*b*c*u*v**2*w**3 + 3*a**4*b*c*u*v*w**4 + a**4*b*c*u*w**5 + a**4*b*c*v**2*w**4 + a**4*b*c*v*w**5 - 9*a**4*c**2*u**2*v**2*w**2 + a**4*c**2*u**2*v*w**3 + a**4*c**2*u**2*w**4 + a**4*c**2*u*v**2*w**3 + 2*a**4*c**2*u*v*w**4 + a**4*c**2*u*w**5 + a**4*c**2*v**2*w**4 + a**4*c**2*v*w**5 + a**3*b**3*u**3*v**3 + a**3*b**3*u**3*v**2*w + a**3*b**3*u**2*v**3*w + 2*a**3*b**3*u**2*v**2*w**2 - 8*a**3*b**3*u**2*v*w**3 - 8*a**3*b**3*u*v**2*w**3 + 2*a**3*b**3*u*v*w**4 + a**3*b**3*u*w**5 + a**3*b**3*v*w**5 + a**3*b**3*w**6 + a**3*b**2*c*u**3*v**3 + 3*a**3*b**2*c*u**3*v**2*w - 6*a**3*b**2*c*u**3*v*w**2 + a**3*b**2*c*u**3*w**3 + 3*a**3*b**2*c*u**2*v**3*w - 10*a**3*b**2*c*u**2*v**2*w**2 + 7*a**3*b**2*c*u**2*v*w**3 + 2*a**3*b**2*c*u**2*w**4 - 6*a**3*b**2*c*u*v**3*w**2 + 7*a**3*b**2*c*u*v**2*w**3 + 6*a**3*b**2*c*u*v*w**4 - 7*a**3*b**2*c*u*w**5 + a**3*b**2*c*v**3*w**3 + 2*a**3*b**2*c*v**2*w**4 - 7*a**3*b**2*c*v*w**5 + a**3*b**2*c*w**6 + a**3*b*c**2*u**3*v**3 - 7*a**3*b*c**2*u**3*v**2*w + 2*a**3*b*c**2*u**3*v*w**2 + a**3*b*c**2*u**3*w**3 - 7*a**3*b*c**2*u**2*v**3*w + 6*a**3*b*c**2*u**2*v**2*w**2 + 7*a**3*b*c**2*u**2*v*w**3 - 6*a**3*b*c**2*u**2*w**4 + 2*a**3*b*c**2*u*v**3*w**2 + 7*a**3*b*c**2*u*v**2*w**3 - 10*a**3*b*c**2*u*v*w**4 + 3*a**3*b*c**2*u*w**5 + a**3*b*c**2*v**3*w**3 - 6*a**3*b*c**2*v**2*w**4 + 3*a**3*b*c**2*v*w**5 + a**3*b*c**2*w**6 + a**3*c**3*u**3*v**3 + a**3*c**3*u**3*v**2*w + a**3*c**3*u**2*v**3*w + 2*a**3*c**3*u**2*v**2*w**2 - 8*a**3*c**3*u**2*v*w**3 - 8*a**3*c**3*u*v**2*w**3 + 2*a**3*c**3*u*v*w**4 + a**3*c**3*u*w**5 + a**3*c**3*v*w**5 + a**3*c**3*w**6 - 9*a**2*b**4*u**2*v**2*w**2 + a**2*b**4*u**2*v*w**3 + a**2*b**4*u**2*w**4 + a**2*b**4*u*v**2*w**3 + 2*a**2*b**4*u*v*w**4 + a**2*b**4*u*w**5 + a**2*b**4*v**2*w**4 + a**2*b**4*v*w**5 + a**2*b**3*c*u**3*v**3 - 7*a**2*b**3*c*u**3*v**2*w + 2*a**2*b**3*c*u**3*v*w**2 + a**2*b**3*c*u**3*w**3 - 7*a**2*b**3*c*u**2*v**3*w + 6*a**2*b**3*c*u**2*v**2*w**2 + 7*a**2*b**3*c*u**2*v*w**3 - 6*a**2*b**3*c*u**2*w**4 + 2*a**2*b**3*c*u*v**3*w**2 + 7*a**2*b**3*c*u*v**2*w**3 - 10*a**2*b**3*c*u*v*w**4 + 3*a**2*b**3*c*u*w**5 + a**2*b**3*c*v**3*w**3 - 6*a**2*b**3*c*v**2*w**4 + 3*a**2*b**3*c*v*w**5 + a**2*b**3*c*w**6 - 9*a**2*b**2*c**2*u**3*v**3 + 3*a**2*b**2*c**2*u**3*v**2*w + 6*a**2*b**2*c**2*u**3*v*w**2 - 6*a**2*b**2*c**2*u**3*w**3 + 3*a**2*b**2*c**2*u**2*v**3*w + 12*a**2*b**2*c**2*u**2*v**2*w**2 - 12*a**2*b**2*c**2*u**2*v*w**3 + 6*a**2*b**2*c**2*u**2*w**4 + 6*a**2*b**2*c**2*u*v**3*w**2 - 12*a**2*b**2*c**2*u*v**2*w**3 + 12*a**2*b**2*c**2*u*v*w**4 + 3*a**2*b**2*c**2*u*w**5 - 6*a**2*b**2*c**2*v**3*w**3 + 6*a**2*b**2*c**2*v**2*w**4 + 3*a**2*b**2*c**2*v*w**5 - 9*a**2*b**2*c**2*w**6 + a**2*b*c**3*u**3*v**3 + 3*a**2*b*c**3*u**3*v**2*w - 6*a**2*b*c**3*u**3*v*w**2 + a**2*b*c**3*u**3*w**3 + 3*a**2*b*c**3*u**2*v**3*w - 10*a**2*b*c**3*u**2*v**2*w**2 + 7*a**2*b*c**3*u**2*v*w**3 + 2*a**2*b*c**3*u**2*w**4 - 6*a**2*b*c**3*u*v**3*w**2 + 7*a**2*b*c**3*u*v**2*w**3 + 6*a**2*b*c**3*u*v*w**4 - 7*a**2*b*c**3*u*w**5 + a**2*b*c**3*v**3*w**3 + 2*a**2*b*c**3*v**2*w**4 - 7*a**2*b*c**3*v*w**5 + a**2*b*c**3*w**6 + a**2*c**4*u**3*v**2*w + a**2*c**4*u**3*v*w**2 + a**2*c**4*u**2*v**3*w + 2*a**2*c**4*u**2*v**2*w**2 + a**2*c**4*u**2*v*w**3 + a**2*c**4*u*v**3*w**2 + a**2*c**4*u*v**2*w**3 - 9*a**2*c**4*u*v*w**4 + a*b**5*u**2*v**2*w**2 + a*b**5*u**2*v*w**3 + a*b**5*u*v**2*w**3 + a*b**5*u*v*w**4 + a*b**4*c*u**3*v**2*w + a*b**4*c*u**3*v*w**2 + a*b**4*c*u**2*v**3*w + 3*a*b**4*c*u**2*v**2*w**2 - 6*a*b**4*c*u**2*v*w**3 + a*b**4*c*u**2*w**4 + a*b**4*c*u*v**3*w**2 - 6*a*b**4*c*u*v**2*w**3 + 3*a*b**4*c*u*v*w**4 + a*b**4*c*u*w**5 + a*b**4*c*v**2*w**4 + a*b**4*c*v*w**5 + a*b**3*c**2*u**3*v**3 + 3*a*b**3*c**2*u**3*v**2*w - 6*a*b**3*c**2*u**3*v*w**2 + a*b**3*c**2*u**3*w**3 + 3*a*b**3*c**2*u**2*v**3*w - 10*a*b**3*c**2*u**2*v**2*w**2 + 7*a*b**3*c**2*u**2*v*w**3 + 2*a*b**3*c**2*u**2*w**4 - 6*a*b**3*c**2*u*v**3*w**2 + 7*a*b**3*c**2*u*v**2*w**3 + 6*a*b**3*c**2*u*v*w**4 - 7*a*b**3*c**2*u*w**5 + a*b**3*c**2*v**3*w**3 + 2*a*b**3*c**2*v**2*w**4 - 7*a*b**3*c**2*v*w**5 + a*b**3*c**2*w**6 + a*b**2*c**3*u**3*v**3 - 7*a*b**2*c**3*u**3*v**2*w + 2*a*b**2*c**3*u**3*v*w**2 + a*b**2*c**3*u**3*w**3 - 7*a*b**2*c**3*u**2*v**3*w + 6*a*b**2*c**3*u**2*v**2*w**2 + 7*a*b**2*c**3*u**2*v*w**3 - 6*a*b**2*c**3*u**2*w**4 + 2*a*b**2*c**3*u*v**3*w**2 + 7*a*b**2*c**3*u*v**2*w**3 - 10*a*b**2*c**3*u*v*w**4 + 3*a*b**2*c**3*u*w**5 + a*b**2*c**3*v**3*w**3 - 6*a*b**2*c**3*v**2*w**4 + 3*a*b**2*c**3*v*w**5 + a*b**2*c**3*w**6 + a*b*c**4*u**3*v**2*w + a*b*c**4*u**3*v*w**2 + a*b*c**4*u**2*v**3*w + 3*a*b*c**4*u**2*v**2*w**2 - 6*a*b*c**4*u**2*v*w**3 + a*b*c**4*u**2*w**4 + a*b*c**4*u*v**3*w**2 - 6*a*b*c**4*u*v**2*w**3 + 3*a*b*c**4*u*v*w**4 + a*b*c**4*u*w**5 + a*b*c**4*v**2*w**4 + a*b*c**4*v*w**5 + a*c**5*u**2*v**2*w**2 + a*c**5*u**2*v*w**3 + a*c**5*u*v**2*w**3 + a*c**5*u*v*w**4 + b**5*c*u**2*v**2*w**2 + b**5*c*u**2*v*w**3 + b**5*c*u*v**2*w**3 + b**5*c*u*v*w**4 + b**4*c**2*u**3*v**2*w + b**4*c**2*u**3*v*w**2 + b**4*c**2*u**2*v**3*w + 2*b**4*c**2*u**2*v**2*w**2 + b**4*c**2*u**2*v*w**3 + b**4*c**2*u*v**3*w**2 + b**4*c**2*u*v**2*w**3 - 9*b**4*c**2*u*v*w**4 + b**3*c**3*u**3*v**3 + b**3*c**3*u**3*v**2*w + b**3*c**3*u**2*v**3*w + 2*b**3*c**3*u**2*v**2*w**2 - 8*b**3*c**3*u**2*v*w**3 - 8*b**3*c**3*u*v**2*w**3 + 2*b**3*c**3*u*v*w**4 + b**3*c**3*u*w**5 + b**3*c**3*v*w**5 + b**3*c**3*w**6 - 9*b**2*c**4*u**2*v**2*w**2 + b**2*c**4*u**2*v*w**3 + b**2*c**4*u**2*w**4 + b**2*c**4*u*v**2*w**3 + 2*b**2*c**4*u*v*w**4 + b**2*c**4*u*w**5 + b**2*c**4*v**2*w**4 + b**2*c**4*v*w**5 + b*c**5*u**2*v**2*w**2 + b*c**5*u**2*v*w**3 + b*c**5*u*v**2*w**3 + b*c**5*u*v*w**4";
		assertEquals(homo, new LongPoly("abcuv", nonHomo).homogenize('w').toString());
		LongPoly f = new LongPoly("abcuvw", homo);
		assertTrue(f == f.homogenize('x'));
	}
}