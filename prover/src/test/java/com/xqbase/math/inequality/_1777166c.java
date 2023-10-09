package com.xqbase.math.inequality;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Properties;

import com.xqbase.math.polys.Poly;

public class _1777166c {
	private static final String VARS = "pqrsuv";

	private static void genCode(PrintStream out, String p) {
		for (Poly coeff : new Poly(VARS, p).coeffsOf("uv").values()) {
			out.println("        " + coeff + ", \\");
		}
	}

	public static void main(String[] args) throws Exception {
		// result from 1777166.py: k1 <= 0, k2, k3 >= 0
		Properties p = new Properties();
		try (InputStream in = _1777166c.class.
				getResourceAsStream("1777166c.properties")) {
			p.load(in);
		}
		try (PrintStream out = new PrintStream("1777166c.py")) {
			out.println("    non_positive_coeffs = [ \\");
			genCode(out, p.getProperty("k1"));
			out.println("    ]");
			out.println("    non_negative_coeffs = [ \\");
			genCode(out, p.getProperty("k2"));
			genCode(out, p.getProperty("k3"));
			out.println("    ]");
		}
	}
}