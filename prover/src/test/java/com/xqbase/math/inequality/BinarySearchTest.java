package com.xqbase.math.inequality;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class BinarySearchTest {
	private static Logger log = LoggerFactory.getLogger(BinarySearchTest.class);

	private static final Rational INFINITY = Rational.valueOf(Long.MAX_VALUE);

	@BeforeClass
	public static void startup() {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.INFO);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
		}
	}

	private static RationalPoly __(String vars, String expr) {
		return new RationalPoly(vars, expr);
	}

	private static String toString(Rational[] result) {
		return Stream.of(result).map(r -> r == null ? null : Double.valueOf(r.doubleValue())).
				collect(Collectors.toList()).toString();
	}

	private static void	positive(RationalPoly f) {
		Rational[] result = BinarySearch.search(f);
		if (result.length > 0) {
			Assert.fail("expected positive, actually " + toString(result));
		}
	}

	private static void	positive01(RationalPoly f) {
		log.info("search01 " + f);
		Rational[] result = BinarySearch.search01(f);
		if (result.length > 0) {
			Assert.fail("expected positive, actually " + toString(result));
		}
	}

	private static void	negative(RationalPoly f, int signum) {
		Rational[] result = BinarySearch.search(f);
		Assert.assertNotEquals(0, result.length);
		String vars = f.getVars();
		RationalPoly f1 = f;
		for (int i = 0; i < result.length - 1; i ++) {
			f1 = f1.subs(vars.charAt(i), result[i]);
		}
		Rational c0 = f1.remove(new Monom(vars.toString(), ""));
		if (c0 == null) {
			c0 = Rational.valueOf(0);
		}
		Assert.assertTrue(f1.isEmpty());
		Assert.assertEquals(result[result.length - 1], c0);
		Assert.assertEquals(signum, c0.signum());
	}

	private static void critical(RationalPoly f, Rational... x) {
		Rational[] result = BinarySearch.search(f);
		Assert.assertNotEquals(0, result.length);
		for (int i = 0; i < x.length; i ++) {
			Assert.assertEquals(x[i], result[i]);
		}
	}

	@Test
	public void testBasic() {
		negative(__("xy", "x**2 - 2*y"), 0);
		negative(__("xy", "-x**2 + 2*x + y"), -1);
		// 1e-22
		String e_22 = "1/10000000000000000000000";
		// fibonacci 91, 92
		long m = 4660046610375530309L;
		long n = 7540113804746346429L;
		// n*x - m can make minimum x < 1
		RationalPoly f = __("x", n + "*x - " + m);
		f = new RationalPoly("x").addMul(f, f);
		positive(__("x", e_22).add(f));
		negative(__("x", "-" + e_22).add(f), -1);
		/*
		// doesn't work due to critical points near (1, 3, 1) and (1, 2, 1, 1) 
		// (3*x - y)**2 + (x - z)**2
		f = __("xyz", "10*x**2 - 6*x*y - 2*x*z + y**2 + z**2");
		// (2*w - x)**2 + (w - y)**2 + (w - z)**2
		f = __("wxyz", "6*w**2 - 4*w*x - 2*w*y - 2*w*z + x**2 + y**2 + z**2");
		*/
		// luckily not stack overflow: x**2*y**2 + 16*y**2 - 24*y + 9 = 0 at (0, 3/4)
		critical(__("xy", "16*x**2 - 24*x*y + 9*y**2 + 1"), INFINITY, INFINITY);
		// - 30*x*y + ... + 1 causes so: 2*x**2*y**2 + 25*y**2 - 30*y + 9 = 0 at (0, 3/5)
		// - 30*x*y causes stack overflow: 25*x**2*y**2 - 30*x*y + 9 = 0 at x*y = 3/5
		positive(__("xy", "25*x**2 - 29*x*y + 9*y**2"));
		// + 1/4 causes so: 2*x**2*y**2 - 3*x*y + 1/4*y**2 + 1 = 0 at (1, 2/3)
		// remove + 1/5 causes so: y**2 - 3*y + 2 = 0 at y = 1
		negative(__("xy", "2*x**2 - 3*x*y + y**2 + 1/5"), -1);
		// luckily not so: x*y**2 + 16*y**2 - 24*y + 9 = 0 at (0, 3/4)
		critical(__("xy", "16*x**2 - 24*x*y + x + 9*y**2"), INFINITY, INFINITY);
		// - 40*x*y causes so: 25*x**2*y**2 - 30*x*y + 9 = 0 at x*y = 4/5
		positive(__("xy", "25*x**2 - 39*x*y + x + 16*y**2"));
		// - 30*x**2*y causes so: 25*y**2 - 30*y + 9 = 0 at y = 3/5
		// - 30*x**2*y + ... + 1 causes so: x**4*y**4 + 25*x**2 - 30*x + 9 = 0 at (0, 3/5)
		positive(__("xy", "9*x**4 - 29*x**2*y + 25*y**2"));
	}

	@Test
	public void testMathSE() {
		// https://math.stackexchange.com/q/3831395
		positive(__("x", "x**5 - 1/2*x**3 - x + 4/5"));
		// https://math.stackexchange.com/q/83670
		positive(__("x", "x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + 5/2"));
		// https://math.stackexchange.com/q/4765187
		// (1 + x)**7 - 7**(7/3)*x**4
		positive(__("x", "x**7 + 7*x**6 + 21*x**5 - 59*x**4 + 35*x**3 + 21*x**2 + 7*x + 1"));
		// https://math.stackexchange.com/q/1775572
		RationalPoly f = __("uv", "40*u**7*v**3 + 120*u**7*v**2 + 120*u**7*v + 65*u**7 + 40*u**6*v**4 + 376*u**6*v**3 + 888*u**6*v**2 + 768*u**6*v + 351*u**6 + 240*u**5*v**4 + 1416*u**5*v**3 + 2808*u**5*v**2 + 2088*u**5*v + 741*u**5 - 40*u**4*v**6 - 240*u**4*v**5 + 2079*u**4*v**3 + 4437*u**4*v**2 + 2997*u**4*v + 754*u**4 + 25*u**3*v**7 - 25*u**3*v**6 - 675*u**3*v**5 - 1286*u**3*v**4 + 546*u**3*v**3 + 3504*u**3*v**2 + 2412*u**3*v + 390*u**3 + 75*u**2*v**7 + 165*u**2*v**6 - 585*u**2*v**5 - 2058*u**2*v**4 - 1476*u**2*v**3 + 1170*u**2*v**2 + 1134*u**2*v + 156*u**2 + 75*u*v**7 + 181*u*v**6 - 489*u*v**5 - 2178*u*v**4 - 2698*u*v**3 - 1056*u*v**2 - 156*u*v + 65*v**7 + 351*v**6 + 741*v**5 + 754*v**4 + 390*v**3 + 156*v**2");
		positive(f);
		// https://math.stackexchange.com/q/4850712
		// from 4850712.py
		// m, n = 5, 13, non-negative, https://math.stackexchange.com/q/1777075
		f = __("uv", "65*u**5*v**2 + 130*u**5*v + 90*u**5 + 65*u**4*v**3 + 351*u**4*v**2 + 442*u**4*v + 216*u**4 - 65*u**3*v**4 + 508*u**3*v**2 + 496*u**3*v + 108*u**3 + 25*u**2*v**5 - 135*u**2*v**4 - 256*u**2*v**3 + 504*u**2*v**2 + 552*u**2*v + 72*u**2 + 50*u*v**5 - 244*u*v**4 - 928*u*v**3 - 516*u*v**2 - 72*u*v + 90*v**5 + 216*v**4 + 108*v**3 + 72*v**2");
		positive(f);
		// m, n = 63, 164, non-negative
		f = __("uv", "10332*u**5*v**2 + 20664*u**5*v + 14301*u**5 + 10332*u**4*v**3 + 55760*u**4*v**2 + 70192*u**4*v + 34277*u**4 - 10332*u**3*v**4 + 80655*u**3*v**2 + 78654*u**3*v + 17025*u**3 + 3969*u**2*v**5 - 21483*u**2*v**4 - 40703*u**2*v**3 + 80131*u**2*v**2 + 87706*u**2*v + 11350*u**2 + 7938*u*v**5 - 38866*u*v**4 - 147662*u*v**3 - 82031*u*v**2 - 11350*u*v + 14301*v**5 + 34277*v**4 + 17025*v**3 + 11350*v**2");
		positive(f);
		// m, n = 121, 315, negative
		f = __("uv", "38115*u**5*v**2 + 76230*u**5*v + 52756*u**5 + 38115*u**4*v**3 + 205695*u**4*v**2 + 258930*u**4*v + 126440*u**4 - 38115*u**3*v**4 + 297524*u**3*v**2 + 290128*u**3*v + 62784*u**3 + 14641*u**2*v**5 - 79255*u**2*v**4 - 150156*u**2*v**3 + 295608*u**2*v**2 + 323544*u**2*v + 41856*u**2 + 29282*u*v**5 - 143390*u*v**4 - 544752*u*v**3 - 302616*u*v**2 - 41856*u*v + 52756*v**5 + 126440*v**4 + 62784*v**3 + 41856*v**2");
		negative(f, -1);
		// https://math.stackexchange.com/q/2016364
		// results from 2016364.py
		String vars = "abcd";
		RationalPoly a10 = __(vars, "1 - a");
		RationalPoly b10 = __(vars, "1 - b");
		RationalPoly c10 = __(vars, "1 - c");
		RationalPoly d10 = __(vars, "1 - d");
		// f(----)
		f = __(vars, "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 - 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d + 8*a*b*c + 8*a*b*d + 12*a*b + 8*a*c*d + 8*a*c - 2*a*d**2 + 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d + 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 - 2*c**2*d + 8*c**2 - 2*c*d**2 + 12*c*d + d**4 - 4*d**3 + 8*d**2");
		positive01(f);
		// f(---+)
		f = __(vars, "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 - 8*b*c*d + 12*b*c - 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2");
		// doesn't work due to f(1, 1, 1, 1) = 0
		// positive01(f);
		positive01(f.subs('a', __(vars, "1/2*a")));
		positive01(f.subs('a', __(vars, "1 - 1/2*a")).subs('b', b10).subs('c', c10).subs('d', d10));
		// f(--++)
		f = __(vars, "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d - 12*b*c - 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(-+++)
		f = __(vars, "a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c + 8*a*b*d - 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(++++)
		f = __(vars, "a**4 + 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 + 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c + 2*a*d**2 + 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(-+-+)
		f = __(vars, "a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c + 8*a*b*d - 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 + 2*b*c**2 + 8*b*c*d - 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2");
		// doesn't work due to
		// positive01(f);
		// f(a = max(abcd))(0, 1, 1, 1) = 0
		f = __(vars, "a**2*b**4 + a**2*b**2*c**2 + a**2*b**2 + 8*a**2*b*c*d + a**2*c**4 + a**2*c**2*d**2 + a**2*d**4 + a**2*d**2 + a**2 + 4*a*b**3 - 2*a*b**2*c - 2*a*b**2 + 2*a*b*c**2 + 8*a*b*c*d - 8*a*b*c + 8*a*b*d + 2*a*b - 4*a*c**3 + 2*a*c**2*d - 2*a*c*d**2 - 8*a*c*d + 4*a*d**3 - 2*a*d**2 + 2*a*d - 4*a + 8*b**2 - 12*b*c + 8*b*d - 12*b + 8*c**2 - 12*c*d + 8*c + 8*d**2 - 12*d + 8");
		positive01(f.subs('b', b10).subs('c', c10).subs('d', d10));
		// f(b = max(abcd))(1, 0, 1, 1) = 0
		f = __(vars, "a**4*b**2 - 4*a**3*b + a**2*b**2*d**2 + a**2*b**2 + 2*a**2*b*d + 2*a**2*b + 8*a**2 + 8*a*b**2*c*d - 8*a*b*c*d - 8*a*b*c - 2*a*b*d**2 + 8*a*b*d - 2*a*b + 8*a*c - 12*a*d - 12*a + b**2*c**4 + b**2*c**2*d**2 + b**2*c**2 + b**2*d**4 + b**2 - 4*b*c**3 + 2*b*c**2*d + 2*b*c**2 - 2*b*c*d**2 + 8*b*c*d - 2*b*c + 4*b*d**3 + 4*b + 8*c**2 - 12*c*d - 12*c + 8*d**2 + 8*d + 8");
		positive01(f.subs('a', a10).subs('c', c10).subs('d', d10));
		// f(c = max(abcd))(1, 1, 0, 1) = 0
		f = __(vars, "a**4*c**2 - 4*a**3*c + a**2*b**2*c**2 + 2*a**2*b*c + a**2*c**2*d**2 + 2*a**2*c*d + 8*a**2 - 2*a*b**2*c + 8*a*b*c**2*d + 8*a*b*c*d - 8*a*b*c - 12*a*b - 2*a*c*d**2 - 8*a*c*d - 12*a*d + 8*a + b**4*c**2 + 4*b**3*c + b**2*c**2 - 2*b**2*c + 8*b**2 + 8*b*c*d + 2*b*c + 8*b*d - 12*b + c**2*d**4 + c**2*d**2 + c**2 + 4*c*d**3 - 2*c*d**2 + 2*c*d - 4*c + 8*d**2 - 12*d + 8");
		positive01(f.subs('a', a10).subs('b', b10).subs('d', d10));
		// f(d = max(abcd))(1, 1, 1, 0) = 0
		f = __(vars, "a**4*d**2 - 4*a**3*d + a**2*b**2*d**2 + 2*a**2*b*d + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2*d + 8*a*b*c*d**2 - 8*a*b*c*d + 8*a*b*d - 12*a*b - 8*a*c*d + 8*a*c - 2*a*d - 12*a + b**4*d**2 + 4*b**3*d + b**2*c**2*d**2 - 2*b**2*c*d + 8*b**2 + 2*b*c**2*d + 8*b*c*d - 12*b*c + 8*b + c**4*d**2 - 4*c**3*d + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d - 12*c + d**2 + 4*d + 8");
		positive01(f.subs('a', a10).subs('b', b10).subs('c', c10));
	}

	@Test
	public void testYang08() {
		// ISBN 9787030207210, p156, §7.1
		RationalPoly f = __("z", "10195920*z**8 + 2109632*z**7 - 5387520*z**6 + 1361336*z**5 + 61445*z**4 - 52468*z**3 + 6350*z**2 - 300*z + 5");
		positive(f);
		// more steps for f - 1/29
		positive(__("z", "-1/29").add(f));
		// negative for f - 1/28
		negative(__("z", "-1/28").add(f), -1);
		// p172, problem 11, results from p172-11.py
		f = __("uv", "170172209*u**4 - 1301377672*u**3*v + 640688836*u**3 + 3553788598*u**2*v**2 - 3203444180*u**2*v + 640688836*u**2 - 3864133016*u*v**3 + 4484821852*u*v**2 - 1281377672*u*v + 1611722090*v**4 - 961033254*v**3 + 2082238717*v**2");
		positive01(f);
		f = __("uv", "2572755344*u**4 - 6426888360*u**3*v - 3844133016*u**3 + 5315682897*u**2*v**2 + 8649299286*u**2*v + 1441549881*u**2 - 1621722090*u*v**3 - 5766199524*u*v**2 - 2883099762*u*v + 1611722090*v**4 - 961033254*v**3 + 2082238717*v**2");
		positive01(f);
		f = __("uv", "2572755344*u**4 - 20000000*u**3*v - 3844133016*u**3 + 30000000*u**2*v**2 + 1441549881*u**2 - 20000000*u*v**3 + 170172209*v**4 + 640688836*v**3 + 640688836*v**2");
		positive01(f);
	}

	@Test
	public void testHan23() {
		// ISBN 9787312056185, p341, ex 11.7
		String vars = "bcuv";
		RationalPoly b0 = __(vars, "1/2*b");
		RationalPoly b1 = __(vars, "1 - 1/2*b");
		RationalPoly c0 = __(vars, "1/2*c");
		RationalPoly c1 = __(vars, "1 - 1/2*c");
		RationalPoly u0 = __(vars, "1/2*u");
		RationalPoly u1 = __(vars, "1 - 1/2*u");
		RationalPoly v0 = __(vars, "1/2*v");
		RationalPoly v1 = __(vars, "1 - 1/2*v");
		RationalPoly u10 = __(vars, "1 - u");
		RationalPoly v10 = __(vars, "1 - v");
		RationalPoly f;
		// f(uv1) from han23-p341.py
		f = __(vars, "b**5*c*u**2*v**2 + b**5*c*u**2*v + b**5*c*u*v**2 + b**5*c*u*v + b**5*u**2*v**2 + b**5*u**2*v + b**5*u*v**2 + b**5*u*v + b**4*c**2*u**3*v**2 + b**4*c**2*u**3*v + b**4*c**2*u**2*v**3 + 2*b**4*c**2*u**2*v**2 + b**4*c**2*u**2*v + b**4*c**2*u*v**3 + b**4*c**2*u*v**2 - 9*b**4*c**2*u*v + b**4*c*u**3*v**2 + b**4*c*u**3*v + b**4*c*u**2*v**3 + 3*b**4*c*u**2*v**2 - 6*b**4*c*u**2*v + b**4*c*u**2 + b**4*c*u*v**3 - 6*b**4*c*u*v**2 + 3*b**4*c*u*v + b**4*c*u + b**4*c*v**2 + b**4*c*v - 9*b**4*u**2*v**2 + b**4*u**2*v + b**4*u**2 + b**4*u*v**2 + 2*b**4*u*v + b**4*u + b**4*v**2 + b**4*v + b**3*c**3*u**3*v**3 + b**3*c**3*u**3*v**2 + b**3*c**3*u**2*v**3 + 2*b**3*c**3*u**2*v**2 - 8*b**3*c**3*u**2*v - 8*b**3*c**3*u*v**2 + 2*b**3*c**3*u*v + b**3*c**3*u + b**3*c**3*v + b**3*c**3 + b**3*c**2*u**3*v**3 + 3*b**3*c**2*u**3*v**2 - 6*b**3*c**2*u**3*v + b**3*c**2*u**3 + 3*b**3*c**2*u**2*v**3 - 10*b**3*c**2*u**2*v**2 + 7*b**3*c**2*u**2*v + 2*b**3*c**2*u**2 - 6*b**3*c**2*u*v**3 + 7*b**3*c**2*u*v**2 + 6*b**3*c**2*u*v - 7*b**3*c**2*u + b**3*c**2*v**3 + 2*b**3*c**2*v**2 - 7*b**3*c**2*v + b**3*c**2 + b**3*c*u**3*v**3 - 7*b**3*c*u**3*v**2 + 2*b**3*c*u**3*v + b**3*c*u**3 - 7*b**3*c*u**2*v**3 + 6*b**3*c*u**2*v**2 + 7*b**3*c*u**2*v - 6*b**3*c*u**2 + 2*b**3*c*u*v**3 + 7*b**3*c*u*v**2 - 10*b**3*c*u*v + 3*b**3*c*u + b**3*c*v**3 - 6*b**3*c*v**2 + 3*b**3*c*v + b**3*c + b**3*u**3*v**3 + b**3*u**3*v**2 + b**3*u**2*v**3 + 2*b**3*u**2*v**2 - 8*b**3*u**2*v - 8*b**3*u*v**2 + 2*b**3*u*v + b**3*u + b**3*v + b**3 - 9*b**2*c**4*u**2*v**2 + b**2*c**4*u**2*v + b**2*c**4*u**2 + b**2*c**4*u*v**2 + 2*b**2*c**4*u*v + b**2*c**4*u + b**2*c**4*v**2 + b**2*c**4*v + b**2*c**3*u**3*v**3 - 7*b**2*c**3*u**3*v**2 + 2*b**2*c**3*u**3*v + b**2*c**3*u**3 - 7*b**2*c**3*u**2*v**3 + 6*b**2*c**3*u**2*v**2 + 7*b**2*c**3*u**2*v - 6*b**2*c**3*u**2 + 2*b**2*c**3*u*v**3 + 7*b**2*c**3*u*v**2 - 10*b**2*c**3*u*v + 3*b**2*c**3*u + b**2*c**3*v**3 - 6*b**2*c**3*v**2 + 3*b**2*c**3*v + b**2*c**3 - 9*b**2*c**2*u**3*v**3 + 3*b**2*c**2*u**3*v**2 + 6*b**2*c**2*u**3*v - 6*b**2*c**2*u**3 + 3*b**2*c**2*u**2*v**3 + 12*b**2*c**2*u**2*v**2 - 12*b**2*c**2*u**2*v + 6*b**2*c**2*u**2 + 6*b**2*c**2*u*v**3 - 12*b**2*c**2*u*v**2 + 12*b**2*c**2*u*v + 3*b**2*c**2*u - 6*b**2*c**2*v**3 + 6*b**2*c**2*v**2 + 3*b**2*c**2*v - 9*b**2*c**2 + b**2*c*u**3*v**3 + 3*b**2*c*u**3*v**2 - 6*b**2*c*u**3*v + b**2*c*u**3 + 3*b**2*c*u**2*v**3 - 10*b**2*c*u**2*v**2 + 7*b**2*c*u**2*v + 2*b**2*c*u**2 - 6*b**2*c*u*v**3 + 7*b**2*c*u*v**2 + 6*b**2*c*u*v - 7*b**2*c*u + b**2*c*v**3 + 2*b**2*c*v**2 - 7*b**2*c*v + b**2*c + b**2*u**3*v**2 + b**2*u**3*v + b**2*u**2*v**3 + 2*b**2*u**2*v**2 + b**2*u**2*v + b**2*u*v**3 + b**2*u*v**2 - 9*b**2*u*v + b*c**5*u**2*v**2 + b*c**5*u**2*v + b*c**5*u*v**2 + b*c**5*u*v + b*c**4*u**3*v**2 + b*c**4*u**3*v + b*c**4*u**2*v**3 + 3*b*c**4*u**2*v**2 - 6*b*c**4*u**2*v + b*c**4*u**2 + b*c**4*u*v**3 - 6*b*c**4*u*v**2 + 3*b*c**4*u*v + b*c**4*u + b*c**4*v**2 + b*c**4*v + b*c**3*u**3*v**3 + 3*b*c**3*u**3*v**2 - 6*b*c**3*u**3*v + b*c**3*u**3 + 3*b*c**3*u**2*v**3 - 10*b*c**3*u**2*v**2 + 7*b*c**3*u**2*v + 2*b*c**3*u**2 - 6*b*c**3*u*v**3 + 7*b*c**3*u*v**2 + 6*b*c**3*u*v - 7*b*c**3*u + b*c**3*v**3 + 2*b*c**3*v**2 - 7*b*c**3*v + b*c**3 + b*c**2*u**3*v**3 - 7*b*c**2*u**3*v**2 + 2*b*c**2*u**3*v + b*c**2*u**3 - 7*b*c**2*u**2*v**3 + 6*b*c**2*u**2*v**2 + 7*b*c**2*u**2*v - 6*b*c**2*u**2 + 2*b*c**2*u*v**3 + 7*b*c**2*u*v**2 - 10*b*c**2*u*v + 3*b*c**2*u + b*c**2*v**3 - 6*b*c**2*v**2 + 3*b*c**2*v + b*c**2 + b*c*u**3*v**2 + b*c*u**3*v + b*c*u**2*v**3 + 3*b*c*u**2*v**2 - 6*b*c*u**2*v + b*c*u**2 + b*c*u*v**3 - 6*b*c*u*v**2 + 3*b*c*u*v + b*c*u + b*c*v**2 + b*c*v + b*u**2*v**2 + b*u**2*v + b*u*v**2 + b*u*v + c**5*u**2*v**2 + c**5*u**2*v + c**5*u*v**2 + c**5*u*v + c**4*u**3*v**2 + c**4*u**3*v + c**4*u**2*v**3 + 2*c**4*u**2*v**2 + c**4*u**2*v + c**4*u*v**3 + c**4*u*v**2 - 9*c**4*u*v + c**3*u**3*v**3 + c**3*u**3*v**2 + c**3*u**2*v**3 + 2*c**3*u**2*v**2 - 8*c**3*u**2*v - 8*c**3*u*v**2 + 2*c**3*u*v + c**3*u + c**3*v + c**3 - 9*c**2*u**2*v**2 + c**2*u**2*v + c**2*u**2 + c**2*u*v**2 + 2*c**2*u*v + c**2*u + c**2*v**2 + c**2*v + c*u**2*v**2 + c*u**2*v + c*u*v**2 + c*u*v");
		log.info("f(uv1),--");
		positive01(f.subs('b', b0).subs('c', c0));
		log.info("f(uv1),-+");
		positive01(f.subs('b', b0).subs('c', c1).subs('u', u10).subs('v', v10));
		log.info("f(uv1),+-");
		positive01(f.subs('b', b1).subs('c', c0).subs('u', u10).subs('v', v10));
		log.info("f(uv1),++");
		positive01(f.subs('b', b1).subs('c', c1));
		// f(u1v) from han23-p341.py
		f = __(vars, "b**5*c*u**2*v**2 + b**5*c*u**2*v + b**5*c*u*v**2 + b**5*c*u*v + b**5*u**2*v**2 + b**5*u**2*v + b**5*u*v**2 + b**5*u*v + b**4*c**2*u**3*v**2 + b**4*c**2*u**3*v + b**4*c**2*u**2*v**2 + 2*b**4*c**2*u**2*v + b**4*c**2*u**2 - 9*b**4*c**2*u*v**2 + b**4*c**2*u*v + b**4*c**2*u + b**4*c*u**3*v**2 + b**4*c*u**3*v + b**4*c*u**2*v**3 - 6*b**4*c*u**2*v**2 + 3*b**4*c*u**2*v + b**4*c*u**2 + b**4*c*u*v**3 + 3*b**4*c*u*v**2 - 6*b**4*c*u*v + b**4*c*u + b**4*c*v**2 + b**4*c*v + b**4*u**2*v**3 + b**4*u**2*v**2 - 9*b**4*u**2*v + b**4*u*v**3 + 2*b**4*u*v**2 + b**4*u*v + b**4*v**2 + b**4*v + b**3*c**3*u**3*v + b**3*c**3*u**3 - 8*b**3*c**3*u**2*v**2 + 2*b**3*c**3*u**2*v + b**3*c**3*u**2 + b**3*c**3*u*v**3 + 2*b**3*c**3*u*v**2 - 8*b**3*c**3*u*v + b**3*c**3*v**3 + b**3*c**3*v**2 + b**3*c**2*u**3*v**3 - 6*b**3*c**2*u**3*v**2 + 3*b**3*c**2*u**3*v + b**3*c**2*u**3 + 2*b**3*c**2*u**2*v**3 + 7*b**3*c**2*u**2*v**2 - 10*b**3*c**2*u**2*v + 3*b**3*c**2*u**2 - 7*b**3*c**2*u*v**3 + 6*b**3*c**2*u*v**2 + 7*b**3*c**2*u*v - 6*b**3*c**2*u + b**3*c**2*v**3 - 7*b**3*c**2*v**2 + 2*b**3*c**2*v + b**3*c**2 + b**3*c*u**3*v**3 + 2*b**3*c*u**3*v**2 - 7*b**3*c*u**3*v + b**3*c*u**3 - 6*b**3*c*u**2*v**3 + 7*b**3*c*u**2*v**2 + 6*b**3*c*u**2*v - 7*b**3*c*u**2 + 3*b**3*c*u*v**3 - 10*b**3*c*u*v**2 + 7*b**3*c*u*v + 2*b**3*c*u + b**3*c*v**3 + 3*b**3*c*v**2 - 6*b**3*c*v + b**3*c + b**3*u**3*v + b**3*u**3 - 8*b**3*u**2*v**2 + 2*b**3*u**2*v + b**3*u**2 + b**3*u*v**3 + 2*b**3*u*v**2 - 8*b**3*u*v + b**3*v**3 + b**3*v**2 + b**2*c**4*u**2*v**3 + b**2*c**4*u**2*v**2 - 9*b**2*c**4*u**2*v + b**2*c**4*u*v**3 + 2*b**2*c**4*u*v**2 + b**2*c**4*u*v + b**2*c**4*v**2 + b**2*c**4*v + b**2*c**3*u**3*v**3 + 2*b**2*c**3*u**3*v**2 - 7*b**2*c**3*u**3*v + b**2*c**3*u**3 - 6*b**2*c**3*u**2*v**3 + 7*b**2*c**3*u**2*v**2 + 6*b**2*c**3*u**2*v - 7*b**2*c**3*u**2 + 3*b**2*c**3*u*v**3 - 10*b**2*c**3*u*v**2 + 7*b**2*c**3*u*v + 2*b**2*c**3*u + b**2*c**3*v**3 + 3*b**2*c**3*v**2 - 6*b**2*c**3*v + b**2*c**3 - 6*b**2*c**2*u**3*v**3 + 6*b**2*c**2*u**3*v**2 + 3*b**2*c**2*u**3*v - 9*b**2*c**2*u**3 + 6*b**2*c**2*u**2*v**3 - 12*b**2*c**2*u**2*v**2 + 12*b**2*c**2*u**2*v + 3*b**2*c**2*u**2 + 3*b**2*c**2*u*v**3 + 12*b**2*c**2*u*v**2 - 12*b**2*c**2*u*v + 6*b**2*c**2*u - 9*b**2*c**2*v**3 + 3*b**2*c**2*v**2 + 6*b**2*c**2*v - 6*b**2*c**2 + b**2*c*u**3*v**3 - 6*b**2*c*u**3*v**2 + 3*b**2*c*u**3*v + b**2*c*u**3 + 2*b**2*c*u**2*v**3 + 7*b**2*c*u**2*v**2 - 10*b**2*c*u**2*v + 3*b**2*c*u**2 - 7*b**2*c*u*v**3 + 6*b**2*c*u*v**2 + 7*b**2*c*u*v - 6*b**2*c*u + b**2*c*v**3 - 7*b**2*c*v**2 + 2*b**2*c*v + b**2*c + b**2*u**3*v**2 + b**2*u**3*v + b**2*u**2*v**2 + 2*b**2*u**2*v + b**2*u**2 - 9*b**2*u*v**2 + b**2*u*v + b**2*u + b*c**5*u**2*v**2 + b*c**5*u**2*v + b*c**5*u*v**2 + b*c**5*u*v + b*c**4*u**3*v**2 + b*c**4*u**3*v + b*c**4*u**2*v**3 - 6*b*c**4*u**2*v**2 + 3*b*c**4*u**2*v + b*c**4*u**2 + b*c**4*u*v**3 + 3*b*c**4*u*v**2 - 6*b*c**4*u*v + b*c**4*u + b*c**4*v**2 + b*c**4*v + b*c**3*u**3*v**3 - 6*b*c**3*u**3*v**2 + 3*b*c**3*u**3*v + b*c**3*u**3 + 2*b*c**3*u**2*v**3 + 7*b*c**3*u**2*v**2 - 10*b*c**3*u**2*v + 3*b*c**3*u**2 - 7*b*c**3*u*v**3 + 6*b*c**3*u*v**2 + 7*b*c**3*u*v - 6*b*c**3*u + b*c**3*v**3 - 7*b*c**3*v**2 + 2*b*c**3*v + b*c**3 + b*c**2*u**3*v**3 + 2*b*c**2*u**3*v**2 - 7*b*c**2*u**3*v + b*c**2*u**3 - 6*b*c**2*u**2*v**3 + 7*b*c**2*u**2*v**2 + 6*b*c**2*u**2*v - 7*b*c**2*u**2 + 3*b*c**2*u*v**3 - 10*b*c**2*u*v**2 + 7*b*c**2*u*v + 2*b*c**2*u + b*c**2*v**3 + 3*b*c**2*v**2 - 6*b*c**2*v + b*c**2 + b*c*u**3*v**2 + b*c*u**3*v + b*c*u**2*v**3 - 6*b*c*u**2*v**2 + 3*b*c*u**2*v + b*c*u**2 + b*c*u*v**3 + 3*b*c*u*v**2 - 6*b*c*u*v + b*c*u + b*c*v**2 + b*c*v + b*u**2*v**2 + b*u**2*v + b*u*v**2 + b*u*v + c**5*u**2*v**2 + c**5*u**2*v + c**5*u*v**2 + c**5*u*v + c**4*u**3*v**2 + c**4*u**3*v + c**4*u**2*v**2 + 2*c**4*u**2*v + c**4*u**2 - 9*c**4*u*v**2 + c**4*u*v + c**4*u + c**3*u**3*v + c**3*u**3 - 8*c**3*u**2*v**2 + 2*c**3*u**2*v + c**3*u**2 + c**3*u*v**3 + 2*c**3*u*v**2 - 8*c**3*u*v + c**3*v**3 + c**3*v**2 + c**2*u**2*v**3 + c**2*u**2*v**2 - 9*c**2*u**2*v + c**2*u*v**3 + 2*c**2*u*v**2 + c**2*u*v + c**2*v**2 + c**2*v + c*u**2*v**2 + c*u**2*v + c*u*v**2 + c*u*v");
		log.info("f(u1v),--");
		positive01(f.subs('b', b0).subs('c', c0));
		log.info("f(u1v),-+-?");
		positive01(f.subs('b', b0).subs('c', c1).subs('u', u0));
		log.info("f(u1v),-+?-");
		positive01(f.subs('b', b0).subs('c', c1).subs('v', v0));
		log.info("f(u1v),-+++");
		positive01(f.subs('b', b0).subs('c', c1).subs('u', u1).subs('v', v1));
		log.info("f(u1v),+--?");
		positive01(f.subs('b', b1).subs('c', c0).subs('u', u0));
		log.info("f(u1v),+-?-");
		positive01(f.subs('b', b1).subs('c', c0).subs('v', v0));
		log.info("f(u1v),+-++");
		positive01(f.subs('b', b1).subs('c', c0).subs('u', u1).subs('v', v1));
		log.info("f(u1v),++");
		positive01(f.subs('b', b1).subs('c', c1));
		// ISBN 9787312056185, p354, ex 11.20 (p113, ex 5.26)
		// f from han23-p354u.py, too slow unable to prove
		f = __("RStUVw", "4*R**4*S**4*U**2*V**2*t**2*w + 8*R**4*S**4*U**2*V**2*t*w + 4*R**4*S**4*U**2*V**2*w + R**4*S**2*U**2*V**4*t**2*w**2 + 2*R**4*S**2*U**2*V**4*t**2*w + R**4*S**2*U**2*V**4*t**2 + 2*R**4*S**2*U**2*V**4*t*w**2 + 4*R**4*S**2*U**2*V**4*t*w + 2*R**4*S**2*U**2*V**4*t + R**4*S**2*U**2*V**4*w**2 + 2*R**4*S**2*U**2*V**4*w + R**4*S**2*U**2*V**4 + 2*R**4*S**2*U**2*V**2*t**2*w**2 - 4*R**4*S**2*U**2*V**2*t**2*w + 2*R**4*S**2*U**2*V**2*t**2 + 4*R**4*S**2*U**2*V**2*t*w**2 - 8*R**4*S**2*U**2*V**2*t*w + 4*R**4*S**2*U**2*V**2*t + 2*R**4*S**2*U**2*V**2*w**2 - 4*R**4*S**2*U**2*V**2*w + 2*R**4*S**2*U**2*V**2 + R**4*S**2*U**2*t**2*w**2 + 2*R**4*S**2*U**2*t**2*w + R**4*S**2*U**2*t**2 + 2*R**4*S**2*U**2*t*w**2 + 4*R**4*S**2*U**2*t*w + 2*R**4*S**2*U**2*t + R**4*S**2*U**2*w**2 + 2*R**4*S**2*U**2*w + R**4*S**2*U**2 + 4*R**4*U**2*V**2*t**2*w + 8*R**4*U**2*V**2*t*w + 4*R**4*U**2*V**2*w - 2*R**3*S**3*U**3*V**3*t**2*w**2 + 2*R**3*S**3*U**3*V**3*t**2 + 2*R**3*S**3*U**3*V**3*w**2 - 2*R**3*S**3*U**3*V**3 + 2*R**3*S**3*U**3*V*t**2*w**2 - 2*R**3*S**3*U**3*V*t**2 - 2*R**3*S**3*U**3*V*w**2 + 2*R**3*S**3*U**3*V + 8*R**3*S**3*U**2*V**2*t**2*w**2 - 16*R**3*S**3*U**2*V**2*t**2*w + 8*R**3*S**3*U**2*V**2*t**2 - 8*R**3*S**3*U**2*V**2*w**2 + 16*R**3*S**3*U**2*V**2*w - 8*R**3*S**3*U**2*V**2 + 2*R**3*S**3*U*V**3*t**2*w**2 - 2*R**3*S**3*U*V**3*t**2 - 2*R**3*S**3*U*V**3*w**2 + 2*R**3*S**3*U*V**3 - 2*R**3*S**3*U*V*t**2*w**2 + 2*R**3*S**3*U*V*t**2 + 2*R**3*S**3*U*V*w**2 - 2*R**3*S**3*U*V + 2*R**3*S*U**3*V**3*t**2*w**2 - 2*R**3*S*U**3*V**3*t**2 - 2*R**3*S*U**3*V**3*w**2 + 2*R**3*S*U**3*V**3 - 2*R**3*S*U**3*V*t**2*w**2 + 2*R**3*S*U**3*V*t**2 + 2*R**3*S*U**3*V*w**2 - 2*R**3*S*U**3*V - 8*R**3*S*U**2*V**2*t**2*w**2 + 16*R**3*S*U**2*V**2*t**2*w - 8*R**3*S*U**2*V**2*t**2 + 8*R**3*S*U**2*V**2*w**2 - 16*R**3*S*U**2*V**2*w + 8*R**3*S*U**2*V**2 - 2*R**3*S*U*V**3*t**2*w**2 + 2*R**3*S*U*V**3*t**2 + 2*R**3*S*U*V**3*w**2 - 2*R**3*S*U*V**3 + 2*R**3*S*U*V*t**2*w**2 - 2*R**3*S*U*V*t**2 - 2*R**3*S*U*V*w**2 + 2*R**3*S*U*V + R**2*S**4*U**4*V**2*t**2*w**2 + 2*R**2*S**4*U**4*V**2*t**2*w + R**2*S**4*U**4*V**2*t**2 + 2*R**2*S**4*U**4*V**2*t*w**2 + 4*R**2*S**4*U**4*V**2*t*w + 2*R**2*S**4*U**4*V**2*t + R**2*S**4*U**4*V**2*w**2 + 2*R**2*S**4*U**4*V**2*w + R**2*S**4*U**4*V**2 + 2*R**2*S**4*U**2*V**2*t**2*w**2 - 4*R**2*S**4*U**2*V**2*t**2*w + 2*R**2*S**4*U**2*V**2*t**2 + 4*R**2*S**4*U**2*V**2*t*w**2 - 8*R**2*S**4*U**2*V**2*t*w + 4*R**2*S**4*U**2*V**2*t + 2*R**2*S**4*U**2*V**2*w**2 - 4*R**2*S**4*U**2*V**2*w + 2*R**2*S**4*U**2*V**2 + R**2*S**4*V**2*t**2*w**2 + 2*R**2*S**4*V**2*t**2*w + R**2*S**4*V**2*t**2 + 2*R**2*S**4*V**2*t*w**2 + 4*R**2*S**4*V**2*t*w + 2*R**2*S**4*V**2*t + R**2*S**4*V**2*w**2 + 2*R**2*S**4*V**2*w + R**2*S**4*V**2 + 4*R**2*S**2*U**4*V**4*t*w**2 + 8*R**2*S**2*U**4*V**4*t*w + 4*R**2*S**2*U**4*V**4*t + 2*R**2*S**2*U**4*V**2*t**2*w**2 + 4*R**2*S**2*U**4*V**2*t**2*w + 2*R**2*S**2*U**4*V**2*t**2 - 4*R**2*S**2*U**4*V**2*t*w**2 - 8*R**2*S**2*U**4*V**2*t*w - 4*R**2*S**2*U**4*V**2*t + 2*R**2*S**2*U**4*V**2*w**2 + 4*R**2*S**2*U**4*V**2*w + 2*R**2*S**2*U**4*V**2 + 4*R**2*S**2*U**4*t*w**2 + 8*R**2*S**2*U**4*t*w + 4*R**2*S**2*U**4*t + 8*R**2*S**2*U**3*V**3*t**2*w**2 - 8*R**2*S**2*U**3*V**3*t**2 - 16*R**2*S**2*U**3*V**3*t*w**2 + 16*R**2*S**2*U**3*V**3*t + 8*R**2*S**2*U**3*V**3*w**2 - 8*R**2*S**2*U**3*V**3 - 8*R**2*S**2*U**3*V*t**2*w**2 + 8*R**2*S**2*U**3*V*t**2 + 16*R**2*S**2*U**3*V*t*w**2 - 16*R**2*S**2*U**3*V*t - 8*R**2*S**2*U**3*V*w**2 + 8*R**2*S**2*U**3*V + 2*R**2*S**2*U**2*V**4*t**2*w**2 + 4*R**2*S**2*U**2*V**4*t**2*w + 2*R**2*S**2*U**2*V**4*t**2 - 4*R**2*S**2*U**2*V**4*t*w**2 - 8*R**2*S**2*U**2*V**4*t*w - 4*R**2*S**2*U**2*V**4*t + 2*R**2*S**2*U**2*V**4*w**2 + 4*R**2*S**2*U**2*V**4*w + 2*R**2*S**2*U**2*V**4 - 24*R**2*S**2*U**2*V**2*t**2*w**2 + 32*R**2*S**2*U**2*V**2*t**2*w - 24*R**2*S**2*U**2*V**2*t**2 + 32*R**2*S**2*U**2*V**2*t*w**2 - 32*R**2*S**2*U**2*V**2*t*w + 32*R**2*S**2*U**2*V**2*t - 24*R**2*S**2*U**2*V**2*w**2 + 32*R**2*S**2*U**2*V**2*w - 24*R**2*S**2*U**2*V**2 + 2*R**2*S**2*U**2*t**2*w**2 + 4*R**2*S**2*U**2*t**2*w + 2*R**2*S**2*U**2*t**2 - 4*R**2*S**2*U**2*t*w**2 - 8*R**2*S**2*U**2*t*w - 4*R**2*S**2*U**2*t + 2*R**2*S**2*U**2*w**2 + 4*R**2*S**2*U**2*w + 2*R**2*S**2*U**2 - 8*R**2*S**2*U*V**3*t**2*w**2 + 8*R**2*S**2*U*V**3*t**2 + 16*R**2*S**2*U*V**3*t*w**2 - 16*R**2*S**2*U*V**3*t - 8*R**2*S**2*U*V**3*w**2 + 8*R**2*S**2*U*V**3 + 8*R**2*S**2*U*V*t**2*w**2 - 8*R**2*S**2*U*V*t**2 - 16*R**2*S**2*U*V*t*w**2 + 16*R**2*S**2*U*V*t + 8*R**2*S**2*U*V*w**2 - 8*R**2*S**2*U*V + 4*R**2*S**2*V**4*t*w**2 + 8*R**2*S**2*V**4*t*w + 4*R**2*S**2*V**4*t + 2*R**2*S**2*V**2*t**2*w**2 + 4*R**2*S**2*V**2*t**2*w + 2*R**2*S**2*V**2*t**2 - 4*R**2*S**2*V**2*t*w**2 - 8*R**2*S**2*V**2*t*w - 4*R**2*S**2*V**2*t + 2*R**2*S**2*V**2*w**2 + 4*R**2*S**2*V**2*w + 2*R**2*S**2*V**2 + 4*R**2*S**2*t*w**2 + 8*R**2*S**2*t*w + 4*R**2*S**2*t + R**2*U**4*V**2*t**2*w**2 + 2*R**2*U**4*V**2*t**2*w + R**2*U**4*V**2*t**2 + 2*R**2*U**4*V**2*t*w**2 + 4*R**2*U**4*V**2*t*w + 2*R**2*U**4*V**2*t + R**2*U**4*V**2*w**2 + 2*R**2*U**4*V**2*w + R**2*U**4*V**2 + 2*R**2*U**2*V**2*t**2*w**2 - 4*R**2*U**2*V**2*t**2*w + 2*R**2*U**2*V**2*t**2 + 4*R**2*U**2*V**2*t*w**2 - 8*R**2*U**2*V**2*t*w + 4*R**2*U**2*V**2*t + 2*R**2*U**2*V**2*w**2 - 4*R**2*U**2*V**2*w + 2*R**2*U**2*V**2 + R**2*V**2*t**2*w**2 + 2*R**2*V**2*t**2*w + R**2*V**2*t**2 + 2*R**2*V**2*t*w**2 + 4*R**2*V**2*t*w + 2*R**2*V**2*t + R**2*V**2*w**2 + 2*R**2*V**2*w + R**2*V**2 + 2*R*S**3*U**3*V**3*t**2*w**2 - 2*R*S**3*U**3*V**3*t**2 - 2*R*S**3*U**3*V**3*w**2 + 2*R*S**3*U**3*V**3 - 2*R*S**3*U**3*V*t**2*w**2 + 2*R*S**3*U**3*V*t**2 + 2*R*S**3*U**3*V*w**2 - 2*R*S**3*U**3*V - 8*R*S**3*U**2*V**2*t**2*w**2 + 16*R*S**3*U**2*V**2*t**2*w - 8*R*S**3*U**2*V**2*t**2 + 8*R*S**3*U**2*V**2*w**2 - 16*R*S**3*U**2*V**2*w + 8*R*S**3*U**2*V**2 - 2*R*S**3*U*V**3*t**2*w**2 + 2*R*S**3*U*V**3*t**2 + 2*R*S**3*U*V**3*w**2 - 2*R*S**3*U*V**3 + 2*R*S**3*U*V*t**2*w**2 - 2*R*S**3*U*V*t**2 - 2*R*S**3*U*V*w**2 + 2*R*S**3*U*V - 2*R*S*U**3*V**3*t**2*w**2 + 2*R*S*U**3*V**3*t**2 + 2*R*S*U**3*V**3*w**2 - 2*R*S*U**3*V**3 + 2*R*S*U**3*V*t**2*w**2 - 2*R*S*U**3*V*t**2 - 2*R*S*U**3*V*w**2 + 2*R*S*U**3*V + 8*R*S*U**2*V**2*t**2*w**2 - 16*R*S*U**2*V**2*t**2*w + 8*R*S*U**2*V**2*t**2 - 8*R*S*U**2*V**2*w**2 + 16*R*S*U**2*V**2*w - 8*R*S*U**2*V**2 + 2*R*S*U*V**3*t**2*w**2 - 2*R*S*U*V**3*t**2 - 2*R*S*U*V**3*w**2 + 2*R*S*U*V**3 - 2*R*S*U*V*t**2*w**2 + 2*R*S*U*V*t**2 + 2*R*S*U*V*w**2 - 2*R*S*U*V + 4*S**4*U**2*V**2*t**2*w + 8*S**4*U**2*V**2*t*w + 4*S**4*U**2*V**2*w + S**2*U**2*V**4*t**2*w**2 + 2*S**2*U**2*V**4*t**2*w + S**2*U**2*V**4*t**2 + 2*S**2*U**2*V**4*t*w**2 + 4*S**2*U**2*V**4*t*w + 2*S**2*U**2*V**4*t + S**2*U**2*V**4*w**2 + 2*S**2*U**2*V**4*w + S**2*U**2*V**4 + 2*S**2*U**2*V**2*t**2*w**2 - 4*S**2*U**2*V**2*t**2*w + 2*S**2*U**2*V**2*t**2 + 4*S**2*U**2*V**2*t*w**2 - 8*S**2*U**2*V**2*t*w + 4*S**2*U**2*V**2*t + 2*S**2*U**2*V**2*w**2 - 4*S**2*U**2*V**2*w + 2*S**2*U**2*V**2 + S**2*U**2*t**2*w**2 + 2*S**2*U**2*t**2*w + S**2*U**2*t**2 + 2*S**2*U**2*t*w**2 + 4*S**2*U**2*t*w + 2*S**2*U**2*t + S**2*U**2*w**2 + 2*S**2*U**2*w + S**2*U**2 + 4*U**2*V**2*t**2*w + 8*U**2*V**2*t*w + 4*U**2*V**2*w");
		// positive(f);
	}
}