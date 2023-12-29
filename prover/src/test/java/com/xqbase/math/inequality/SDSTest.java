package com.xqbase.math.inequality;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import com.xqbase.math.inequality.SDS.SDSResult;
import com.xqbase.math.polys.BigPoly;
import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.MutableBigInteger;
import com.xqbase.math.polys.MutableLong;
import com.xqbase.math.polys.MutableNumber;
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
	public void testBasic() {
		LongPoly f = new LongPoly("ab", "a^2+b");
		try {
			SDS.sds(new LongPoly("ab", "a^2+b^2"));
			SDS.sds(f);
			Assert.fail();
		} catch (IllegalArgumentException e) {
			assertEquals(f + " is not homogeneous", e.getMessage());
		}
		SDSResult<MutableLong> result = SDS.sds(new LongPoly("xy", "x**2 + x*y + y**2"));
		assertTrue(result.isNonNegative());
		assertEquals("[]", result.getZeroAt().toString());
		assertEquals(0, result.getDepth());

		result = SDS.sds(new LongPoly("xy", "x**2 - 2*x*y + y**2"));
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());

		result = SDS.sds(new LongPoly("xy", "x**2 - 3*x*y + y**2"));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());

		result = SDS.sds(new LongPoly("xyz", "x**2*y + y**2*z + z**2*x - 3*x*y*z"));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
	}

	private static <T extends MutableNumber<T>> T
			subs(Poly<T> f, List<T> values, char startsWith) {
		Poly<T> f1 = f;
		StringBuilder vars = new StringBuilder();
		for (int i = 0; i < values.size(); i ++) {
			char from = (char) (startsWith + i);
			f1 = f1.subs(from, values.get(i));
			vars.append(from);
		}
		Mono constant = new Mono(vars.toString(), "");
		for (Map.Entry<Mono, T> entry : f1.entrySet()) {
			assertEquals(constant, entry.getKey());
			return entry.getValue(); 
		}
		return f.valueOf(0);
	}

	@Test
	public void testTsds() {
		// sds vs tsds
		// example 1:
		// fibonacci 91, 92
		long m = 4660046610375530309L;
		long n = 7540113804746346429L;
		Poly<MutableBigInteger> f = new BigPoly("xy", m + "*x - " + n + "*y");
		f = new BigPoly().addMul(f, f);
		SDSResult<MutableBigInteger> result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[" + n + ", " + m + "]]", result.getZeroAt().toString());
		assertEquals(91, result.getDepth());
		// 1e22
		f = new BigPoly().add(f.valueOf("10000000000000000000000"), f);
		// tsds works within 99 iterations (sds 72)
		result = SDS.tsds(new BigPoly("xy", "x**2 + y**2").add(f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// tsds finds negative within 98 iterations (sds 71)
		f = new BigPoly("xy", "-x**2 - y**2").add(f);
		result = SDS.tsds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').compareTo(f.valueOf(0)) < 0);
		assertEquals(98, result.getDepth());

		// example 2
		// (3*x - y)**2 + (x - z)**2
		f = new BigPoly("xyz", "10*x**2 - 6*x*y - 2*x*z + y**2 + z**2");
		// zero at (1, 3, 1), not on sds or tsds's boundary
		assertTrue(subs(f, Arrays.asList(f.valueOf(1), f.valueOf(3), f.valueOf(1)), 'x').equals(f.valueOf(0)));
		// sds works for 6 but doesn't seem to work for 7
		result = SDS.sds(new BigPoly("xyz", "x**2 + y**2 + z**2").add(new BigPoly().add(6, f)));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(9, result.getDepth());
		// sds finds negative for 1e22 (maybe larger), why?
		result = SDS.sds(new BigPoly("xyz", "-x**2 - y**2 - z**2").add(new BigPoly().add(f.valueOf("10000000000000000000000"), f)));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 3, 1]",result.getNegativeAt().toString());
		assertEquals(2, result.getDepth());
		// 1e8
		f = new BigPoly().add(f.valueOf(100_000_000), f);
		// tsds works within 16 iterations (sds doesn't work)
		result = SDS.tsds(new BigPoly("xyz", "x**2 + y**2 + z**2").add(f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// tsds finds negative within 11 iterations
		f = new BigPoly("xyz", "-x**2 - y**2 - z**2").add(f);
		result = SDS.tsds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').compareTo(f.valueOf(0)) < 0);
		assertEquals(11, result.getDepth());
	}

	private static LongPoly replaceAn(String expr) {
		String s = expr;
		String vars = "";
		for (int i = 26; i > 0; i --) {
			char from = (char) ('a' + (i - 1));
			String s1 = s.replace("a" + i, Character.toString(from));
			if (s1.length() < s.length()) {
				s = s1;
				vars = from + vars;
			}
		}
		return new LongPoly(vars, s);
	}

	private static List<List<MutableLong>> getZeroAt(LongPoly fn,
			LongPoly fd, Set<List<MutableLong>> fnZeroAt) {
		List<List<MutableLong>> zeroAts = new ArrayList<>();
		for (List<MutableLong> zeroAt : fnZeroAt) {
			// test if fn is zero
			assertEquals(fn.valueOf(0), subs(fn, zeroAt, 'a'));
			// keep only if fd is not zero
			if (!subs(fd, zeroAt, 'a').equals(fd.valueOf(0))) {
				zeroAts.add(zeroAt);
			}
		}
		return zeroAts;
	}

	@Test
	public void testYang08P170() {
		// ISBN 9787030207210, p169, §7.3.2, problem 5
		// a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) >= 5/2
		LongPoly fn = replaceAn("2*a1**3*a3*a4 + 2*a1**3*a3*a5 + 2*a1**3*a4**2 + 2*a1**3*a4*a5 + 2*a1**2*a2**2*a4 + 2*a1**2*a2**2*a5 + 2*a1**2*a2*a3**2 + a1**2*a2*a3*a4 - a1**2*a2*a3*a5 - 3*a1**2*a2*a4**2 - 3*a1**2*a2*a4*a5 + 2*a1**2*a3**3 - 3*a1**2*a3**2*a4 - 5*a1**2*a3**2*a5 - 5*a1**2*a3*a4**2 - 3*a1**2*a3*a4*a5 + 2*a1**2*a3*a5**2 + 2*a1**2*a4**2*a5 + 2*a1**2*a4*a5**2 + 2*a1*a2**3*a4 + 2*a1*a2**3*a5 + 2*a1*a2**2*a3**2 - a1*a2**2*a3*a4 - 3*a1*a2**2*a3*a5 - 5*a1*a2**2*a4**2 - 3*a1*a2**2*a4*a5 + 2*a1*a2**2*a5**2 + 2*a1*a2*a3**3 - 3*a1*a2*a3**2*a4 - 3*a1*a2*a3**2*a5 - 3*a1*a2*a3*a4**2 + a1*a2*a3*a5**2 + 2*a1*a2*a4**3 + a1*a2*a4**2*a5 - a1*a2*a4*a5**2 + 2*a1*a3**3*a5 + 2*a1*a3**2*a4**2 + a1*a3**2*a4*a5 - 3*a1*a3**2*a5**2 + 2*a1*a3*a4**3 - a1*a3*a4**2*a5 - 3*a1*a3*a4*a5**2 + 2*a2**3*a4*a5 + 2*a2**3*a5**2 + 2*a2**2*a3**2*a5 + 2*a2**2*a3*a4**2 + a2**2*a3*a4*a5 - 3*a2**2*a3*a5**2 + 2*a2**2*a4**3 - 3*a2**2*a4**2*a5 - 5*a2**2*a4*a5**2 + 2*a2*a3**3*a5 + 2*a2*a3**2*a4**2 - a2*a3**2*a4*a5 - 5*a2*a3**2*a5**2 + 2*a2*a3*a4**3 - 3*a2*a3*a4**2*a5 - 3*a2*a3*a4*a5**2 + 2*a2*a3*a5**3 + 2*a2*a4**2*a5**2 + 2*a2*a4*a5**3 + 2*a3**2*a4*a5**2 + 2*a3**2*a5**3 + 2*a3*a4**2*a5**2 + 2*a3*a4*a5**3"); 
		for (Mono key : fn.keySet()) {
			assertEquals("abcde", key.getVars());
			break;
		}
		LongPoly fd = replaceAn("2*a1**2*a2*a3*a4 + 2*a1**2*a2*a3*a5 + 2*a1**2*a2*a4**2 + 2*a1**2*a2*a4*a5 + 2*a1**2*a3**2*a4 + 2*a1**2*a3**2*a5 + 2*a1**2*a3*a4**2 + 2*a1**2*a3*a4*a5 + 2*a1*a2**2*a3*a4 + 2*a1*a2**2*a3*a5 + 2*a1*a2**2*a4**2 + 2*a1*a2**2*a4*a5 + 2*a1*a2*a3**2*a4 + 2*a1*a2*a3**2*a5 + 2*a1*a2*a3*a4**2 + 4*a1*a2*a3*a4*a5 + 2*a1*a2*a3*a5**2 + 2*a1*a2*a4**2*a5 + 2*a1*a2*a4*a5**2 + 2*a1*a3**2*a4*a5 + 2*a1*a3**2*a5**2 + 2*a1*a3*a4**2*a5 + 2*a1*a3*a4*a5**2 + 2*a2**2*a3*a4*a5 + 2*a2**2*a3*a5**2 + 2*a2**2*a4**2*a5 + 2*a2**2*a4*a5**2 + 2*a2*a3**2*a4*a5 + 2*a2*a3**2*a5**2 + 2*a2*a3*a4**2*a5 + 2*a2*a3*a4*a5**2");
		SDSResult<MutableLong> result = SDS.sds(fn);
		assertTrue(result.isNonNegative());
		assertEquals(21, result.getZeroAt().size());
		assertEquals("[[1, 1, 1, 1, 1]]", getZeroAt(fn, fd, result.getZeroAt()).toString());
		assertEquals(1, result.getDepth());
		// p170, §7.3.3
		fn = replaceAn("a1**3*a3 + a1**3*a4 + a1**2*a2**2 - a1**2*a2*a4 - 2*a1**2*a3**2 - a1**2*a3*a4 + a1**2*a4**2 + a1*a2**3 - a1*a2**2*a3 - a1*a2**2*a4 - a1*a2*a3**2 + a1*a3**3 - a1*a3*a4**2 + a2**3*a4 + a2**2*a3**2 - 2*a2**2*a4**2 + a2*a3**3 - a2*a3**2*a4 - a2*a3*a4**2 + a2*a4**3 + a3**2*a4**2 + a3*a4**3"); 
		for (Mono key : fn.keySet()) {
			assertEquals("abcd", key.getVars());
			break;
		}
		fd = replaceAn("a1**2*a2*a3 + a1**2*a2*a4 + a1**2*a3**2 + a1**2*a3*a4 + a1*a2**2*a3 + a1*a2**2*a4 + a1*a2*a3**2 + 2*a1*a2*a3*a4 + a1*a2*a4**2 + a1*a3**2*a4 + a1*a3*a4**2 + a2**2*a3*a4 + a2**2*a4**2 + a2*a3**2*a4 + a2*a3*a4**2"); 
		result = SDS.sds(fn);
		assertTrue(result.isNonNegative());
		assertEquals(13, result.getZeroAt().size());
		List<List<MutableLong>> zeroAts = getZeroAt(fn, fd, result.getZeroAt());
		assertEquals(9, zeroAts.size());
		// general solution: (u, v, u, v)
		for (List<MutableLong> zeroAt : zeroAts) {
			assertEquals(zeroAt.get(0), zeroAt.get(2));
			assertEquals(zeroAt.get(1), zeroAt.get(3));
		}
		assertEquals(2, result.getDepth());
		// p171, problem 8
		String f = "x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6";
		result = SDS.sds(new LongPoly("xyz", f));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [1, 0, 0], [1, 1, 0], [4, 2, 3]]", result.getZeroAt().toString());
		assertEquals(5, result.getDepth());
		// p171, problem 9
		f = "8*x**7 + 6*x**6*y + 8*x**6*z + 62*x**5*y**2 - 154*x**5*y*z - 69*x**4*y**3 + 202*x**4*y**2*z + 2*x**4*y*z**2 + 18*x**3*y**4 - 170*x**3*y**3*z + 114*x**3*y**2*z**2 + 18*x**3*y*z**3 + 54*x**2*y**4*z - 124*x**2*y**3*z**2 - 26*x**2*y**2*z**3 + 54*x*y**4*z**2 - 22*x*y**3*z**3 + 18*y**4*z**3 + y**3*z**4";
		result = SDS.sds(new LongPoly("xyz", f));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 1, 1], [1, 1, 5], [3, 1, 3]]", result.getZeroAt().toString());
		assertEquals(18, result.getDepth());
		// p172, problem 10
		f = "a**6 + 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 + 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 + a*b**5 - 5*a*c**5 + b**6 - 5*b**5*c + 10*b**4*c**2 - 10*b**3*c**3 + 5*b**2*c**4 - b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(4, result.getDepth());
		f = "a**6 - 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 - 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 - a*b**5 - 5*a*c**5 + b**6 + 5*b**5*c + 10*b**4*c**2 + 10*b**3*c**3 + 5*b**2*c**4 + b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(4, result.getDepth());
		// p172, problem 11
		f = "2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2" +
				" + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4" +
				" - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3" +
				" + 1611722090*z**4";
		// LongPoly: long overflow at depth = 12
		SDSResult<MutableBigInteger> bigResult = SDS.sds(new BigPoly("xyz", f));
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(46, bigResult.getDepth());
		// p174, 6-var Vasc's conjecture, doesn't seem to work here
		/*
		fn = replaceAn("a1**3*a3*a4*a5 + a1**3*a3*a4*a6 + a1**3*a3*a5**2 + a1**3*a3*a5*a6 + a1**3*a4**2*a5 + a1**3*a4**2*a6 + a1**3*a4*a5**2 + a1**3*a4*a5*a6 + a1**2*a2**2*a4*a5 + a1**2*a2**2*a4*a6 + a1**2*a2**2*a5**2 + a1**2*a2**2*a5*a6 + a1**2*a2*a3**2*a5 + a1**2*a2*a3**2*a6 + a1**2*a2*a3*a4**2 - a1**2*a2*a3*a4*a5 - a1**2*a2*a3*a4*a6 - 2*a1**2*a2*a3*a5**2 - a1**2*a2*a3*a5*a6 + a1**2*a2*a4**3 - 2*a1**2*a2*a4**2*a5 - 2*a1**2*a2*a4**2*a6 - 2*a1**2*a2*a4*a5**2 - a1**2*a2*a4*a5*a6 + a1**2*a3**3*a5 + a1**2*a3**3*a6 + a1**2*a3**2*a4**2 - 2*a1**2*a3**2*a4*a5 - 2*a1**2*a3**2*a4*a6 - 3*a1**2*a3**2*a5**2 - 2*a1**2*a3**2*a5*a6 + a1**2*a3*a4**3 - 2*a1**2*a3*a4**2*a5 - 2*a1**2*a3*a4**2*a6 - 2*a1**2*a3*a4*a5**2 + a1**2*a3*a4*a6**2 + a1**2*a3*a5**2*a6 + a1**2*a3*a5*a6**2 + a1**2*a4**2*a5*a6 + a1**2*a4**2*a6**2 + a1**2*a4*a5**2*a6 + a1**2*a4*a5*a6**2 + a1*a2**3*a4*a5 + a1*a2**3*a4*a6 + a1*a2**3*a5**2 + a1*a2**3*a5*a6 + a1*a2**2*a3**2*a5 + a1*a2**2*a3**2*a6 + a1*a2**2*a3*a4**2 - a1*a2**2*a3*a4*a5 - a1*a2**2*a3*a4*a6 - 2*a1*a2**2*a3*a5**2 - a1*a2**2*a3*a5*a6 + a1*a2**2*a4**3 - 2*a1*a2**2*a4**2*a5 - 2*a1*a2**2*a4**2*a6 - 2*a1*a2**2*a4*a5**2 + a1*a2**2*a4*a6**2 + a1*a2**2*a5**2*a6 + a1*a2**2*a5*a6**2 + a1*a2*a3**3*a5 + a1*a2*a3**3*a6 + a1*a2*a3**2*a4**2 - a1*a2*a3**2*a4*a5 - a1*a2*a3**2*a4*a6 - 2*a1*a2*a3**2*a5**2 + a1*a2*a3**2*a6**2 + a1*a2*a3*a4**3 - a1*a2*a3*a4**2*a5 - a1*a2*a3*a4*a6**2 + a1*a2*a3*a5**3 - a1*a2*a3*a5**2*a6 - a1*a2*a3*a5*a6**2 + a1*a2*a4**3*a6 + a1*a2*a4**2*a5**2 - a1*a2*a4**2*a5*a6 - 2*a1*a2*a4**2*a6**2 + a1*a2*a4*a5**3 - a1*a2*a4*a5**2*a6 - a1*a2*a4*a5*a6**2 + a1*a3**3*a5*a6 + a1*a3**3*a6**2 + a1*a3**2*a4**2*a6 + a1*a3**2*a4*a5**2 - a1*a3**2*a4*a5*a6 - 2*a1*a3**2*a4*a6**2 + a1*a3**2*a5**3 - 2*a1*a3**2*a5**2*a6 - 2*a1*a3**2*a5*a6**2 + a1*a3*a4**3*a6 + a1*a3*a4**2*a5**2 - a1*a3*a4**2*a5*a6 - 2*a1*a3*a4**2*a6**2 + a1*a3*a4*a5**3 - a1*a3*a4*a5**2*a6 - a1*a3*a4*a5*a6**2 + a2**3*a4*a5*a6 + a2**3*a4*a6**2 + a2**3*a5**2*a6 + a2**3*a5*a6**2 + a2**2*a3**2*a5*a6 + a2**2*a3**2*a6**2 + a2**2*a3*a4**2*a6 + a2**2*a3*a4*a5**2 - a2**2*a3*a4*a5*a6 - 2*a2**2*a3*a4*a6**2 + a2**2*a3*a5**3 - 2*a2**2*a3*a5**2*a6 - 2*a2**2*a3*a5*a6**2 + a2**2*a4**3*a6 + a2**2*a4**2*a5**2 - 2*a2**2*a4**2*a5*a6 - 3*a2**2*a4**2*a6**2 + a2**2*a4*a5**3 - 2*a2**2*a4*a5**2*a6 - 2*a2**2*a4*a5*a6**2 + a2*a3**3*a5*a6 + a2*a3**3*a6**2 + a2*a3**2*a4**2*a6 + a2*a3**2*a4*a5**2 - a2*a3**2*a4*a5*a6 - 2*a2*a3**2*a4*a6**2 + a2*a3**2*a5**3 - 2*a2*a3**2*a5**2*a6 - 2*a2*a3**2*a5*a6**2 + a2*a3*a4**3*a6 + a2*a3*a4**2*a5**2 - a2*a3*a4**2*a5*a6 - 2*a2*a3*a4**2*a6**2 + a2*a3*a4*a5**3 - a2*a3*a4*a5**2*a6 + a2*a3*a4*a6**3 + a2*a3*a5**2*a6**2 + a2*a3*a5*a6**3 + a2*a4**2*a5*a6**2 + a2*a4**2*a6**3 + a2*a4*a5**2*a6**2 + a2*a4*a5*a6**3 + a3**2*a4*a5*a6**2 + a3**2*a4*a6**3 + a3**2*a5**2*a6**2 + a3**2*a5*a6**3 + a3*a4**2*a5*a6**2 + a3*a4**2*a6**3 + a3*a4*a5**2*a6**2 + a3*a4*a5*a6**3");
		result = SDS.sds(fn);
		*/
		// 5-var Vasc's inequality
		fn = replaceAn("a1**3*a3*a4 + a1**3*a3*a5 + a1**3*a4**2 + a1**3*a4*a5 + a1**2*a2**2*a4 + a1**2*a2**2*a5 + a1**2*a2*a3**2 - a1**2*a2*a3*a4 - a1**2*a2*a3*a5 - 2*a1**2*a2*a4**2 - a1**2*a2*a4*a5 + a1**2*a3**3 - 2*a1**2*a3**2*a4 - 2*a1**2*a3**2*a5 - 2*a1**2*a3*a4**2 + a1**2*a3*a5**2 + a1**2*a4**2*a5 + a1**2*a4*a5**2 + a1*a2**3*a4 + a1*a2**3*a5 + a1*a2**2*a3**2 - a1*a2**2*a3*a4 - a1*a2**2*a3*a5 - 2*a1*a2**2*a4**2 + a1*a2**2*a5**2 + a1*a2*a3**3 - a1*a2*a3**2*a4 - a1*a2*a3*a5**2 + a1*a2*a4**3 - a1*a2*a4**2*a5 - a1*a2*a4*a5**2 + a1*a3**3*a5 + a1*a3**2*a4**2 - a1*a3**2*a4*a5 - 2*a1*a3**2*a5**2 + a1*a3*a4**3 - a1*a3*a4**2*a5 - a1*a3*a4*a5**2 + a2**3*a4*a5 + a2**3*a5**2 + a2**2*a3**2*a5 + a2**2*a3*a4**2 - a2**2*a3*a4*a5 - 2*a2**2*a3*a5**2 + a2**2*a4**3 - 2*a2**2*a4**2*a5 - 2*a2**2*a4*a5**2 + a2*a3**3*a5 + a2*a3**2*a4**2 - a2*a3**2*a4*a5 - 2*a2*a3**2*a5**2 + a2*a3*a4**3 - a2*a3*a4**2*a5 + a2*a3*a5**3 + a2*a4**2*a5**2 + a2*a4*a5**3 + a3**2*a4*a5**2 + a3**2*a5**3 + a3*a4**2*a5**2 + a3*a4*a5**3");
		fd = replaceAn("a1**2*a2*a3*a4 + a1**2*a2*a3*a5 + a1**2*a2*a4**2 + a1**2*a2*a4*a5 + a1**2*a3**2*a4 + a1**2*a3**2*a5 + a1**2*a3*a4**2 + a1**2*a3*a4*a5 + a1*a2**2*a3*a4 + a1*a2**2*a3*a5 + a1*a2**2*a4**2 + a1*a2**2*a4*a5 + a1*a2*a3**2*a4 + a1*a2*a3**2*a5 + a1*a2*a3*a4**2 + 2*a1*a2*a3*a4*a5 + a1*a2*a3*a5**2 + a1*a2*a4**2*a5 + a1*a2*a4*a5**2 + a1*a3**2*a4*a5 + a1*a3**2*a5**2 + a1*a3*a4**2*a5 + a1*a3*a4*a5**2 + a2**2*a3*a4*a5 + a2**2*a3*a5**2 + a2**2*a4**2*a5 + a2**2*a4*a5**2 + a2*a3**2*a4*a5 + a2*a3**2*a5**2 + a2*a3*a4**2*a5 + a2*a3*a4*a5**2");
		result = SDS.sds(fn);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1, 1, 1]]", getZeroAt(fn, fd, result.getZeroAt()).toString());
		assertEquals(2, result.getDepth());
		// 7-var Vasc's inequality, too slow even if skip negative finding
		/*
		fn = replaceAn("a1**3*a3*a4*a5*a6 + a1**3*a3*a4*a5*a7 + a1**3*a3*a4*a6**2 + a1**3*a3*a4*a6*a7 + a1**3*a3*a5**2*a6 + a1**3*a3*a5**2*a7 + a1**3*a3*a5*a6**2 + a1**3*a3*a5*a6*a7 + a1**3*a4**2*a5*a6 + a1**3*a4**2*a5*a7 + a1**3*a4**2*a6**2 + a1**3*a4**2*a6*a7 + a1**3*a4*a5**2*a6 + a1**3*a4*a5**2*a7 + a1**3*a4*a5*a6**2 + a1**3*a4*a5*a6*a7 + a1**2*a2**2*a4*a5*a6 + a1**2*a2**2*a4*a5*a7 + a1**2*a2**2*a4*a6**2 + a1**2*a2**2*a4*a6*a7 + a1**2*a2**2*a5**2*a6 + a1**2*a2**2*a5**2*a7 + a1**2*a2**2*a5*a6**2 + a1**2*a2**2*a5*a6*a7 + a1**2*a2*a3**2*a5*a6 + a1**2*a2*a3**2*a5*a7 + a1**2*a2*a3**2*a6**2 + a1**2*a2*a3**2*a6*a7 + a1**2*a2*a3*a4**2*a6 + a1**2*a2*a3*a4**2*a7 + a1**2*a2*a3*a4*a5**2 - a1**2*a2*a3*a4*a5*a6 - a1**2*a2*a3*a4*a5*a7 - 2*a1**2*a2*a3*a4*a6**2 - a1**2*a2*a3*a4*a6*a7 + a1**2*a2*a3*a5**3 - 2*a1**2*a2*a3*a5**2*a6 - 2*a1**2*a2*a3*a5**2*a7 - 2*a1**2*a2*a3*a5*a6**2 - a1**2*a2*a3*a5*a6*a7 + a1**2*a2*a4**3*a6 + a1**2*a2*a4**3*a7 + a1**2*a2*a4**2*a5**2 - 2*a1**2*a2*a4**2*a5*a6 - 2*a1**2*a2*a4**2*a5*a7 - 3*a1**2*a2*a4**2*a6**2 - 2*a1**2*a2*a4**2*a6*a7 + a1**2*a2*a4*a5**3 - 2*a1**2*a2*a4*a5**2*a6 - 2*a1**2*a2*a4*a5**2*a7 - 2*a1**2*a2*a4*a5*a6**2 - a1**2*a2*a4*a5*a6*a7 + a1**2*a3**3*a5*a6 + a1**2*a3**3*a5*a7 + a1**2*a3**3*a6**2 + a1**2*a3**3*a6*a7 + a1**2*a3**2*a4**2*a6 + a1**2*a3**2*a4**2*a7 + a1**2*a3**2*a4*a5**2 - 2*a1**2*a3**2*a4*a5*a6 - 2*a1**2*a3**2*a4*a5*a7 - 3*a1**2*a3**2*a4*a6**2 - 2*a1**2*a3**2*a4*a6*a7 + a1**2*a3**2*a5**3 - 3*a1**2*a3**2*a5**2*a6 - 3*a1**2*a3**2*a5**2*a7 - 3*a1**2*a3**2*a5*a6**2 - 2*a1**2*a3**2*a5*a6*a7 + a1**2*a3*a4**3*a6 + a1**2*a3*a4**3*a7 + a1**2*a3*a4**2*a5**2 - 2*a1**2*a3*a4**2*a5*a6 - 2*a1**2*a3*a4**2*a5*a7 - 3*a1**2*a3*a4**2*a6**2 - 2*a1**2*a3*a4**2*a6*a7 + a1**2*a3*a4*a5**3 - 2*a1**2*a3*a4*a5**2*a6 - 2*a1**2*a3*a4*a5**2*a7 - 2*a1**2*a3*a4*a5*a6**2 + a1**2*a3*a4*a5*a7**2 + a1**2*a3*a4*a6**2*a7 + a1**2*a3*a4*a6*a7**2 + a1**2*a3*a5**2*a6*a7 + a1**2*a3*a5**2*a7**2 + a1**2*a3*a5*a6**2*a7 + a1**2*a3*a5*a6*a7**2 + a1**2*a4**2*a5*a6*a7 + a1**2*a4**2*a5*a7**2 + a1**2*a4**2*a6**2*a7 + a1**2*a4**2*a6*a7**2 + a1**2*a4*a5**2*a6*a7 + a1**2*a4*a5**2*a7**2 + a1**2*a4*a5*a6**2*a7 + a1**2*a4*a5*a6*a7**2 + a1*a2**3*a4*a5*a6 + a1*a2**3*a4*a5*a7 + a1*a2**3*a4*a6**2 + a1*a2**3*a4*a6*a7 + a1*a2**3*a5**2*a6 + a1*a2**3*a5**2*a7 + a1*a2**3*a5*a6**2 + a1*a2**3*a5*a6*a7 + a1*a2**2*a3**2*a5*a6 + a1*a2**2*a3**2*a5*a7 + a1*a2**2*a3**2*a6**2 + a1*a2**2*a3**2*a6*a7 + a1*a2**2*a3*a4**2*a6 + a1*a2**2*a3*a4**2*a7 + a1*a2**2*a3*a4*a5**2 - a1*a2**2*a3*a4*a5*a6 - a1*a2**2*a3*a4*a5*a7 - 2*a1*a2**2*a3*a4*a6**2 - a1*a2**2*a3*a4*a6*a7 + a1*a2**2*a3*a5**3 - 2*a1*a2**2*a3*a5**2*a6 - 2*a1*a2**2*a3*a5**2*a7 - 2*a1*a2**2*a3*a5*a6**2 - a1*a2**2*a3*a5*a6*a7 + a1*a2**2*a4**3*a6 + a1*a2**2*a4**3*a7 + a1*a2**2*a4**2*a5**2 - 2*a1*a2**2*a4**2*a5*a6 - 2*a1*a2**2*a4**2*a5*a7 - 3*a1*a2**2*a4**2*a6**2 - 2*a1*a2**2*a4**2*a6*a7 + a1*a2**2*a4*a5**3 - 2*a1*a2**2*a4*a5**2*a6 - 2*a1*a2**2*a4*a5**2*a7 - 2*a1*a2**2*a4*a5*a6**2 + a1*a2**2*a4*a5*a7**2 + a1*a2**2*a4*a6**2*a7 + a1*a2**2*a4*a6*a7**2 + a1*a2**2*a5**2*a6*a7 + a1*a2**2*a5**2*a7**2 + a1*a2**2*a5*a6**2*a7 + a1*a2**2*a5*a6*a7**2 + a1*a2*a3**3*a5*a6 + a1*a2*a3**3*a5*a7 + a1*a2*a3**3*a6**2 + a1*a2*a3**3*a6*a7 + a1*a2*a3**2*a4**2*a6 + a1*a2*a3**2*a4**2*a7 + a1*a2*a3**2*a4*a5**2 - a1*a2*a3**2*a4*a5*a6 - a1*a2*a3**2*a4*a5*a7 - 2*a1*a2*a3**2*a4*a6**2 - a1*a2*a3**2*a4*a6*a7 + a1*a2*a3**2*a5**3 - 2*a1*a2*a3**2*a5**2*a6 - 2*a1*a2*a3**2*a5**2*a7 - 2*a1*a2*a3**2*a5*a6**2 + a1*a2*a3**2*a5*a7**2 + a1*a2*a3**2*a6**2*a7 + a1*a2*a3**2*a6*a7**2 + a1*a2*a3*a4**3*a6 + a1*a2*a3*a4**3*a7 + a1*a2*a3*a4**2*a5**2 - a1*a2*a3*a4**2*a5*a6 - a1*a2*a3*a4**2*a5*a7 - 2*a1*a2*a3*a4**2*a6**2 + a1*a2*a3*a4**2*a7**2 + a1*a2*a3*a4*a5**3 - a1*a2*a3*a4*a5**2*a6 - a1*a2*a3*a4*a5*a7**2 + a1*a2*a3*a4*a6**3 - a1*a2*a3*a4*a6**2*a7 - a1*a2*a3*a4*a6*a7**2 + a1*a2*a3*a5**3*a7 + a1*a2*a3*a5**2*a6**2 - a1*a2*a3*a5**2*a6*a7 - 2*a1*a2*a3*a5**2*a7**2 + a1*a2*a3*a5*a6**3 - a1*a2*a3*a5*a6**2*a7 - a1*a2*a3*a5*a6*a7**2 + a1*a2*a4**3*a6*a7 + a1*a2*a4**3*a7**2 + a1*a2*a4**2*a5**2*a7 + a1*a2*a4**2*a5*a6**2 - a1*a2*a4**2*a5*a6*a7 - 2*a1*a2*a4**2*a5*a7**2 + a1*a2*a4**2*a6**3 - 2*a1*a2*a4**2*a6**2*a7 - 2*a1*a2*a4**2*a6*a7**2 + a1*a2*a4*a5**3*a7 + a1*a2*a4*a5**2*a6**2 - a1*a2*a4*a5**2*a6*a7 - 2*a1*a2*a4*a5**2*a7**2 + a1*a2*a4*a5*a6**3 - a1*a2*a4*a5*a6**2*a7 - a1*a2*a4*a5*a6*a7**2 + a1*a3**3*a5*a6*a7 + a1*a3**3*a5*a7**2 + a1*a3**3*a6**2*a7 + a1*a3**3*a6*a7**2 + a1*a3**2*a4**2*a6*a7 + a1*a3**2*a4**2*a7**2 + a1*a3**2*a4*a5**2*a7 + a1*a3**2*a4*a5*a6**2 - a1*a3**2*a4*a5*a6*a7 - 2*a1*a3**2*a4*a5*a7**2 + a1*a3**2*a4*a6**3 - 2*a1*a3**2*a4*a6**2*a7 - 2*a1*a3**2*a4*a6*a7**2 + a1*a3**2*a5**3*a7 + a1*a3**2*a5**2*a6**2 - 2*a1*a3**2*a5**2*a6*a7 - 3*a1*a3**2*a5**2*a7**2 + a1*a3**2*a5*a6**3 - 2*a1*a3**2*a5*a6**2*a7 - 2*a1*a3**2*a5*a6*a7**2 + a1*a3*a4**3*a6*a7 + a1*a3*a4**3*a7**2 + a1*a3*a4**2*a5**2*a7 + a1*a3*a4**2*a5*a6**2 - a1*a3*a4**2*a5*a6*a7 - 2*a1*a3*a4**2*a5*a7**2 + a1*a3*a4**2*a6**3 - 2*a1*a3*a4**2*a6**2*a7 - 2*a1*a3*a4**2*a6*a7**2 + a1*a3*a4*a5**3*a7 + a1*a3*a4*a5**2*a6**2 - a1*a3*a4*a5**2*a6*a7 - 2*a1*a3*a4*a5**2*a7**2 + a1*a3*a4*a5*a6**3 - a1*a3*a4*a5*a6**2*a7 - a1*a3*a4*a5*a6*a7**2 + a2**3*a4*a5*a6*a7 + a2**3*a4*a5*a7**2 + a2**3*a4*a6**2*a7 + a2**3*a4*a6*a7**2 + a2**3*a5**2*a6*a7 + a2**3*a5**2*a7**2 + a2**3*a5*a6**2*a7 + a2**3*a5*a6*a7**2 + a2**2*a3**2*a5*a6*a7 + a2**2*a3**2*a5*a7**2 + a2**2*a3**2*a6**2*a7 + a2**2*a3**2*a6*a7**2 + a2**2*a3*a4**2*a6*a7 + a2**2*a3*a4**2*a7**2 + a2**2*a3*a4*a5**2*a7 + a2**2*a3*a4*a5*a6**2 - a2**2*a3*a4*a5*a6*a7 - 2*a2**2*a3*a4*a5*a7**2 + a2**2*a3*a4*a6**3 - 2*a2**2*a3*a4*a6**2*a7 - 2*a2**2*a3*a4*a6*a7**2 + a2**2*a3*a5**3*a7 + a2**2*a3*a5**2*a6**2 - 2*a2**2*a3*a5**2*a6*a7 - 3*a2**2*a3*a5**2*a7**2 + a2**2*a3*a5*a6**3 - 2*a2**2*a3*a5*a6**2*a7 - 2*a2**2*a3*a5*a6*a7**2 + a2**2*a4**3*a6*a7 + a2**2*a4**3*a7**2 + a2**2*a4**2*a5**2*a7 + a2**2*a4**2*a5*a6**2 - 2*a2**2*a4**2*a5*a6*a7 - 3*a2**2*a4**2*a5*a7**2 + a2**2*a4**2*a6**3 - 3*a2**2*a4**2*a6**2*a7 - 3*a2**2*a4**2*a6*a7**2 + a2**2*a4*a5**3*a7 + a2**2*a4*a5**2*a6**2 - 2*a2**2*a4*a5**2*a6*a7 - 3*a2**2*a4*a5**2*a7**2 + a2**2*a4*a5*a6**3 - 2*a2**2*a4*a5*a6**2*a7 - 2*a2**2*a4*a5*a6*a7**2 + a2*a3**3*a5*a6*a7 + a2*a3**3*a5*a7**2 + a2*a3**3*a6**2*a7 + a2*a3**3*a6*a7**2 + a2*a3**2*a4**2*a6*a7 + a2*a3**2*a4**2*a7**2 + a2*a3**2*a4*a5**2*a7 + a2*a3**2*a4*a5*a6**2 - a2*a3**2*a4*a5*a6*a7 - 2*a2*a3**2*a4*a5*a7**2 + a2*a3**2*a4*a6**3 - 2*a2*a3**2*a4*a6**2*a7 - 2*a2*a3**2*a4*a6*a7**2 + a2*a3**2*a5**3*a7 + a2*a3**2*a5**2*a6**2 - 2*a2*a3**2*a5**2*a6*a7 - 3*a2*a3**2*a5**2*a7**2 + a2*a3**2*a5*a6**3 - 2*a2*a3**2*a5*a6**2*a7 - 2*a2*a3**2*a5*a6*a7**2 + a2*a3*a4**3*a6*a7 + a2*a3*a4**3*a7**2 + a2*a3*a4**2*a5**2*a7 + a2*a3*a4**2*a5*a6**2 - a2*a3*a4**2*a5*a6*a7 - 2*a2*a3*a4**2*a5*a7**2 + a2*a3*a4**2*a6**3 - 2*a2*a3*a4**2*a6**2*a7 - 2*a2*a3*a4**2*a6*a7**2 + a2*a3*a4*a5**3*a7 + a2*a3*a4*a5**2*a6**2 - a2*a3*a4*a5**2*a6*a7 - 2*a2*a3*a4*a5**2*a7**2 + a2*a3*a4*a5*a6**3 - a2*a3*a4*a5*a6**2*a7 + a2*a3*a4*a5*a7**3 + a2*a3*a4*a6**2*a7**2 + a2*a3*a4*a6*a7**3 + a2*a3*a5**2*a6*a7**2 + a2*a3*a5**2*a7**3 + a2*a3*a5*a6**2*a7**2 + a2*a3*a5*a6*a7**3 + a2*a4**2*a5*a6*a7**2 + a2*a4**2*a5*a7**3 + a2*a4**2*a6**2*a7**2 + a2*a4**2*a6*a7**3 + a2*a4*a5**2*a6*a7**2 + a2*a4*a5**2*a7**3 + a2*a4*a5*a6**2*a7**2 + a2*a4*a5*a6*a7**3 + a3**2*a4*a5*a6*a7**2 + a3**2*a4*a5*a7**3 + a3**2*a4*a6**2*a7**2 + a3**2*a4*a6*a7**3 + a3**2*a5**2*a6*a7**2 + a3**2*a5**2*a7**3 + a3**2*a5*a6**2*a7**2 + a3**2*a5*a6*a7**3 + a3*a4**2*a5*a6*a7**2 + a3*a4**2*a5*a7**3 + a3*a4**2*a6**2*a7**2 + a3*a4**2*a6*a7**3 + a3*a4*a5**2*a6*a7**2 + a3*a4*a5**2*a7**3 + a3*a4*a5*a6**2*a7**2 + a3*a4*a5*a6*a7**3");
		fd = replaceAn("a1**2*a2*a3*a4*a5*a6 + a1**2*a2*a3*a4*a5*a7 + a1**2*a2*a3*a4*a6**2 + a1**2*a2*a3*a4*a6*a7 + a1**2*a2*a3*a5**2*a6 + a1**2*a2*a3*a5**2*a7 + a1**2*a2*a3*a5*a6**2 + a1**2*a2*a3*a5*a6*a7 + a1**2*a2*a4**2*a5*a6 + a1**2*a2*a4**2*a5*a7 + a1**2*a2*a4**2*a6**2 + a1**2*a2*a4**2*a6*a7 + a1**2*a2*a4*a5**2*a6 + a1**2*a2*a4*a5**2*a7 + a1**2*a2*a4*a5*a6**2 + a1**2*a2*a4*a5*a6*a7 + a1**2*a3**2*a4*a5*a6 + a1**2*a3**2*a4*a5*a7 + a1**2*a3**2*a4*a6**2 + a1**2*a3**2*a4*a6*a7 + a1**2*a3**2*a5**2*a6 + a1**2*a3**2*a5**2*a7 + a1**2*a3**2*a5*a6**2 + a1**2*a3**2*a5*a6*a7 + a1**2*a3*a4**2*a5*a6 + a1**2*a3*a4**2*a5*a7 + a1**2*a3*a4**2*a6**2 + a1**2*a3*a4**2*a6*a7 + a1**2*a3*a4*a5**2*a6 + a1**2*a3*a4*a5**2*a7 + a1**2*a3*a4*a5*a6**2 + a1**2*a3*a4*a5*a6*a7 + a1*a2**2*a3*a4*a5*a6 + a1*a2**2*a3*a4*a5*a7 + a1*a2**2*a3*a4*a6**2 + a1*a2**2*a3*a4*a6*a7 + a1*a2**2*a3*a5**2*a6 + a1*a2**2*a3*a5**2*a7 + a1*a2**2*a3*a5*a6**2 + a1*a2**2*a3*a5*a6*a7 + a1*a2**2*a4**2*a5*a6 + a1*a2**2*a4**2*a5*a7 + a1*a2**2*a4**2*a6**2 + a1*a2**2*a4**2*a6*a7 + a1*a2**2*a4*a5**2*a6 + a1*a2**2*a4*a5**2*a7 + a1*a2**2*a4*a5*a6**2 + a1*a2**2*a4*a5*a6*a7 + a1*a2*a3**2*a4*a5*a6 + a1*a2*a3**2*a4*a5*a7 + a1*a2*a3**2*a4*a6**2 + a1*a2*a3**2*a4*a6*a7 + a1*a2*a3**2*a5**2*a6 + a1*a2*a3**2*a5**2*a7 + a1*a2*a3**2*a5*a6**2 + a1*a2*a3**2*a5*a6*a7 + a1*a2*a3*a4**2*a5*a6 + a1*a2*a3*a4**2*a5*a7 + a1*a2*a3*a4**2*a6**2 + a1*a2*a3*a4**2*a6*a7 + a1*a2*a3*a4*a5**2*a6 + a1*a2*a3*a4*a5**2*a7 + a1*a2*a3*a4*a5*a6**2 + 2*a1*a2*a3*a4*a5*a6*a7 + a1*a2*a3*a4*a5*a7**2 + a1*a2*a3*a4*a6**2*a7 + a1*a2*a3*a4*a6*a7**2 + a1*a2*a3*a5**2*a6*a7 + a1*a2*a3*a5**2*a7**2 + a1*a2*a3*a5*a6**2*a7 + a1*a2*a3*a5*a6*a7**2 + a1*a2*a4**2*a5*a6*a7 + a1*a2*a4**2*a5*a7**2 + a1*a2*a4**2*a6**2*a7 + a1*a2*a4**2*a6*a7**2 + a1*a2*a4*a5**2*a6*a7 + a1*a2*a4*a5**2*a7**2 + a1*a2*a4*a5*a6**2*a7 + a1*a2*a4*a5*a6*a7**2 + a1*a3**2*a4*a5*a6*a7 + a1*a3**2*a4*a5*a7**2 + a1*a3**2*a4*a6**2*a7 + a1*a3**2*a4*a6*a7**2 + a1*a3**2*a5**2*a6*a7 + a1*a3**2*a5**2*a7**2 + a1*a3**2*a5*a6**2*a7 + a1*a3**2*a5*a6*a7**2 + a1*a3*a4**2*a5*a6*a7 + a1*a3*a4**2*a5*a7**2 + a1*a3*a4**2*a6**2*a7 + a1*a3*a4**2*a6*a7**2 + a1*a3*a4*a5**2*a6*a7 + a1*a3*a4*a5**2*a7**2 + a1*a3*a4*a5*a6**2*a7 + a1*a3*a4*a5*a6*a7**2 + a2**2*a3*a4*a5*a6*a7 + a2**2*a3*a4*a5*a7**2 + a2**2*a3*a4*a6**2*a7 + a2**2*a3*a4*a6*a7**2 + a2**2*a3*a5**2*a6*a7 + a2**2*a3*a5**2*a7**2 + a2**2*a3*a5*a6**2*a7 + a2**2*a3*a5*a6*a7**2 + a2**2*a4**2*a5*a6*a7 + a2**2*a4**2*a5*a7**2 + a2**2*a4**2*a6**2*a7 + a2**2*a4**2*a6*a7**2 + a2**2*a4*a5**2*a6*a7 + a2**2*a4*a5**2*a7**2 + a2**2*a4*a5*a6**2*a7 + a2**2*a4*a5*a6*a7**2 + a2*a3**2*a4*a5*a6*a7 + a2*a3**2*a4*a5*a7**2 + a2*a3**2*a4*a6**2*a7 + a2*a3**2*a4*a6*a7**2 + a2*a3**2*a5**2*a6*a7 + a2*a3**2*a5**2*a7**2 + a2*a3**2*a5*a6**2*a7 + a2*a3**2*a5*a6*a7**2 + a2*a3*a4**2*a5*a6*a7 + a2*a3*a4**2*a5*a7**2 + a2*a3*a4**2*a6**2*a7 + a2*a3*a4**2*a6*a7**2 + a2*a3*a4*a5**2*a6*a7 + a2*a3*a4*a5**2*a7**2 + a2*a3*a4*a5*a6**2*a7 + a2*a3*a4*a5*a6*a7**2");
		result = SDS.sds(fn, false, true);
		assertTrue(result.isNonNegative());
		// assertEquals("[[1, 1, 1, 1, 1]]", getZeroAt(fn, fd, result.getZeroAt()).toString());
		assertEquals(2, result.getDepth());
		*/
	}

	@Test
	public void testMathSE() {
		// https://math.stackexchange.com/a/2120874
		// https://math.stackexchange.com/q/1775572
		BigPoly f = new BigPoly("xyz", "200*x**7*y**3 + 125*x**7*z**3 + 200*x**6*y**4 - 320*x**6*y**3*z - 200*x**6*y*z**3 - 200*x**6*z**4 - 200*x**4*y**6 + 195*x**4*y**3*z**3 + 200*x**4*z**6 + 125*x**3*y**7 - 200*x**3*y**6*z + 195*x**3*y**4*z**3 + 195*x**3*y**3*z**4 - 320*x**3*y*z**6 + 200*x**3*z**7 - 320*x*y**6*z**3 - 200*x*y**3*z**6 + 200*y**7*z**3 + 200*y**6*z**4 - 200*y**4*z**6 + 125*y**3*z**7");
		SDSResult<MutableBigInteger> result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// sds need 2
		assertEquals(3, result.getDepth());
		// https://math.stackexchange.com/q/1777075
		f = new BigPoly("xyz", "325*x**5*y**2 + 125*x**5*z**2 + 325*x**4*y**3 - 845*x**4*y**2*z - 325*x**4*y*z**2 - 325*x**4*z**3 - 325*x**3*y**4 + 720*x**3*y**2*z**2 + 325*x**3*z**4 + 125*x**2*y**5 - 325*x**2*y**4*z + 720*x**2*y**3*z**2 + 720*x**2*y**2*z**3 - 845*x**2*y*z**4 + 325*x**2*z**5 - 845*x*y**4*z**2 - 325*x*y**2*z**4 + 325*y**5*z**2 + 325*y**4*z**3 - 325*y**3*z**4 + 125*y**2*z**5");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// sds needs 5
		assertEquals(4, result.getDepth());
		f = new BigPoly("xyz", "72*x**5*y**2 + 27*x**5*z**2 + 72*x**4*y**3 - 192*x**4*y**2*z - 72*x**4*y*z**2 - 72*x**4*z**3 - 72*x**3*y**4 + 165*x**3*y**2*z**2 + 72*x**3*z**4 + 27*x**2*y**5 - 72*x**2*y**4*z + 165*x**2*y**3*z**2 + 165*x**2*y**2*z**3 - 192*x**2*y*z**4 + 72*x**2*z**5 - 192*x*y**4*z**2 - 72*x*y**2*z**4 + 72*y**5*z**2 + 72*y**4*z**3 - 72*y**3*z**4 + 27*y**2*z**5");
		result = SDS.tsds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').compareTo(f.valueOf(0)) < 0);
		assertEquals(2, result.getDepth());
		// https://math.stackexchange.com/q/3526427
		f = new BigPoly("xyz", "x**9*y**3 - x**9*y**2*z - x**9*y*z**2 + x**9*z**3 + 6*x**8*y**4 + x**8*y**3*z - 10*x**8*y**2*z**2 + x**8*y*z**3 + 6*x**8*z**4 + 15*x**7*y**5 + 19*x**7*y**4*z - 26*x**7*y**3*z**2 - 26*x**7*y**2*z**3 + 19*x**7*y*z**4 + 15*x**7*z**5 + 20*x**6*y**6 + 45*x**6*y**5*z - 30*x**6*y**4*z**2 - 110*x**6*y**3*z**3 - 30*x**6*y**2*z**4 + 45*x**6*y*z**5 + 20*x**6*z**6 + 15*x**5*y**7 + 45*x**5*y**6*z - 26*x**5*y**5*z**2 - 202*x**5*y**4*z**3 - 202*x**5*y**3*z**4 - 26*x**5*y**2*z**5 + 45*x**5*y*z**6 + 15*x**5*z**7 + 6*x**4*y**8 + 19*x**4*y**7*z - 30*x**4*y**6*z**2 - 202*x**4*y**5*z**3 + 1410*x**4*y**4*z**4 - 202*x**4*y**3*z**5 - 30*x**4*y**2*z**6 + 19*x**4*y*z**7 + 6*x**4*z**8 + x**3*y**9 + x**3*y**8*z - 26*x**3*y**7*z**2 - 110*x**3*y**6*z**3 - 202*x**3*y**5*z**4 - 202*x**3*y**4*z**5 - 110*x**3*y**3*z**6 - 26*x**3*y**2*z**7 + x**3*y*z**8 + x**3*z**9 - x**2*y**9*z - 10*x**2*y**8*z**2 - 26*x**2*y**7*z**3 - 30*x**2*y**6*z**4 - 26*x**2*y**5*z**5 - 30*x**2*y**4*z**6 - 26*x**2*y**3*z**7 - 10*x**2*y**2*z**8 - x**2*y*z**9 - x*y**9*z**2 + x*y**8*z**3 + 19*x*y**7*z**4 + 45*x*y**6*z**5 + 45*x*y**5*z**6 + 19*x*y**4*z**7 + x*y**3*z**8 - x*y**2*z**9 + y**9*z**3 + 6*y**8*z**4 + 15*y**7*z**5 + 20*y**6*z**6 + 15*y**5*z**7 + 6*y**4*z**8 + y**3*z**9");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1]]", result.getZeroAt().toString());
		// sds needs 2
		assertEquals(4, result.getDepth());
	}

	@Test
	public void testXiong23() {
		// ISBN 9787542878021, p112, §7.2, ex6
		LongPoly f = replaceAn("17*a1**12 + 156*a1**11*a2 + 156*a1**11*a3 + 108*a1**11*a4 + 642*a1**10*a2**2 + 1284*a1**10*a2*a3 + 900*a1**10*a2*a4 + 642*a1**10*a3**2 + 900*a1**10*a3*a4 + 258*a1**10*a4**2 + 1020*a1**9*a2**3 + 4692*a1**9*a2**2*a3 + 3348*a1**9*a2**2*a4 + 4692*a1**9*a2*a3**2 + 6696*a1**9*a2*a3*a4 + 2004*a1**9*a2*a4**2 + 1836*a1**9*a3**3 + 3348*a1**9*a3**2*a4 + 2004*a1**9*a3*a4**2 + 492*a1**9*a4**3 - 33*a1**8*a2**4 + 7500*a1**8*a2**3*a3 + 4044*a1**8*a2**3*a4 + 15066*a1**8*a2**2*a3**2 + 22068*a1**8*a2**2*a3*a4 + 7002*a1**8*a2**2*a4**2 + 10908*a1**8*a2*a3**3 + 22068*a1**8*a2*a3**2*a4 + 14004*a1**8*a2*a3*a4**2 + 3660*a1**8*a2*a4**3 + 4191*a1**8*a3**4 + 8268*a1**8*a3**3*a4 + 7002*a1**8*a3**2*a4**2 + 2844*a1**8*a3*a4**3 + 735*a1**8*a4**4 - 1800*a1**7*a2**5 + 4824*a1**7*a2**4*a3 - 2376*a1**7*a2**4*a4 + 23472*a1**7*a2**3*a3**2 + 29664*a1**7*a2**3*a3*a4 + 6192*a1**7*a2**3*a4**2 + 28272*a1**7*a2**2*a3**3 + 64080*a1**7*a2**2*a3**2*a4 + 43920*a1**7*a2**2*a3*a4**2 + 12336*a1**7*a2**2*a4**3 + 18648*a1**7*a2*a3**4 + 43488*a1**7*a2*a3**3*a4 + 43920*a1**7*a2*a3**2*a4**2 + 20448*a1**7*a2*a3*a4**3 + 5592*a1**7*a2*a4**4 + 7224*a1**7*a3**5 + 15672*a1**7*a3**4*a4 + 15216*a1**7*a3**3*a4**2 + 8112*a1**7*a3**2*a4**3 + 1368*a1**7*a3*a4**4 + 24*a1**7*a4**5 - 1636*a1**6*a2**6 + 1896*a1**6*a2**5*a3 - 8472*a1**6*a2**5*a4 + 22308*a1**6*a2**4*a3**2 + 15816*a1**6*a2**4*a3*a4 - 6492*a1**6*a2**4*a4**2 + 30192*a1**6*a2**3*a3**3 + 89808*a1**6*a2**3*a3**2*a4 + 55248*a1**6*a2**3*a3*a4**2 + 4656*a1**6*a2**3*a4**3 + 35364*a1**6*a2**2*a3**4 + 102864*a1**6*a2**2*a3**3*a4 + 123480*a1**6*a2**2*a3**2*a4**2 + 65808*a1**6*a2**2*a3*a4**3 + 18852*a1**6*a2**2*a4**4 + 23976*a1**6*a2*a3**5 + 59976*a1**6*a2*a3**4*a4 + 77328*a1**6*a2*a3**3*a4**2 + 56784*a1**6*a2*a3**2*a4**3 + 19656*a1**6*a2*a3*a4**4 + 4200*a1**6*a2*a4**5 + 8732*a1**6*a3**6 + 22632*a1**6*a3**5*a4 + 24612*a1**6*a3**4*a4**2 + 19056*a1**6*a3**3*a4**3 + 804*a1**6*a3**2*a4**4 - 4824*a1**6*a3*a4**5 - 1636*a1**6*a4**6 + 24*a1**5*a2**7 + 4200*a1**5*a2**6*a3 - 4824*a1**5*a2**6*a4 + 20664*a1**5*a2**5*a3**2 + 10224*a1**5*a2**5*a3*a4 - 10440*a1**5*a2**5*a4**2 + 10344*a1**5*a2**4*a3**3 + 84312*a1**5*a2**4*a3**2*a4 + 41112*a1**5*a2**4*a3*a4**2 - 9432*a1**5*a2**4*a4**3 + 24264*a1**5*a2**3*a3**4 + 109344*a1**5*a2**3*a3**3*a4 + 175536*a1**5*a2**3*a3**2*a4**2 + 67872*a1**5*a2**3*a3*a4**3 + 840*a1**5*a2**3*a4**4 + 32760*a1**5*a2**2*a3**5 + 108504*a1**5*a2**2*a3**4*a4 + 187632*a1**5*a2**2*a3**3*a4**2 + 170352*a1**5*a2**2*a3**2*a4**3 + 79128*a1**5*a2**2*a3*a4**4 + 20664*a1**5*a2**2*a4**5 + 22632*a1**5*a2*a3**6 + 65520*a1**5*a2*a3**5*a4 + 96408*a1**5*a2*a3**4*a4**2 + 93984*a1**5*a2*a3**3*a4**3 + 48024*a1**5*a2*a3**2*a4**4 + 10224*a1**5*a2*a3*a4**5 + 1896*a1**5*a2*a4**6 + 7224*a1**5*a3**7 + 23976*a1**5*a3**6*a4 + 32760*a1**5*a3**5*a4**2 + 24360*a1**5*a3**4*a4**3 + 5352*a1**5*a3**3*a4**4 - 10440*a1**5*a3**2*a4**5 - 8472*a1**5*a3*a4**6 - 1800*a1**5*a4**7 + 735*a1**4*a2**8 + 5592*a1**4*a2**7*a3 + 1368*a1**4*a2**7*a4 + 18852*a1**4*a2**6*a3**2 + 19656*a1**4*a2**6*a3*a4 + 804*a1**4*a2**6*a4**2 + 840*a1**4*a2**5*a3**3 + 79128*a1**4*a2**5*a3**2*a4 + 48024*a1**4*a2**5*a3*a4**2 + 5352*a1**4*a2**5*a4**3 - 1926*a1**4*a2**4*a3**4 + 76488*a1**4*a2**4*a3**3*a4 + 184860*a1**4*a2**4*a3**2*a4**2 + 68904*a1**4*a2**4*a3*a4**3 - 1926*a1**4*a2**4*a4**4 + 24360*a1**4*a2**3*a3**5 + 99144*a1**4*a2**3*a3**4*a4 + 238224*a1**4*a2**3*a3**3*a4**2 + 229584*a1**4*a2**3*a3**2*a4**3 + 76488*a1**4*a2**3*a3*a4**4 + 10344*a1**4*a2**3*a4**5 + 24612*a1**4*a2**2*a3**6 + 96408*a1**4*a2**2*a3**5*a4 + 202140*a1**4*a2**2*a3**4*a4**2 + 240912*a1**4*a2**2*a3**3*a4**3 + 184860*a1**4*a2**2*a3**2*a4**4 + 84312*a1**4*a2**2*a3*a4**5 + 22308*a1**4*a2**2*a4**6 + 15672*a1**4*a2*a3**7 + 59976*a1**4*a2*a3**6*a4 + 108504*a1**4*a2*a3**5*a4**2 + 99144*a1**4*a2*a3**4*a4**3 + 68904*a1**4*a2*a3**3*a4**4 + 41112*a1**4*a2*a3**2*a4**5 + 15816*a1**4*a2*a3*a4**6 + 4824*a1**4*a2*a4**7 + 4191*a1**4*a3**8 + 18648*a1**4*a3**7*a4 + 35364*a1**4*a3**6*a4**2 + 24264*a1**4*a3**5*a4**3 - 1926*a1**4*a3**4*a4**4 - 9432*a1**4*a3**3*a4**5 - 6492*a1**4*a3**2*a4**6 - 2376*a1**4*a3*a4**7 - 33*a1**4*a4**8 + 492*a1**3*a2**9 + 3660*a1**3*a2**8*a3 + 2844*a1**3*a2**8*a4 + 12336*a1**3*a2**7*a3**2 + 20448*a1**3*a2**7*a3*a4 + 8112*a1**3*a2**7*a4**2 + 4656*a1**3*a2**6*a3**3 + 65808*a1**3*a2**6*a3**2*a4 + 56784*a1**3*a2**6*a3*a4**2 + 19056*a1**3*a2**6*a4**3 - 9432*a1**3*a2**5*a3**4 + 67872*a1**3*a2**5*a3**3*a4 + 170352*a1**3*a2**5*a3**2*a4**2 + 93984*a1**3*a2**5*a3*a4**3 + 24360*a1**3*a2**5*a4**4 + 5352*a1**3*a2**4*a3**5 + 68904*a1**3*a2**4*a3**4*a4 + 229584*a1**3*a2**4*a3**3*a4**2 + 240912*a1**3*a2**4*a3**2*a4**3 + 99144*a1**3*a2**4*a3*a4**4 + 24264*a1**3*a2**4*a4**5 + 19056*a1**3*a2**3*a3**6 + 93984*a1**3*a2**3*a3**5*a4 + 240912*a1**3*a2**3*a3**4*a4**2 + 175040*a1**3*a2**3*a3**3*a4**3 + 238224*a1**3*a2**3*a3**2*a4**4 + 109344*a1**3*a2**3*a3*a4**5 + 30192*a1**3*a2**3*a4**6 + 15216*a1**3*a2**2*a3**7 + 77328*a1**3*a2**2*a3**6*a4 + 187632*a1**3*a2**2*a3**5*a4**2 + 238224*a1**3*a2**2*a3**4*a4**3 + 229584*a1**3*a2**2*a3**3*a4**4 + 175536*a1**3*a2**2*a3**2*a4**5 + 89808*a1**3*a2**2*a3*a4**6 + 23472*a1**3*a2**2*a4**7 + 8268*a1**3*a2*a3**8 + 43488*a1**3*a2*a3**7*a4 + 102864*a1**3*a2*a3**6*a4**2 + 109344*a1**3*a2*a3**5*a4**3 + 76488*a1**3*a2*a3**4*a4**4 + 67872*a1**3*a2*a3**3*a4**5 + 55248*a1**3*a2*a3**2*a4**6 + 29664*a1**3*a2*a3*a4**7 + 7500*a1**3*a2*a4**8 + 1836*a1**3*a3**9 + 10908*a1**3*a3**8*a4 + 28272*a1**3*a3**7*a4**2 + 30192*a1**3*a3**6*a4**3 + 10344*a1**3*a3**5*a4**4 + 840*a1**3*a3**4*a4**5 + 4656*a1**3*a3**3*a4**6 + 6192*a1**3*a3**2*a4**7 + 4044*a1**3*a3*a4**8 + 1020*a1**3*a4**9 + 258*a1**2*a2**10 + 2004*a1**2*a2**9*a3 + 2004*a1**2*a2**9*a4 + 7002*a1**2*a2**8*a3**2 + 14004*a1**2*a2**8*a3*a4 + 7002*a1**2*a2**8*a4**2 + 6192*a1**2*a2**7*a3**3 + 43920*a1**2*a2**7*a3**2*a4 + 43920*a1**2*a2**7*a3*a4**2 + 15216*a1**2*a2**7*a4**3 - 6492*a1**2*a2**6*a3**4 + 55248*a1**2*a2**6*a3**3*a4 + 123480*a1**2*a2**6*a3**2*a4**2 + 77328*a1**2*a2**6*a3*a4**3 + 24612*a1**2*a2**6*a4**4 - 10440*a1**2*a2**5*a3**5 + 41112*a1**2*a2**5*a3**4*a4 + 175536*a1**2*a2**5*a3**3*a4**2 + 187632*a1**2*a2**5*a3**2*a4**3 + 96408*a1**2*a2**5*a3*a4**4 + 32760*a1**2*a2**5*a4**5 + 804*a1**2*a2**4*a3**6 + 48024*a1**2*a2**4*a3**5*a4 + 184860*a1**2*a2**4*a3**4*a4**2 + 238224*a1**2*a2**4*a3**3*a4**3 + 202140*a1**2*a2**4*a3**2*a4**4 + 108504*a1**2*a2**4*a3*a4**5 + 35364*a1**2*a2**4*a4**6 + 8112*a1**2*a2**3*a3**7 + 56784*a1**2*a2**3*a3**6*a4 + 170352*a1**2*a2**3*a3**5*a4**2 + 229584*a1**2*a2**3*a3**4*a4**3 + 240912*a1**2*a2**3*a3**3*a4**4 + 187632*a1**2*a2**3*a3**2*a4**5 + 102864*a1**2*a2**3*a3*a4**6 + 28272*a1**2*a2**3*a4**7 + 7002*a1**2*a2**2*a3**8 + 43920*a1**2*a2**2*a3**7*a4 + 123480*a1**2*a2**2*a3**6*a4**2 + 175536*a1**2*a2**2*a3**5*a4**3 + 184860*a1**2*a2**2*a3**4*a4**4 + 170352*a1**2*a2**2*a3**3*a4**5 + 123480*a1**2*a2**2*a3**2*a4**6 + 64080*a1**2*a2**2*a3*a4**7 + 15066*a1**2*a2**2*a4**8 + 3348*a1**2*a2*a3**9 + 22068*a1**2*a2*a3**8*a4 + 64080*a1**2*a2*a3**7*a4**2 + 89808*a1**2*a2*a3**6*a4**3 + 84312*a1**2*a2*a3**5*a4**4 + 79128*a1**2*a2*a3**4*a4**5 + 65808*a1**2*a2*a3**3*a4**6 + 43920*a1**2*a2*a3**2*a4**7 + 22068*a1**2*a2*a3*a4**8 + 4692*a1**2*a2*a4**9 + 642*a1**2*a3**10 + 4692*a1**2*a3**9*a4 + 15066*a1**2*a3**8*a4**2 + 23472*a1**2*a3**7*a4**3 + 22308*a1**2*a3**6*a4**4 + 20664*a1**2*a3**5*a4**5 + 18852*a1**2*a3**4*a4**6 + 12336*a1**2*a3**3*a4**7 + 7002*a1**2*a3**2*a4**8 + 3348*a1**2*a3*a4**9 + 642*a1**2*a4**10 + 108*a1*a2**11 + 900*a1*a2**10*a3 + 900*a1*a2**10*a4 + 3348*a1*a2**9*a3**2 + 6696*a1*a2**9*a3*a4 + 3348*a1*a2**9*a4**2 + 4044*a1*a2**8*a3**3 + 22068*a1*a2**8*a3**2*a4 + 22068*a1*a2**8*a3*a4**2 + 8268*a1*a2**8*a4**3 - 2376*a1*a2**7*a3**4 + 29664*a1*a2**7*a3**3*a4 + 64080*a1*a2**7*a3**2*a4**2 + 43488*a1*a2**7*a3*a4**3 + 15672*a1*a2**7*a4**4 - 8472*a1*a2**6*a3**5 + 15816*a1*a2**6*a3**4*a4 + 89808*a1*a2**6*a3**3*a4**2 + 102864*a1*a2**6*a3**2*a4**3 + 59976*a1*a2**6*a3*a4**4 + 22632*a1*a2**6*a4**5 - 4824*a1*a2**5*a3**6 + 10224*a1*a2**5*a3**5*a4 + 84312*a1*a2**5*a3**4*a4**2 + 109344*a1*a2**5*a3**3*a4**3 + 108504*a1*a2**5*a3**2*a4**4 + 65520*a1*a2**5*a3*a4**5 + 23976*a1*a2**5*a4**6 + 1368*a1*a2**4*a3**7 + 19656*a1*a2**4*a3**6*a4 + 79128*a1*a2**4*a3**5*a4**2 + 76488*a1*a2**4*a3**4*a4**3 + 99144*a1*a2**4*a3**3*a4**4 + 96408*a1*a2**4*a3**2*a4**5 + 59976*a1*a2**4*a3*a4**6 + 18648*a1*a2**4*a4**7 + 2844*a1*a2**3*a3**8 + 20448*a1*a2**3*a3**7*a4 + 65808*a1*a2**3*a3**6*a4**2 + 67872*a1*a2**3*a3**5*a4**3 + 68904*a1*a2**3*a3**4*a4**4 + 93984*a1*a2**3*a3**3*a4**5 + 77328*a1*a2**3*a3**2*a4**6 + 43488*a1*a2**3*a3*a4**7 + 10908*a1*a2**3*a4**8 + 2004*a1*a2**2*a3**9 + 14004*a1*a2**2*a3**8*a4 + 43920*a1*a2**2*a3**7*a4**2 + 55248*a1*a2**2*a3**6*a4**3 + 41112*a1*a2**2*a3**5*a4**4 + 48024*a1*a2**2*a3**4*a4**5 + 56784*a1*a2**2*a3**3*a4**6 + 43920*a1*a2**2*a3**2*a4**7 + 22068*a1*a2**2*a3*a4**8 + 4692*a1*a2**2*a4**9 + 900*a1*a2*a3**10 + 6696*a1*a2*a3**9*a4 + 22068*a1*a2*a3**8*a4**2 + 29664*a1*a2*a3**7*a4**3 + 15816*a1*a2*a3**6*a4**4 + 10224*a1*a2*a3**5*a4**5 + 19656*a1*a2*a3**4*a4**6 + 20448*a1*a2*a3**3*a4**7 + 14004*a1*a2*a3**2*a4**8 + 6696*a1*a2*a3*a4**9 + 1284*a1*a2*a4**10 + 156*a1*a3**11 + 1284*a1*a3**10*a4 + 4692*a1*a3**9*a4**2 + 7500*a1*a3**8*a4**3 + 4824*a1*a3**7*a4**4 + 1896*a1*a3**6*a4**5 + 4200*a1*a3**5*a4**6 + 5592*a1*a3**4*a4**7 + 3660*a1*a3**3*a4**8 + 2004*a1*a3**2*a4**9 + 900*a1*a3*a4**10 + 156*a1*a4**11 + 17*a2**12 + 156*a2**11*a3 + 156*a2**11*a4 + 642*a2**10*a3**2 + 1284*a2**10*a3*a4 + 642*a2**10*a4**2 + 1020*a2**9*a3**3 + 4692*a2**9*a3**2*a4 + 4692*a2**9*a3*a4**2 + 1836*a2**9*a4**3 - 33*a2**8*a3**4 + 7500*a2**8*a3**3*a4 + 15066*a2**8*a3**2*a4**2 + 10908*a2**8*a3*a4**3 + 4191*a2**8*a4**4 - 1800*a2**7*a3**5 + 4824*a2**7*a3**4*a4 + 23472*a2**7*a3**3*a4**2 + 28272*a2**7*a3**2*a4**3 + 18648*a2**7*a3*a4**4 + 7224*a2**7*a4**5 - 1636*a2**6*a3**6 + 1896*a2**6*a3**5*a4 + 22308*a2**6*a3**4*a4**2 + 30192*a2**6*a3**3*a4**3 + 35364*a2**6*a3**2*a4**4 + 23976*a2**6*a3*a4**5 + 8732*a2**6*a4**6 + 24*a2**5*a3**7 + 4200*a2**5*a3**6*a4 + 20664*a2**5*a3**5*a4**2 + 10344*a2**5*a3**4*a4**3 + 24264*a2**5*a3**3*a4**4 + 32760*a2**5*a3**2*a4**5 + 22632*a2**5*a3*a4**6 + 7224*a2**5*a4**7 + 735*a2**4*a3**8 + 5592*a2**4*a3**7*a4 + 18852*a2**4*a3**6*a4**2 + 840*a2**4*a3**5*a4**3 - 1926*a2**4*a3**4*a4**4 + 24360*a2**4*a3**3*a4**5 + 24612*a2**4*a3**2*a4**6 + 15672*a2**4*a3*a4**7 + 4191*a2**4*a4**8 + 492*a2**3*a3**9 + 3660*a2**3*a3**8*a4 + 12336*a2**3*a3**7*a4**2 + 4656*a2**3*a3**6*a4**3 - 9432*a2**3*a3**5*a4**4 + 5352*a2**3*a3**4*a4**5 + 19056*a2**3*a3**3*a4**6 + 15216*a2**3*a3**2*a4**7 + 8268*a2**3*a3*a4**8 + 1836*a2**3*a4**9 + 258*a2**2*a3**10 + 2004*a2**2*a3**9*a4 + 7002*a2**2*a3**8*a4**2 + 6192*a2**2*a3**7*a4**3 - 6492*a2**2*a3**6*a4**4 - 10440*a2**2*a3**5*a4**5 + 804*a2**2*a3**4*a4**6 + 8112*a2**2*a3**3*a4**7 + 7002*a2**2*a3**2*a4**8 + 3348*a2**2*a3*a4**9 + 642*a2**2*a4**10 + 108*a2*a3**11 + 900*a2*a3**10*a4 + 3348*a2*a3**9*a4**2 + 4044*a2*a3**8*a4**3 - 2376*a2*a3**7*a4**4 - 8472*a2*a3**6*a4**5 - 4824*a2*a3**5*a4**6 + 1368*a2*a3**4*a4**7 + 2844*a2*a3**3*a4**8 + 2004*a2*a3**2*a4**9 + 900*a2*a3*a4**10 + 156*a2*a4**11 + 17*a3**12 + 156*a3**11*a4 + 642*a3**10*a4**2 + 1020*a3**9*a4**3 - 33*a3**8*a4**4 - 1800*a3**7*a4**5 - 1636*a3**6*a4**6 + 24*a3**5*a4**7 + 735*a3**4*a4**8 + 492*a3**3*a4**9 + 258*a3**2*a4**10 + 108*a3*a4**11 + 17*a4**12");
		SDSResult<MutableBigInteger> result = SDS.tsds(new BigPoly("abcd", f.toString()));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
	}

	@Test
	public void testHan13() {
		// http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545
		// ex 4.1
		Poly<MutableBigInteger> f = new BigPoly("xyz", "9*x**2 + 6*x*y - 6*x*z + y**2 - 2*y*z + z**2");
		// tsds works for 3e6 within 16 iterations (73801 polynomials in 13th iteration), 3e7 within 18 iteration; sds doesn't work
		SDSResult<MutableBigInteger> result = SDS.tsds(new BigPoly("xyz", "z**2").add(3_000_000, f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// ex 4.2
		// too slow in making permMat
		/*
		f = replaceAn("a1**2 + a2**2 + a3**2 + a4**2 + a5**2 + a6**2 + a7**2 + a8**2 + a9**2 + a10**2 - 4*a1*a2");
		result = SDS.sds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'a').compareTo(f.valueOf(0)) < 0);
		assertEquals(0, result.getDepth());
		*/
		// ex 4.3
		f = new BigPoly("xyz", "x**3 + y**3 + z**3 - 3*x*y*z");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
		// ex 4.4
		f = new BigPoly("abc", "a**4 - 3*a**3*b + 2*a**2*b**2 + 2*a**2*c**2 - 3*a*c**3 + b**4 - 3*b**3*c + 2*b**2*c**2 + c**4");
		// zero at (1, 1, 1)
		assertTrue(subs(f, Arrays.asList(f.valueOf(1), f.valueOf(1), f.valueOf(1)), 'a').equals(f.valueOf(0)));
		// tsds doesn't work (46455 polynomials in 50th iteration)
		// result = SDS.tsds(f);
		// sds works for 1e9 but doesn't seem to work for 1e10
		result = SDS.sds(new BigPoly("abc", "a**4 + b**4 + c**4").add(new BigPoly().add(f.valueOf(1_000_000_000), f)));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(14, result.getDepth());
		// 1e22
		f = new BigPoly().add(f.valueOf("10000000000000000000000"), f);
		// tsds works within 32 iterations
		result = SDS.tsds(new BigPoly("abc", "a**4 + b**4 + c**4").add(f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(32, result.getDepth());
		// both sds and tsds find negative without iteration
		result = SDS.sds(new BigPoly("abc", "-a**4 - b**4 - c**4").add(f));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// ex 4.5
		// result from han13-ex5.py
		// g1, sds needs 4 iterations
		f = new BigPoly("pqrst", "11*p**2*q**6 + 44*p**2*q**5*r + 22*p**2*q**5*s + 66*p**2*q**5*t + 66*p**2*q**4*r**2 + 66*p**2*q**4*r*s + 220*p**2*q**4*r*t + 11*p**2*q**4*s**2 + 110*p**2*q**4*s*t + 192*p**2*q**4*t**2 + 44*p**2*q**3*r**3 + 66*p**2*q**3*r**2*s + 264*p**2*q**3*r**2*t + 22*p**2*q**3*r*s**2 + 264*p**2*q**3*r*s*t + 512*p**2*q**3*r*t**2 + 44*p**2*q**3*s**2*t + 256*p**2*q**3*s*t**2 + 328*p**2*q**3*t**3 + 11*p**2*q**2*r**4 + 22*p**2*q**2*r**3*s + 132*p**2*q**2*r**3*t + 11*p**2*q**2*r**2*s**2 + 198*p**2*q**2*r**2*s*t + 468*p**2*q**2*r**2*t**2 + 66*p**2*q**2*r*s**2*t + 468*p**2*q**2*r*s*t**2 + 656*p**2*q**2*r*t**3 + 84*p**2*q**2*s**2*t**2 + 328*p**2*q**2*s*t**3 + 336*p**2*q**2*t**4 + 22*p**2*q*r**4*t + 44*p**2*q*r**3*s*t + 168*p**2*q*r**3*t**2 + 22*p**2*q*r**2*s**2*t + 252*p**2*q*r**2*s*t**2 + 408*p**2*q*r**2*t**3 + 84*p**2*q*r*s**2*t**2 + 408*p**2*q*r*s*t**3 + 448*p**2*q*r*t**4 + 80*p**2*q*s**2*t**3 + 224*p**2*q*s*t**4 + 192*p**2*q*t**5 + 20*p**2*r**4*t**2 + 40*p**2*r**3*s*t**2 + 80*p**2*r**3*t**3 + 20*p**2*r**2*s**2*t**2 + 120*p**2*r**2*s*t**3 + 144*p**2*r**2*t**4 + 40*p**2*r*s**2*t**3 + 144*p**2*r*s*t**4 + 128*p**2*r*t**5 + 32*p**2*s**2*t**4 + 64*p**2*s*t**5 + 48*p**2*t**6 + 22*p*q**6*t + 88*p*q**5*r*t + 44*p*q**5*s*t + 36*p*q**5*t**2 + 132*p*q**4*r**2*t + 132*p*q**4*r*s*t + 120*p*q**4*r*t**2 + 22*p*q**4*s**2*t + 60*p*q**4*s*t**2 - 96*p*q**4*t**3 + 88*p*q**3*r**3*t + 132*p*q**3*r**2*s*t + 144*p*q**3*r**2*t**2 + 44*p*q**3*r*s**2*t + 144*p*q**3*r*s*t**2 - 256*p*q**3*r*t**3 + 24*p*q**3*s**2*t**2 - 128*p*q**3*s*t**3 - 304*p*q**3*t**4 + 22*p*q**2*r**4*t + 44*p*q**2*r**3*s*t + 72*p*q**2*r**3*t**2 + 22*p*q**2*r**2*s**2*t + 108*p*q**2*r**2*s*t**2 - 216*p*q**2*r**2*t**3 + 36*p*q**2*r*s**2*t**2 - 216*p*q**2*r*s*t**3 - 608*p*q**2*r*t**4 - 24*p*q**2*s**2*t**3 - 304*p*q**2*s*t**4 - 288*p*q**2*t**5 + 12*p*q*r**4*t**2 + 24*p*q*r**3*s*t**2 - 48*p*q*r**3*t**3 + 12*p*q*r**2*s**2*t**2 - 72*p*q*r**2*s*t**3 - 336*p*q*r**2*t**4 - 24*p*q*r*s**2*t**3 - 336*p*q*r*s*t**4 - 384*p*q*r*t**5 - 32*p*q*s**2*t**4 - 192*p*q*s*t**5 - 96*p*q*t**6 + 8*p*r**4*t**3 + 16*p*r**3*s*t**3 - 32*p*r**3*t**4 + 8*p*r**2*s**2*t**3 - 48*p*r**2*s*t**4 - 96*p*r**2*t**5 - 16*p*r*s**2*t**4 - 96*p*r*s*t**5 - 64*p*r*t**6 - 32*p*s*t**6 + 92*q**6*t**2 + 368*q**5*r*t**2 + 184*q**5*s*t**2 + 456*q**5*t**3 + 552*q**4*r**2*t**2 + 552*q**4*r*s*t**2 + 1520*q**4*r*t**3 + 92*q**4*s**2*t**2 + 760*q**4*s*t**3 + 864*q**4*t**4 + 368*q**3*r**3*t**2 + 552*q**3*r**2*s*t**2 + 1824*q**3*r**2*t**3 + 184*q**3*r*s**2*t**2 + 1824*q**3*r*s*t**3 + 2304*q**3*r*t**4 + 304*q**3*s**2*t**3 + 1152*q**3*s*t**4 + 736*q**3*t**5 + 92*q**2*r**4*t**2 + 184*q**2*r**3*s*t**2 + 912*q**2*r**3*t**3 + 92*q**2*r**2*s**2*t**2 + 1368*q**2*r**2*s*t**3 + 2096*q**2*r**2*t**4 + 456*q**2*r*s**2*t**3 + 2096*q**2*r*s*t**4 + 1472*q**2*r*t**5 + 368*q**2*s**2*t**4 + 736*q**2*s*t**5 + 240*q**2*t**6 + 152*q*r**4*t**3 + 304*q*r**3*s*t**3 + 736*q*r**3*t**4 + 152*q*r**2*s**2*t**3 + 1104*q*r**2*s*t**4 + 928*q*r**2*t**5 + 368*q*r*s**2*t**4 + 928*q*r*s*t**5 + 320*q*r*t**6 + 192*q*s**2*t**5 + 160*q*s*t**6 + 80*r**4*t**4 + 160*r**3*s*t**4 + 192*r**3*t**5 + 80*r**2*s**2*t**4 + 288*r**2*s*t**5 + 128*r**2*t**6 + 96*r*s**2*t**5 + 128*r*s*t**6 + 48*s**2*t**6");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals(2, result.getDepth());
		// g2, sds can use LongPoly
		f = new BigPoly("pqrst", "9*p**4*r**4 + 18*p**4*r**3*s + 36*p**4*r**3*t + 9*p**4*r**2*s**2 + 54*p**4*r**2*s*t + 60*p**4*r**2*t**2 + 18*p**4*r*s**2*t + 60*p**4*r*s*t**2 + 48*p**4*r*t**3 + 12*p**4*s**2*t**2 + 24*p**4*s*t**3 + 16*p**4*t**4 + 18*p**3*q*r**4 + 36*p**3*q*r**3*s + 72*p**3*q*r**3*t + 18*p**3*q*r**2*s**2 + 108*p**3*q*r**2*s*t + 120*p**3*q*r**2*t**2 + 36*p**3*q*r*s**2*t + 120*p**3*q*r*s*t**2 + 96*p**3*q*r*t**3 + 24*p**3*q*s**2*t**2 + 48*p**3*q*s*t**3 + 32*p**3*q*t**4 + 36*p**3*r**4*t + 72*p**3*r**3*s*t + 144*p**3*r**3*t**2 + 36*p**3*r**2*s**2*t + 216*p**3*r**2*s*t**2 + 240*p**3*r**2*t**3 + 72*p**3*r*s**2*t**2 + 240*p**3*r*s*t**3 + 192*p**3*r*t**4 + 48*p**3*s**2*t**3 + 96*p**3*s*t**4 + 64*p**3*t**5 + 9*p**2*q**2*r**4 + 18*p**2*q**2*r**3*s + 36*p**2*q**2*r**3*t + 9*p**2*q**2*r**2*s**2 + 54*p**2*q**2*r**2*s*t + 60*p**2*q**2*r**2*t**2 + 18*p**2*q**2*r*s**2*t + 60*p**2*q**2*r*s*t**2 + 48*p**2*q**2*r*t**3 + 12*p**2*q**2*s**2*t**2 + 24*p**2*q**2*s*t**3 + 16*p**2*q**2*t**4 + 54*p**2*q*r**4*t + 108*p**2*q*r**3*s*t + 216*p**2*q*r**3*t**2 + 54*p**2*q*r**2*s**2*t + 324*p**2*q*r**2*s*t**2 + 360*p**2*q*r**2*t**3 + 108*p**2*q*r*s**2*t**2 + 360*p**2*q*r*s*t**3 + 288*p**2*q*r*t**4 + 72*p**2*q*s**2*t**3 + 144*p**2*q*s*t**4 + 96*p**2*q*t**5 + 44*p**2*r**4*t**2 + 88*p**2*r**3*s*t**2 + 176*p**2*r**3*t**3 + 44*p**2*r**2*s**2*t**2 + 264*p**2*r**2*s*t**3 + 336*p**2*r**2*t**4 + 88*p**2*r*s**2*t**3 + 336*p**2*r*s*t**4 + 320*p**2*r*t**5 + 80*p**2*s**2*t**4 + 160*p**2*s*t**5 + 128*p**2*t**6 + 18*p*q**2*r**4*t + 36*p*q**2*r**3*s*t + 72*p*q**2*r**3*t**2 + 18*p*q**2*r**2*s**2*t + 108*p*q**2*r**2*s*t**2 + 120*p*q**2*r**2*t**3 + 36*p*q**2*r*s**2*t**2 + 120*p*q**2*r*s*t**3 + 96*p*q**2*r*t**4 + 24*p*q**2*s**2*t**3 + 48*p*q**2*s*t**4 + 32*p*q**2*t**5 + 44*p*q*r**4*t**2 + 88*p*q*r**3*s*t**2 + 176*p*q*r**3*t**3 + 44*p*q*r**2*s**2*t**2 + 264*p*q*r**2*s*t**3 + 336*p*q*r**2*t**4 + 88*p*q*r*s**2*t**3 + 336*p*q*r*s*t**4 + 320*p*q*r*t**5 + 80*p*q*s**2*t**4 + 160*p*q*s*t**5 + 128*p*q*t**6 + 16*p*r**4*t**3 + 32*p*r**3*s*t**3 - 64*p*r**3*t**4 + 16*p*r**2*s**2*t**3 - 96*p*r**2*s*t**4 - 192*p*r**2*t**5 - 32*p*r*s**2*t**4 - 192*p*r*s*t**5 - 128*p*r*t**6 - 64*p*s*t**6 + 20*q**2*r**4*t**2 + 40*q**2*r**3*s*t**2 + 80*q**2*r**3*t**3 + 20*q**2*r**2*s**2*t**2 + 120*q**2*r**2*s*t**3 + 144*q**2*r**2*t**4 + 40*q**2*r*s**2*t**3 + 144*q**2*r*s*t**4 + 128*q**2*r*t**5 + 32*q**2*s**2*t**4 + 64*q**2*s*t**5 + 48*q**2*t**6 + 8*q*r**4*t**3 + 16*q*r**3*s*t**3 - 32*q*r**3*t**4 + 8*q*r**2*s**2*t**3 - 48*q*r**2*s*t**4 - 96*q*r**2*t**5 - 16*q*r*s**2*t**4 - 96*q*r*s*t**5 - 64*q*r*t**6 - 32*q*s*t**6 + 80*r**4*t**4 + 160*r**3*s*t**4 + 192*r**3*t**5 + 80*r**2*s**2*t**4 + 288*r**2*s*t**5 + 128*r**2*t**6 + 96*r*s**2*t**5 + 128*r*s*t**6 + 48*s**2*t**6");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals(1, result.getDepth());
		// g3, sds needs 4 iterations
		f = new BigPoly("pqrst", "3*p**6*s**2 + 6*p**6*s*t + 4*p**6*t**2 + 12*p**5*q*s**2 + 24*p**5*q*s*t + 16*p**5*q*t**2 + 6*p**5*r*s**2 + 12*p**5*r*s*t + 8*p**5*r*t**2 + 18*p**5*s**2*t + 36*p**5*s*t**2 + 24*p**5*t**3 + 18*p**4*q**2*s**2 + 36*p**4*q**2*s*t + 24*p**4*q**2*t**2 + 18*p**4*q*r*s**2 + 36*p**4*q*r*s*t + 24*p**4*q*r*t**2 + 60*p**4*q*s**2*t + 120*p**4*q*s*t**2 + 80*p**4*q*t**3 + 3*p**4*r**2*s**2 + 6*p**4*r**2*s*t + 4*p**4*r**2*t**2 + 30*p**4*r*s**2*t + 60*p**4*r*s*t**2 + 40*p**4*r*t**3 + 72*p**4*s**2*t**2 + 144*p**4*s*t**3 + 96*p**4*t**4 + 12*p**3*q**3*s**2 + 24*p**3*q**3*s*t + 16*p**3*q**3*t**2 + 18*p**3*q**2*r*s**2 + 36*p**3*q**2*r*s*t + 24*p**3*q**2*r*t**2 + 72*p**3*q**2*s**2*t + 144*p**3*q**2*s*t**2 + 96*p**3*q**2*t**3 + 6*p**3*q*r**2*s**2 + 12*p**3*q*r**2*s*t + 8*p**3*q*r**2*t**2 + 72*p**3*q*r*s**2*t + 144*p**3*q*r*s*t**2 + 96*p**3*q*r*t**3 + 192*p**3*q*s**2*t**2 + 384*p**3*q*s*t**3 + 256*p**3*q*t**4 + 12*p**3*r**2*s**2*t + 24*p**3*r**2*s*t**2 + 16*p**3*r**2*t**3 + 96*p**3*r*s**2*t**2 + 192*p**3*r*s*t**3 + 128*p**3*r*t**4 + 168*p**3*s**2*t**3 + 336*p**3*s*t**4 + 224*p**3*t**5 + 3*p**2*q**4*s**2 + 6*p**2*q**4*s*t + 4*p**2*q**4*t**2 + 6*p**2*q**3*r*s**2 + 12*p**2*q**3*r*s*t + 8*p**2*q**3*r*t**2 + 36*p**2*q**3*s**2*t + 72*p**2*q**3*s*t**2 + 48*p**2*q**3*t**3 + 3*p**2*q**2*r**2*s**2 + 6*p**2*q**2*r**2*s*t + 4*p**2*q**2*r**2*t**2 + 54*p**2*q**2*r*s**2*t + 108*p**2*q**2*r*s*t**2 + 72*p**2*q**2*r*t**3 + 180*p**2*q**2*s**2*t**2 + 360*p**2*q**2*s*t**3 + 240*p**2*q**2*t**4 + 18*p**2*q*r**2*s**2*t + 36*p**2*q*r**2*s*t**2 + 24*p**2*q*r**2*t**3 + 180*p**2*q*r*s**2*t**2 + 360*p**2*q*r*s*t**3 + 240*p**2*q*r*t**4 + 336*p**2*q*s**2*t**3 + 672*p**2*q*s*t**4 + 448*p**2*q*t**5 + 36*p**2*r**2*s**2*t**2 + 72*p**2*r**2*s*t**3 + 48*p**2*r**2*t**4 + 168*p**2*r*s**2*t**3 + 336*p**2*r*s*t**4 + 224*p**2*r*t**5 + 144*p**2*s**2*t**4 + 288*p**2*s*t**5 + 240*p**2*t**6 + 6*p*q**4*s**2*t + 12*p*q**4*s*t**2 + 8*p*q**4*t**3 + 12*p*q**3*r*s**2*t + 24*p*q**3*r*s*t**2 + 16*p*q**3*r*t**3 + 72*p*q**3*s**2*t**2 + 144*p*q**3*s*t**3 + 96*p*q**3*t**4 + 6*p*q**2*r**2*s**2*t + 12*p*q**2*r**2*s*t**2 + 8*p*q**2*r**2*t**3 + 108*p*q**2*r*s**2*t**2 + 216*p*q**2*r*s*t**3 + 144*p*q**2*r*t**4 + 216*p*q**2*s**2*t**3 + 432*p*q**2*s*t**4 + 288*p*q**2*t**5 + 36*p*q*r**2*s**2*t**2 + 72*p*q*r**2*s*t**3 + 48*p*q*r**2*t**4 + 216*p*q*r*s**2*t**3 + 432*p*q*r*s*t**4 + 288*p*q*r*t**5 + 192*p*q*s**2*t**4 + 384*p*q*s*t**5 + 320*p*q*t**6 + 48*p*r**2*s**2*t**3 + 96*p*r**2*s*t**4 + 64*p*r**2*t**5 + 96*p*r*s**2*t**4 + 192*p*r*s*t**5 + 160*p*r*t**6 - 96*p*s*t**6 + 12*q**4*s**2*t**2 + 24*q**4*s*t**3 + 16*q**4*t**4 + 24*q**3*r*s**2*t**2 + 48*q**3*r*s*t**3 + 32*q**3*r*t**4 + 48*q**3*s**2*t**3 + 96*q**3*s*t**4 + 64*q**3*t**5 + 12*q**2*r**2*s**2*t**2 + 24*q**2*r**2*s*t**3 + 16*q**2*r**2*t**4 + 72*q**2*r*s**2*t**3 + 144*q**2*r*s*t**4 + 96*q**2*r*t**5 + 80*q**2*s**2*t**4 + 160*q**2*s*t**5 + 128*q**2*t**6 + 24*q*r**2*s**2*t**3 + 48*q*r**2*s*t**4 + 32*q*r**2*t**5 + 80*q*r*s**2*t**4 + 160*q*r*s*t**5 + 128*q*r*t**6 - 64*q*s*t**6 + 32*r**2*s**2*t**4 + 64*r**2*s*t**5 + 48*r**2*t**6 - 32*r*s*t**6 + 48*s**2*t**6");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals(2, result.getDepth());
	}

	@Test
	public void testHan14() {
		// ISBN 9787560349800, p301, ex 12.9
		// f2 from han14-p301.py
		BigPoly f = new BigPoly("abc", "81*a**6*b**2 + 162*a**6*b*c + 81*a**6*c**2 - 412*a**5*b**3 + 1100*a**5*b**2*c + 2124*a**5*b*c**2 + 612*a**5*c**3 + 294*a**4*b**4 + 4314*a**4*b**3*c + 9320*a**4*b**2*c**2 + 5338*a**4*b*c**3 + 294*a**4*c**4 + 612*a**3*b**5 + 5338*a**3*b**4*c + 16090*a**3*b**3*c**2 + 16090*a**3*b**2*c**3 + 4314*a**3*b*c**4 - 412*a**3*c**5 + 81*a**2*b**6 + 2124*a**2*b**5*c + 9320*a**2*b**4*c**2 + 16090*a**2*b**3*c**3 + 9320*a**2*b**2*c**4 + 1100*a**2*b*c**5 + 81*a**2*c**6 + 162*a*b**6*c + 1100*a*b**5*c**2 + 4314*a*b**4*c**3 + 5338*a*b**3*c**4 + 2124*a*b**2*c**5 + 162*a*b*c**6 + 81*b**6*c**2 - 412*b**5*c**3 + 294*b**4*c**4 + 612*b**3*c**5 + 81*b**2*c**6");
		SDSResult<MutableBigInteger> result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		String zeroAt = "[[0, 0, 1], [0, 1, 0], [0, 3, 1], [1, 0, 0], [1, 0, 3], [3, 1, 0]]";
		assertEquals(zeroAt, result.getZeroAt().toString());
		assertEquals(3, result.getDepth());
		// f3 from han14-p301.py
		f = new BigPoly("abc", "6561*a**12*b**4 + 26244*a**12*b**3*c + 39366*a**12*b**2*c**2 + 26244*a**12*b*c**3 + 6561*a**12*c**4 - 66744*a**11*b**5 + 44712*a**11*b**4*c + 633744*a**11*b**3*c**2 + 965520*a**11*b**2*c**3 + 542376*a**11*b*c**4 + 99144*a**11*c**5 + 217372*a**10*b**6 - 112276*a**10*b**5*c + 2415028*a**10*b**4*c**2 + 8751816*a**10*b**3*c**3 + 9144756*a**10*b**2*c**4 + 3559788*a**10*b*c**5 + 422172*a**10*c**6 - 143112*a**9*b**7 - 1844892*a**9*b**6*c + 941668*a**9*b**5*c**2 + 23814912*a**9*b**4*c**3 + 45230848*a**9*b**3*c**4 + 32114276*a**9*b**2*c**5 + 8348004*a**9*b*c**6 + 293112*a**9*c**7 - 404730*a**8*b**8 - 145148*a**8*b**7*c + 1172710*a**8*b**6*c**2 + 30229204*a**8*b**5*c**3 + 90765272*a**8*b**4*c**4 + 100858580*a**8*b**3*c**5 + 46752998*a**8*b**2*c**6 + 6873348*a**8*b*c**7 - 404730*a**8*c**8 + 293112*a**7*b**9 + 6873348*a**7*b**8*c + 25171160*a**7*b**7*c**2 + 55499920*a**7*b**6*c**3 + 118778844*a**7*b**5*c**4 + 161741788*a**7*b**4*c**5 + 105045136*a**7*b**3*c**6 + 25171160*a**7*b**2*c**7 - 145148*a**7*b*c**8 - 143112*a**7*c**9 + 422172*a**6*b**10 + 8348004*a**6*b**9*c + 46752998*a**6*b**8*c**2 + 105045136*a**6*b**7*c**3 + 157443246*a**6*b**6*c**4 + 196665720*a**6*b**5*c**5 + 157443246*a**6*b**4*c**6 + 55499920*a**6*b**3*c**7 + 1172710*a**6*b**2*c**8 - 1844892*a**6*b*c**9 + 217372*a**6*c**10 + 99144*a**5*b**11 + 3559788*a**5*b**10*c + 32114276*a**5*b**9*c**2 + 100858580*a**5*b**8*c**3 + 161741788*a**5*b**7*c**4 + 196665720*a**5*b**6*c**5 + 196665720*a**5*b**5*c**6 + 118778844*a**5*b**4*c**7 + 30229204*a**5*b**3*c**8 + 941668*a**5*b**2*c**9 - 112276*a**5*b*c**10 - 66744*a**5*c**11 + 6561*a**4*b**12 + 542376*a**4*b**11*c + 9144756*a**4*b**10*c**2 + 45230848*a**4*b**9*c**3 + 90765272*a**4*b**8*c**4 + 118778844*a**4*b**7*c**5 + 157443246*a**4*b**6*c**6 + 161741788*a**4*b**5*c**7 + 90765272*a**4*b**4*c**8 + 23814912*a**4*b**3*c**9 + 2415028*a**4*b**2*c**10 + 44712*a**4*b*c**11 + 6561*a**4*c**12 + 26244*a**3*b**12*c + 965520*a**3*b**11*c**2 + 8751816*a**3*b**10*c**3 + 23814912*a**3*b**9*c**4 + 30229204*a**3*b**8*c**5 + 55499920*a**3*b**7*c**6 + 105045136*a**3*b**6*c**7 + 100858580*a**3*b**5*c**8 + 45230848*a**3*b**4*c**9 + 8751816*a**3*b**3*c**10 + 633744*a**3*b**2*c**11 + 26244*a**3*b*c**12 + 39366*a**2*b**12*c**2 + 633744*a**2*b**11*c**3 + 2415028*a**2*b**10*c**4 + 941668*a**2*b**9*c**5 + 1172710*a**2*b**8*c**6 + 25171160*a**2*b**7*c**7 + 46752998*a**2*b**6*c**8 + 32114276*a**2*b**5*c**9 + 9144756*a**2*b**4*c**10 + 965520*a**2*b**3*c**11 + 39366*a**2*b**2*c**12 + 26244*a*b**12*c**3 + 44712*a*b**11*c**4 - 112276*a*b**10*c**5 - 1844892*a*b**9*c**6 - 145148*a*b**8*c**7 + 6873348*a*b**7*c**8 + 8348004*a*b**6*c**9 + 3559788*a*b**5*c**10 + 542376*a*b**4*c**11 + 26244*a*b**3*c**12 + 6561*b**12*c**4 - 66744*b**11*c**5 + 217372*b**10*c**6 - 143112*b**9*c**7 - 404730*b**8*c**8 + 293112*b**7*c**9 + 422172*b**6*c**10 + 99144*b**5*c**11 + 6561*b**4*c**12");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals(zeroAt, result.getZeroAt().toString());
		assertEquals(3, result.getDepth());

		// f3 from han14-p301.py, p302
		f = new BigPoly("uvw", "u**16 + 100*u**15*v + 84*u**15*w + 1570*u**14*v**2 + 2252*u**14*v*w + 746*u**14*w**2 + 11092*u**13*v**3 + 24064*u**13*v**2*w + 15336*u**13*v*w**2 + 2412*u**13*w**3 + 44619*u**12*v**4 + 134508*u**12*v**3*w + 133150*u**12*v**2*w**2 + 45604*u**12*v*w**3 + 1955*u**12*w**4 + 112268*u**11*v**5 + 443976*u**11*v**4*w + 614400*u**11*v**3*w**2 + 343744*u**11*v**2*w**3 + 55192*u**11*v*w**4 - 5876*u**11*w**5 + 182940*u**10*v**6 + 914032*u**10*v**5*w + 1651578*u**10*v**4*w**2 + 1301492*u**10*v**3*w**3 + 389122*u**10*v**2*w**4 - 1552*u**10*v*w**5 - 8708*u**10*w**6 + 191208*u**9*v**7 + 1183380*u**9*v**6*w + 2655284*u**9*v**5*w**2 + 2636292*u**9*v**4*w**3 + 1042044*u**9*v**3*w**4 + 49100*u**9*v**2*w**5 + 10564*u**9*v*w**6 + 30248*u**9*w**7 + 118413*u**8*v**8 + 917972*u**8*v**7*w + 2444248*u**8*v**6*w**2 + 2615728*u**8*v**5*w**3 + 605604*u**8*v**4*w**4 - 614856*u**8*v**3*w**5 - 16976*u**8*v**2*w**6 + 352132*u**8*v*w**7 + 118413*u**8*w**8 + 30248*u**7*v**9 + 352132*u**7*v**8*w + 1034596*u**7*v**7*w**2 + 419556*u**7*v**6*w**3 - 2502520*u**7*v**5*w**4 - 3924376*u**7*v**4*w**5 - 1407260*u**7*v**3*w**6 + 1034596*u**7*v**2*w**7 + 917972*u**7*v*w**8 + 191208*u**7*w**9 - 8708*u**6*v**10 + 10564*u**6*v**9*w - 16976*u**6*v**8*w**2 - 1407260*u**6*v**7*w**3 - 5548262*u**6*v**6*w**4 - 8702220*u**6*v**5*w**5 - 5548262*u**6*v**4*w**6 + 419556*u**6*v**3*w**7 + 2444248*u**6*v**2*w**8 + 1183380*u**6*v*w**9 + 182940*u**6*w**10 - 5876*u**5*v**11 - 1552*u**5*v**10*w + 49100*u**5*v**9*w**2 - 614856*u**5*v**8*w**3 - 3924376*u**5*v**7*w**4 - 8702220*u**5*v**6*w**5 - 8702220*u**5*v**5*w**6 - 2502520*u**5*v**4*w**7 + 2615728*u**5*v**3*w**8 + 2655284*u**5*v**2*w**9 + 914032*u**5*v*w**10 + 112268*u**5*w**11 + 1955*u**4*v**12 + 55192*u**4*v**11*w + 389122*u**4*v**10*w**2 + 1042044*u**4*v**9*w**3 + 605604*u**4*v**8*w**4 - 2502520*u**4*v**7*w**5 - 5548262*u**4*v**6*w**6 - 3924376*u**4*v**5*w**7 + 605604*u**4*v**4*w**8 + 2636292*u**4*v**3*w**9 + 1651578*u**4*v**2*w**10 + 443976*u**4*v*w**11 + 44619*u**4*w**12 + 2412*u**3*v**13 + 45604*u**3*v**12*w + 343744*u**3*v**11*w**2 + 1301492*u**3*v**10*w**3 + 2636292*u**3*v**9*w**4 + 2615728*u**3*v**8*w**5 + 419556*u**3*v**7*w**6 - 1407260*u**3*v**6*w**7 - 614856*u**3*v**5*w**8 + 1042044*u**3*v**4*w**9 + 1301492*u**3*v**3*w**10 + 614400*u**3*v**2*w**11 + 134508*u**3*v*w**12 + 11092*u**3*w**13 + 746*u**2*v**14 + 15336*u**2*v**13*w + 133150*u**2*v**12*w**2 + 614400*u**2*v**11*w**3 + 1651578*u**2*v**10*w**4 + 2655284*u**2*v**9*w**5 + 2444248*u**2*v**8*w**6 + 1034596*u**2*v**7*w**7 - 16976*u**2*v**6*w**8 + 49100*u**2*v**5*w**9 + 389122*u**2*v**4*w**10 + 343744*u**2*v**3*w**11 + 133150*u**2*v**2*w**12 + 24064*u**2*v*w**13 + 1570*u**2*w**14 + 84*u*v**15 + 2252*u*v**14*w + 24064*u*v**13*w**2 + 134508*u*v**12*w**3 + 443976*u*v**11*w**4 + 914032*u*v**10*w**5 + 1183380*u*v**9*w**6 + 917972*u*v**8*w**7 + 352132*u*v**7*w**8 + 10564*u*v**6*w**9 - 1552*u*v**5*w**10 + 55192*u*v**4*w**11 + 45604*u*v**3*w**12 + 15336*u*v**2*w**13 + 2252*u*v*w**14 + 100*u*w**15 + v**16 + 100*v**15*w + 1570*v**14*w**2 + 11092*v**13*w**3 + 44619*v**12*w**4 + 112268*v**11*w**5 + 182940*v**10*w**6 + 191208*v**9*w**7 + 118413*v**8*w**8 + 30248*v**7*w**9 - 8708*v**6*w**10 - 5876*v**5*w**11 + 1955*v**4*w**12 + 2412*v**3*w**13 + 746*v**2*w**14 + 84*v*w**15 + w**16");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());

		// ISBN 9787312056185, p341, ex 11.7
		// fn from han23-p341u.py
		/*
		LongPoly fn = new LongPoly("abcuvw", "a**5*b*u**2*v**2*w**2 + a**5*b*u**2*v*w**3 + a**5*b*u*v**2*w**3 + a**5*b*u*v*w**4 + a**5*c*u**2*v**2*w**2 + a**5*c*u**2*v*w**3 + a**5*c*u*v**2*w**3 + a**5*c*u*v*w**4 + a**4*b**2*u**3*v**2*w + a**4*b**2*u**3*v*w**2 + a**4*b**2*u**2*v**3*w + 2*a**4*b**2*u**2*v**2*w**2 + a**4*b**2*u**2*v*w**3 + a**4*b**2*u*v**3*w**2 + a**4*b**2*u*v**2*w**3 - 9*a**4*b**2*u*v*w**4 + a**4*b*c*u**3*v**2*w + a**4*b*c*u**3*v*w**2 + a**4*b*c*u**2*v**3*w + 3*a**4*b*c*u**2*v**2*w**2 - 6*a**4*b*c*u**2*v*w**3 + a**4*b*c*u**2*w**4 + a**4*b*c*u*v**3*w**2 - 6*a**4*b*c*u*v**2*w**3 + 3*a**4*b*c*u*v*w**4 + a**4*b*c*u*w**5 + a**4*b*c*v**2*w**4 + a**4*b*c*v*w**5 - 9*a**4*c**2*u**2*v**2*w**2 + a**4*c**2*u**2*v*w**3 + a**4*c**2*u**2*w**4 + a**4*c**2*u*v**2*w**3 + 2*a**4*c**2*u*v*w**4 + a**4*c**2*u*w**5 + a**4*c**2*v**2*w**4 + a**4*c**2*v*w**5 + a**3*b**3*u**3*v**3 + a**3*b**3*u**3*v**2*w + a**3*b**3*u**2*v**3*w + 2*a**3*b**3*u**2*v**2*w**2 - 8*a**3*b**3*u**2*v*w**3 - 8*a**3*b**3*u*v**2*w**3 + 2*a**3*b**3*u*v*w**4 + a**3*b**3*u*w**5 + a**3*b**3*v*w**5 + a**3*b**3*w**6 + a**3*b**2*c*u**3*v**3 + 3*a**3*b**2*c*u**3*v**2*w - 6*a**3*b**2*c*u**3*v*w**2 + a**3*b**2*c*u**3*w**3 + 3*a**3*b**2*c*u**2*v**3*w - 10*a**3*b**2*c*u**2*v**2*w**2 + 7*a**3*b**2*c*u**2*v*w**3 + 2*a**3*b**2*c*u**2*w**4 - 6*a**3*b**2*c*u*v**3*w**2 + 7*a**3*b**2*c*u*v**2*w**3 + 6*a**3*b**2*c*u*v*w**4 - 7*a**3*b**2*c*u*w**5 + a**3*b**2*c*v**3*w**3 + 2*a**3*b**2*c*v**2*w**4 - 7*a**3*b**2*c*v*w**5 + a**3*b**2*c*w**6 + a**3*b*c**2*u**3*v**3 - 7*a**3*b*c**2*u**3*v**2*w + 2*a**3*b*c**2*u**3*v*w**2 + a**3*b*c**2*u**3*w**3 - 7*a**3*b*c**2*u**2*v**3*w + 6*a**3*b*c**2*u**2*v**2*w**2 + 7*a**3*b*c**2*u**2*v*w**3 - 6*a**3*b*c**2*u**2*w**4 + 2*a**3*b*c**2*u*v**3*w**2 + 7*a**3*b*c**2*u*v**2*w**3 - 10*a**3*b*c**2*u*v*w**4 + 3*a**3*b*c**2*u*w**5 + a**3*b*c**2*v**3*w**3 - 6*a**3*b*c**2*v**2*w**4 + 3*a**3*b*c**2*v*w**5 + a**3*b*c**2*w**6 + a**3*c**3*u**3*v**3 + a**3*c**3*u**3*v**2*w + a**3*c**3*u**2*v**3*w + 2*a**3*c**3*u**2*v**2*w**2 - 8*a**3*c**3*u**2*v*w**3 - 8*a**3*c**3*u*v**2*w**3 + 2*a**3*c**3*u*v*w**4 + a**3*c**3*u*w**5 + a**3*c**3*v*w**5 + a**3*c**3*w**6 - 9*a**2*b**4*u**2*v**2*w**2 + a**2*b**4*u**2*v*w**3 + a**2*b**4*u**2*w**4 + a**2*b**4*u*v**2*w**3 + 2*a**2*b**4*u*v*w**4 + a**2*b**4*u*w**5 + a**2*b**4*v**2*w**4 + a**2*b**4*v*w**5 + a**2*b**3*c*u**3*v**3 - 7*a**2*b**3*c*u**3*v**2*w + 2*a**2*b**3*c*u**3*v*w**2 + a**2*b**3*c*u**3*w**3 - 7*a**2*b**3*c*u**2*v**3*w + 6*a**2*b**3*c*u**2*v**2*w**2 + 7*a**2*b**3*c*u**2*v*w**3 - 6*a**2*b**3*c*u**2*w**4 + 2*a**2*b**3*c*u*v**3*w**2 + 7*a**2*b**3*c*u*v**2*w**3 - 10*a**2*b**3*c*u*v*w**4 + 3*a**2*b**3*c*u*w**5 + a**2*b**3*c*v**3*w**3 - 6*a**2*b**3*c*v**2*w**4 + 3*a**2*b**3*c*v*w**5 + a**2*b**3*c*w**6 - 9*a**2*b**2*c**2*u**3*v**3 + 3*a**2*b**2*c**2*u**3*v**2*w + 6*a**2*b**2*c**2*u**3*v*w**2 - 6*a**2*b**2*c**2*u**3*w**3 + 3*a**2*b**2*c**2*u**2*v**3*w + 12*a**2*b**2*c**2*u**2*v**2*w**2 - 12*a**2*b**2*c**2*u**2*v*w**3 + 6*a**2*b**2*c**2*u**2*w**4 + 6*a**2*b**2*c**2*u*v**3*w**2 - 12*a**2*b**2*c**2*u*v**2*w**3 + 12*a**2*b**2*c**2*u*v*w**4 + 3*a**2*b**2*c**2*u*w**5 - 6*a**2*b**2*c**2*v**3*w**3 + 6*a**2*b**2*c**2*v**2*w**4 + 3*a**2*b**2*c**2*v*w**5 - 9*a**2*b**2*c**2*w**6 + a**2*b*c**3*u**3*v**3 + 3*a**2*b*c**3*u**3*v**2*w - 6*a**2*b*c**3*u**3*v*w**2 + a**2*b*c**3*u**3*w**3 + 3*a**2*b*c**3*u**2*v**3*w - 10*a**2*b*c**3*u**2*v**2*w**2 + 7*a**2*b*c**3*u**2*v*w**3 + 2*a**2*b*c**3*u**2*w**4 - 6*a**2*b*c**3*u*v**3*w**2 + 7*a**2*b*c**3*u*v**2*w**3 + 6*a**2*b*c**3*u*v*w**4 - 7*a**2*b*c**3*u*w**5 + a**2*b*c**3*v**3*w**3 + 2*a**2*b*c**3*v**2*w**4 - 7*a**2*b*c**3*v*w**5 + a**2*b*c**3*w**6 + a**2*c**4*u**3*v**2*w + a**2*c**4*u**3*v*w**2 + a**2*c**4*u**2*v**3*w + 2*a**2*c**4*u**2*v**2*w**2 + a**2*c**4*u**2*v*w**3 + a**2*c**4*u*v**3*w**2 + a**2*c**4*u*v**2*w**3 - 9*a**2*c**4*u*v*w**4 + a*b**5*u**2*v**2*w**2 + a*b**5*u**2*v*w**3 + a*b**5*u*v**2*w**3 + a*b**5*u*v*w**4 + a*b**4*c*u**3*v**2*w + a*b**4*c*u**3*v*w**2 + a*b**4*c*u**2*v**3*w + 3*a*b**4*c*u**2*v**2*w**2 - 6*a*b**4*c*u**2*v*w**3 + a*b**4*c*u**2*w**4 + a*b**4*c*u*v**3*w**2 - 6*a*b**4*c*u*v**2*w**3 + 3*a*b**4*c*u*v*w**4 + a*b**4*c*u*w**5 + a*b**4*c*v**2*w**4 + a*b**4*c*v*w**5 + a*b**3*c**2*u**3*v**3 + 3*a*b**3*c**2*u**3*v**2*w - 6*a*b**3*c**2*u**3*v*w**2 + a*b**3*c**2*u**3*w**3 + 3*a*b**3*c**2*u**2*v**3*w - 10*a*b**3*c**2*u**2*v**2*w**2 + 7*a*b**3*c**2*u**2*v*w**3 + 2*a*b**3*c**2*u**2*w**4 - 6*a*b**3*c**2*u*v**3*w**2 + 7*a*b**3*c**2*u*v**2*w**3 + 6*a*b**3*c**2*u*v*w**4 - 7*a*b**3*c**2*u*w**5 + a*b**3*c**2*v**3*w**3 + 2*a*b**3*c**2*v**2*w**4 - 7*a*b**3*c**2*v*w**5 + a*b**3*c**2*w**6 + a*b**2*c**3*u**3*v**3 - 7*a*b**2*c**3*u**3*v**2*w + 2*a*b**2*c**3*u**3*v*w**2 + a*b**2*c**3*u**3*w**3 - 7*a*b**2*c**3*u**2*v**3*w + 6*a*b**2*c**3*u**2*v**2*w**2 + 7*a*b**2*c**3*u**2*v*w**3 - 6*a*b**2*c**3*u**2*w**4 + 2*a*b**2*c**3*u*v**3*w**2 + 7*a*b**2*c**3*u*v**2*w**3 - 10*a*b**2*c**3*u*v*w**4 + 3*a*b**2*c**3*u*w**5 + a*b**2*c**3*v**3*w**3 - 6*a*b**2*c**3*v**2*w**4 + 3*a*b**2*c**3*v*w**5 + a*b**2*c**3*w**6 + a*b*c**4*u**3*v**2*w + a*b*c**4*u**3*v*w**2 + a*b*c**4*u**2*v**3*w + 3*a*b*c**4*u**2*v**2*w**2 - 6*a*b*c**4*u**2*v*w**3 + a*b*c**4*u**2*w**4 + a*b*c**4*u*v**3*w**2 - 6*a*b*c**4*u*v**2*w**3 + 3*a*b*c**4*u*v*w**4 + a*b*c**4*u*w**5 + a*b*c**4*v**2*w**4 + a*b*c**4*v*w**5 + a*c**5*u**2*v**2*w**2 + a*c**5*u**2*v*w**3 + a*c**5*u*v**2*w**3 + a*c**5*u*v*w**4 + b**5*c*u**2*v**2*w**2 + b**5*c*u**2*v*w**3 + b**5*c*u*v**2*w**3 + b**5*c*u*v*w**4 + b**4*c**2*u**3*v**2*w + b**4*c**2*u**3*v*w**2 + b**4*c**2*u**2*v**3*w + 2*b**4*c**2*u**2*v**2*w**2 + b**4*c**2*u**2*v*w**3 + b**4*c**2*u*v**3*w**2 + b**4*c**2*u*v**2*w**3 - 9*b**4*c**2*u*v*w**4 + b**3*c**3*u**3*v**3 + b**3*c**3*u**3*v**2*w + b**3*c**3*u**2*v**3*w + 2*b**3*c**3*u**2*v**2*w**2 - 8*b**3*c**3*u**2*v*w**3 - 8*b**3*c**3*u*v**2*w**3 + 2*b**3*c**3*u*v*w**4 + b**3*c**3*u*w**5 + b**3*c**3*v*w**5 + b**3*c**3*w**6 - 9*b**2*c**4*u**2*v**2*w**2 + b**2*c**4*u**2*v*w**3 + b**2*c**4*u**2*w**4 + b**2*c**4*u*v**2*w**3 + 2*b**2*c**4*u*v*w**4 + b**2*c**4*u*w**5 + b**2*c**4*v**2*w**4 + b**2*c**4*v*w**5 + b*c**5*u**2*v**2*w**2 + b*c**5*u**2*v*w**3 + b*c**5*u*v**2*w**3 + b*c**5*u*v*w**4");
		System.out.println(SDS.sds(fn, false, true));
		/*/
	}
}