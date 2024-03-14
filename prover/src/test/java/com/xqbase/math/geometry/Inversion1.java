package com.xqbase.math.geometry;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import com.xqbase.math.polys.LongPoly;

public class Inversion1 {
	private static final String VARS = "acdefPQRS";

	// results from inversion-1.py
	private static final String X_E = "-2*R**2*a**3*c*e**3 - 2*R**2*a**3*c*e*f**2 - 4*R**2*a**2*c**2*e**3 + 4*R**2*a**2*c**2*e*f**2 - 8*R**2*a**2*c*e**3 - 2*R**2*a*c**3*e**3 - 2*R**2*a*c**3*e*f**2 - 8*R**2*a*c**2*e**3 - 8*R**2*a*c*e**3 - 2*R*a**3*d*e**3 - 2*R*a**3*d*e*f**2 - 6*R*a**2*c*d*e**3 + 2*R*a**2*c*d*e*f**2 - 8*R*a**2*d*e**3 - 6*R*a*c**2*d*e**3 + 2*R*a*c**2*d*e*f**2 - 16*R*a*c*d*e**3 - 8*R*a*d*e**3 - 2*R*c**3*d*e**3 - 2*R*c**3*d*e*f**2 - 8*R*c**2*d*e**3 - 8*R*c*d*e**3 - 2*a**2*d**2*e**3 - 2*a**2*d**2*e*f**2 - 4*a*c*d**2*e**3 + 4*a*c*d**2*e*f**2 - 8*a*d**2*e**3 - 2*c**2*d**2*e**3 - 2*c**2*d**2*e*f**2 - 8*c*d**2*e**3 - 8*d**2*e**3";
	private static final String Y_E = "2*R**2*a**3*c*e**2*f + 2*R**2*a**3*c*f**3 + 4*R**2*a**2*c**2*e**2*f - 4*R**2*a**2*c**2*f**3 + 8*R**2*a**2*c*e**2*f + 2*R**2*a*c**3*e**2*f + 2*R**2*a*c**3*f**3 + 8*R**2*a*c**2*e**2*f + 8*R**2*a*c*e**2*f + 2*R*a**3*d*e**2*f + 2*R*a**3*d*f**3 + 6*R*a**2*c*d*e**2*f - 2*R*a**2*c*d*f**3 + 8*R*a**2*d*e**2*f + 6*R*a*c**2*d*e**2*f - 2*R*a*c**2*d*f**3 + 16*R*a*c*d*e**2*f + 8*R*a*d*e**2*f + 2*R*c**3*d*e**2*f + 2*R*c**3*d*f**3 + 8*R*c**2*d*e**2*f + 8*R*c*d*e**2*f + 2*a**2*d**2*e**2*f + 2*a**2*d**2*f**3 + 4*a*c*d**2*e**2*f - 4*a*c*d**2*f**3 + 8*a*d**2*e**2*f + 2*c**2*d**2*e**2*f + 2*c**2*d**2*f**3 + 8*c*d**2*e**2*f + 8*d**2*e**2*f";
	private static final String X_F = "2*R**2*a**3*c*e**3 + 2*R**2*a**3*c*e*f**2 + 4*R**2*a**2*c**2*e**3 - 4*R**2*a**2*c**2*e*f**2 + 8*R**2*a**2*c*e**3 + 2*R**2*a*c**3*e**3 + 2*R**2*a*c**3*e*f**2 + 8*R**2*a*c**2*e**3 + 8*R**2*a*c*e**3 + 2*R*a**3*d*e**3 + 2*R*a**3*d*e*f**2 + 6*R*a**2*c*d*e**3 - 2*R*a**2*c*d*e*f**2 + 8*R*a**2*d*e**3 + 6*R*a*c**2*d*e**3 - 2*R*a*c**2*d*e*f**2 + 16*R*a*c*d*e**3 + 8*R*a*d*e**3 + 2*R*c**3*d*e**3 + 2*R*c**3*d*e*f**2 + 8*R*c**2*d*e**3 + 8*R*c*d*e**3 + 2*a**2*d**2*e**3 + 2*a**2*d**2*e*f**2 + 4*a*c*d**2*e**3 - 4*a*c*d**2*e*f**2 + 8*a*d**2*e**3 + 2*c**2*d**2*e**3 + 2*c**2*d**2*e*f**2 + 8*c*d**2*e**3 + 8*d**2*e**3";
	private static final String Y_F = "2*R**2*a**3*c*e**2*f + 2*R**2*a**3*c*f**3 + 4*R**2*a**2*c**2*e**2*f - 4*R**2*a**2*c**2*f**3 + 8*R**2*a**2*c*e**2*f + 2*R**2*a*c**3*e**2*f + 2*R**2*a*c**3*f**3 + 8*R**2*a*c**2*e**2*f + 8*R**2*a*c*e**2*f + 2*R*a**3*d*e**2*f + 2*R*a**3*d*f**3 + 6*R*a**2*c*d*e**2*f - 2*R*a**2*c*d*f**3 + 8*R*a**2*d*e**2*f + 6*R*a*c**2*d*e**2*f - 2*R*a*c**2*d*f**3 + 16*R*a*c*d*e**2*f + 8*R*a*d*e**2*f + 2*R*c**3*d*e**2*f + 2*R*c**3*d*f**3 + 8*R*c**2*d*e**2*f + 8*R*c*d*e**2*f + 2*a**2*d**2*e**2*f + 2*a**2*d**2*f**3 + 4*a*c*d**2*e**2*f - 4*a*c*d**2*f**3 + 8*a*d**2*e**2*f + 2*c**2*d**2*e**2*f + 2*c**2*d**2*f**3 + 8*c*d**2*e**2*f + 8*d**2*e**2*f";
	private static final String X_G = "R**4*a**4*c*e + R**4*a**3*c**2*e + 2*R**4*a**3*c*e - R**4*a**2*c**3*e - R**4*a*c**4*e - 2*R**4*a*c**3*e + 3*R**3*a**3*c*d*e + R**3*a**2*c**2*d*e + 6*R**3*a**2*c*d*e - 3*R**3*a*c**3*d*e - 4*R**3*a*c**2*d*e - R**3*c**4*d*e - 2*R**3*c**3*d*e + R**2*S*a**2*c*f - R**2*S*a*c**2*f - R**2*a**4*c*e**3 - R**2*a**4*c*e*f**2 - R**2*a**3*c**2*e**3 + 3*R**2*a**3*c**2*e*f**2 - 4*R**2*a**3*c*e**3 + R**2*a**2*c**3*e**3 - 3*R**2*a**2*c**3*e*f**2 + 2*R**2*a**2*c*d**2*e - 4*R**2*a**2*c*e**3 + R**2*a*c**4*e**3 + R**2*a*c**4*e*f**2 + 4*R**2*a*c**3*e**3 + 4*R**2*a*c**2*e**3 + 4*R**2*a*c*d**2*e - 2*R**2*c**3*d**2*e - 4*R**2*c**2*d**2*e + R*S*a*c*d*f - R*S*c**2*d*f + R*a**3*c*d*e**3 + R*a**3*c*d*e*f**2 + 2*R*a**3*d*e**3 + 2*R*a**3*d*e*f**2 + 3*R*a**2*c**2*d*e**3 - R*a**2*c**2*d*e*f**2 + 8*R*a**2*c*d*e**3 - 4*R*a**2*c*d*e*f**2 + 8*R*a**2*d*e**3 + 3*R*a*c**3*d*e**3 - R*a*c**3*d*e*f**2 + 10*R*a*c**2*d*e**3 + 2*R*a*c**2*d*e*f**2 + 12*R*a*c*d*e**3 + 8*R*a*d*e**3 + R*c**4*d*e**3 + R*c**4*d*e*f**2 + 4*R*c**3*d*e**3 + 4*R*c**2*d*e**3 + 2*a**2*c*d**2*e**3 + 2*a**2*c*d**2*e*f**2 + 2*a**2*d**2*e**3 + 2*a**2*d**2*e*f**2 + 4*a*c**2*d**2*e**3 - 4*a*c**2*d**2*e*f**2 + 12*a*c*d**2*e**3 - 4*a*c*d**2*e*f**2 + 8*a*d**2*e**3 + 2*c**3*d**2*e**3 + 2*c**3*d**2*e*f**2 + 10*c**2*d**2*e**3 + 2*c**2*d**2*e*f**2 + 16*c*d**2*e**3 + 8*d**2*e**3";
	private static final String Y_G = "-R**4*a**4*c*f + R**4*a**3*c**2*f + R**4*a**2*c**3*f - R**4*a*c**4*f - 3*R**3*a**3*c*d*f + 5*R**3*a**2*c**2*d*f - R**3*a*c**3*d*f - R**3*c**4*d*f + R**2*S*a**2*c*e + R**2*S*a*c**2*e + 2*R**2*S*a*c*e + R**2*a**4*c*e**2*f + R**2*a**4*c*f**3 + 3*R**2*a**3*c**2*e**2*f - R**2*a**3*c**2*f**3 + 6*R**2*a**3*c*e**2*f + 2*R**2*a**3*c*f**3 + 3*R**2*a**2*c**3*e**2*f - R**2*a**2*c**3*f**3 + 12*R**2*a**2*c**2*e**2*f - 4*R**2*a**2*c**2*f**3 - 2*R**2*a**2*c*d**2*f + 12*R**2*a**2*c*e**2*f + R**2*a*c**4*e**2*f + R**2*a*c**4*f**3 + 6*R**2*a*c**3*e**2*f + 2*R**2*a*c**3*f**3 + 4*R**2*a*c**2*d**2*f + 12*R**2*a*c**2*e**2*f + 8*R**2*a*c*e**2*f - 2*R**2*c**3*d**2*f + R*S*a*c*d*e + R*S*c**2*d*e + 2*R*S*c*d*e + 3*R*a**3*c*d*e**2*f + 3*R*a**3*c*d*f**3 + 2*R*a**3*d*e**2*f + 2*R*a**3*d*f**3 + 7*R*a**2*c**2*d*e**2*f - 5*R*a**2*c**2*d*f**3 + 18*R*a**2*c*d*e**2*f - 2*R*a**2*c*d*f**3 + 8*R*a**2*d*e**2*f + 5*R*a*c**3*d*e**2*f + R*a*c**3*d*f**3 + 22*R*a*c**2*d*e**2*f - 2*R*a*c**2*d*f**3 + 28*R*a*c*d*e**2*f + 8*R*a*d*e**2*f + R*c**4*d*e**2*f + R*c**4*d*f**3 + 6*R*c**3*d*e**2*f + 2*R*c**3*d*f**3 + 12*R*c**2*d*e**2*f + 8*R*c*d*e**2*f + 2*a**2*c*d**2*e**2*f + 2*a**2*c*d**2*f**3 + 2*a**2*d**2*e**2*f + 2*a**2*d**2*f**3 + 4*a*c**2*d**2*e**2*f - 4*a*c**2*d**2*f**3 + 12*a*c*d**2*e**2*f - 4*a*c*d**2*f**3 + 8*a*d**2*e**2*f + 2*c**3*d**2*e**2*f + 2*c**3*d**2*f**3 + 10*c**2*d**2*e**2*f + 2*c**2*d**2*f**3 + 16*c*d**2*e**2*f + 8*d**2*e**2*f";
	private static final String X_H = "R**4*a**4*c*e + R**4*a**3*c**2*e + 2*R**4*a**3*c*e - R**4*a**2*c**3*e - R**4*a*c**4*e - 2*R**4*a*c**3*e + R**3*a**4*d*e + 3*R**3*a**3*c*d*e + 2*R**3*a**3*d*e - R**3*a**2*c**2*d*e + 4*R**3*a**2*c*d*e - 3*R**3*a*c**3*d*e - 6*R**3*a*c**2*d*e + R**2*S*a**2*c*f - R**2*S*a*c**2*f - R**2*a**4*c*e**3 - R**2*a**4*c*e*f**2 - R**2*a**3*c**2*e**3 + 3*R**2*a**3*c**2*e*f**2 - 4*R**2*a**3*c*e**3 + 2*R**2*a**3*d**2*e + R**2*a**2*c**3*e**3 - 3*R**2*a**2*c**3*e*f**2 - 4*R**2*a**2*c*e**3 + 4*R**2*a**2*d**2*e + R**2*a*c**4*e**3 + R**2*a*c**4*e*f**2 + 4*R**2*a*c**3*e**3 - 2*R**2*a*c**2*d**2*e + 4*R**2*a*c**2*e**3 - 4*R**2*a*c*d**2*e + R*S*a**2*d*f - R*S*a*c*d*f - R*a**4*d*e**3 - R*a**4*d*e*f**2 - 3*R*a**3*c*d*e**3 + R*a**3*c*d*e*f**2 - 4*R*a**3*d*e**3 - 3*R*a**2*c**2*d*e**3 + R*a**2*c**2*d*e*f**2 - 10*R*a**2*c*d*e**3 - 2*R*a**2*c*d*e*f**2 - 4*R*a**2*d*e**3 - R*a*c**3*d*e**3 - R*a*c**3*d*e*f**2 - 8*R*a*c**2*d*e**3 + 4*R*a*c**2*d*e*f**2 - 12*R*a*c*d*e**3 - 2*R*c**3*d*e**3 - 2*R*c**3*d*e*f**2 - 8*R*c**2*d*e**3 - 8*R*c*d*e**3 - 2*a**3*d**2*e**3 - 2*a**3*d**2*e*f**2 - 4*a**2*c*d**2*e**3 + 4*a**2*c*d**2*e*f**2 - 10*a**2*d**2*e**3 - 2*a**2*d**2*e*f**2 - 2*a*c**2*d**2*e**3 - 2*a*c**2*d**2*e*f**2 - 12*a*c*d**2*e**3 + 4*a*c*d**2*e*f**2 - 16*a*d**2*e**3 - 2*c**2*d**2*e**3 - 2*c**2*d**2*e*f**2 - 8*c*d**2*e**3 - 8*d**2*e**3";
	private static final String Y_H = "-R**4*a**4*c*f + R**4*a**3*c**2*f + R**4*a**2*c**3*f - R**4*a*c**4*f - R**3*a**4*d*f - R**3*a**3*c*d*f + 5*R**3*a**2*c**2*d*f - 3*R**3*a*c**3*d*f + R**2*S*a**2*c*e + R**2*S*a*c**2*e + 2*R**2*S*a*c*e + R**2*a**4*c*e**2*f + R**2*a**4*c*f**3 + 3*R**2*a**3*c**2*e**2*f - R**2*a**3*c**2*f**3 + 6*R**2*a**3*c*e**2*f + 2*R**2*a**3*c*f**3 - 2*R**2*a**3*d**2*f + 3*R**2*a**2*c**3*e**2*f - R**2*a**2*c**3*f**3 + 12*R**2*a**2*c**2*e**2*f - 4*R**2*a**2*c**2*f**3 + 4*R**2*a**2*c*d**2*f + 12*R**2*a**2*c*e**2*f + R**2*a*c**4*e**2*f + R**2*a*c**4*f**3 + 6*R**2*a*c**3*e**2*f + 2*R**2*a*c**3*f**3 - 2*R**2*a*c**2*d**2*f + 12*R**2*a*c**2*e**2*f + 8*R**2*a*c*e**2*f + R*S*a**2*d*e + R*S*a*c*d*e + 2*R*S*a*d*e + R*a**4*d*e**2*f + R*a**4*d*f**3 + 5*R*a**3*c*d*e**2*f + R*a**3*c*d*f**3 + 6*R*a**3*d*e**2*f + 2*R*a**3*d*f**3 + 7*R*a**2*c**2*d*e**2*f - 5*R*a**2*c**2*d*f**3 + 22*R*a**2*c*d*e**2*f - 2*R*a**2*c*d*f**3 + 12*R*a**2*d*e**2*f + 3*R*a*c**3*d*e**2*f + 3*R*a*c**3*d*f**3 + 18*R*a*c**2*d*e**2*f - 2*R*a*c**2*d*f**3 + 28*R*a*c*d*e**2*f + 8*R*a*d*e**2*f + 2*R*c**3*d*e**2*f + 2*R*c**3*d*f**3 + 8*R*c**2*d*e**2*f + 8*R*c*d*e**2*f + 2*a**3*d**2*e**2*f + 2*a**3*d**2*f**3 + 4*a**2*c*d**2*e**2*f - 4*a**2*c*d**2*f**3 + 10*a**2*d**2*e**2*f + 2*a**2*d**2*f**3 + 2*a*c**2*d**2*e**2*f + 2*a*c**2*d**2*f**3 + 12*a*c*d**2*e**2*f - 4*a*c*d**2*f**3 + 16*a*d**2*e**2*f + 2*c**2*d**2*e**2*f + 2*c**2*d**2*f**3 + 8*c*d**2*e**2*f + 8*d**2*e**2*f";
	private static final LongPoly R2 = new LongPoly(VARS, "e**2 + f**2");
	private static final LongPoly S2 = new LongPoly(VARS, "-R**4*a**4 + 2*R**4*a**2*c**2 - R**4*c**4 - 4*R**3*a**3*d + 4*R**3*a**2*c*d + 4*R**3*a*c**2*d - 4*R**3*c**3*d + 2*R**2*a**4*e**2 + 2*R**2*a**4*f**2 + 4*R**2*a**3*c*e**2 - 4*R**2*a**3*c*f**2 + 8*R**2*a**3*e**2 + 4*R**2*a**2*c**2*e**2 + 4*R**2*a**2*c**2*f**2 + 8*R**2*a**2*c*e**2 - 4*R**2*a**2*d**2 + 8*R**2*a**2*e**2 + 4*R**2*a*c**3*e**2 - 4*R**2*a*c**3*f**2 + 8*R**2*a*c**2*e**2 + 8*R**2*a*c*d**2 + 2*R**2*c**4*e**2 + 2*R**2*c**4*f**2 + 8*R**2*c**3*e**2 - 4*R**2*c**2*d**2 + 8*R**2*c**2*e**2 + 4*R*a**3*d*e**2 + 4*R*a**3*d*f**2 + 12*R*a**2*c*d*e**2 - 4*R*a**2*c*d*f**2 + 16*R*a**2*d*e**2 + 12*R*a*c**2*d*e**2 - 4*R*a*c**2*d*f**2 + 32*R*a*c*d*e**2 + 16*R*a*d*e**2 + 4*R*c**3*d*e**2 + 4*R*c**3*d*f**2 + 16*R*c**2*d*e**2 + 16*R*c*d*e**2 - a**4*e**4 - 2*a**4*e**2*f**2 - a**4*f**4 - 4*a**3*c*e**4 + 4*a**3*c*f**4 - 8*a**3*e**4 - 8*a**3*e**2*f**2 - 6*a**2*c**2*e**4 + 4*a**2*c**2*e**2*f**2 - 6*a**2*c**2*f**4 - 24*a**2*c*e**4 + 8*a**2*c*e**2*f**2 + 4*a**2*d**2*e**2 + 4*a**2*d**2*f**2 - 24*a**2*e**4 - 8*a**2*e**2*f**2 - 4*a*c**3*e**4 + 4*a*c**3*f**4 - 24*a*c**2*e**4 + 8*a*c**2*e**2*f**2 + 8*a*c*d**2*e**2 - 8*a*c*d**2*f**2 - 48*a*c*e**4 + 16*a*c*e**2*f**2 + 16*a*d**2*e**2 - 32*a*e**4 - c**4*e**4 - 2*c**4*e**2*f**2 - c**4*f**4 - 8*c**3*e**4 - 8*c**3*e**2*f**2 + 4*c**2*d**2*e**2 + 4*c**2*d**2*f**2 - 24*c**2*e**4 - 8*c**2*e**2*f**2 + 16*c*d**2*e**2 - 32*c*e**4 + 16*d**2*e**2 - 16*e**4");

	static {
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
	}

	private static Point P(String x, String y) {
		return new Point(new LongPoly(VARS, x), new LongPoly(VARS, y), new LongPoly(VARS, "1"));
	}

	public static void main(String[] args) {
		LongPoly g = Circle.concyclic(P(X_E, Y_E), P(X_F, Y_F), P(X_G, Y_G), P(X_H, Y_H));
		g = new LongPoly(VARS, g.toString().replace("S**3", "Q*S").replace("S**2", "Q")).subs('Q', S2);
		g = new LongPoly(VARS, g.toString().
				replace("R**11", "P**5*R").replace("R**10", "P**5").
				replace("R**9", "P**4*R").replace("R**8", "P**4").
				replace("R**7", "P**3*R").replace("R**6", "P**3").
				replace("R**5", "P**2*R").replace("R**4", "P**2").
				replace("R**3", "P*R").replace("R**2", "P")).subs('P', R2);
		System.out.println("Are E, F, G and H concyclic? " + g.isEmpty());
	}
}