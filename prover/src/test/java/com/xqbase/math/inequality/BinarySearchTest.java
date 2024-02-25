package com.xqbase.math.inequality;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class BinarySearchTest {
	@BeforeClass
	public static void startup() {
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINE);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
		}
	}

	private static RationalPoly __(String vars, String expr) {
		return new RationalPoly(vars, expr);
	}

	private static void	positive(RationalPoly f) {
		Assert.assertEquals(0, BinarySearch.search(f).length);
	}

	private static void	positive01(RationalPoly f) {
		Assert.assertEquals(0, BinarySearch.search01(f).length);
	}

	private static void	negative(RationalPoly f, int signum) {
		Rational[] result = BinarySearch.search(f);
		Assert.assertNotEquals(0, result.length);
		String vars = f.getVars();
		RationalPoly f1 = f;
		for (int i = 0; i < result.length - 1; i ++) {
			f1 = f1.subs(vars.charAt(i), result[i]);
		}
		Rational c0 = f1.remove(new Mono(vars.toString(), ""));
		if (c0 == null) {
			c0 = Rational.valueOf(0);
		}
		Assert.assertTrue(f1.isEmpty());
		Assert.assertEquals(result[result.length - 1], c0);
		Assert.assertEquals(signum, c0.signum());
	}

	@Test
	public void testBasic() {
		negative(__("xy", "x**2 - y"), 0);
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
		// luckily not stack overflow: x**2*y**2 + 16*y**2 - 24*y + 9 at (0, 3/4)
		negative(__("xy", "16*x**2 - 24*x*y + 9*y**2 + 1"), 1);
		// - 30*x*y + ... + 1 causes so: 2*x**2*y**2 + 25*y**2 - 30*y + 9 = 0 at (0, 3/5)
		// - 30*x*y causes stack overflow: 25*x**2*y**2 - 30*x*y + 9 = 0 at x*y = 3/5
		positive(__("xy", "25*x**2 - 29*x*y + 9*y**2"));
		// + 1/4 causes so: 2*x**2*y**2 - 3*x*y + 1/4*y**2 + 1 = 0 at (1, 2/3)
		// remove + 1/5 causes so: y**2 - 3*y + 2 = 0 at y = 1
		negative(__("xy", "2*x**2 - 3*x*y + y**2 + 1/5"), -1);
		// luckily not so: x*y**2 + 16*y**2 - 24*y + 9 = 0 at (0, 3/4)
		negative(__("xy", "16*x**2 - 24*x*y + x + 9*y**2"), 1);
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
		RationalPoly f = __("uv", "25*u**8*v**7 + 310*u**8*v**6 + 1620*u**8*v**5 + 4640*u**8*v**4 + 7960*u**8*v**3 + 8400*u**8*v**2 + 5280*u**8*v + 1600*u**8 + 75*u**7*v**7 + 1025*u**7*v**6 + 5760*u**7*v**5 + 17340*u**7*v**4 + 30696*u**7*v**3 + 33336*u**7*v**2 + 22272*u**7*v + 7648*u**7 + 75*u**6*v**7 + 1215*u**6*v**6 + 7605*u**6*v**5 + 24150*u**6*v**4 + 42816*u**6*v**3 + 45384*u**6*v**2 + 31944*u**6*v + 13680*u**6 + 65*u**5*v**7 + 1091*u**5*v**6 + 7047*u**5*v**5 + 21924*u**5*v**4 + 33751*u**5*v**3 + 24738*u**5*v**2 + 12868*u**5*v + 10073*u**5 + 351*u**4*v**6 + 3723*u**4*v**5 + 14112*u**4*v**4 + 20682*u**4*v**3 + 3441*u**4*v**2 - 11196*u**4*v + 531*u**4 + 741*u**3*v**5 + 5232*u**3*v**4 + 10740*u**3*v**3 + 1656*u**3*v**2 - 11115*u**3*v - 2193*u**3 + 754*u**2*v**4 + 3334*u**2*v**3 + 3078*u**2*v**2 - 1156*u**2*v + 738*u**2 + 390*u*v**3 + 1284*u*v**2 + 1590*u*v + 1554*u + 156*v**2 + 468*v + 468");
		positive(f);
		f = __("uv", "65*u**10*v**8 + 865*u**9*v**8 + 546*u**9*v**7 + 5145*u**8*v**8 + 6417*u**8*v**7 + 1989*u**8*v**6 + 18095*u**7*v**8 + 33168*u**7*v**7 + 20196*u**7*v**6 + 4095*u**7*v**5 + 41930*u**6*v**8 + 99425*u**6*v**7 + 88116*u**6*v**6 + 34758*u**6*v**5 + 5226*u**6*v**4 + 67380*u**5*v**8 + 191868*u**5*v**7 + 216555*u**5*v**6 + 122112*u**5*v**5 + 35385*u**5*v**4 + 4329*u**5*v**3 + 76600*u**4*v**8 + 249636*u**4*v**7 + 330390*u**4*v**6 + 229495*u**4*v**5 + 92637*u**4*v**4 + 22215*u**4*v**3 + 2392*u**4*v**2 + 61160*u**3*v**8 + 221472*u**3*v**7 + 324744*u**3*v**6 + 249474*u**3*v**5 + 115662*u**3*v**4 + 38988*u**3*v**3 + 9242*u**3*v**2 + 858*u**3*v + 32880*u**2*v**8 + 130488*u**2*v**7 + 204816*u**2*v**6 + 159063*u**2*v**5 + 67386*u**2*v**4 + 24186*u**2*v**3 + 10974*u**2*v**2 + 2766*u**2*v + 156*u**2 + 10720*u*v**8 + 46560*u*v**7 + 77496*u*v**6 + 57643*u*v**5 + 14382*u*v**4 + 150*u*v**3 + 4108*u*v**2 + 3072*u*v + 468*u + 1600*v**8 + 7648*v**7 + 13680*v**6 + 10073*v**5 + 531*v**4 - 2193*v**3 + 738*v**2 + 1554*v + 468");
		positive(f);
		// https://math.stackexchange.com/q/4850712
		// from 4850712.py
		// m, n = 5, 13, non-negative, https://math.stackexchange.com/q/1777075
		f = __("uv", "25*u**5*v**5 + 185*u**5*v**4 + 545*u**5*v**3 + 895*u**5*v**2 + 960*u**5*v + 540*u**5 + 50*u**4*v**5 + 365*u**4*v**4 + 920*u**4*v**3 + 1111*u**4*v**2 + 1214*u**4*v + 1104*u**4 + 90*u**3*v**5 + 656*u**3*v**4 + 1392*u**3*v**3 + 316*u**3*v**2 - 1206*u**3*v - 66*u**3 + 216*u**2*v**4 + 800*u**2*v**3 + 120*u**2*v**2 - 1712*u**2*v - 744*u**2 + 108*u*v**3 + 132*u*v**2 - 216*u*v + 12*u + 72*v**2 + 216*v + 216");
		positive(f);
		f = __("uv", "90*u**7*v**5 + 820*u**6*v**5 + 396*u**6*v**4 + 3150*u**5*v**5 + 2918*u**5*v**4 + 630*u**5*v**3 + 6655*u**4*v**5 + 8691*u**4*v**4 + 3314*u**4*v**3 + 504*u**4*v**2 + 8430*u**3*v**5 + 13464*u**3*v**4 + 6132*u**3*v**3 + 1600*u**3*v**2 + 252*u**3*v + 6475*u**2*v**5 + 11601*u**2*v**4 + 4480*u**2*v**3 + 792*u**2*v**2 + 600*u**2*v + 72*u**2 + 2820*u*v**5 + 5410*u*v**4 + 876*u*v**3 - 1264*u*v**2 + 252*u*v + 216*u + 540*v**5 + 1104*v**4 - 66*v**3 - 744*v**2 + 12*v + 216");
		positive(f);
		// m, n = 63, 164, non-negative
		f = __("uv", "3969*u**5*v**5 + 29358*u**5*v**4 + 86436*u**5*v**3 + 141876*u**5*v**2 + 152208*u**5*v + 85680*u**5 + 7938*u**4*v**5 + 57897*u**4*v**4 + 145656*u**4*v**3 + 175208*u**4*v**2 + 191288*u**4*v + 174656*u**4 + 14301*u**3*v**5 + 104144*u**3*v**4 + 220409*u**3*v**3 + 47733*u**3*v**2 - 195256*u**3*v - 12543*u**3 + 34277*u**2*v**4 + 126554*u**2*v**3 + 16807*u**2*v**2 - 275902*u**2*v - 120755*u**2 + 17025*u*v**3 + 20119*u*v**2 - 36118*u*v + 513*u + 11350*v**2 + 34050*v + 34050");
		positive(f);
		f = __("uv", "14301*u**7*v**5 + 130284*u**6*v**5 + 62879*u**6*v**4 + 500409*u**5*v**5 + 463216*u**5*v**4 + 99880*u**5*v**3 + 1057014*u**4*v**5 + 1379137*u**4*v**4 + 524834*u**4*v**3 + 79677*u**4*v**2 + 1338624*u**3*v**5 + 2135416*u**3*v**4 + 968896*u**3*v**3 + 251746*u**3*v**2 + 39725*u**3*v + 1027908*u**2*v**5 + 1838608*u**2*v**4 + 703327*u**2*v**3 + 119983*u**2*v**2 + 93894*u**2*v + 11350*u**2 + 447552*u*v**5 + 856648*u*v**4 + 132541*u*v**3 - 207118*u*v**2 + 37657*u*v + 34050*u + 85680*v**5 + 174656*v**4 - 12543*v**3 - 120755*v**2 + 513*v + 34050");
		positive(f);
		// m, n = 121, 315, negative
		negative(__("uv", "14641*u**5*v**5 + 108295*u**5*v**4 + 318835*u**5*v**3 + 523325*u**5*v**2 + 561440*u**5*v + 316052*u**5 + 29282*u**4*v**5 + 213565*u**4*v**4 + 537240*u**4*v**3 + 646135*u**4*v**2 + 705410*u**4*v + 644184*u**4 + 52756*u**3*v**5 + 384170*u**3*v**4 + 812964*u**3*v**3 + 175708*u**3*v**2 - 720846*u**3*v - 46584*u**3 + 126440*u**2*v**4 + 466768*u**2*v**3 + 61656*u**2*v**2 - 1018384*u**2*v - 445848*u**2 + 62784*u*v**3 + 74088*u*v**2 - 133512*u*v + 1680*u + 41856*v**2 + 125568*v + 125568"), -1);
		positive(__("uv", "52756*u**7*v**5 + 480612*u**6*v**5 + 231952*u**6*v**4 + 1845976*u**5*v**5 + 1708722*u**5*v**4 + 368420*u**5*v**3 + 3899225*u**4*v**5 + 5087315*u**4*v**4 + 1935830*u**4*v**3 + 293864*u**4*v**2 + 4938010*u**3*v**5 + 7876880*u**3*v**4 + 3573396*u**3*v**3 + 928304*u**3*v**2 + 146496*u**3*v + 3791777*u**2*v**5 + 6781845*u**2*v**4 + 2593252*u**2*v**3 + 441720*u**2*v**2 + 346152*u**2*v + 41856*u**2 + 1650924*u*v**5 + 3159694*u*v**4 + 487926*u*v**3 - 765008*u*v**2 + 138552*u*v + 125568*u + 316052*v**5 + 644184*v**4 - 46584*v**3 - 445848*v**2 + 1680*v + 125568"));
		// https://math.stackexchange.com/q/2016364
		// results from 2016364.py, doesn't seem to work
		// f(----)
		f = __("abcd", "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 - 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d + 8*a*b*c + 8*a*b*d + 12*a*b + 8*a*c*d + 8*a*c - 2*a*d**2 + 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d + 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 - 2*c**2*d + 8*c**2 - 2*c*d**2 + 12*c*d + d**4 - 4*d**3 + 8*d**2");
		positive01(f);
		// f(---+), doesn't work due to f(1, 1, 1, 1) = 0
		f = __("abcd", "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 - 2*b*c**2 - 8*b*c*d + 12*b*c - 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2");
		// positive01(f);
		// f(---+, d <= 3/4)
		f = __("abcd", "16*a**4 - 64*a**3 + 16*a**2*b**2 - 32*a**2*b + 4*a**2*d**2 + 16*a**2*d + 128*a**2 - 32*a*b**2 - 64*a*b*c*d + 128*a*b*c - 64*a*b*d + 192*a*b - 64*a*c*d + 128*a*c - 8*a*d**2 - 96*a*d + 16*b**4 - 64*b**3 + 16*b**2*c**2 - 32*b**2*c + 128*b**2 - 32*b*c**2 - 64*b*c*d + 192*b*c - 64*b*d + 16*c**4 - 64*c**3 + 4*c**2*d**2 + 16*c**2*d + 128*c**2 - 8*c*d**2 - 96*c*d + d**4 + 8*d**3 + 32*d**2");
		positive01(f);
		// f(---+, d >= 3/4), min-degree monimials: a**2, b**4, c**2, d
		f = __("abcd", "16*a**4 + 16*a**2*b**2 + 4*a**2*d**2 - 32*a**2*d + 64*a**2 - 64*a*b*c*d + 128*a*b*d + 128*a*c*d - 256*a*d + 16*b**4 + 16*b**2*c**2 + 128*b*c*d - 256*b*d + 16*c**4 + 4*c**2*d**2 - 32*c**2*d + 64*c**2 - 256*c*d + d**4 - 16*d**3 + 96*d**2 + 256*d");
		// positive01(f.subs('a', __("abcd", "a**2")).subs('c', __("abcd", "c**2")).subs('d', __("abcd", "d**4")));
		// f(--++)
		f = __("abcd", "a**4 - 4*a**3 + a**2*b**2 - 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 - 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 - 2*b*c**2 + 8*b*c*d - 12*b*c - 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(-+++)
		f = __("abcd", "a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 - 8*a*b*c*d + 8*a*b*c + 8*a*b*d - 12*a*b + 8*a*c*d - 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(++++)
		f = __("abcd", "a**4 + 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 + 2*a*b**2 + 8*a*b*c*d - 8*a*b*c - 8*a*b*d + 12*a*b - 8*a*c*d + 8*a*c + 2*a*d**2 + 12*a*d + b**4 + 4*b**3 + b**2*c**2 + 2*b**2*c + 8*b**2 + 2*b*c**2 - 8*b*c*d + 12*b*c + 8*b*d + c**4 + 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 + 2*c*d**2 + 12*c*d + d**4 + 4*d**3 + 8*d**2");
		positive01(f);
		// f(-+-+), doesn't work due to f(a = max(abcd))(0, 1, 1, 1) = 0
		f = __("abcd", "a**4 - 4*a**3 + a**2*b**2 + 2*a**2*b + a**2*d**2 + 2*a**2*d + 8*a**2 - 2*a*b**2 + 8*a*b*c*d - 8*a*b*c + 8*a*b*d - 12*a*b - 8*a*c*d + 8*a*c - 2*a*d**2 - 12*a*d + b**4 + 4*b**3 + b**2*c**2 - 2*b**2*c + 8*b**2 + 2*b*c**2 + 8*b*c*d - 12*b*c + 8*b*d + c**4 - 4*c**3 + c**2*d**2 + 2*c**2*d + 8*c**2 - 2*c*d**2 - 12*c*d + d**4 + 4*d**3 + 8*d**2");
		// TODO how to prove?
		// positive01(f);
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
}