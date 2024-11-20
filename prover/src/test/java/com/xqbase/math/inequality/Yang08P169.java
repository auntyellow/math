package com.xqbase.math.inequality;

import java.io.PrintStream;

import com.xqbase.math.polys.BigPoly;

public class Yang08P169 {
	private static final String[] VARS = {"a", "b", "c", "d", "u", "v", "w"};
	private static final String SUB_POLY = "-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2";

	private static BigPoly subsAll(BigPoly p) {
		/*
		return p.subs("d", new BigPoly("a + u", VARS)).
				subs("c", new BigPoly("a + u + v", VARS)).
				subs("b", new BigPoly("a + u + v + w", VARS));
		*/
		// much faster
		return p.subs("d", new BigPoly("c + w", VARS)).
				subs("c", new BigPoly("b + v", VARS)).
				subs("b", new BigPoly("a + u", VARS));
	}

	private static BigPoly pow(String expr, int exp) {
		BigPoly p = subsAll(new BigPoly(expr, VARS));
		BigPoly t = new BigPoly("1", VARS);
		for (int i = 0; i < exp; i ++) {
			t = new BigPoly(VARS).addMul(t, p);
		}
		return t;
	}

	private static BigPoly sym(String vars) {
		String p = SUB_POLY;
		for (int i = 0; i < 4; i ++) {
			p = p.replace("x" + (i + 1), "" + vars.charAt(i));
		}
		return subsAll(new BigPoly(p, VARS));
	}

	public static void main(String[] args) throws Exception {
		long t0 = System.currentTimeMillis();
		int n = 1000;
		BigPoly p = new BigPoly(VARS);
		p.addMul(pow("a - b", n), sym("abcd"));
		p.addMul(pow("a - c", n), sym("acbd"));
		p.addMul(pow("a - d", n), sym("adbc"));
		p.addMul(pow("b - c", n), sym("bcad"));
		p.addMul(pow("b - d", n), sym("bdac"));
		p.addMul(pow("c - d", n), sym("cdab"));
		// avoid IDE console crash
		try (PrintStream out = new PrintStream("Yang08P169.py")) {
			out.println("f = " + p);
		}
		System.out.println(System.currentTimeMillis() - t0);
	}
}