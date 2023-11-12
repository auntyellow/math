package com.xqbase.math.inequality;

import java.io.PrintStream;
import java.math.BigInteger;
import java.util.Map;

import com.xqbase.math.polys.BigMono;
import com.xqbase.math.polys.BigPoly;

public class Yang2008p169 {
	private static final int MAX_EXP = 53;
	private static final BigInteger _1 = BigInteger.ONE;
	private static final String VARS = "abcduvw";
	private static final String SUB_POLY = "-x3**2 - 2*x4*x1 + 6*x1**2 + 6*x2**2 + 4*x2*x1 - x4**2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2";

	private static BigPoly pow(BigPoly p, int exp) {
		BigPoly t = new BigPoly(VARS, "1");
		for (int i = 0; i < exp; i ++) {
			t = new BigPoly().addMul(BigInteger.ONE, t, p);
		}
		return t;
	}

	private static String sym(String vars) {
		String p = SUB_POLY;
		for (int i = 0; i < 4; i ++) {
			p = p.replace("x" + (i + 1), "" + vars.charAt(i));
		}
		return p;
	}

	public static BigPoly subs(BigPoly p0, String from, String to) {
		BigPoly p = new BigPoly();
		BigPoly toP = new BigPoly(VARS, to);
		BigPoly[] pows = new BigPoly[MAX_EXP];
		BigPoly t = new BigPoly(VARS, "1");
		pows[0] = t;
		for (int i = 1; i < MAX_EXP; i ++) {
			t = new BigPoly().addMul(BigInteger.ONE, t, toP);
			pows[i] = t;
		}
		char c = from.charAt(0);
		for (Map.Entry<BigMono, BigPoly> entry : p0.coeffsOf(from).entrySet()) {
			// p.addMul(_1, entry.getValue(), pow(toP, entry.getKey().getExps()[VARS.indexOf(c)]));
			p.addMul(_1, entry.getValue(), pows[entry.getKey().getExps()[VARS.indexOf(c)]]);
		}
		return p;
	}

	public static void main(String[] args) throws Exception {
		int n = MAX_EXP - 3;
		BigPoly p = new BigPoly();
		long t0 = System.currentTimeMillis();
		p.addMul(_1, pow(new BigPoly(VARS, "a - b"), n), new BigPoly(VARS, sym("abcd")));
		p.addMul(_1, pow(new BigPoly(VARS, "a - c"), n), new BigPoly(VARS, sym("acbd")));
		p.addMul(_1, pow(new BigPoly(VARS, "a - d"), n), new BigPoly(VARS, sym("adbc")));
		p.addMul(_1, pow(new BigPoly(VARS, "b - c"), n), new BigPoly(VARS, sym("bcad")));
		p.addMul(_1, pow(new BigPoly(VARS, "b - d"), n), new BigPoly(VARS, sym("bdac")));
		p.addMul(_1, pow(new BigPoly(VARS, "c - d"), n), new BigPoly(VARS, sym("cdab")));
		p = subs(p, "b", "a + u");
		p = subs(p, "c", "a + u + v");
		p = subs(p, "d", "a + u + v + w");
		long t1 = System.currentTimeMillis();
		System.out.println(t1 - t0);
		try (PrintStream out = new PrintStream("Yang2008p169.py")) {
			out.println(p);
		}
	}
}