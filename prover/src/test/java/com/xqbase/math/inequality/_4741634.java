package com.xqbase.math.inequality;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Properties;
import java.util.TreeMap;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;

import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class _4741634 {
	private static final String VARS = "xyz";
	private static final Rational _1 = Rational.valueOf(1);
	// results from 4741634-sage.py, 16 positive real_roots
	private static final String[][] ROOTS = {
		{"0", "42826689/2147483648"},
		{"24662133/536870912", "154470375/2147483648"},
		{"266114061/2147483648", "588049965/4294967296"},
		{"10060497/67108864", "136305819/536870912"},
		{"1159263549/2147483648", "2374348941/4294967296"},
		{"75942837/134217728", "663364539/1073741824"},
		{"6590818701/8589934592", "13237459245/17179869184"},
		{"207707517/268435456", "471236877/536870912"},
		{"16470585/16777216", "578727597537/549755813888"},
		{"308873532897/274877906944", "2510007731433/2199023255552"},
		{"1274513599845/1099511627776", "656766534051/549755813888"},
		{"1586669345901/1099511627776", "101585857605921/70368744177664"},
		{"50812438537089/35184372088832", "25425729002673/17592186044416"},
		{"106482984417/68719476736", "464951405925/274877906944"},
		{"251985437091/137438953472", "2054902964985/1099511627776"},
		{"1046961216621/549755813888", "542990342439/274877906944"},
	};

	static {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINE);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
		}
	}

	private static RationalPoly solve(RationalPoly f, String var) {
		TreeMap<Monom, RationalPoly> poly = f.coeffsOf(var);
		RationalPoly a1 = poly.remove(new Monom(VARS, var));
		RationalPoly a0 = poly.remove(new Monom(VARS, ""));
		if (!poly.isEmpty()) {
			throw new RuntimeException("Should be empty: " + poly);
		}
		Rational denominator = a1.remove(new Monom(VARS, "")).negate();
		if (!a1.isEmpty()) {
			throw new RuntimeException("Should be empty: " + a1);
		}
		RationalPoly ret = new RationalPoly(VARS);
		a0.forEach((m, c) -> {
			ret.put(m, c.div(denominator));
		});
		return ret;
	}

	public static void main(String[] args) throws Exception {
		Properties p = new Properties();
		// results from 4741634-sage.py, B[1] and B[2]
		try (InputStream in = _4741634.class.getResourceAsStream("4741634.properties")) {
			p.load(in);
		}
		RationalPoly f = new RationalPoly(VARS, "-x**4*y*z**2 - x**3*y**3*z**3 - x**3*y**2 - x**2*y**4*z - x**2*z**3 - x*y**2*z**4 - 5*x*y*z + 4*x*y + 4*x*z - y**3*z**2 + 4*y*z");
		RationalPoly b1 = new RationalPoly(VARS, p.getProperty("B1"));
		RationalPoly b2 = new RationalPoly(VARS, p.getProperty("B2"));
		RationalPoly x = solve(b1, "x");
		RationalPoly y = solve(b2, "y");
		System.out.println("x(z = 1) = " + x.subs('z', _1));
		System.out.println("y(z = 1) = " + y.subs('z', _1));
		// too slow
		RationalPoly fz = f.subs('x', x).subs('y', y);
		// avoid IDE console crash
		try (PrintStream out = new PrintStream("4741634.txt")) {
			out.println("f(z) = " + fz);
		}
		for (int i = 1; i < ROOTS.length; i ++) {
			String[] roots = ROOTS[i];
			Rational z0 = new Rational(roots[0]);
			Rational z1 = new Rational(roots[1]);
			System.out.print("prove f(" + z0 + " <= z <= " + z1 + ") >= 0: ");
			z1.add(z0.negate());
			System.out.println(Bisection.
					search01(fz.subs('z', new RationalPoly(VARS, z1 + "*z + " + z0))).length == 0);
		}
	}
}