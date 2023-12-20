package com.xqbase.math.inequality;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.polys.LongPoly;

public class SDSTest {
	@BeforeClass
	public static void startup() {
		// https://stackoverflow.com/a/6308286/4260959
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
	}

	@Test
	public void testHomogeneous() {
		LongPoly f = new LongPoly("ab", "a^2+b");
		try {
			SDS.sds(new LongPoly("ab", "a^2+b^2"), false);
			SDS.sds(f, false);
			Assert.fail();
		} catch (IllegalArgumentException e) {
			Assert.assertEquals(f + " is not homogeneous", e.getMessage());
		}
	}

	private static String replaceAn(String expr) {
		String s = expr;
		for (int i = 9; i >= 1; i --) {
			s = s.replace("a" + i, Character.toString((char) ('a' + (i - 1))));
		}
		return s;
	}

	@Test
	public void testYang08P169_5() {
		// ISBN 9787030207210, p169, §7.3.2, problem 5
		// a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) >= 5/2
		String vars = "abcde";
		String fn = replaceAn("2*a1**3*a3*a4 + 2*a1**3*a3*a5 + 2*a1**3*a4**2 + 2*a1**3*a4*a5 + 2*a1**2*a2**2*a4 + 2*a1**2*a2**2*a5 + 2*a1**2*a2*a3**2 + a1**2*a2*a3*a4 - a1**2*a2*a3*a5 - 3*a1**2*a2*a4**2 - 3*a1**2*a2*a4*a5 + 2*a1**2*a3**3 - 3*a1**2*a3**2*a4 - 5*a1**2*a3**2*a5 - 5*a1**2*a3*a4**2 - 3*a1**2*a3*a4*a5 + 2*a1**2*a3*a5**2 + 2*a1**2*a4**2*a5 + 2*a1**2*a4*a5**2 + 2*a1*a2**3*a4 + 2*a1*a2**3*a5 + 2*a1*a2**2*a3**2 - a1*a2**2*a3*a4 - 3*a1*a2**2*a3*a5 - 5*a1*a2**2*a4**2 - 3*a1*a2**2*a4*a5 + 2*a1*a2**2*a5**2 + 2*a1*a2*a3**3 - 3*a1*a2*a3**2*a4 - 3*a1*a2*a3**2*a5 - 3*a1*a2*a3*a4**2 + a1*a2*a3*a5**2 + 2*a1*a2*a4**3 + a1*a2*a4**2*a5 - a1*a2*a4*a5**2 + 2*a1*a3**3*a5 + 2*a1*a3**2*a4**2 + a1*a3**2*a4*a5 - 3*a1*a3**2*a5**2 + 2*a1*a3*a4**3 - a1*a3*a4**2*a5 - 3*a1*a3*a4*a5**2 + 2*a2**3*a4*a5 + 2*a2**3*a5**2 + 2*a2**2*a3**2*a5 + 2*a2**2*a3*a4**2 + a2**2*a3*a4*a5 - 3*a2**2*a3*a5**2 + 2*a2**2*a4**3 - 3*a2**2*a4**2*a5 - 5*a2**2*a4*a5**2 + 2*a2*a3**3*a5 + 2*a2*a3**2*a4**2 - a2*a3**2*a4*a5 - 5*a2*a3**2*a5**2 + 2*a2*a3*a4**3 - 3*a2*a3*a4**2*a5 - 3*a2*a3*a4*a5**2 + 2*a2*a3*a5**3 + 2*a2*a4**2*a5**2 + 2*a2*a4*a5**3 + 2*a3**2*a4*a5**2 + 2*a3**2*a5**3 + 2*a3*a4**2*a5**2 + 2*a3*a4*a5**3"); 
		// String fd = replaceAn("2*a1**2*a2*a3*a4 + 2*a1**2*a2*a3*a5 + 2*a1**2*a2*a4**2 + 2*a1**2*a2*a4*a5 + 2*a1**2*a3**2*a4 + 2*a1**2*a3**2*a5 + 2*a1**2*a3*a4**2 + 2*a1**2*a3*a4*a5 + 2*a1*a2**2*a3*a4 + 2*a1*a2**2*a3*a5 + 2*a1*a2**2*a4**2 + 2*a1*a2**2*a4*a5 + 2*a1*a2*a3**2*a4 + 2*a1*a2*a3**2*a5 + 2*a1*a2*a3*a4**2 + 4*a1*a2*a3*a4*a5 + 2*a1*a2*a3*a5**2 + 2*a1*a2*a4**2*a5 + 2*a1*a2*a4*a5**2 + 2*a1*a3**2*a4*a5 + 2*a1*a3**2*a5**2 + 2*a1*a3*a4**2*a5 + 2*a1*a3*a4*a5**2 + 2*a2**2*a3*a4*a5 + 2*a2**2*a3*a5**2 + 2*a2**2*a4**2*a5 + 2*a2**2*a4*a5**2 + 2*a2*a3**2*a4*a5 + 2*a2*a3**2*a5**2 + 2*a2*a3*a4**2*a5 + 2*a2*a3*a4*a5**2");
		System.out.println(SDS.sds(new LongPoly(vars, fn)));
		// p170, §7.3.3
		vars = "abcd";
		fn = replaceAn("a1**3*a3 + a1**3*a4 + a1**2*a2**2 - a1**2*a2*a4 - 2*a1**2*a3**2 - a1**2*a3*a4 + a1**2*a4**2 + a1*a2**3 - a1*a2**2*a3 - a1*a2**2*a4 - a1*a2*a3**2 + a1*a3**3 - a1*a3*a4**2 + a2**3*a4 + a2**2*a3**2 - 2*a2**2*a4**2 + a2*a3**3 - a2*a3**2*a4 - a2*a3*a4**2 + a2*a4**3 + a3**2*a4**2 + a3*a4**3"); 
		// fd = replaceAn("a1**2*a2*a3 + a1**2*a2*a4 + a1**2*a3**2 + a1**2*a3*a4 + a1*a2**2*a3 + a1*a2**2*a4 + a1*a2*a3**2 + 2*a1*a2*a3*a4 + a1*a2*a4**2 + a1*a3**2*a4 + a1*a3*a4**2 + a2**2*a3*a4 + a2**2*a4**2 + a2*a3**2*a4 + a2*a3*a4**2"); 
		System.out.println(SDS.sds(new LongPoly(vars, fn)));
		// p171, problem 8
		String f = "x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6";
		System.out.println(SDS.sds(new LongPoly("xyz", f)));
		// p171, problem 9
		f = "8*x**7 + 6*x**6*y + 8*x**6*z + 62*x**5*y**2 - 154*x**5*y*z - 69*x**4*y**3 + 202*x**4*y**2*z + 2*x**4*y*z**2 + 18*x**3*y**4 - 170*x**3*y**3*z + 114*x**3*y**2*z**2 + 18*x**3*y*z**3 + 54*x**2*y**4*z - 124*x**2*y**3*z**2 - 26*x**2*y**2*z**3 + 54*x*y**4*z**2 - 22*x*y**3*z**3 + 18*y**4*z**3 + y**3*z**4";
		System.out.println(SDS.sds(new LongPoly("xyz", f)));
		// p172, problem 10
		f = "a**6 + 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 + 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 + a*b**5 - 5*a*c**5 + b**6 - 5*b**5*c + 10*b**4*c**2 - 10*b**3*c**3 + 5*b**2*c**4 - b*c**5 + c**6";
		System.out.println(SDS.sds(new LongPoly("abc", f)));
		f = "a**6 - 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 - 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 - a*b**5 - 5*a*c**5 + b**6 + 5*b**5*c + 10*b**4*c**2 + 10*b**3*c**3 + 5*b**2*c**4 + b*c**5 + c**6";
		System.out.println(SDS.sds(new LongPoly("abc", f)));
		// p172, problem 11
		f = "2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2" +
				" + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4" +
				" - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3" +
				" + 1611722090*z**4";
		// long overflow at depth = 12
		// System.out.println(SDS.sds(new LongPoly("xyz", f)));
	}
}