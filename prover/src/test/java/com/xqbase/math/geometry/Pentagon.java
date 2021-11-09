package com.xqbase.math.geometry;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import com.xqbase.math.geometry.Circle;
import com.xqbase.math.geometry.Point;
import com.xqbase.math.polys.Poly;

public class Pentagon {
	private static final int VARS = 7;

	// Results from pentagon.py
	private static final String X_C4 = "b**2*c**2*d*e**2*g**2 - b**2*c**2*d*e*g**3 - b**2*c**2*e**3*f*g + b**2*c**2*e**2*f*g**2 - b**2*c*d*e**3*g**2 + b**2*c*d*e*g**4 + b**2*c*e**4*f*g - b**2*c*e**2*f*g**3 + b**2*d*e**3*g**3 - b**2*d*e**2*g**4 - b**2*e**4*f*g**2 + b**2*e**3*f*g**3 - b*c**3*d**2*e*g**2 + b*c**3*d**2*g**3 + b*c**3*e**3*f**2 - b*c**3*e**2*f**2*g + b*c**2*d**2*e**2*g**2 - b*c**2*d**2*g**4 - b*c**2*e**4*f**2 + b*c**2*e**2*f**2*g**2 - b*c*d**2*e**2*g**3 + b*c*d**2*e*g**4 + b*c*e**4*f**2*g - b*c*e**3*f**2*g**2 + c**4*d**2*e*f*g - c**4*d**2*f*g**2 - c**4*d*e**2*f**2 + c**4*d*e*f**2*g - c**3*d**2*e**2*f*g + c**3*d**2*f*g**3 + c**3*d*e**3*f**2 - c**3*d*e*f**2*g**2 + c**2*d**2*e**2*f*g**2 - c**2*d**2*e*f*g**3 - c**2*d*e**3*f**2*g + c**2*d*e**2*f**2*g**2";
	private static final String Y_C4 = "-b**2*c**2*d**2*g**3 + b**2*c**2*d*e**2*f*g + b**2*c**2*d*e*f*g**2 - b**2*c**2*e**3*f**2 + 2*b**2*c*d**2*e*g**3 - b**2*c*d*e**3*f*g - 2*b**2*c*d*e**2*f*g**2 - b**2*c*d*e*f*g**3 - b**2*c*e**4*g**2 + 2*b**2*c*e**3*f**2*g + 2*b**2*c*e**3*g**3 - b**2*c*e**2*g**4 - b**2*d**2*e**2*g**3 + b**2*d*e**3*f*g**2 + b**2*d*e**2*f*g**3 - b**2*e**3*f**2*g**2 - b*c**3*d**2*e*f*g + b*c**3*d**2*f*g**2 + b*c**3*d*e**2*f**2 + b*c**3*d*e**2*g**2 - b*c**3*d*e*f**2*g - b*c**3*d*e*g**3 - b*c**3*e**3*f*g + b*c**3*e**2*f*g**2 + b*c**2*d**2*e**2*f*g - 2*b*c**2*d**2*e*f*g**2 + b*c**2*d**2*f*g**3 + b*c**2*d*e**3*f**2 + b*c**2*d*e**3*g**2 - 2*b*c**2*d*e**2*f**2*g - 2*b*c**2*d*e**2*g**3 + b*c**2*d*e*f**2*g**2 + b*c**2*d*e*g**4 + b*c**2*e**4*f*g - 2*b*c**2*e**3*f*g**2 + b*c**2*e**2*f*g**3 + b*c*d**2*e**2*f*g**2 - b*c*d**2*e*f*g**3 - b*c*d*e**3*f**2*g - b*c*d*e**3*g**3 + b*c*d*e**2*f**2*g**2 + b*c*d*e**2*g**4 + b*c*e**4*f*g**2 - b*c*e**3*f*g**3 - c**4*d**2*e*g**2 + c**4*d*e**2*f*g + c**4*d*e*f*g**2 - c**4*e**2*f**2*g - c**3*d**2*e**2*f**2 + 2*c**3*d**2*e*f**2*g + 2*c**3*d**2*e*g**3 - c**3*d**2*f**2*g**2 - c**3*d*e**3*f*g - 2*c**3*d*e**2*f*g**2 - c**3*d*e*f*g**3 + 2*c**3*e**3*f**2*g - c**2*d**2*e*g**4 + c**2*d*e**3*f*g**2 + c**2*d*e**2*f*g**3 - c**2*e**4*f**2*g";
	private static final String Z_C4 = "b**2*c**2*d**2*g**4 - 2*b**2*c**2*d*e**2*f*g**2 + b**2*c**2*e**4*f**2 + b**2*c**2*e**4*g**2 - 2*b**2*c**2*e**3*g**3 + b**2*c**2*e**2*g**4 - 2*b**2*c*d**2*e*g**4 + 2*b**2*c*d*e**3*f*g**2 + 2*b**2*c*d*e**2*f*g**3 - 2*b**2*c*e**4*f**2*g + b**2*d**2*e**2*g**4 - 2*b**2*d*e**3*f*g**3 + b**2*e**4*f**2*g**2 + 2*b*c**3*d**2*e*f*g**2 - 2*b*c**3*d**2*f*g**3 - 2*b*c**3*d*e**3*f**2 - 2*b*c**3*d*e**3*g**2 + 2*b*c**3*d*e**2*f**2*g + 2*b*c**3*d*e**2*g**3 + 2*b*c**3*e**3*f*g**2 - 2*b*c**3*e**2*f*g**3 - 2*b*c**2*d**2*e**2*f*g**2 + 2*b*c**2*d**2*e*f*g**3 + 2*b*c**2*d*e**3*f**2*g + 2*b*c**2*d*e**3*g**3 - 2*b*c**2*d*e**2*f**2*g**2 - 2*b*c**2*d*e**2*g**4 - 2*b*c**2*e**4*f*g**2 + 2*b*c**2*e**3*f*g**3 + c**4*d**2*e**2*f**2 + c**4*d**2*e**2*g**2 - 2*c**4*d**2*e*f**2*g + c**4*d**2*f**2*g**2 - 2*c**4*d*e**2*f*g**2 + c**4*e**2*f**2*g**2 - 2*c**3*d**2*e**2*g**3 + 2*c**3*d*e**3*f*g**2 + 2*c**3*d*e**2*f*g**3 - 2*c**3*e**3*f**2*g**2 + c**2*d**2*e**2*g**4 - 2*c**2*d*e**3*f*g**3 + c**2*e**4*f**2*g**2";
	private static final String X_C0 = "a**2*d*e**2*g**2 - a**2*d*e*g**3 - a**2*e**3*f*g + a**2*e**2*f*g**2 - a*d**2*e*g**2 + a*d**2*g**3 + a*e**3*f**2 - a*e**2*f**2*g + d**2*e*f*g - d**2*f*g**2 - d*e**2*f**2 + d*e*f**2*g";
	private static final String Y_C0 = "-a**2*d**2*g**3 + a**2*d*e**2*f*g + a**2*d*e*f*g**2 - a**2*e**3*f**2 - a*d**2*e*f*g + a*d**2*f*g**2 + a*d*e**2*f**2 + a*d*e**2*g**2 - a*d*e*f**2*g - a*d*e*g**3 - a*e**3*f*g + a*e**2*f*g**2 - d**2*e*g**2 + d*e**2*f*g + d*e*f*g**2 - e**2*f**2*g";
	private static final String Z_C0 = "a**2*d**2*g**4 - 2*a**2*d*e**2*f*g**2 + a**2*e**4*f**2 + a**2*e**4*g**2 - 2*a**2*e**3*g**3 + a**2*e**2*g**4 + 2*a*d**2*e*f*g**2 - 2*a*d**2*f*g**3 - 2*a*d*e**3*f**2 - 2*a*d*e**3*g**2 + 2*a*d*e**2*f**2*g + 2*a*d*e**2*g**3 + 2*a*e**3*f*g**2 - 2*a*e**2*f*g**3 + d**2*e**2*f**2 + d**2*e**2*g**2 - 2*d**2*e*f**2*g + d**2*f**2*g**2 - 2*d*e**2*f*g**2 + e**2*f**2*g**2";
	private static final String X_C1 = "a**2*b*c**2*g**2 - a**2*b*c*g**3 - a**2*c**3*f*g + a**2*c**2*f*g**2 - a*b**2*c*g**2 + a*b**2*g**3 + a*c**3*f**2 - a*c**2*f**2*g + b**2*c*f*g - b**2*f*g**2 - b*c**2*f**2 + b*c*f**2*g";
	private static final String Y_C1 = "-a**2*b**2*g**3 + a**2*b*c**2*f*g + a**2*b*c*f*g**2 - a**2*c**3*f**2 - a*b**2*c*f*g + a*b**2*f*g**2 + a*b*c**2*f**2 + a*b*c**2*g**2 - a*b*c*f**2*g - a*b*c*g**3 - a*c**3*f*g + a*c**2*f*g**2 - b**2*c*g**2 + b*c**2*f*g + b*c*f*g**2 - c**2*f**2*g";
	private static final String Z_C1 = "a**2*b**2*g**4 - 2*a**2*b*c**2*f*g**2 + a**2*c**4*f**2 + a**2*c**4*g**2 - 2*a**2*c**3*g**3 + a**2*c**2*g**4 + 2*a*b**2*c*f*g**2 - 2*a*b**2*f*g**3 - 2*a*b*c**3*f**2 - 2*a*b*c**3*g**2 + 2*a*b*c**2*f**2*g + 2*a*b*c**2*g**3 + 2*a*c**3*f*g**2 - 2*a*c**2*f*g**3 + b**2*c**2*f**2 + b**2*c**2*g**2 - 2*b**2*c*f**2*g + b**2*f**2*g**2 - 2*b*c**2*f*g**2 + c**2*f**2*g**2";
	private static final String X_C2 = "a**2*b*c**2*e**2 - a**2*b*c*e**3 - a**2*c**3*d*e + a**2*c**2*d*e**2 - a*b**2*c*e**2 + a*b**2*e**3 + a*c**3*d**2 - a*c**2*d**2*e + b**2*c*d*e - b**2*d*e**2 - b*c**2*d**2 + b*c*d**2*e";
	private static final String Y_C2 = "-a**2*b**2*e**3 + a**2*b*c**2*d*e + a**2*b*c*d*e**2 - a**2*c**3*d**2 - a*b**2*c*d*e + a*b**2*d*e**2 + a*b*c**2*d**2 + a*b*c**2*e**2 - a*b*c*d**2*e - a*b*c*e**3 - a*c**3*d*e + a*c**2*d*e**2 - b**2*c*e**2 + b*c**2*d*e + b*c*d*e**2 - c**2*d**2*e";
	private static final String Z_C2 = "a**2*b**2*e**4 - 2*a**2*b*c**2*d*e**2 + a**2*c**4*d**2 + a**2*c**4*e**2 - 2*a**2*c**3*e**3 + a**2*c**2*e**4 + 2*a*b**2*c*d*e**2 - 2*a*b**2*d*e**3 - 2*a*b*c**3*d**2 - 2*a*b*c**3*e**2 + 2*a*b*c**2*d**2*e + 2*a*b*c**2*e**3 + 2*a*c**3*d*e**2 - 2*a*c**2*d*e**3 + b**2*c**2*d**2 + b**2*c**2*e**2 - 2*b**2*c*d**2*e + b**2*d**2*e**2 - 2*b*c**2*d*e**2 + c**2*d**2*e**2";

	static {
		// https://stackoverflow.com/a/6308286/4260959
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
	}

	private static Point P(String x, String y, String z) {
		return new Point(new Poly(VARS, x), new Poly(VARS, y), new Poly(VARS, z));
	}

	public static void main(String[] args) {
		System.out.println("Are C4, C0, C1 and C2 concyclic? " +
				Circle.concyclic(P(X_C4, Y_C4, Z_C4), P(X_C0, Y_C0, Z_C0), P(X_C1, Y_C1, Z_C1), P(X_C2, Y_C2, Z_C2)));
	}
}