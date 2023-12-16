package com.xqbase.math.inequality;

import com.xqbase.math.polys.Poly;

public class Yang08P169Tiny {
	private static final String VARS = "abcduvw";
	private static final String SUB_POLY = "-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2";

	private static Poly subsAll(Poly p) {
		/*
		return p.subs('d', new Poly(VARS, "a + u")).
				subs('c', new Poly(VARS, "a + u + v")).
				subs('b', new Poly(VARS, "a + u + v + w"));
		*/
		// much faster
		return p.subs('d', new Poly(VARS, "c + w")).
				subs('c', new Poly(VARS, "b + v")).
				subs('b', new Poly(VARS, "a + u"));
	}

	private static Poly pow(String expr, int exp) {
		Poly p = subsAll(new Poly(VARS, expr));
		Poly t = new Poly(VARS, "1");
		for (int i = 0; i < exp; i ++) {
			t = new Poly().addMul(1, t, p);
		}
		return t;
	}

	private static Poly sym(String vars) {
		String p = SUB_POLY;
		for (int i = 0; i < 4; i ++) {
			p = p.replace("x" + (i + 1), "" + vars.charAt(i));
		}
		return new Poly(VARS, p);
	}

	public static void main(String[] args) throws Exception {
		int n = 40;
		Poly p = new Poly();
		p.addMul(1, pow("a - b", n), sym("abcd"));
		p.addMul(1, pow("a - c", n), sym("acbd"));
		p.addMul(1, pow("a - d", n), sym("adbc"));
		p.addMul(1, pow("b - c", n), sym("bcad"));
		p.addMul(1, pow("b - d", n), sym("bdac"));
		p.addMul(1, pow("c - d", n), sym("cdab"));
		p = subsAll(p);
		System.out.println("f = " + p);
	}
}