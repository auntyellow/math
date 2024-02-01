package com.xqbase.math.inequality;

import static org.junit.Assert.assertTrue;
import static com.xqbase.math.inequality.BinarySearch.binarySearch;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.polys.RationalPoly;

public class BinarySearchTest {
	@BeforeClass
	public static void startup() {
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.INFO);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.INFO);
		}
	}

	@Test
	public void testMathSE() {
		// https://math.stackexchange.com/q/3831395
		RationalPoly f = new RationalPoly("x", "x**5 - 1/2*x**3 - x + 4/5");
		assertTrue(binarySearch(f).length == 0);
		// https://math.stackexchange.com/q/83670
		f = new RationalPoly("x", "x**8 - x**7 + 2*x**6 - 2*x**5 + 3*x**4 - 3*x**3 + 4*x**2 - 4*x + 5/2");
		assertTrue(binarySearch(f).length == 0);
		// https://math.stackexchange.com/q/4765187
		// (1 + x)**7 - 7**(7/3)*x**4
		f = new RationalPoly("x", "x**7 + 7*x**6 + 21*x**5 - 59*x**4 + 35*x**3 + 21*x**2 + 7*x + 1");
		assertTrue(binarySearch(f).length == 0);
		// https://math.stackexchange.com/q/1775572, too slow
		f = new RationalPoly("uv", "25*u**8*v**7 + 310*u**8*v**6 + 1620*u**8*v**5 + 4640*u**8*v**4 + 7960*u**8*v**3 + 8400*u**8*v**2 + 5280*u**8*v + 1600*u**8 + 75*u**7*v**7 + 1025*u**7*v**6 + 5760*u**7*v**5 + 17340*u**7*v**4 + 30696*u**7*v**3 + 33336*u**7*v**2 + 22272*u**7*v + 7648*u**7 + 75*u**6*v**7 + 1215*u**6*v**6 + 7605*u**6*v**5 + 24150*u**6*v**4 + 42816*u**6*v**3 + 45384*u**6*v**2 + 31944*u**6*v + 13680*u**6 + 65*u**5*v**7 + 1091*u**5*v**6 + 7047*u**5*v**5 + 21924*u**5*v**4 + 33751*u**5*v**3 + 24738*u**5*v**2 + 12868*u**5*v + 10073*u**5 + 351*u**4*v**6 + 3723*u**4*v**5 + 14112*u**4*v**4 + 20682*u**4*v**3 + 3441*u**4*v**2 - 11196*u**4*v + 531*u**4 + 741*u**3*v**5 + 5232*u**3*v**4 + 10740*u**3*v**3 + 1656*u**3*v**2 - 11115*u**3*v - 2193*u**3 + 754*u**2*v**4 + 3334*u**2*v**3 + 3078*u**2*v**2 - 1156*u**2*v + 738*u**2 + 390*u*v**3 + 1284*u*v**2 + 1590*u*v + 1554*u + 156*v**2 + 468*v + 468");
		assertTrue(binarySearch(f).length == 0);
		f = new RationalPoly("uv", "65*u**10*v**8 + 865*u**9*v**8 + 546*u**9*v**7 + 5145*u**8*v**8 + 6417*u**8*v**7 + 1989*u**8*v**6 + 18095*u**7*v**8 + 33168*u**7*v**7 + 20196*u**7*v**6 + 4095*u**7*v**5 + 41930*u**6*v**8 + 99425*u**6*v**7 + 88116*u**6*v**6 + 34758*u**6*v**5 + 5226*u**6*v**4 + 67380*u**5*v**8 + 191868*u**5*v**7 + 216555*u**5*v**6 + 122112*u**5*v**5 + 35385*u**5*v**4 + 4329*u**5*v**3 + 76600*u**4*v**8 + 249636*u**4*v**7 + 330390*u**4*v**6 + 229495*u**4*v**5 + 92637*u**4*v**4 + 22215*u**4*v**3 + 2392*u**4*v**2 + 61160*u**3*v**8 + 221472*u**3*v**7 + 324744*u**3*v**6 + 249474*u**3*v**5 + 115662*u**3*v**4 + 38988*u**3*v**3 + 9242*u**3*v**2 + 858*u**3*v + 32880*u**2*v**8 + 130488*u**2*v**7 + 204816*u**2*v**6 + 159063*u**2*v**5 + 67386*u**2*v**4 + 24186*u**2*v**3 + 10974*u**2*v**2 + 2766*u**2*v + 156*u**2 + 10720*u*v**8 + 46560*u*v**7 + 77496*u*v**6 + 57643*u*v**5 + 14382*u*v**4 + 150*u*v**3 + 4108*u*v**2 + 3072*u*v + 468*u + 1600*v**8 + 7648*v**7 + 13680*v**6 + 10073*v**5 + 531*v**4 - 2193*v**3 + 738*v**2 + 1554*v + 468");
		assertTrue(binarySearch(f).length == 0);
	}

	@Test
	public void testYang08() {
		// ISBN 9787030207210, p156, §7.1
		// too slow if estimate |grad f|^2 = sum_i(sum_j(|a_i*c_j|)^2)
		RationalPoly f = new RationalPoly("z", "10195920*z**8 + 2109632*z**7 - 5387520*z**6 + 1361336*z**5 + 61445*z**4 - 52468*z**3 + 6350*z**2 - 300*z + 5");
		assertTrue(binarySearch(f).length == 0);
	}
}