package com.xqbase.math.inequality;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Properties;

import com.xqbase.math.polys.BigPoly;

public class _1777166 {
	private static final String VARS = "pquv";

	private static void genCode(PrintStream out, String p, boolean nonPos) {
		for (BigPoly c : new BigPoly(VARS, p).coeffsOf("uv").values()) {
			BigPoly c1;
			if (nonPos) {
				c1 = new BigPoly(VARS);
				c1.add(-1, c);
			} else {
				c1 = c;
			}
			out.println("        " + c1 + ",");
		}
	}

	public static void main(String[] args) throws Exception {
		// result from 1777166.m: k1 <= 0; k2, k3, k4 >= 0
		Properties p = new Properties();
		try (InputStream in = _1777166.class.getResourceAsStream("1777166.properties")) {
			p.load(in);
		}
		try (PrintStream out = new PrintStream("1777166.py")) {
			genCode(out, p.getProperty("k1"), true);
			genCode(out, p.getProperty("k2"), false);
			genCode(out, p.getProperty("k3"), false);
			genCode(out, p.getProperty("k4"), false);
		}
	}
}