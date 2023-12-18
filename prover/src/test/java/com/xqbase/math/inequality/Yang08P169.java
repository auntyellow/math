package com.xqbase.math.inequality;

import java.io.PrintStream;
import java.math.BigInteger;

import com.xqbase.math.polys.BigPoly;
import com.xqbase.math.polys.MutableBigInteger;

public class Yang08P169 {
	private static final MutableBigInteger _1 = new MutableBigInteger(BigInteger.ONE);
	private static final String VARS = "abcduvw";
	private static final String SUB_POLY = "-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2";

	private static BigPoly subsAll(BigPoly p) {
		/*
		return p.subs('d', new BigPoly(VARS, "a + u")).
				subs('c', new BigPoly(VARS, "a + u + v")).
				subs('b', new BigPoly(VARS, "a + u + v + w"));
		*/
		// much faster
		return (BigPoly) p.subs('d', new BigPoly(VARS, "c + w")).
				subs('c', new BigPoly(VARS, "b + v")).
				subs('b', new BigPoly(VARS, "a + u"));
	}

	private static BigPoly pow(String expr, int exp) {
		BigPoly p = subsAll(new BigPoly(VARS, expr));
		BigPoly t = new BigPoly(VARS, "1");
		for (int i = 0; i < exp; i ++) {
			t = (BigPoly) new BigPoly().addMul(_1, t, p);
		}
		return t;
	}

	private static BigPoly sym(String vars) {
		String p = SUB_POLY;
		for (int i = 0; i < 4; i ++) {
			p = p.replace("x" + (i + 1), "" + vars.charAt(i));
		}
		return new BigPoly(VARS, p);
	}

	public static void main(String[] args) throws Exception {
		int n = 1000;
		BigPoly p = new BigPoly();
		p.addMul(_1, pow("a - b", n), sym("abcd"));
		p.addMul(_1, pow("a - c", n), sym("acbd"));
		p.addMul(_1, pow("a - d", n), sym("adbc"));
		p.addMul(_1, pow("b - c", n), sym("bcad"));
		p.addMul(_1, pow("b - d", n), sym("bdac"));
		p.addMul(_1, pow("c - d", n), sym("cdab"));
		p = subsAll(p);
		// avoid console crash in IDE
		try (PrintStream out = new PrintStream("Yang08P169.py")) {
			out.println("f = " + p);
		}
	}
}