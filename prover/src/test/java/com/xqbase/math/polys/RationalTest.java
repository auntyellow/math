package com.xqbase.math.polys;

import java.util.Collections;

import org.junit.Assert;
import org.junit.Test;

public class RationalTest {
	private static final String ZERO_308 = String.join("", Collections.nCopies(308, "0"));
	private static final String[] RATIONALS = {
		"-175" + ZERO_308 + "/10",
		"-175" + ZERO_308 + "/100",
		"-5/20000000000000000" + ZERO_308,
		"-5/200000000000000000" + ZERO_308,
		"5/200000000000000000" + ZERO_308,
		"5/20000000000000000" + ZERO_308,
		"175" + ZERO_308 + "/100",
		"175" + ZERO_308 + "/10",
	};
	private static final double[] DOUBLES = {
		Double.NEGATIVE_INFINITY,
		-1.75e308,
		-2.5e-324,
		-.0,
		.0,
		2.5e-324,
		1.75e308,
		Double.POSITIVE_INFINITY,
	};

	@Test
	public void testDoubleValue() {
		for (int i = 0; i < RATIONALS.length; i ++) {
			double d = new Rational(RATIONALS[i]).doubleValue();
			Assert.assertFalse(Double.isNaN(d));
			System.out.println(d + " = " + RATIONALS[i]);
			Assert.assertTrue(Double.compare(DOUBLES[i], d) == 0);
		}
	}

	// TODO testFloatValue()
}