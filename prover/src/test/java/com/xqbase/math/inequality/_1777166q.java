package com.xqbase.math.inequality;

import java.io.InputStream;
import java.util.Properties;

import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.MutableLong;
import com.xqbase.math.polys.Poly;

public class _1777166q {
	private static final String VARS = "pqrsuv";

	/** @param nonPos for Java */
	private static void genCode(String p, boolean nonPos) {
		for (Poly<MutableLong> coeff : new LongPoly(VARS, p).coeffsOf("uv").values()) {
			System.out.println("        " + coeff + ",");
			// Generate Java Code
			/*
			String expr = coeff.toString();
			// d**5 -> d*d*d*d*d
			int pow;
			while ((pow = expr.indexOf("**")) > 0) {
				expr = expr.substring(0, pow - 1) +
						String.join("*", Collections.nCopies(expr.charAt(pow + 2) - '0',
						(Character.toString(expr.charAt(pow - 1))))) +
						expr.substring(pow + 3);
			}
			for (int i = 0; i < 10; i ++) {
				expr = expr.replace(i + "*", i + "L*");
			}
			for (int i = 0; i < 10; i ++) {
				if (expr.endsWith(Integer.toString(i))) {
					expr = expr + "L";
					break;
				}
			}
			System.out.println("c = " + expr + ";");
			System.out.println("v += c " + (nonPos ? ">" : "<") + " 0 ? c*c : 0;");
			System.out.println("if (v >= u) {");
			System.out.println("\treturn v;");
			System.out.println("}");
			*/
		}
	}

	public static void main(String[] args) throws Exception {
		_1777166c.class.toString();
		// result from 1777166.py: k1, k3 >= 0; k2 <= 0
		Properties p = new Properties();
		try (InputStream in = _1777166q.class.getResourceAsStream("1777166q.properties")) {
			p.load(in);
		}
		System.out.println("    non_negative_coeffs = [");
		genCode(p.getProperty("k1"), false);
		genCode(p.getProperty("k3"), false);
		System.out.println("    ]");
		System.out.println("    non_positive_coeffs = [");
		genCode(p.getProperty("k2"), true);
		System.out.println("    ]");
	}
}