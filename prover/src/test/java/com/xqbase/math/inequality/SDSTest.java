package com.xqbase.math.inequality;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
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
		// can be proved positive by tsds within 99 iterations (sds 72)
		result = SDS.tsds(new BigPoly("xy", "x**2 + y**2").add(f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// can be found negative by tsds within 98 iterations (sds 71)
		f = new BigPoly("xy", "-x**2 - y**2").add(f);
		result = SDS.tsds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').compareTo(f.valueOf(0)) < 0);
		assertEquals(98, result.getDepth());

		// TODO example 2
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
		assertEquals(1, result.depth);
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
		assertEquals(2, result.depth);
		// p171, problem 8
		String f = "x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6";
		result = SDS.sds(new LongPoly("xyz", f));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [1, 0, 0], [1, 1, 0], [4, 2, 3]]", result.getZeroAt().toString());
		assertEquals(5, result.depth);
		// p171, problem 9
		f = "8*x**7 + 6*x**6*y + 8*x**6*z + 62*x**5*y**2 - 154*x**5*y*z - 69*x**4*y**3 + 202*x**4*y**2*z + 2*x**4*y*z**2 + 18*x**3*y**4 - 170*x**3*y**3*z + 114*x**3*y**2*z**2 + 18*x**3*y*z**3 + 54*x**2*y**4*z - 124*x**2*y**3*z**2 - 26*x**2*y**2*z**3 + 54*x*y**4*z**2 - 22*x*y**3*z**3 + 18*y**4*z**3 + y**3*z**4";
		result = SDS.sds(new LongPoly("xyz", f));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 1, 1], [1, 1, 5], [3, 1, 3]]", result.getZeroAt().toString());
		assertEquals(18, result.depth);
		// p172, problem 10
		f = "a**6 + 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 + 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 + a*b**5 - 5*a*c**5 + b**6 - 5*b**5*c + 10*b**4*c**2 - 10*b**3*c**3 + 5*b**2*c**4 - b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(4, result.depth);
		f = "a**6 - 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 - 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 - a*b**5 - 5*a*c**5 + b**6 + 5*b**5*c + 10*b**4*c**2 + 10*b**3*c**3 + 5*b**2*c**4 + b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(4, result.depth);
		// p172, problem 11
		f = "2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2" +
				" + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4" +
				" - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3" +
				" + 1611722090*z**4";
		// LongPoly: long overflow at depth = 12
		SDSResult<MutableBigInteger> bigResult = SDS.sds(new BigPoly("xyz", f));
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(46, bigResult.depth);
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
		assertEquals(3, result.depth);
		// https://math.stackexchange.com/q/1777075
		f = new BigPoly("xyz", "325*x**5*y**2 + 125*x**5*z**2 + 325*x**4*y**3 - 845*x**4*y**2*z - 325*x**4*y*z**2 - 325*x**4*z**3 - 325*x**3*y**4 + 720*x**3*y**2*z**2 + 325*x**3*z**4 + 125*x**2*y**5 - 325*x**2*y**4*z + 720*x**2*y**3*z**2 + 720*x**2*y**2*z**3 - 845*x**2*y*z**4 + 325*x**2*z**5 - 845*x*y**4*z**2 - 325*x*y**2*z**4 + 325*y**5*z**2 + 325*y**4*z**3 - 325*y**3*z**4 + 125*y**2*z**5");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// sds needs 5
		assertEquals(4, result.depth);
		f = new BigPoly("xyz", "72*x**5*y**2 + 27*x**5*z**2 + 72*x**4*y**3 - 192*x**4*y**2*z - 72*x**4*y*z**2 - 72*x**4*z**3 - 72*x**3*y**4 + 165*x**3*y**2*z**2 + 72*x**3*z**4 + 27*x**2*y**5 - 72*x**2*y**4*z + 165*x**2*y**3*z**2 + 165*x**2*y**2*z**3 - 192*x**2*y*z**4 + 72*x**2*z**5 - 192*x*y**4*z**2 - 72*x*y**2*z**4 + 72*y**5*z**2 + 72*y**4*z**3 - 72*y**3*z**4 + 27*y**2*z**5");
		result = SDS.tsds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').compareTo(f.valueOf(0)) < 0);
		assertEquals(2, result.depth);
		// https://math.stackexchange.com/q/3526427
		f = new BigPoly("xyz", "x**9*y**3 - x**9*y**2*z - x**9*y*z**2 + x**9*z**3 + 6*x**8*y**4 + x**8*y**3*z - 10*x**8*y**2*z**2 + x**8*y*z**3 + 6*x**8*z**4 + 15*x**7*y**5 + 19*x**7*y**4*z - 26*x**7*y**3*z**2 - 26*x**7*y**2*z**3 + 19*x**7*y*z**4 + 15*x**7*z**5 + 20*x**6*y**6 + 45*x**6*y**5*z - 30*x**6*y**4*z**2 - 110*x**6*y**3*z**3 - 30*x**6*y**2*z**4 + 45*x**6*y*z**5 + 20*x**6*z**6 + 15*x**5*y**7 + 45*x**5*y**6*z - 26*x**5*y**5*z**2 - 202*x**5*y**4*z**3 - 202*x**5*y**3*z**4 - 26*x**5*y**2*z**5 + 45*x**5*y*z**6 + 15*x**5*z**7 + 6*x**4*y**8 + 19*x**4*y**7*z - 30*x**4*y**6*z**2 - 202*x**4*y**5*z**3 + 1410*x**4*y**4*z**4 - 202*x**4*y**3*z**5 - 30*x**4*y**2*z**6 + 19*x**4*y*z**7 + 6*x**4*z**8 + x**3*y**9 + x**3*y**8*z - 26*x**3*y**7*z**2 - 110*x**3*y**6*z**3 - 202*x**3*y**5*z**4 - 202*x**3*y**4*z**5 - 110*x**3*y**3*z**6 - 26*x**3*y**2*z**7 + x**3*y*z**8 + x**3*z**9 - x**2*y**9*z - 10*x**2*y**8*z**2 - 26*x**2*y**7*z**3 - 30*x**2*y**6*z**4 - 26*x**2*y**5*z**5 - 30*x**2*y**4*z**6 - 26*x**2*y**3*z**7 - 10*x**2*y**2*z**8 - x**2*y*z**9 - x*y**9*z**2 + x*y**8*z**3 + 19*x*y**7*z**4 + 45*x*y**6*z**5 + 45*x*y**5*z**6 + 19*x*y**4*z**7 + x*y**3*z**8 - x*y**2*z**9 + y**9*z**3 + 6*y**8*z**4 + 15*y**7*z**5 + 20*y**6*z**6 + 15*y**5*z**7 + 6*y**4*z**8 + y**3*z**9");
		result = SDS.tsds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1]]", result.getZeroAt().toString());
		// sds needs 2
		assertEquals(4, result.depth);
	}

	@Test
	public void testXiong23() {
		// ISBN 9787542878021, p112, §7.2, ex6
		LongPoly f = replaceAn("17*a1**12 + 156*a1**11*a2 + 156*a1**11*a3 + 108*a1**11*a4 + 642*a1**10*a2**2 + 1284*a1**10*a2*a3 + 900*a1**10*a2*a4 + 642*a1**10*a3**2 + 900*a1**10*a3*a4 + 258*a1**10*a4**2 + 1020*a1**9*a2**3 + 4692*a1**9*a2**2*a3 + 3348*a1**9*a2**2*a4 + 4692*a1**9*a2*a3**2 + 6696*a1**9*a2*a3*a4 + 2004*a1**9*a2*a4**2 + 1836*a1**9*a3**3 + 3348*a1**9*a3**2*a4 + 2004*a1**9*a3*a4**2 + 492*a1**9*a4**3 - 33*a1**8*a2**4 + 7500*a1**8*a2**3*a3 + 4044*a1**8*a2**3*a4 + 15066*a1**8*a2**2*a3**2 + 22068*a1**8*a2**2*a3*a4 + 7002*a1**8*a2**2*a4**2 + 10908*a1**8*a2*a3**3 + 22068*a1**8*a2*a3**2*a4 + 14004*a1**8*a2*a3*a4**2 + 3660*a1**8*a2*a4**3 + 4191*a1**8*a3**4 + 8268*a1**8*a3**3*a4 + 7002*a1**8*a3**2*a4**2 + 2844*a1**8*a3*a4**3 + 735*a1**8*a4**4 - 1800*a1**7*a2**5 + 4824*a1**7*a2**4*a3 - 2376*a1**7*a2**4*a4 + 23472*a1**7*a2**3*a3**2 + 29664*a1**7*a2**3*a3*a4 + 6192*a1**7*a2**3*a4**2 + 28272*a1**7*a2**2*a3**3 + 64080*a1**7*a2**2*a3**2*a4 + 43920*a1**7*a2**2*a3*a4**2 + 12336*a1**7*a2**2*a4**3 + 18648*a1**7*a2*a3**4 + 43488*a1**7*a2*a3**3*a4 + 43920*a1**7*a2*a3**2*a4**2 + 20448*a1**7*a2*a3*a4**3 + 5592*a1**7*a2*a4**4 + 7224*a1**7*a3**5 + 15672*a1**7*a3**4*a4 + 15216*a1**7*a3**3*a4**2 + 8112*a1**7*a3**2*a4**3 + 1368*a1**7*a3*a4**4 + 24*a1**7*a4**5 - 1636*a1**6*a2**6 + 1896*a1**6*a2**5*a3 - 8472*a1**6*a2**5*a4 + 22308*a1**6*a2**4*a3**2 + 15816*a1**6*a2**4*a3*a4 - 6492*a1**6*a2**4*a4**2 + 30192*a1**6*a2**3*a3**3 + 89808*a1**6*a2**3*a3**2*a4 + 55248*a1**6*a2**3*a3*a4**2 + 4656*a1**6*a2**3*a4**3 + 35364*a1**6*a2**2*a3**4 + 102864*a1**6*a2**2*a3**3*a4 + 123480*a1**6*a2**2*a3**2*a4**2 + 65808*a1**6*a2**2*a3*a4**3 + 18852*a1**6*a2**2*a4**4 + 23976*a1**6*a2*a3**5 + 59976*a1**6*a2*a3**4*a4 + 77328*a1**6*a2*a3**3*a4**2 + 56784*a1**6*a2*a3**2*a4**3 + 19656*a1**6*a2*a3*a4**4 + 4200*a1**6*a2*a4**5 + 8732*a1**6*a3**6 + 22632*a1**6*a3**5*a4 + 24612*a1**6*a3**4*a4**2 + 19056*a1**6*a3**3*a4**3 + 804*a1**6*a3**2*a4**4 - 4824*a1**6*a3*a4**5 - 1636*a1**6*a4**6 + 24*a1**5*a2**7 + 4200*a1**5*a2**6*a3 - 4824*a1**5*a2**6*a4 + 20664*a1**5*a2**5*a3**2 + 10224*a1**5*a2**5*a3*a4 - 10440*a1**5*a2**5*a4**2 + 10344*a1**5*a2**4*a3**3 + 84312*a1**5*a2**4*a3**2*a4 + 41112*a1**5*a2**4*a3*a4**2 - 9432*a1**5*a2**4*a4**3 + 24264*a1**5*a2**3*a3**4 + 109344*a1**5*a2**3*a3**3*a4 + 175536*a1**5*a2**3*a3**2*a4**2 + 67872*a1**5*a2**3*a3*a4**3 + 840*a1**5*a2**3*a4**4 + 32760*a1**5*a2**2*a3**5 + 108504*a1**5*a2**2*a3**4*a4 + 187632*a1**5*a2**2*a3**3*a4**2 + 170352*a1**5*a2**2*a3**2*a4**3 + 79128*a1**5*a2**2*a3*a4**4 + 20664*a1**5*a2**2*a4**5 + 22632*a1**5*a2*a3**6 + 65520*a1**5*a2*a3**5*a4 + 96408*a1**5*a2*a3**4*a4**2 + 93984*a1**5*a2*a3**3*a4**3 + 48024*a1**5*a2*a3**2*a4**4 + 10224*a1**5*a2*a3*a4**5 + 1896*a1**5*a2*a4**6 + 7224*a1**5*a3**7 + 23976*a1**5*a3**6*a4 + 32760*a1**5*a3**5*a4**2 + 24360*a1**5*a3**4*a4**3 + 5352*a1**5*a3**3*a4**4 - 10440*a1**5*a3**2*a4**5 - 8472*a1**5*a3*a4**6 - 1800*a1**5*a4**7 + 735*a1**4*a2**8 + 5592*a1**4*a2**7*a3 + 1368*a1**4*a2**7*a4 + 18852*a1**4*a2**6*a3**2 + 19656*a1**4*a2**6*a3*a4 + 804*a1**4*a2**6*a4**2 + 840*a1**4*a2**5*a3**3 + 79128*a1**4*a2**5*a3**2*a4 + 48024*a1**4*a2**5*a3*a4**2 + 5352*a1**4*a2**5*a4**3 - 1926*a1**4*a2**4*a3**4 + 76488*a1**4*a2**4*a3**3*a4 + 184860*a1**4*a2**4*a3**2*a4**2 + 68904*a1**4*a2**4*a3*a4**3 - 1926*a1**4*a2**4*a4**4 + 24360*a1**4*a2**3*a3**5 + 99144*a1**4*a2**3*a3**4*a4 + 238224*a1**4*a2**3*a3**3*a4**2 + 229584*a1**4*a2**3*a3**2*a4**3 + 76488*a1**4*a2**3*a3*a4**4 + 10344*a1**4*a2**3*a4**5 + 24612*a1**4*a2**2*a3**6 + 96408*a1**4*a2**2*a3**5*a4 + 202140*a1**4*a2**2*a3**4*a4**2 + 240912*a1**4*a2**2*a3**3*a4**3 + 184860*a1**4*a2**2*a3**2*a4**4 + 84312*a1**4*a2**2*a3*a4**5 + 22308*a1**4*a2**2*a4**6 + 15672*a1**4*a2*a3**7 + 59976*a1**4*a2*a3**6*a4 + 108504*a1**4*a2*a3**5*a4**2 + 99144*a1**4*a2*a3**4*a4**3 + 68904*a1**4*a2*a3**3*a4**4 + 41112*a1**4*a2*a3**2*a4**5 + 15816*a1**4*a2*a3*a4**6 + 4824*a1**4*a2*a4**7 + 4191*a1**4*a3**8 + 18648*a1**4*a3**7*a4 + 35364*a1**4*a3**6*a4**2 + 24264*a1**4*a3**5*a4**3 - 1926*a1**4*a3**4*a4**4 - 9432*a1**4*a3**3*a4**5 - 6492*a1**4*a3**2*a4**6 - 2376*a1**4*a3*a4**7 - 33*a1**4*a4**8 + 492*a1**3*a2**9 + 3660*a1**3*a2**8*a3 + 2844*a1**3*a2**8*a4 + 12336*a1**3*a2**7*a3**2 + 20448*a1**3*a2**7*a3*a4 + 8112*a1**3*a2**7*a4**2 + 4656*a1**3*a2**6*a3**3 + 65808*a1**3*a2**6*a3**2*a4 + 56784*a1**3*a2**6*a3*a4**2 + 19056*a1**3*a2**6*a4**3 - 9432*a1**3*a2**5*a3**4 + 67872*a1**3*a2**5*a3**3*a4 + 170352*a1**3*a2**5*a3**2*a4**2 + 93984*a1**3*a2**5*a3*a4**3 + 24360*a1**3*a2**5*a4**4 + 5352*a1**3*a2**4*a3**5 + 68904*a1**3*a2**4*a3**4*a4 + 229584*a1**3*a2**4*a3**3*a4**2 + 240912*a1**3*a2**4*a3**2*a4**3 + 99144*a1**3*a2**4*a3*a4**4 + 24264*a1**3*a2**4*a4**5 + 19056*a1**3*a2**3*a3**6 + 93984*a1**3*a2**3*a3**5*a4 + 240912*a1**3*a2**3*a3**4*a4**2 + 175040*a1**3*a2**3*a3**3*a4**3 + 238224*a1**3*a2**3*a3**2*a4**4 + 109344*a1**3*a2**3*a3*a4**5 + 30192*a1**3*a2**3*a4**6 + 15216*a1**3*a2**2*a3**7 + 77328*a1**3*a2**2*a3**6*a4 + 187632*a1**3*a2**2*a3**5*a4**2 + 238224*a1**3*a2**2*a3**4*a4**3 + 229584*a1**3*a2**2*a3**3*a4**4 + 175536*a1**3*a2**2*a3**2*a4**5 + 89808*a1**3*a2**2*a3*a4**6 + 23472*a1**3*a2**2*a4**7 + 8268*a1**3*a2*a3**8 + 43488*a1**3*a2*a3**7*a4 + 102864*a1**3*a2*a3**6*a4**2 + 109344*a1**3*a2*a3**5*a4**3 + 76488*a1**3*a2*a3**4*a4**4 + 67872*a1**3*a2*a3**3*a4**5 + 55248*a1**3*a2*a3**2*a4**6 + 29664*a1**3*a2*a3*a4**7 + 7500*a1**3*a2*a4**8 + 1836*a1**3*a3**9 + 10908*a1**3*a3**8*a4 + 28272*a1**3*a3**7*a4**2 + 30192*a1**3*a3**6*a4**3 + 10344*a1**3*a3**5*a4**4 + 840*a1**3*a3**4*a4**5 + 4656*a1**3*a3**3*a4**6 + 6192*a1**3*a3**2*a4**7 + 4044*a1**3*a3*a4**8 + 1020*a1**3*a4**9 + 258*a1**2*a2**10 + 2004*a1**2*a2**9*a3 + 2004*a1**2*a2**9*a4 + 7002*a1**2*a2**8*a3**2 + 14004*a1**2*a2**8*a3*a4 + 7002*a1**2*a2**8*a4**2 + 6192*a1**2*a2**7*a3**3 + 43920*a1**2*a2**7*a3**2*a4 + 43920*a1**2*a2**7*a3*a4**2 + 15216*a1**2*a2**7*a4**3 - 6492*a1**2*a2**6*a3**4 + 55248*a1**2*a2**6*a3**3*a4 + 123480*a1**2*a2**6*a3**2*a4**2 + 77328*a1**2*a2**6*a3*a4**3 + 24612*a1**2*a2**6*a4**4 - 10440*a1**2*a2**5*a3**5 + 41112*a1**2*a2**5*a3**4*a4 + 175536*a1**2*a2**5*a3**3*a4**2 + 187632*a1**2*a2**5*a3**2*a4**3 + 96408*a1**2*a2**5*a3*a4**4 + 32760*a1**2*a2**5*a4**5 + 804*a1**2*a2**4*a3**6 + 48024*a1**2*a2**4*a3**5*a4 + 184860*a1**2*a2**4*a3**4*a4**2 + 238224*a1**2*a2**4*a3**3*a4**3 + 202140*a1**2*a2**4*a3**2*a4**4 + 108504*a1**2*a2**4*a3*a4**5 + 35364*a1**2*a2**4*a4**6 + 8112*a1**2*a2**3*a3**7 + 56784*a1**2*a2**3*a3**6*a4 + 170352*a1**2*a2**3*a3**5*a4**2 + 229584*a1**2*a2**3*a3**4*a4**3 + 240912*a1**2*a2**3*a3**3*a4**4 + 187632*a1**2*a2**3*a3**2*a4**5 + 102864*a1**2*a2**3*a3*a4**6 + 28272*a1**2*a2**3*a4**7 + 7002*a1**2*a2**2*a3**8 + 43920*a1**2*a2**2*a3**7*a4 + 123480*a1**2*a2**2*a3**6*a4**2 + 175536*a1**2*a2**2*a3**5*a4**3 + 184860*a1**2*a2**2*a3**4*a4**4 + 170352*a1**2*a2**2*a3**3*a4**5 + 123480*a1**2*a2**2*a3**2*a4**6 + 64080*a1**2*a2**2*a3*a4**7 + 15066*a1**2*a2**2*a4**8 + 3348*a1**2*a2*a3**9 + 22068*a1**2*a2*a3**8*a4 + 64080*a1**2*a2*a3**7*a4**2 + 89808*a1**2*a2*a3**6*a4**3 + 84312*a1**2*a2*a3**5*a4**4 + 79128*a1**2*a2*a3**4*a4**5 + 65808*a1**2*a2*a3**3*a4**6 + 43920*a1**2*a2*a3**2*a4**7 + 22068*a1**2*a2*a3*a4**8 + 4692*a1**2*a2*a4**9 + 642*a1**2*a3**10 + 4692*a1**2*a3**9*a4 + 15066*a1**2*a3**8*a4**2 + 23472*a1**2*a3**7*a4**3 + 22308*a1**2*a3**6*a4**4 + 20664*a1**2*a3**5*a4**5 + 18852*a1**2*a3**4*a4**6 + 12336*a1**2*a3**3*a4**7 + 7002*a1**2*a3**2*a4**8 + 3348*a1**2*a3*a4**9 + 642*a1**2*a4**10 + 108*a1*a2**11 + 900*a1*a2**10*a3 + 900*a1*a2**10*a4 + 3348*a1*a2**9*a3**2 + 6696*a1*a2**9*a3*a4 + 3348*a1*a2**9*a4**2 + 4044*a1*a2**8*a3**3 + 22068*a1*a2**8*a3**2*a4 + 22068*a1*a2**8*a3*a4**2 + 8268*a1*a2**8*a4**3 - 2376*a1*a2**7*a3**4 + 29664*a1*a2**7*a3**3*a4 + 64080*a1*a2**7*a3**2*a4**2 + 43488*a1*a2**7*a3*a4**3 + 15672*a1*a2**7*a4**4 - 8472*a1*a2**6*a3**5 + 15816*a1*a2**6*a3**4*a4 + 89808*a1*a2**6*a3**3*a4**2 + 102864*a1*a2**6*a3**2*a4**3 + 59976*a1*a2**6*a3*a4**4 + 22632*a1*a2**6*a4**5 - 4824*a1*a2**5*a3**6 + 10224*a1*a2**5*a3**5*a4 + 84312*a1*a2**5*a3**4*a4**2 + 109344*a1*a2**5*a3**3*a4**3 + 108504*a1*a2**5*a3**2*a4**4 + 65520*a1*a2**5*a3*a4**5 + 23976*a1*a2**5*a4**6 + 1368*a1*a2**4*a3**7 + 19656*a1*a2**4*a3**6*a4 + 79128*a1*a2**4*a3**5*a4**2 + 76488*a1*a2**4*a3**4*a4**3 + 99144*a1*a2**4*a3**3*a4**4 + 96408*a1*a2**4*a3**2*a4**5 + 59976*a1*a2**4*a3*a4**6 + 18648*a1*a2**4*a4**7 + 2844*a1*a2**3*a3**8 + 20448*a1*a2**3*a3**7*a4 + 65808*a1*a2**3*a3**6*a4**2 + 67872*a1*a2**3*a3**5*a4**3 + 68904*a1*a2**3*a3**4*a4**4 + 93984*a1*a2**3*a3**3*a4**5 + 77328*a1*a2**3*a3**2*a4**6 + 43488*a1*a2**3*a3*a4**7 + 10908*a1*a2**3*a4**8 + 2004*a1*a2**2*a3**9 + 14004*a1*a2**2*a3**8*a4 + 43920*a1*a2**2*a3**7*a4**2 + 55248*a1*a2**2*a3**6*a4**3 + 41112*a1*a2**2*a3**5*a4**4 + 48024*a1*a2**2*a3**4*a4**5 + 56784*a1*a2**2*a3**3*a4**6 + 43920*a1*a2**2*a3**2*a4**7 + 22068*a1*a2**2*a3*a4**8 + 4692*a1*a2**2*a4**9 + 900*a1*a2*a3**10 + 6696*a1*a2*a3**9*a4 + 22068*a1*a2*a3**8*a4**2 + 29664*a1*a2*a3**7*a4**3 + 15816*a1*a2*a3**6*a4**4 + 10224*a1*a2*a3**5*a4**5 + 19656*a1*a2*a3**4*a4**6 + 20448*a1*a2*a3**3*a4**7 + 14004*a1*a2*a3**2*a4**8 + 6696*a1*a2*a3*a4**9 + 1284*a1*a2*a4**10 + 156*a1*a3**11 + 1284*a1*a3**10*a4 + 4692*a1*a3**9*a4**2 + 7500*a1*a3**8*a4**3 + 4824*a1*a3**7*a4**4 + 1896*a1*a3**6*a4**5 + 4200*a1*a3**5*a4**6 + 5592*a1*a3**4*a4**7 + 3660*a1*a3**3*a4**8 + 2004*a1*a3**2*a4**9 + 900*a1*a3*a4**10 + 156*a1*a4**11 + 17*a2**12 + 156*a2**11*a3 + 156*a2**11*a4 + 642*a2**10*a3**2 + 1284*a2**10*a3*a4 + 642*a2**10*a4**2 + 1020*a2**9*a3**3 + 4692*a2**9*a3**2*a4 + 4692*a2**9*a3*a4**2 + 1836*a2**9*a4**3 - 33*a2**8*a3**4 + 7500*a2**8*a3**3*a4 + 15066*a2**8*a3**2*a4**2 + 10908*a2**8*a3*a4**3 + 4191*a2**8*a4**4 - 1800*a2**7*a3**5 + 4824*a2**7*a3**4*a4 + 23472*a2**7*a3**3*a4**2 + 28272*a2**7*a3**2*a4**3 + 18648*a2**7*a3*a4**4 + 7224*a2**7*a4**5 - 1636*a2**6*a3**6 + 1896*a2**6*a3**5*a4 + 22308*a2**6*a3**4*a4**2 + 30192*a2**6*a3**3*a4**3 + 35364*a2**6*a3**2*a4**4 + 23976*a2**6*a3*a4**5 + 8732*a2**6*a4**6 + 24*a2**5*a3**7 + 4200*a2**5*a3**6*a4 + 20664*a2**5*a3**5*a4**2 + 10344*a2**5*a3**4*a4**3 + 24264*a2**5*a3**3*a4**4 + 32760*a2**5*a3**2*a4**5 + 22632*a2**5*a3*a4**6 + 7224*a2**5*a4**7 + 735*a2**4*a3**8 + 5592*a2**4*a3**7*a4 + 18852*a2**4*a3**6*a4**2 + 840*a2**4*a3**5*a4**3 - 1926*a2**4*a3**4*a4**4 + 24360*a2**4*a3**3*a4**5 + 24612*a2**4*a3**2*a4**6 + 15672*a2**4*a3*a4**7 + 4191*a2**4*a4**8 + 492*a2**3*a3**9 + 3660*a2**3*a3**8*a4 + 12336*a2**3*a3**7*a4**2 + 4656*a2**3*a3**6*a4**3 - 9432*a2**3*a3**5*a4**4 + 5352*a2**3*a3**4*a4**5 + 19056*a2**3*a3**3*a4**6 + 15216*a2**3*a3**2*a4**7 + 8268*a2**3*a3*a4**8 + 1836*a2**3*a4**9 + 258*a2**2*a3**10 + 2004*a2**2*a3**9*a4 + 7002*a2**2*a3**8*a4**2 + 6192*a2**2*a3**7*a4**3 - 6492*a2**2*a3**6*a4**4 - 10440*a2**2*a3**5*a4**5 + 804*a2**2*a3**4*a4**6 + 8112*a2**2*a3**3*a4**7 + 7002*a2**2*a3**2*a4**8 + 3348*a2**2*a3*a4**9 + 642*a2**2*a4**10 + 108*a2*a3**11 + 900*a2*a3**10*a4 + 3348*a2*a3**9*a4**2 + 4044*a2*a3**8*a4**3 - 2376*a2*a3**7*a4**4 - 8472*a2*a3**6*a4**5 - 4824*a2*a3**5*a4**6 + 1368*a2*a3**4*a4**7 + 2844*a2*a3**3*a4**8 + 2004*a2*a3**2*a4**9 + 900*a2*a3*a4**10 + 156*a2*a4**11 + 17*a3**12 + 156*a3**11*a4 + 642*a3**10*a4**2 + 1020*a3**9*a4**3 - 33*a3**8*a4**4 - 1800*a3**7*a4**5 - 1636*a3**6*a4**6 + 24*a3**5*a4**7 + 735*a3**4*a4**8 + 492*a3**3*a4**9 + 258*a3**2*a4**10 + 108*a3*a4**11 + 17*a4**12");
		SDSResult<MutableBigInteger> result = SDS.tsds(new BigPoly("abcd", f.toString()));
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]", result.getZeroAt().toString());
		assertEquals(1, result.depth);
	}

	@Test
	public void testHan13() {
		// http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545
		LongPoly f;
		SDSResult<MutableLong> result;
		// ex 4.2
		// Too slow in making permMat
		/*
		f = replaceAn("a1**2 + a2**2 + a3**2 + a4**2 + a5**2 + a6**2 + a7**2 + a8**2 + a9**2 + a10**2 - 4*a1*a2");
		result = SDS.sds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'a').compareTo(f.valueOf(0)) < 0);
		assertEquals(0, result.depth);
		*/
		// ex 4.3
		f = new LongPoly("xyz", "x**3 + y**3 + z**3 - 3*x*y*z");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.depth);
	}
}