package com.xqbase.math.inequality;

import java.io.PrintStream;
import java.math.BigInteger;
import java.util.Map;
import java.util.TreeMap;

import com.xqbase.math.polys.BigMono;
import com.xqbase.math.polys.BigPoly;

public class Yang2008p169 {
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

	public static BigPoly subs(BigPoly p0, char from, String to) {
		BigPoly x = new BigPoly(VARS, to);
		TreeMap<BigMono, BigPoly> ai = p0.coeffsOf(String.valueOf(from));
		// a_0x^n+a_1x^{n-1}+a_2x^{n-2}+...+a_{n-1}x+a_n = (...((a_0x+a_1)x+a2)+...+a_{n-1})x+a_n
		Map.Entry<BigMono, BigPoly> lt = ai.firstEntry();
		System.out.println(lt);
		BigPoly p = lt.getValue();
		short[] exps = new short[VARS.length()];
		int fromIndex = VARS.indexOf(from);
		for (int i = lt.getKey().getExps()[fromIndex] - 1; i >= 0; i --) {
			exps[fromIndex] = (short) i;
			BigPoly p1 = new BigPoly();
			p1.addMul(_1, p, x);
			BigPoly a = ai.get(new BigMono(VARS, exps));
			if (a != null) {
				p1.add(_1, a);
			}
			p = p1;
			System.out.println(i + "," + p.size());
		}
		return p;
	}

	public static void main(String[] args) throws Exception {
		int n = 200;
		BigPoly p = new BigPoly();
		long t0 = System.currentTimeMillis();
		p.addMul(_1, pow(new BigPoly(VARS, "a - b"), n), new BigPoly(VARS, sym("abcd")));
		p.addMul(_1, pow(new BigPoly(VARS, "a - c"), n), new BigPoly(VARS, sym("acbd")));
		p.addMul(_1, pow(new BigPoly(VARS, "a - d"), n), new BigPoly(VARS, sym("adbc")));
		p.addMul(_1, pow(new BigPoly(VARS, "b - c"), n), new BigPoly(VARS, sym("bcad")));
		p.addMul(_1, pow(new BigPoly(VARS, "b - d"), n), new BigPoly(VARS, sym("bdac")));
		p.addMul(_1, pow(new BigPoly(VARS, "c - d"), n), new BigPoly(VARS, sym("cdab")));
		/*
		p = subs(p, 'b', "a + u");
		p = subs(p, 'c', "a + u + v");
		p = subs(p, 'd', "a + u + v + w");
		*/
		// much faster
		p = subs(p, 'd', "c + w");
		p = subs(p, 'c', "b + v");
		p = subs(p, 'b', "a + u");
		long t1 = System.currentTimeMillis();
		System.out.println(t1 - t0);
		try (PrintStream out = new PrintStream("Yang2008p169.py")) {
			out.println(p);
		}
	}
}