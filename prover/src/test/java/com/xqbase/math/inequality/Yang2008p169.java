package com.xqbase.math.inequality;

import java.io.PrintStream;
import java.math.BigInteger;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

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

	static {
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
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
		p = p.subs('d', new BigPoly(VARS, "c + w"));
		p = p.subs('c', new BigPoly(VARS, "b + v"));
		p = p.subs('b', new BigPoly(VARS, "a + u"));
		long t1 = System.currentTimeMillis();
		System.out.println(t1 - t0);
		try (PrintStream out = new PrintStream("Yang2008p169.py")) {
			out.println(p);
		}
	}
}