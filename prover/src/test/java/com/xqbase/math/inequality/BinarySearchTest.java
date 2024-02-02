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
		rootLogger.setLevel(Level.FINE);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
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
		// https://math.stackexchange.com/q/1775572
		f = new RationalPoly("uv", "25*u**8*v**7 + 310*u**8*v**6 + 1620*u**8*v**5 + 4640*u**8*v**4 + 7960*u**8*v**3 + 8400*u**8*v**2 + 5280*u**8*v + 1600*u**8 + 75*u**7*v**7 + 1025*u**7*v**6 + 5760*u**7*v**5 + 17340*u**7*v**4 + 30696*u**7*v**3 + 33336*u**7*v**2 + 22272*u**7*v + 7648*u**7 + 75*u**6*v**7 + 1215*u**6*v**6 + 7605*u**6*v**5 + 24150*u**6*v**4 + 42816*u**6*v**3 + 45384*u**6*v**2 + 31944*u**6*v + 13680*u**6 + 65*u**5*v**7 + 1091*u**5*v**6 + 7047*u**5*v**5 + 21924*u**5*v**4 + 33751*u**5*v**3 + 24738*u**5*v**2 + 12868*u**5*v + 10073*u**5 + 351*u**4*v**6 + 3723*u**4*v**5 + 14112*u**4*v**4 + 20682*u**4*v**3 + 3441*u**4*v**2 - 11196*u**4*v + 531*u**4 + 741*u**3*v**5 + 5232*u**3*v**4 + 10740*u**3*v**3 + 1656*u**3*v**2 - 11115*u**3*v - 2193*u**3 + 754*u**2*v**4 + 3334*u**2*v**3 + 3078*u**2*v**2 - 1156*u**2*v + 738*u**2 + 390*u*v**3 + 1284*u*v**2 + 1590*u*v + 1554*u + 156*v**2 + 468*v + 468");
		// FIXME unable to terminate
		assertTrue(binarySearch(f).length == 0);
		System.exit(0);
		f = new RationalPoly("uv", "65*u**10*v**8 + 865*u**9*v**8 + 546*u**9*v**7 + 5145*u**8*v**8 + 6417*u**8*v**7 + 1989*u**8*v**6 + 18095*u**7*v**8 + 33168*u**7*v**7 + 20196*u**7*v**6 + 4095*u**7*v**5 + 41930*u**6*v**8 + 99425*u**6*v**7 + 88116*u**6*v**6 + 34758*u**6*v**5 + 5226*u**6*v**4 + 67380*u**5*v**8 + 191868*u**5*v**7 + 216555*u**5*v**6 + 122112*u**5*v**5 + 35385*u**5*v**4 + 4329*u**5*v**3 + 76600*u**4*v**8 + 249636*u**4*v**7 + 330390*u**4*v**6 + 229495*u**4*v**5 + 92637*u**4*v**4 + 22215*u**4*v**3 + 2392*u**4*v**2 + 61160*u**3*v**8 + 221472*u**3*v**7 + 324744*u**3*v**6 + 249474*u**3*v**5 + 115662*u**3*v**4 + 38988*u**3*v**3 + 9242*u**3*v**2 + 858*u**3*v + 32880*u**2*v**8 + 130488*u**2*v**7 + 204816*u**2*v**6 + 159063*u**2*v**5 + 67386*u**2*v**4 + 24186*u**2*v**3 + 10974*u**2*v**2 + 2766*u**2*v + 156*u**2 + 10720*u*v**8 + 46560*u*v**7 + 77496*u*v**6 + 57643*u*v**5 + 14382*u*v**4 + 150*u*v**3 + 4108*u*v**2 + 3072*u*v + 468*u + 1600*v**8 + 7648*v**7 + 13680*v**6 + 10073*v**5 + 531*v**4 - 2193*v**3 + 738*v**2 + 1554*v + 468");
		assertTrue(binarySearch(f).length == 0);
		// https://math.stackexchange.com/q/4850712
		// from 4850712u.py
		// m, n = 5, 13, non-negative, https://math.stackexchange.com/q/1777075
		f = new RationalPoly("uv", "25*u**5*v**5 + 185*u**5*v**4 + 545*u**5*v**3 + 895*u**5*v**2 + 960*u**5*v + 540*u**5 + 50*u**4*v**5 + 365*u**4*v**4 + 920*u**4*v**3 + 1111*u**4*v**2 + 1214*u**4*v + 1104*u**4 + 90*u**3*v**5 + 656*u**3*v**4 + 1392*u**3*v**3 + 316*u**3*v**2 - 1206*u**3*v - 66*u**3 + 216*u**2*v**4 + 800*u**2*v**3 + 120*u**2*v**2 - 1712*u**2*v - 744*u**2 + 108*u*v**3 + 132*u*v**2 - 216*u*v + 12*u + 72*v**2 + 216*v + 216");
		// FIXME unable to terminate
		assertTrue(binarySearch(f).length == 0);
		System.exit(0);
		f = new RationalPoly("uv", "90*u**7*v**5 + 820*u**6*v**5 + 396*u**6*v**4 + 3150*u**5*v**5 + 2918*u**5*v**4 + 630*u**5*v**3 + 6655*u**4*v**5 + 8691*u**4*v**4 + 3314*u**4*v**3 + 504*u**4*v**2 + 8430*u**3*v**5 + 13464*u**3*v**4 + 6132*u**3*v**3 + 1600*u**3*v**2 + 252*u**3*v + 6475*u**2*v**5 + 11601*u**2*v**4 + 4480*u**2*v**3 + 792*u**2*v**2 + 600*u**2*v + 72*u**2 + 2820*u*v**5 + 5410*u*v**4 + 876*u*v**3 - 1264*u*v**2 + 252*u*v + 216*u + 540*v**5 + 1104*v**4 - 66*v**3 - 744*v**2 + 12*v + 216");
		assertTrue(binarySearch(f).length == 0);
		// m, n = 63, 164, non-negative
		f = new RationalPoly("uv", "14301*u**7 + 30177*u**6*v + 62879*u**6 + 19026*u**5*v**2 + 85942*u**5*v + 99880*u**5 + 8694*u**4*v**3 + 6242*u**4*v**2 + 25434*u**4*v + 79677*u**4 + 9513*u**3*v**4 - 6552*u**3*v**3 - 131640*u**3*v**2 - 66962*u**3*v + 39725*u**3 + 3969*u**2*v**5 + 18207*u**2*v**4 - 53157*u**2*v**3 - 157193*u**2*v**2 - 25281*u**2*v + 11350*u**2 + 7938*u*v**5 + 32639*u*v**4 - 10554*u*v**3 - 30956*u*v**2 + 11350*u*v + 14301*v**5 + 34277*v**4 + 17025*v**3 + 11350*v**2");
		assertTrue(binarySearch(f).length == 0);
		// m, n = 121, 315, negative
		f = new RationalPoly("uv", "52756*u**7 + 111320*u**6*v + 231952*u**6 + 70180*u**5*v**2 + 317010*u**5*v + 368420*u**5 + 32065*u**4*v**3 + 22985*u**4*v**2 + 93730*u**4*v + 293864*u**4 + 35090*u**3*v**4 - 24200*u**3*v**3 - 485724*u**3*v**2 - 247152*u**3*v + 146496*u**3 + 14641*u**2*v**5 + 67155*u**2*v**4 - 196156*u**2*v**3 - 580008*u**2*v**2 - 93336*u**2*v + 41856*u**2 + 29282*u*v**5 + 120390*u*v**4 - 38992*u*v**3 - 114264*u*v**2 + 41856*u*v + 52756*v**5 + 126440*v**4 + 62784*v**3 + 41856*v**2");
		assertTrue(binarySearch(f).length == 0);
	}

	@Test
	public void testYang08() {
		// ISBN 9787030207210, p156, §7.1
		RationalPoly f = new RationalPoly("z", "10195920*z**8 + 2109632*z**7 - 5387520*z**6 + 1361336*z**5 + 61445*z**4 - 52468*z**3 + 6350*z**2 - 300*z + 5");
		assertTrue(binarySearch(f).length == 0);
	}
}