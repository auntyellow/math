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
}