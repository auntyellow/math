package com.xqbase.math.polys;

import java.util.Collections;

import org.junit.Assert;
import org.junit.Test;

public class RationalTest {
	private static final String ZERO_308 = String.join("", Collections.nCopies(308, "0"));
	private static final String ZERO_38 = String.join("", Collections.nCopies(38, "0"));
	private static final String[] RATIONALS = {
		"-17654321098765432" + ZERO_308 + "/1000000000000000",
		"-17654321098765432" + ZERO_308 + "/10000000000000000",
		"-321098765" + ZERO_38 + "/10000000",
		"-321098765" + ZERO_38 + "/100000000",
		"-1/3",
		"-29/400000000" + ZERO_38,
		"-29/4000000000" + ZERO_38,
		"-5/20000000000000000" + ZERO_308,
		"-5/200000000000000000" + ZERO_308,
		"5/200000000000000000" + ZERO_308,
		"5/20000000000000000" + ZERO_308,
		"29/4000000000" + ZERO_38,
		"29/400000000" + ZERO_38,
		"1/3",
		"321098765" + ZERO_38 + "/100000000",
		"321098765" + ZERO_38 + "/10000000",
		"17654321098765432" + ZERO_308 + "/10000000000000000",
		"17654321098765432" + ZERO_308 + "/1000000000000000",
	};
	private static final double[] DOUBLES = {
		Double.NEGATIVE_INFINITY,
		-1.76543210987654321e308,
		-3.21098765e39,
		-3.21098765e38,
		-.3333333333333333,
		-7.25e-46,
		-7.25e-47,
		-2.5e-324,
		-.0,
		.0,
		2.5e-324,
		7.25e-47,
		7.25e-46,
		.3333333333333333,
		3.21098765e38,
		3.21098765e39,
		1.7654321098765432e308,
		Double.POSITIVE_INFINITY,
	};
	private static final float[] FLOATS = {
		Float.NEGATIVE_INFINITY,
		Float.NEGATIVE_INFINITY,
		Float.NEGATIVE_INFINITY,
		-3.21098765e38f,
		-.33333333f,
		-7.25e-46f,
		-.0f,
		-.0f,
		-.0f,
		.0f,
		.0f,
		.0f,
		7.25e-46f,
		.33333333f,
		3.21098765e38f,
		Float.POSITIVE_INFINITY,
		Float.POSITIVE_INFINITY,
		Float.POSITIVE_INFINITY,
	};

	@Test
	public void testValue() {
		for (int i = 0; i < RATIONALS.length; i ++) {
			Rational r = new Rational(RATIONALS[i]);
			float f = r.floatValue();
			double d = r.doubleValue();
			Assert.assertFalse(Float.isNaN(f));
			Assert.assertFalse(Double.isNaN(d));
			System.out.println(f + " = " + d + " = " + r);
			Assert.assertTrue(Float.compare(FLOATS[i], f) == 0);
			Assert.assertTrue(Double.compare(DOUBLES[i], d) == 0);
		}
	}
}