package com.xqbase.math.inequality;

import java.io.InputStream;
import java.util.Properties;

import com.xqbase.math.polys.LongPoly;

public class _1777166c {
	private static final String VARS = "pqrsuv";

	private static void genCode(String p) {
		for (LongPoly coeff : new LongPoly(VARS, p).coeffsOf("uv").values()) {
			System.out.println("        " + coeff + ",");
		}
	}

	public static void main(String[] args) throws Exception {
		// result from 1777166.py: k1 <= 0, k2, k3 >= 0
		Properties p = new Properties();
		try (InputStream in = _1777166c.class.
				getResourceAsStream("1777166c.properties")) {
			p.load(in);
		}
		System.out.println("    non_positive_coeffs = [");
		genCode(p.getProperty("k1"));
		System.out.println("    ]");
		System.out.println("    non_negative_coeffs = [");
		genCode(p.getProperty("k2"));
		genCode(p.getProperty("k3"));
		System.out.println("    ]");
	}
}