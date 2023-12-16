package com.xqbase.math.inequality;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.polys.Poly;

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
		Poly f = new Poly("ab", "a^2+b");
		try {
			SDS.sds(new Poly("ab", "a^2+b^2"), false);
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
		SDS.sds(new Poly(vars, fn));
	}
}