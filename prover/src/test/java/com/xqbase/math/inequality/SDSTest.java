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

import com.xqbase.math.polys.BigPoly;
import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.MutableBig;
import com.xqbase.math.polys.MutableLong;
import com.xqbase.math.polys.MutableNumber;
import com.xqbase.math.polys.Poly;

public class SDSTest {
	private static BigPoly __() {
		return new BigPoly();
	}

	@BeforeClass
	public static void startup() {
		// https://stackoverflow.com/a/6308286/4260959
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINE);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
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
		SDS.Result<MutableLong> result = SDS.sds(new LongPoly("xy", "x**2 + x*y + y**2"));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
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

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> T
			subs(P f, List<T> values, char startsWith) {
		P f1 = f;
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

	private static <T extends MutableNumber<T>, P extends Poly<T, P>> List<T> asList(P f, long... values) {
		List<T> list = new ArrayList<>();
		for (long value : values) {
			list.add(f.valueOf(value));
		}
		return list;
	}

	private static final SDS.Transform T_n = SDS.Transform.T_n;
	private static final SDS.Transform H_3 = SDS.Transform.H_3;
	private static final SDS.Transform J_4 = SDS.Transform.J_4;
	private static final SDS.Transform Z_n = SDS.Transform.Z_n;
	private static final SDS.Transform Y_n = SDS.Transform.Y_n;

	@Test
	public void testTransform() {
		// A_n vs T_n vs H_3 vs J_4 vs Z_n
		// example 1:
		// fibonacci 91, 92
		String vars = "xy";
		long m = 4660046610375530309L;
		long n = 7540113804746346429L;
		BigPoly f = new BigPoly(vars, m + "*x - " + n + "*y");
		f = __().addMul(f, f);
		SDS.Result<MutableBig> result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[" + n + ", " + m + "]]", result.getZeroAt().toString());
		assertEquals(91, result.getDepth());
		// 1e22
		f = __().add(f.valueOf("10000000000000000000000"), f);
		// T_2 works within 99 iterations (A_2 72)
		result = SDS.sds(new BigPoly(vars, "x**2 + y**2").add(f), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// Z_2 == T_2
		result = SDS.sds(new BigPoly(vars, "x**2 + y**2").add(f), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// T_2 finds negative within 98 iterations (A_2 71)
		f = new BigPoly(vars, "-x**2 - y**2").add(f);
		result = SDS.sds(f, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(98, result.getDepth());
		// Z_2 == T_2
		result = SDS.sds(f, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(98, result.getDepth());

		// example 2
		// (3*x - y)**2 + (x - z)**2
		vars = "xyz";
		f = new BigPoly(vars, "10*x**2 - 6*x*y - 2*x*z + y**2 + z**2");
		// zero at (1, 3, 1), not on A_3 or T_3's lattice?
		assertEquals(0, subs(f, asList(f, 1, 3, 1), 'x').signum());
		// A_3 works for 6 but doesn't seem to work for 7
		String smallPos = "x**2 + y**2 + z**2";
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(6, f)));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(9, result.getDepth());
		// A_3 finds negative for 1e22 (maybe larger)
		String smallNeg = "-x**2 - y**2 - z**2";
		result = SDS.sds(new BigPoly(vars, smallNeg).add(__().add(f.valueOf("10000000000000000000000"), f)));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 3, 1]", result.getNegativeAt().toString());
		assertEquals(2, result.getDepth());
		// 1e8
		f = __().add(f.valueOf(100_000_000), f);
		// T_3 works within 16 iterations (A_3 doesn't work)
		result = SDS.sds(new BigPoly(vars, smallPos).add(f), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// H_3 works within 15 iterations
		result = SDS.sds(new BigPoly(vars, smallPos).add(f), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Y_3 == H3
		result = SDS.sds(new BigPoly(vars, smallPos).add(f), Y_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Z_3 works within 26 iterations
		result = SDS.sds(new BigPoly(vars, smallPos).add(f), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(26, result.getDepth());
		// T_3 finds negative within 11 iterations
		f = new BigPoly(vars, smallNeg).add(f);
		result = SDS.sds(f, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(11, result.getDepth());
		// H_3 finds negative within 13 iterations
		result = SDS.sds(f, H_3);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(13, result.getDepth());
		// Y_3 == H_3
		result = SDS.sds(f, Y_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(13, result.getDepth());
		// Z_3 finds negative within 16 iterations
		result = SDS.sds(f, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(16, result.getDepth());

		// example 3
		// (2*w - x)**2 + (w - y)**2 + (w - z)**2
		vars = "wxyz";
		f = new BigPoly(vars, "6*w**2 - 4*w*x - 2*w*y - 2*w*z + x**2 + y**2 + z**2");
		// zero at (1, 2, 1, 1), not on A_4 or T_4's lattice?
		assertEquals(0, subs(f, asList(f, 1, 2, 1, 1), 'w').signum());
		// A_4 works for 8 but doesn't seem to work for 9
		smallPos = "w**2 + x**2 + y**2 + z**2";
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(8, f)));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(6, result.getDepth());
		// T_4 needs 12 for 1e5 (A_4 doesn't work)
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(f.valueOf(100_000), f)), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(12, result.getDepth());
		// J_4 needs 16 for 1e5, 21 for 1e7, 27 for 1e9
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(f.valueOf(100_000), f)), J_4);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// Y_4 works within 47 iterations for 1e22
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(f.valueOf("10000000000000000000000"), f)), Y_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(47, result.getDepth());
		// Z_4 works within 16 iterations for 1e3, within 20 iterations for 1e4 (374376 polynomials at 19th iteration)
		result = SDS.sds(new BigPoly(vars, smallPos).add(__().add(f.valueOf(1_000), f)), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// A_4 finds negative for 1e22 (maybe larger)
		smallNeg = "-w**2 - x**2 - y**2 - z**2";
		result = SDS.sds(new BigPoly(vars, smallNeg).add(__().add(f.valueOf("10000000000000000000000"), f)));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 2, 1, 1]", result.getNegativeAt().toString());
		assertEquals(1, result.getDepth());
		// 1e5
		f = new BigPoly(vars, smallNeg).add(__().add(f.valueOf(100_000), f));
		// T_4 finds negative within 11 iterations
		result = SDS.sds(f, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(7, result.getDepth());
		// J_4 finds negative within 9 iterations
		result = SDS.sds(f, J_4);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(9, result.getDepth());
		// Z_4 finds negative within 13 iterations
		result = SDS.sds(f, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(13, result.getDepth());
		// Y_4 finds negative within 5 iterations
		result = SDS.sds(f, Y_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(5, result.getDepth());
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
			assertEquals(0, subs(fn, zeroAt, 'a').signum());
			// keep only if fd is not zero
			if (subs(fd, zeroAt, 'a').signum() != 0) {
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
		// T_5 works
		SDS.Result<MutableLong> result = SDS.sds(fn);
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
		// T_4 got 17 zeros, 13 verified, within 3 iterations
		// J_4 and Z_4 don't work
		// result = SDS.sds(fn, J_4);
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
		// T_3, H_3 and Z_3 don't work
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [1, 0, 0], [1, 1, 0], [4, 2, 3]]", result.getZeroAt().toString());
		assertEquals(5, result.getDepth());
		// p171, problem 9
		f = "8*x**7 + 6*x**6*y + 8*x**6*z + 62*x**5*y**2 - 154*x**5*y*z - 69*x**4*y**3 + 202*x**4*y**2*z + 2*x**4*y*z**2 + 18*x**3*y**4 - 170*x**3*y**3*z + 114*x**3*y**2*z**2 + 18*x**3*y*z**3 + 54*x**2*y**4*z - 124*x**2*y**3*z**2 - 26*x**2*y**2*z**3 + 54*x*y**4*z**2 - 22*x*y**3*z**3 + 18*y**4*z**3 + y**3*z**4";
		result = SDS.sds(new LongPoly("xyz", f));
		// T_3, H_3 and Z_3 don't work
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 1, 1], [1, 1, 5], [3, 1, 3]]", result.getZeroAt().toString());
		assertEquals(18, result.getDepth());
		// p172, problem 10
		f = "a**6 + 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 + 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 + a*b**5 - 5*a*c**5 + b**6 - 5*b**5*c + 10*b**4*c**2 - 10*b**3*c**3 + 5*b**2*c**4 - b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		// T_3, H_3 and Y_3 need 3; Z_3 needs 6
		assertEquals(4, result.getDepth());
		f = "a**6 - 5*a**5*b - a**5*c + 10*a**4*b**2 + 5*a**4*c**2 - 10*a**3*b**3 - 10*a**3*c**3 + 5*a**2*b**4 + 10*a**2*c**4 - a*b**5 - 5*a*c**5 + b**6 + 5*b**5*c + 10*b**4*c**2 + 10*b**3*c**3 + 5*b**2*c**4 + b*c**5 + c**6";
		result = SDS.sds(new LongPoly("abc", f));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		// T_3, H_3 and Y_3 need 3; Z_3 needs 6
		assertEquals(4, result.getDepth());
		// p172, problem 11
		f = "2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2" +
				" + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4" +
				" - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3" +
				" + 1611722090*z**4";
		// LongPoly: long overflow at depth = 12
		SDS.Result<MutableBig> bigResult = SDS.sds(new BigPoly("xyz", f));
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(46, bigResult.getDepth());
		// T_3 needs 4; H_3 and Z_3 don't work
		bigResult = SDS.sds(new BigPoly("xyz", f), T_n);
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(4, bigResult.getDepth());
		// p174, 6-var Vasc's conjecture, too slow
		// results run on Oracle JRE 1.8.0, depend on implementation of HashMap.hashCode():
		// T_6 FULL terminates at depth = 3, 5/515, negative at (317, 12, 317, 27, 287, 0)
		// T_6 FAST terminates at depth = 4, 8/19164, negative at (516881, 61742, 474011, 60290, 441548, 728)
		// Y_6 FULL terminates at depth = 8, 144/9352, negative at (376711, 0, 403036, 49152, 342976, 0)
		// Z_6 FULL terminates at depth = 9, 2277/82901, negative at (6932357, 937500, 5877485, 0, 6408050, 0)
		// A_6 (can use LongPoly) not tested
		/*
		fn = replaceAn("a1**3*a3*a4*a5 + a1**3*a3*a4*a6 + a1**3*a3*a5**2 + a1**3*a3*a5*a6 + a1**3*a4**2*a5 + a1**3*a4**2*a6 + a1**3*a4*a5**2 + a1**3*a4*a5*a6 + a1**2*a2**2*a4*a5 + a1**2*a2**2*a4*a6 + a1**2*a2**2*a5**2 + a1**2*a2**2*a5*a6 + a1**2*a2*a3**2*a5 + a1**2*a2*a3**2*a6 + a1**2*a2*a3*a4**2 - a1**2*a2*a3*a4*a5 - a1**2*a2*a3*a4*a6 - 2*a1**2*a2*a3*a5**2 - a1**2*a2*a3*a5*a6 + a1**2*a2*a4**3 - 2*a1**2*a2*a4**2*a5 - 2*a1**2*a2*a4**2*a6 - 2*a1**2*a2*a4*a5**2 - a1**2*a2*a4*a5*a6 + a1**2*a3**3*a5 + a1**2*a3**3*a6 + a1**2*a3**2*a4**2 - 2*a1**2*a3**2*a4*a5 - 2*a1**2*a3**2*a4*a6 - 3*a1**2*a3**2*a5**2 - 2*a1**2*a3**2*a5*a6 + a1**2*a3*a4**3 - 2*a1**2*a3*a4**2*a5 - 2*a1**2*a3*a4**2*a6 - 2*a1**2*a3*a4*a5**2 + a1**2*a3*a4*a6**2 + a1**2*a3*a5**2*a6 + a1**2*a3*a5*a6**2 + a1**2*a4**2*a5*a6 + a1**2*a4**2*a6**2 + a1**2*a4*a5**2*a6 + a1**2*a4*a5*a6**2 + a1*a2**3*a4*a5 + a1*a2**3*a4*a6 + a1*a2**3*a5**2 + a1*a2**3*a5*a6 + a1*a2**2*a3**2*a5 + a1*a2**2*a3**2*a6 + a1*a2**2*a3*a4**2 - a1*a2**2*a3*a4*a5 - a1*a2**2*a3*a4*a6 - 2*a1*a2**2*a3*a5**2 - a1*a2**2*a3*a5*a6 + a1*a2**2*a4**3 - 2*a1*a2**2*a4**2*a5 - 2*a1*a2**2*a4**2*a6 - 2*a1*a2**2*a4*a5**2 + a1*a2**2*a4*a6**2 + a1*a2**2*a5**2*a6 + a1*a2**2*a5*a6**2 + a1*a2*a3**3*a5 + a1*a2*a3**3*a6 + a1*a2*a3**2*a4**2 - a1*a2*a3**2*a4*a5 - a1*a2*a3**2*a4*a6 - 2*a1*a2*a3**2*a5**2 + a1*a2*a3**2*a6**2 + a1*a2*a3*a4**3 - a1*a2*a3*a4**2*a5 - a1*a2*a3*a4*a6**2 + a1*a2*a3*a5**3 - a1*a2*a3*a5**2*a6 - a1*a2*a3*a5*a6**2 + a1*a2*a4**3*a6 + a1*a2*a4**2*a5**2 - a1*a2*a4**2*a5*a6 - 2*a1*a2*a4**2*a6**2 + a1*a2*a4*a5**3 - a1*a2*a4*a5**2*a6 - a1*a2*a4*a5*a6**2 + a1*a3**3*a5*a6 + a1*a3**3*a6**2 + a1*a3**2*a4**2*a6 + a1*a3**2*a4*a5**2 - a1*a3**2*a4*a5*a6 - 2*a1*a3**2*a4*a6**2 + a1*a3**2*a5**3 - 2*a1*a3**2*a5**2*a6 - 2*a1*a3**2*a5*a6**2 + a1*a3*a4**3*a6 + a1*a3*a4**2*a5**2 - a1*a3*a4**2*a5*a6 - 2*a1*a3*a4**2*a6**2 + a1*a3*a4*a5**3 - a1*a3*a4*a5**2*a6 - a1*a3*a4*a5*a6**2 + a2**3*a4*a5*a6 + a2**3*a4*a6**2 + a2**3*a5**2*a6 + a2**3*a5*a6**2 + a2**2*a3**2*a5*a6 + a2**2*a3**2*a6**2 + a2**2*a3*a4**2*a6 + a2**2*a3*a4*a5**2 - a2**2*a3*a4*a5*a6 - 2*a2**2*a3*a4*a6**2 + a2**2*a3*a5**3 - 2*a2**2*a3*a5**2*a6 - 2*a2**2*a3*a5*a6**2 + a2**2*a4**3*a6 + a2**2*a4**2*a5**2 - 2*a2**2*a4**2*a5*a6 - 3*a2**2*a4**2*a6**2 + a2**2*a4*a5**3 - 2*a2**2*a4*a5**2*a6 - 2*a2**2*a4*a5*a6**2 + a2*a3**3*a5*a6 + a2*a3**3*a6**2 + a2*a3**2*a4**2*a6 + a2*a3**2*a4*a5**2 - a2*a3**2*a4*a5*a6 - 2*a2*a3**2*a4*a6**2 + a2*a3**2*a5**3 - 2*a2*a3**2*a5**2*a6 - 2*a2*a3**2*a5*a6**2 + a2*a3*a4**3*a6 + a2*a3*a4**2*a5**2 - a2*a3*a4**2*a5*a6 - 2*a2*a3*a4**2*a6**2 + a2*a3*a4*a5**3 - a2*a3*a4*a5**2*a6 + a2*a3*a4*a6**3 + a2*a3*a5**2*a6**2 + a2*a3*a5*a6**3 + a2*a4**2*a5*a6**2 + a2*a4**2*a6**3 + a2*a4*a5**2*a6**2 + a2*a4*a5*a6**3 + a3**2*a4*a5*a6**2 + a3**2*a4*a6**3 + a3**2*a5**2*a6**2 + a3**2*a5*a6**3 + a3*a4**2*a5*a6**2 + a3*a4**2*a6**3 + a3*a4*a5**2*a6**2 + a3*a4*a5*a6**3");
		bigResult = SDS.sds(new BigPoly("abcdef", fn.toString()), T_n);
		assertTrue(!bigResult.isNonNegative());
		System.out.println(bigResult.getNegativeAt());
		*/
	}

	@Test
	public void testVasc() {
		// 5-var Vasc's inequality
		LongPoly fn = replaceAn("a1**3*a3*a4 + a1**3*a3*a5 + a1**3*a4**2 + a1**3*a4*a5 + a1**2*a2**2*a4 + a1**2*a2**2*a5 + a1**2*a2*a3**2 - a1**2*a2*a3*a4 - a1**2*a2*a3*a5 - 2*a1**2*a2*a4**2 - a1**2*a2*a4*a5 + a1**2*a3**3 - 2*a1**2*a3**2*a4 - 2*a1**2*a3**2*a5 - 2*a1**2*a3*a4**2 + a1**2*a3*a5**2 + a1**2*a4**2*a5 + a1**2*a4*a5**2 + a1*a2**3*a4 + a1*a2**3*a5 + a1*a2**2*a3**2 - a1*a2**2*a3*a4 - a1*a2**2*a3*a5 - 2*a1*a2**2*a4**2 + a1*a2**2*a5**2 + a1*a2*a3**3 - a1*a2*a3**2*a4 - a1*a2*a3*a5**2 + a1*a2*a4**3 - a1*a2*a4**2*a5 - a1*a2*a4*a5**2 + a1*a3**3*a5 + a1*a3**2*a4**2 - a1*a3**2*a4*a5 - 2*a1*a3**2*a5**2 + a1*a3*a4**3 - a1*a3*a4**2*a5 - a1*a3*a4*a5**2 + a2**3*a4*a5 + a2**3*a5**2 + a2**2*a3**2*a5 + a2**2*a3*a4**2 - a2**2*a3*a4*a5 - 2*a2**2*a3*a5**2 + a2**2*a4**3 - 2*a2**2*a4**2*a5 - 2*a2**2*a4*a5**2 + a2*a3**3*a5 + a2*a3**2*a4**2 - a2*a3**2*a4*a5 - 2*a2*a3**2*a5**2 + a2*a3*a4**3 - a2*a3*a4**2*a5 + a2*a3*a5**3 + a2*a4**2*a5**2 + a2*a4*a5**3 + a3**2*a4*a5**2 + a3**2*a5**3 + a3*a4**2*a5**2 + a3*a4*a5**3");
		LongPoly fd = replaceAn("a1**2*a2*a3*a4 + a1**2*a2*a3*a5 + a1**2*a2*a4**2 + a1**2*a2*a4*a5 + a1**2*a3**2*a4 + a1**2*a3**2*a5 + a1**2*a3*a4**2 + a1**2*a3*a4*a5 + a1*a2**2*a3*a4 + a1*a2**2*a3*a5 + a1*a2**2*a4**2 + a1*a2**2*a4*a5 + a1*a2*a3**2*a4 + a1*a2*a3**2*a5 + a1*a2*a3*a4**2 + 2*a1*a2*a3*a4*a5 + a1*a2*a3*a5**2 + a1*a2*a4**2*a5 + a1*a2*a4*a5**2 + a1*a3**2*a4*a5 + a1*a3**2*a5**2 + a1*a3*a4**2*a5 + a1*a3*a4*a5**2 + a2**2*a3*a4*a5 + a2**2*a3*a5**2 + a2**2*a4**2*a5 + a2**2*a4*a5**2 + a2*a3**2*a4*a5 + a2*a3**2*a5**2 + a2*a3*a4**2*a5 + a2*a3*a4*a5**2");
		SDS.Result<MutableLong> result = SDS.sds(fn);
		// T_5 works; Z_5 and Y_5 doesn't work
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1, 1, 1]]", getZeroAt(fn, fd, result.getZeroAt()).toString());
		assertEquals(2, result.getDepth());
		// 7-var Vasc's inequality, too slow even if skip finding negative
		/*
		fn = replaceAn("a1**3*a3*a4*a5*a6 + a1**3*a3*a4*a5*a7 + a1**3*a3*a4*a6**2 + a1**3*a3*a4*a6*a7 + a1**3*a3*a5**2*a6 + a1**3*a3*a5**2*a7 + a1**3*a3*a5*a6**2 + a1**3*a3*a5*a6*a7 + a1**3*a4**2*a5*a6 + a1**3*a4**2*a5*a7 + a1**3*a4**2*a6**2 + a1**3*a4**2*a6*a7 + a1**3*a4*a5**2*a6 + a1**3*a4*a5**2*a7 + a1**3*a4*a5*a6**2 + a1**3*a4*a5*a6*a7 + a1**2*a2**2*a4*a5*a6 + a1**2*a2**2*a4*a5*a7 + a1**2*a2**2*a4*a6**2 + a1**2*a2**2*a4*a6*a7 + a1**2*a2**2*a5**2*a6 + a1**2*a2**2*a5**2*a7 + a1**2*a2**2*a5*a6**2 + a1**2*a2**2*a5*a6*a7 + a1**2*a2*a3**2*a5*a6 + a1**2*a2*a3**2*a5*a7 + a1**2*a2*a3**2*a6**2 + a1**2*a2*a3**2*a6*a7 + a1**2*a2*a3*a4**2*a6 + a1**2*a2*a3*a4**2*a7 + a1**2*a2*a3*a4*a5**2 - a1**2*a2*a3*a4*a5*a6 - a1**2*a2*a3*a4*a5*a7 - 2*a1**2*a2*a3*a4*a6**2 - a1**2*a2*a3*a4*a6*a7 + a1**2*a2*a3*a5**3 - 2*a1**2*a2*a3*a5**2*a6 - 2*a1**2*a2*a3*a5**2*a7 - 2*a1**2*a2*a3*a5*a6**2 - a1**2*a2*a3*a5*a6*a7 + a1**2*a2*a4**3*a6 + a1**2*a2*a4**3*a7 + a1**2*a2*a4**2*a5**2 - 2*a1**2*a2*a4**2*a5*a6 - 2*a1**2*a2*a4**2*a5*a7 - 3*a1**2*a2*a4**2*a6**2 - 2*a1**2*a2*a4**2*a6*a7 + a1**2*a2*a4*a5**3 - 2*a1**2*a2*a4*a5**2*a6 - 2*a1**2*a2*a4*a5**2*a7 - 2*a1**2*a2*a4*a5*a6**2 - a1**2*a2*a4*a5*a6*a7 + a1**2*a3**3*a5*a6 + a1**2*a3**3*a5*a7 + a1**2*a3**3*a6**2 + a1**2*a3**3*a6*a7 + a1**2*a3**2*a4**2*a6 + a1**2*a3**2*a4**2*a7 + a1**2*a3**2*a4*a5**2 - 2*a1**2*a3**2*a4*a5*a6 - 2*a1**2*a3**2*a4*a5*a7 - 3*a1**2*a3**2*a4*a6**2 - 2*a1**2*a3**2*a4*a6*a7 + a1**2*a3**2*a5**3 - 3*a1**2*a3**2*a5**2*a6 - 3*a1**2*a3**2*a5**2*a7 - 3*a1**2*a3**2*a5*a6**2 - 2*a1**2*a3**2*a5*a6*a7 + a1**2*a3*a4**3*a6 + a1**2*a3*a4**3*a7 + a1**2*a3*a4**2*a5**2 - 2*a1**2*a3*a4**2*a5*a6 - 2*a1**2*a3*a4**2*a5*a7 - 3*a1**2*a3*a4**2*a6**2 - 2*a1**2*a3*a4**2*a6*a7 + a1**2*a3*a4*a5**3 - 2*a1**2*a3*a4*a5**2*a6 - 2*a1**2*a3*a4*a5**2*a7 - 2*a1**2*a3*a4*a5*a6**2 + a1**2*a3*a4*a5*a7**2 + a1**2*a3*a4*a6**2*a7 + a1**2*a3*a4*a6*a7**2 + a1**2*a3*a5**2*a6*a7 + a1**2*a3*a5**2*a7**2 + a1**2*a3*a5*a6**2*a7 + a1**2*a3*a5*a6*a7**2 + a1**2*a4**2*a5*a6*a7 + a1**2*a4**2*a5*a7**2 + a1**2*a4**2*a6**2*a7 + a1**2*a4**2*a6*a7**2 + a1**2*a4*a5**2*a6*a7 + a1**2*a4*a5**2*a7**2 + a1**2*a4*a5*a6**2*a7 + a1**2*a4*a5*a6*a7**2 + a1*a2**3*a4*a5*a6 + a1*a2**3*a4*a5*a7 + a1*a2**3*a4*a6**2 + a1*a2**3*a4*a6*a7 + a1*a2**3*a5**2*a6 + a1*a2**3*a5**2*a7 + a1*a2**3*a5*a6**2 + a1*a2**3*a5*a6*a7 + a1*a2**2*a3**2*a5*a6 + a1*a2**2*a3**2*a5*a7 + a1*a2**2*a3**2*a6**2 + a1*a2**2*a3**2*a6*a7 + a1*a2**2*a3*a4**2*a6 + a1*a2**2*a3*a4**2*a7 + a1*a2**2*a3*a4*a5**2 - a1*a2**2*a3*a4*a5*a6 - a1*a2**2*a3*a4*a5*a7 - 2*a1*a2**2*a3*a4*a6**2 - a1*a2**2*a3*a4*a6*a7 + a1*a2**2*a3*a5**3 - 2*a1*a2**2*a3*a5**2*a6 - 2*a1*a2**2*a3*a5**2*a7 - 2*a1*a2**2*a3*a5*a6**2 - a1*a2**2*a3*a5*a6*a7 + a1*a2**2*a4**3*a6 + a1*a2**2*a4**3*a7 + a1*a2**2*a4**2*a5**2 - 2*a1*a2**2*a4**2*a5*a6 - 2*a1*a2**2*a4**2*a5*a7 - 3*a1*a2**2*a4**2*a6**2 - 2*a1*a2**2*a4**2*a6*a7 + a1*a2**2*a4*a5**3 - 2*a1*a2**2*a4*a5**2*a6 - 2*a1*a2**2*a4*a5**2*a7 - 2*a1*a2**2*a4*a5*a6**2 + a1*a2**2*a4*a5*a7**2 + a1*a2**2*a4*a6**2*a7 + a1*a2**2*a4*a6*a7**2 + a1*a2**2*a5**2*a6*a7 + a1*a2**2*a5**2*a7**2 + a1*a2**2*a5*a6**2*a7 + a1*a2**2*a5*a6*a7**2 + a1*a2*a3**3*a5*a6 + a1*a2*a3**3*a5*a7 + a1*a2*a3**3*a6**2 + a1*a2*a3**3*a6*a7 + a1*a2*a3**2*a4**2*a6 + a1*a2*a3**2*a4**2*a7 + a1*a2*a3**2*a4*a5**2 - a1*a2*a3**2*a4*a5*a6 - a1*a2*a3**2*a4*a5*a7 - 2*a1*a2*a3**2*a4*a6**2 - a1*a2*a3**2*a4*a6*a7 + a1*a2*a3**2*a5**3 - 2*a1*a2*a3**2*a5**2*a6 - 2*a1*a2*a3**2*a5**2*a7 - 2*a1*a2*a3**2*a5*a6**2 + a1*a2*a3**2*a5*a7**2 + a1*a2*a3**2*a6**2*a7 + a1*a2*a3**2*a6*a7**2 + a1*a2*a3*a4**3*a6 + a1*a2*a3*a4**3*a7 + a1*a2*a3*a4**2*a5**2 - a1*a2*a3*a4**2*a5*a6 - a1*a2*a3*a4**2*a5*a7 - 2*a1*a2*a3*a4**2*a6**2 + a1*a2*a3*a4**2*a7**2 + a1*a2*a3*a4*a5**3 - a1*a2*a3*a4*a5**2*a6 - a1*a2*a3*a4*a5*a7**2 + a1*a2*a3*a4*a6**3 - a1*a2*a3*a4*a6**2*a7 - a1*a2*a3*a4*a6*a7**2 + a1*a2*a3*a5**3*a7 + a1*a2*a3*a5**2*a6**2 - a1*a2*a3*a5**2*a6*a7 - 2*a1*a2*a3*a5**2*a7**2 + a1*a2*a3*a5*a6**3 - a1*a2*a3*a5*a6**2*a7 - a1*a2*a3*a5*a6*a7**2 + a1*a2*a4**3*a6*a7 + a1*a2*a4**3*a7**2 + a1*a2*a4**2*a5**2*a7 + a1*a2*a4**2*a5*a6**2 - a1*a2*a4**2*a5*a6*a7 - 2*a1*a2*a4**2*a5*a7**2 + a1*a2*a4**2*a6**3 - 2*a1*a2*a4**2*a6**2*a7 - 2*a1*a2*a4**2*a6*a7**2 + a1*a2*a4*a5**3*a7 + a1*a2*a4*a5**2*a6**2 - a1*a2*a4*a5**2*a6*a7 - 2*a1*a2*a4*a5**2*a7**2 + a1*a2*a4*a5*a6**3 - a1*a2*a4*a5*a6**2*a7 - a1*a2*a4*a5*a6*a7**2 + a1*a3**3*a5*a6*a7 + a1*a3**3*a5*a7**2 + a1*a3**3*a6**2*a7 + a1*a3**3*a6*a7**2 + a1*a3**2*a4**2*a6*a7 + a1*a3**2*a4**2*a7**2 + a1*a3**2*a4*a5**2*a7 + a1*a3**2*a4*a5*a6**2 - a1*a3**2*a4*a5*a6*a7 - 2*a1*a3**2*a4*a5*a7**2 + a1*a3**2*a4*a6**3 - 2*a1*a3**2*a4*a6**2*a7 - 2*a1*a3**2*a4*a6*a7**2 + a1*a3**2*a5**3*a7 + a1*a3**2*a5**2*a6**2 - 2*a1*a3**2*a5**2*a6*a7 - 3*a1*a3**2*a5**2*a7**2 + a1*a3**2*a5*a6**3 - 2*a1*a3**2*a5*a6**2*a7 - 2*a1*a3**2*a5*a6*a7**2 + a1*a3*a4**3*a6*a7 + a1*a3*a4**3*a7**2 + a1*a3*a4**2*a5**2*a7 + a1*a3*a4**2*a5*a6**2 - a1*a3*a4**2*a5*a6*a7 - 2*a1*a3*a4**2*a5*a7**2 + a1*a3*a4**2*a6**3 - 2*a1*a3*a4**2*a6**2*a7 - 2*a1*a3*a4**2*a6*a7**2 + a1*a3*a4*a5**3*a7 + a1*a3*a4*a5**2*a6**2 - a1*a3*a4*a5**2*a6*a7 - 2*a1*a3*a4*a5**2*a7**2 + a1*a3*a4*a5*a6**3 - a1*a3*a4*a5*a6**2*a7 - a1*a3*a4*a5*a6*a7**2 + a2**3*a4*a5*a6*a7 + a2**3*a4*a5*a7**2 + a2**3*a4*a6**2*a7 + a2**3*a4*a6*a7**2 + a2**3*a5**2*a6*a7 + a2**3*a5**2*a7**2 + a2**3*a5*a6**2*a7 + a2**3*a5*a6*a7**2 + a2**2*a3**2*a5*a6*a7 + a2**2*a3**2*a5*a7**2 + a2**2*a3**2*a6**2*a7 + a2**2*a3**2*a6*a7**2 + a2**2*a3*a4**2*a6*a7 + a2**2*a3*a4**2*a7**2 + a2**2*a3*a4*a5**2*a7 + a2**2*a3*a4*a5*a6**2 - a2**2*a3*a4*a5*a6*a7 - 2*a2**2*a3*a4*a5*a7**2 + a2**2*a3*a4*a6**3 - 2*a2**2*a3*a4*a6**2*a7 - 2*a2**2*a3*a4*a6*a7**2 + a2**2*a3*a5**3*a7 + a2**2*a3*a5**2*a6**2 - 2*a2**2*a3*a5**2*a6*a7 - 3*a2**2*a3*a5**2*a7**2 + a2**2*a3*a5*a6**3 - 2*a2**2*a3*a5*a6**2*a7 - 2*a2**2*a3*a5*a6*a7**2 + a2**2*a4**3*a6*a7 + a2**2*a4**3*a7**2 + a2**2*a4**2*a5**2*a7 + a2**2*a4**2*a5*a6**2 - 2*a2**2*a4**2*a5*a6*a7 - 3*a2**2*a4**2*a5*a7**2 + a2**2*a4**2*a6**3 - 3*a2**2*a4**2*a6**2*a7 - 3*a2**2*a4**2*a6*a7**2 + a2**2*a4*a5**3*a7 + a2**2*a4*a5**2*a6**2 - 2*a2**2*a4*a5**2*a6*a7 - 3*a2**2*a4*a5**2*a7**2 + a2**2*a4*a5*a6**3 - 2*a2**2*a4*a5*a6**2*a7 - 2*a2**2*a4*a5*a6*a7**2 + a2*a3**3*a5*a6*a7 + a2*a3**3*a5*a7**2 + a2*a3**3*a6**2*a7 + a2*a3**3*a6*a7**2 + a2*a3**2*a4**2*a6*a7 + a2*a3**2*a4**2*a7**2 + a2*a3**2*a4*a5**2*a7 + a2*a3**2*a4*a5*a6**2 - a2*a3**2*a4*a5*a6*a7 - 2*a2*a3**2*a4*a5*a7**2 + a2*a3**2*a4*a6**3 - 2*a2*a3**2*a4*a6**2*a7 - 2*a2*a3**2*a4*a6*a7**2 + a2*a3**2*a5**3*a7 + a2*a3**2*a5**2*a6**2 - 2*a2*a3**2*a5**2*a6*a7 - 3*a2*a3**2*a5**2*a7**2 + a2*a3**2*a5*a6**3 - 2*a2*a3**2*a5*a6**2*a7 - 2*a2*a3**2*a5*a6*a7**2 + a2*a3*a4**3*a6*a7 + a2*a3*a4**3*a7**2 + a2*a3*a4**2*a5**2*a7 + a2*a3*a4**2*a5*a6**2 - a2*a3*a4**2*a5*a6*a7 - 2*a2*a3*a4**2*a5*a7**2 + a2*a3*a4**2*a6**3 - 2*a2*a3*a4**2*a6**2*a7 - 2*a2*a3*a4**2*a6*a7**2 + a2*a3*a4*a5**3*a7 + a2*a3*a4*a5**2*a6**2 - a2*a3*a4*a5**2*a6*a7 - 2*a2*a3*a4*a5**2*a7**2 + a2*a3*a4*a5*a6**3 - a2*a3*a4*a5*a6**2*a7 + a2*a3*a4*a5*a7**3 + a2*a3*a4*a6**2*a7**2 + a2*a3*a4*a6*a7**3 + a2*a3*a5**2*a6*a7**2 + a2*a3*a5**2*a7**3 + a2*a3*a5*a6**2*a7**2 + a2*a3*a5*a6*a7**3 + a2*a4**2*a5*a6*a7**2 + a2*a4**2*a5*a7**3 + a2*a4**2*a6**2*a7**2 + a2*a4**2*a6*a7**3 + a2*a4*a5**2*a6*a7**2 + a2*a4*a5**2*a7**3 + a2*a4*a5*a6**2*a7**2 + a2*a4*a5*a6*a7**3 + a3**2*a4*a5*a6*a7**2 + a3**2*a4*a5*a7**3 + a3**2*a4*a6**2*a7**2 + a3**2*a4*a6*a7**3 + a3**2*a5**2*a6*a7**2 + a3**2*a5**2*a7**3 + a3**2*a5*a6**2*a7**2 + a3**2*a5*a6*a7**3 + a3*a4**2*a5*a6*a7**2 + a3*a4**2*a5*a7**3 + a3*a4**2*a6**2*a7**2 + a3*a4**2*a6*a7**3 + a3*a4*a5**2*a6*a7**2 + a3*a4*a5**2*a7**3 + a3*a4*a5*a6**2*a7**2 + a3*a4*a5*a6*a7**3");
		// fd = replaceAn("a1**2*a2*a3*a4*a5*a6 + a1**2*a2*a3*a4*a5*a7 + a1**2*a2*a3*a4*a6**2 + a1**2*a2*a3*a4*a6*a7 + a1**2*a2*a3*a5**2*a6 + a1**2*a2*a3*a5**2*a7 + a1**2*a2*a3*a5*a6**2 + a1**2*a2*a3*a5*a6*a7 + a1**2*a2*a4**2*a5*a6 + a1**2*a2*a4**2*a5*a7 + a1**2*a2*a4**2*a6**2 + a1**2*a2*a4**2*a6*a7 + a1**2*a2*a4*a5**2*a6 + a1**2*a2*a4*a5**2*a7 + a1**2*a2*a4*a5*a6**2 + a1**2*a2*a4*a5*a6*a7 + a1**2*a3**2*a4*a5*a6 + a1**2*a3**2*a4*a5*a7 + a1**2*a3**2*a4*a6**2 + a1**2*a3**2*a4*a6*a7 + a1**2*a3**2*a5**2*a6 + a1**2*a3**2*a5**2*a7 + a1**2*a3**2*a5*a6**2 + a1**2*a3**2*a5*a6*a7 + a1**2*a3*a4**2*a5*a6 + a1**2*a3*a4**2*a5*a7 + a1**2*a3*a4**2*a6**2 + a1**2*a3*a4**2*a6*a7 + a1**2*a3*a4*a5**2*a6 + a1**2*a3*a4*a5**2*a7 + a1**2*a3*a4*a5*a6**2 + a1**2*a3*a4*a5*a6*a7 + a1*a2**2*a3*a4*a5*a6 + a1*a2**2*a3*a4*a5*a7 + a1*a2**2*a3*a4*a6**2 + a1*a2**2*a3*a4*a6*a7 + a1*a2**2*a3*a5**2*a6 + a1*a2**2*a3*a5**2*a7 + a1*a2**2*a3*a5*a6**2 + a1*a2**2*a3*a5*a6*a7 + a1*a2**2*a4**2*a5*a6 + a1*a2**2*a4**2*a5*a7 + a1*a2**2*a4**2*a6**2 + a1*a2**2*a4**2*a6*a7 + a1*a2**2*a4*a5**2*a6 + a1*a2**2*a4*a5**2*a7 + a1*a2**2*a4*a5*a6**2 + a1*a2**2*a4*a5*a6*a7 + a1*a2*a3**2*a4*a5*a6 + a1*a2*a3**2*a4*a5*a7 + a1*a2*a3**2*a4*a6**2 + a1*a2*a3**2*a4*a6*a7 + a1*a2*a3**2*a5**2*a6 + a1*a2*a3**2*a5**2*a7 + a1*a2*a3**2*a5*a6**2 + a1*a2*a3**2*a5*a6*a7 + a1*a2*a3*a4**2*a5*a6 + a1*a2*a3*a4**2*a5*a7 + a1*a2*a3*a4**2*a6**2 + a1*a2*a3*a4**2*a6*a7 + a1*a2*a3*a4*a5**2*a6 + a1*a2*a3*a4*a5**2*a7 + a1*a2*a3*a4*a5*a6**2 + 2*a1*a2*a3*a4*a5*a6*a7 + a1*a2*a3*a4*a5*a7**2 + a1*a2*a3*a4*a6**2*a7 + a1*a2*a3*a4*a6*a7**2 + a1*a2*a3*a5**2*a6*a7 + a1*a2*a3*a5**2*a7**2 + a1*a2*a3*a5*a6**2*a7 + a1*a2*a3*a5*a6*a7**2 + a1*a2*a4**2*a5*a6*a7 + a1*a2*a4**2*a5*a7**2 + a1*a2*a4**2*a6**2*a7 + a1*a2*a4**2*a6*a7**2 + a1*a2*a4*a5**2*a6*a7 + a1*a2*a4*a5**2*a7**2 + a1*a2*a4*a5*a6**2*a7 + a1*a2*a4*a5*a6*a7**2 + a1*a3**2*a4*a5*a6*a7 + a1*a3**2*a4*a5*a7**2 + a1*a3**2*a4*a6**2*a7 + a1*a3**2*a4*a6*a7**2 + a1*a3**2*a5**2*a6*a7 + a1*a3**2*a5**2*a7**2 + a1*a3**2*a5*a6**2*a7 + a1*a3**2*a5*a6*a7**2 + a1*a3*a4**2*a5*a6*a7 + a1*a3*a4**2*a5*a7**2 + a1*a3*a4**2*a6**2*a7 + a1*a3*a4**2*a6*a7**2 + a1*a3*a4*a5**2*a6*a7 + a1*a3*a4*a5**2*a7**2 + a1*a3*a4*a5*a6**2*a7 + a1*a3*a4*a5*a6*a7**2 + a2**2*a3*a4*a5*a6*a7 + a2**2*a3*a4*a5*a7**2 + a2**2*a3*a4*a6**2*a7 + a2**2*a3*a4*a6*a7**2 + a2**2*a3*a5**2*a6*a7 + a2**2*a3*a5**2*a7**2 + a2**2*a3*a5*a6**2*a7 + a2**2*a3*a5*a6*a7**2 + a2**2*a4**2*a5*a6*a7 + a2**2*a4**2*a5*a7**2 + a2**2*a4**2*a6**2*a7 + a2**2*a4**2*a6*a7**2 + a2**2*a4*a5**2*a6*a7 + a2**2*a4*a5**2*a7**2 + a2**2*a4*a5*a6**2*a7 + a2**2*a4*a5*a6*a7**2 + a2*a3**2*a4*a5*a6*a7 + a2*a3**2*a4*a5*a7**2 + a2*a3**2*a4*a6**2*a7 + a2*a3**2*a4*a6*a7**2 + a2*a3**2*a5**2*a6*a7 + a2*a3**2*a5**2*a7**2 + a2*a3**2*a5*a6**2*a7 + a2*a3**2*a5*a6*a7**2 + a2*a3*a4**2*a5*a6*a7 + a2*a3*a4**2*a5*a7**2 + a2*a3*a4**2*a6**2*a7 + a2*a3*a4**2*a6*a7**2 + a2*a3*a4*a5**2*a6*a7 + a2*a3*a4*a5**2*a7**2 + a2*a3*a4*a5*a6**2*a7 + a2*a3*a4*a5*a6*a7**2");
		result = SDS.sds(fn, false, true);
		assertTrue(result.isNonNegative());
		// assertEquals("[[1, 1, 1, 1, 1, 1, 1]]", getZeroAt(fn, fd, result.getZeroAt()).toString());
		assertEquals(2, result.getDepth());
		*/
	}
	
	@Test
	public void testMathSE() {
		// https://math.stackexchange.com/a/2120874
		// https://math.stackexchange.com/q/1775572
		BigPoly f = new BigPoly("xyz", "200*x**7*y**3 + 125*x**7*z**3 + 200*x**6*y**4 - 320*x**6*y**3*z - 200*x**6*y*z**3 - 200*x**6*z**4 - 200*x**4*y**6 + 195*x**4*y**3*z**3 + 200*x**4*z**6 + 125*x**3*y**7 - 200*x**3*y**6*z + 195*x**3*y**4*z**3 + 195*x**3*y**3*z**4 - 320*x**3*y*z**6 + 200*x**3*z**7 - 320*x*y**6*z**3 - 200*x*y**3*z**6 + 200*y**7*z**3 + 200*y**6*z**4 - 200*y**4*z**6 + 125*y**3*z**7");
		SDS.Result<MutableBig> result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 2; H_3 and Z_3 don't work
		assertEquals(3, result.getDepth());
		// https://math.stackexchange.com/q/1777075
		f = new BigPoly("xyz", "325*x**5*y**2 + 125*x**5*z**2 + 325*x**4*y**3 - 845*x**4*y**2*z - 325*x**4*y*z**2 - 325*x**4*z**3 - 325*x**3*y**4 + 720*x**3*y**2*z**2 + 325*x**3*z**4 + 125*x**2*y**5 - 325*x**2*y**4*z + 720*x**2*y**3*z**2 + 720*x**2*y**2*z**3 - 845*x**2*y*z**4 + 325*x**2*z**5 - 845*x*y**4*z**2 - 325*x*y**2*z**4 + 325*y**5*z**2 + 325*y**4*z**3 - 325*y**3*z**4 + 125*y**2*z**5");
		result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 5; H_3 and Z_3 don't work
		assertEquals(4, result.getDepth());
		f = new BigPoly("xyz", "72*x**5*y**2 + 27*x**5*z**2 + 72*x**4*y**3 - 192*x**4*y**2*z - 72*x**4*y*z**2 - 72*x**4*z**3 - 72*x**3*y**4 + 165*x**3*y**2*z**2 + 72*x**3*z**4 + 27*x**2*y**5 - 72*x**2*y**4*z + 165*x**2*y**3*z**2 + 165*x**2*y**2*z**3 - 192*x**2*y*z**4 + 72*x**2*z**5 - 192*x*y**4*z**2 - 72*x*y**2*z**4 + 72*y**5*z**2 + 72*y**4*z**3 - 72*y**3*z**4 + 27*y**2*z**5");
		result = SDS.sds(f, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(2, result.getDepth());
		result = SDS.sds(f, H_3); // Y_3 == H_3
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(3, result.getDepth());
		result = SDS.sds(f, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(2, result.getDepth());
		// https://math.stackexchange.com/q/3526427
		f = new BigPoly("xyz", "x**9*y**3 - x**9*y**2*z - x**9*y*z**2 + x**9*z**3 + 6*x**8*y**4 + x**8*y**3*z - 10*x**8*y**2*z**2 + x**8*y*z**3 + 6*x**8*z**4 + 15*x**7*y**5 + 19*x**7*y**4*z - 26*x**7*y**3*z**2 - 26*x**7*y**2*z**3 + 19*x**7*y*z**4 + 15*x**7*z**5 + 20*x**6*y**6 + 45*x**6*y**5*z - 30*x**6*y**4*z**2 - 110*x**6*y**3*z**3 - 30*x**6*y**2*z**4 + 45*x**6*y*z**5 + 20*x**6*z**6 + 15*x**5*y**7 + 45*x**5*y**6*z - 26*x**5*y**5*z**2 - 202*x**5*y**4*z**3 - 202*x**5*y**3*z**4 - 26*x**5*y**2*z**5 + 45*x**5*y*z**6 + 15*x**5*z**7 + 6*x**4*y**8 + 19*x**4*y**7*z - 30*x**4*y**6*z**2 - 202*x**4*y**5*z**3 + 1410*x**4*y**4*z**4 - 202*x**4*y**3*z**5 - 30*x**4*y**2*z**6 + 19*x**4*y*z**7 + 6*x**4*z**8 + x**3*y**9 + x**3*y**8*z - 26*x**3*y**7*z**2 - 110*x**3*y**6*z**3 - 202*x**3*y**5*z**4 - 202*x**3*y**4*z**5 - 110*x**3*y**3*z**6 - 26*x**3*y**2*z**7 + x**3*y*z**8 + x**3*z**9 - x**2*y**9*z - 10*x**2*y**8*z**2 - 26*x**2*y**7*z**3 - 30*x**2*y**6*z**4 - 26*x**2*y**5*z**5 - 30*x**2*y**4*z**6 - 26*x**2*y**3*z**7 - 10*x**2*y**2*z**8 - x**2*y*z**9 - x*y**9*z**2 + x*y**8*z**3 + 19*x*y**7*z**4 + 45*x*y**6*z**5 + 45*x*y**5*z**6 + 19*x*y**4*z**7 + x*y**3*z**8 - x*y**2*z**9 + y**9*z**3 + 6*y**8*z**4 + 15*y**7*z**5 + 20*y**6*z**6 + 15*y**5*z**7 + 6*y**4*z**8 + y**3*z**9");
		result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 2; H_3 and Z_3 don't work
		assertEquals(4, result.getDepth());
		// https://math.stackexchange.com/q/4575195
		// f4 from 4575195.py when x <= y, z <= 6x
		// A_3, T_3 and H_3 need 2; Z_3 needs 4
		f = new BigPoly("uv", "65229815808*u**20*v**18 + 3841210712064*u**20*v**17 + 106386007523328*u**20*v**16 + 1836062607409152*u**20*v**15 + 22068203379752960*u**20*v**14 + 195647436373622784*u**20*v**13 + 1322388049958756352*u**20*v**12 + 6948379560610750464*u**20*v**11 + 28689781337302706176*u**20*v**10 + 93498839754505694720*u**20*v**9 + 240294278574849852144*u**20*v**8 + 484158188907187919712*u**20*v**7 + 756187219382142505544*u**20*v**6 + 899220031735368259496*u**20*v**5 + 792330160274721563135*u**20*v**4 + 496370871841934860668*u**20*v**3 + 206892147657584998674*u**20*v**2 + 50858358615534673908*u**20*v + 5510843761656428847*u**20 - 65229815808*u**19*v**19 - 1350146457600*u**19*v**18 + 42999176232960*u**19*v**17 + 2369603814555648*u**19*v**16 + 51579654927548416*u**19*v**15 + 701005036633849856*u**19*v**14 + 6717417768146698240*u**19*v**13 + 47935580996177899520*u**19*v**12 + 262218713067253786624*u**19*v**11 + 1116895267830994094848*u**19*v**10 + 3731100410431355981536*u**19*v**9 + 9784250268509396748880*u**19*v**8 + 20047473766377125993560*u**19*v**7 + 31762777495659561595404*u**19*v**6 + 38249095433668111331348*u**19*v**5 + 34092757575753196505872*u**19*v**4 + 21596033768078340803040*u**19*v**3 + 9103780972630352839500*u**19*v**2 + 2265487781297475289428*u**19*v + 248951816106702217416*u**19 + 65229815808*u**18*v**20 + 654663745536*u**18*v**19 - 44640135806976*u**18*v**18 - 1011536181067776*u**18*v**17 + 2188019200491520*u**18*v**16 + 394396218056769536*u**18*v**15 + 7866376405333506048*u**18*v**14 + 90923473483090624512*u**18*v**13 + 727618637635661079552*u**18*v**12 + 4303055218566316588160*u**18*v**11 + 19393146056830067475080*u**18*v**10 + 67600360020170640020088*u**18*v**9 + 183209276225103752102602*u**18*v**8 + 385296873352915265535032*u**18*v**7 + 623420898019711164742910*u**18*v**6 + 763871330645431314320384*u**18*v**5 + 691027727811625547950826*u**18*v**4 + 443588324550540379149864*u**18*v**3 + 189395268117586934823954*u**18*v**2 + 47759245309141330052520*u**18*v + 5326424442242119556532*u**18 + 3841210712064*u**17*v**20 + 149254116999168*u**17*v**19 + 1886187128094720*u**17*v**18 - 2477681687003136*u**17*v**17 - 312297658069811200*u**17*v**16 - 2856637559480068096*u**17*v**15 + 8627374162049439744*u**17*v**14 + 443385666332939274240*u**17*v**13 + 5196474576007995536192*u**17*v**12 + 37285704278127266198920*u**17*v**11 + 189185089546721085256588*u**17*v**10 + 714297700184092922591384*u**17*v**9 + 2049321369748489041006920*u**17*v**8 + 4495251931864888790296692*u**17*v**7 + 7510182847226655523894040*u**17*v**6 + 9434847753100896508502620*u**17*v**5 + 8708208356165973622460808*u**17*v**4 + 5685192739987722574284900*u**17*v**3 + 2464466442731652650252364*u**17*v**2 + 630744700306000573461420*u**17*v + 71467606335042287695872*u**17 + 106386007523328*u**16*v**20 + 5012559784574976*u**16*v**19 + 97037317348589568*u**16*v**18 + 896238464570228736*u**16*v**17 + 1634632375183081472*u**16*v**16 - 54057349806087505920*u**16*v**15 - 640955789871486523392*u**16*v**14 - 2977057360451974976896*u**16*v**13 + 2700683933288823056303*u**16*v**12 + 133447660173066531594476*u**16*v**11 + 1004332479297953331426982*u**16*v**10 + 4586060203139804243916388*u**16*v**9 + 14729002530599219856509654*u**16*v**8 + 34793395760282444251272248*u**16*v**7 + 61212178880761330324275686*u**16*v**6 + 79845551231292862472057136*u**16*v**5 + 75818843825270568353642881*u**16*v**4 + 50621400496302788347769868*u**16*v**3 + 22361675710989253122416556*u**16*v**2 + 5822741245808180372323932*u**16*v + 671293359983341647255906*u**16 + 1836062607409152*u**15*v**20 + 92453259590500352*u**15*v**19 + 2024190106792361984*u**15*v**18 + 24513759096709732352*u**15*v**17 + 162333804134306113536*u**15*v**16 + 272748341746958413824*u**15*v**15 - 5367373508260720663104*u**15*v**14 - 57477665807922310336588*u**15*v**13 - 287854481694601483213944*u**15*v**12 - 676615249265551581622312*u**15*v**11 + 939520541643317102673460*u**15*v**10 + 14766498771022203849270836*u**15*v**9 + 65376514492150191181347972*u**15*v**8 + 180656114731233045033573256*u**15*v**7 + 348753389774622366653702268*u**15*v**6 + 483375471255383417604138356*u**15*v**5 + 478830837024009842260542292*u**15*v**4 + 329822246114852483929088544*u**15*v**3 + 149310057069751504077447552*u**15*v**2 + 39698919342945320102110116*u**15*v + 4667264836237437107147568*u**15 + 22068203379752960*u**14*v**20 + 1140120609823522816*u**14*v**19 + 26324147064008570880*u**14*v**18 + 353579420561536993280*u**14*v**17 + 2959043402993173284864*u**14*v**16 + 14414839716285483674048*u**14*v**15 + 17664024006845285889738*u**14*v**14 - 304867492245939095408440*u**14*v**13 - 2665682274666181643079790*u**14*v**12 - 11642455604939947766114568*u**14*v**11 - 29187067325172329047086866*u**14*v**10 - 24504937074002649369770772*u**14*v**9 + 116789323659398557090839280*u**14*v**8 + 570947014501486195524580780*u**14*v**7 + 1360372766639638604157842322*u**14*v**6 + 2106937353492236012288016664*u**14*v**5 + 2234331927848383274288382306*u**14*v**4 + 1611289022167357306455236100*u**14*v**3 + 754195405690018095657616350*u**14*v**2 + 205893476488459057965773004*u**14*v + 24768428522319866494490868*u**14 + 195647436373622784*u**13*v**20 + 10187021081027084288*u**13*v**19 + 241161572178937577472*u**13*v**18 + 3407882456944984430592*u**13*v**17 + 31503808949341290875520*u**13*v**16 + 192997646543846258387508*u**13*v**15 + 710577570489729650654984*u**13*v**14 + 604618840731253636232436*u**13*v**13 - 10078507505902585174820784*u**13*v**12 - 70165000930478518727509940*u**13*v**11 - 253536321001866467327417920*u**13*v**10 - 558013428596304316755706596*u**13*v**9 - 610771885723591033036840844*u**13*v**8 + 443609520343543104633711956*u**13*v**7 + 3140035078500542768478928260*u**13*v**6 + 6353135959532670237281814572*u**13*v**5 + 7642628311252304248277027708*u**13*v**4 + 5931714507649614797428921692*u**13*v**3 + 2914128146163873086370253332*u**13*v**2 + 824044198321087091442851220*u**13*v + 101968745120491817370357216*u**13 + 1322388049958756352*u**12*v**20 + 68765621190353711104*u**12*v**19 + 1645723529132989793280*u**12*v**18 + 23887499347988119404352*u**12*v**17 + 232574352915658879278735*u**12*v**16 + 1575815864817801684609672*u**12*v**15 + 7335666694090516011668482*u**12*v**14 + 20904618966171000615040880*u**12*v**13 + 12660731623063064669789181*u**12*v**12 - 198098914137719752720902060*u**12*v**11 - 1096718461233375136007039366*u**12*v**10 - 3212266531042140163591463148*u**12*v**9 - 5850800985170173281921332780*u**12*v**8 - 5844937668681766736810441244*u**12*v**7 + 348397183227155024262195600*u**12*v**6 + 11030106506514288001988150860*u**12*v**5 + 18202064642795038323153781349*u**12*v**4 + 16186584619979727695658342120*u**12*v**3 + 8585429585056078382225799552*u**12*v**2 + 2552380039756886262454874520*u**12*v + 327644072523039178528636671*u**12 + 6948379560610750464*u**11*v**20 + 359055821748207413248*u**11*v**19 + 8618021517298813377664*u**11*v**18 + 126836932546147171997768*u**11*v**17 + 1271372438842672898740236*u**11*v**16 + 9091407517824584059977160*u**11*v**15 + 46936837580780722064678584*u**11*v**14 + 170345474622023926748074892*u**11*v**13 + 383589437609031023372899764*u**11*v**12 + 181380231323253777872963088*u**11*v**11 - 2348118546110619304516339624*u**11*v**10 - 10401552516920955841478695776*u**11*v**9 - 24405682517539534445843213008*u**11*v**8 - 35670386108741135774924789976*u**11*v**7 - 29358067690135689917723152332*u**11*v**6 - 2671128605270997057547092572*u**11*v**5 + 24585985280169133617623338888*u**11*v**4 + 30914485585180902633775977264*u**11*v**3 + 18872596624370344752840308028*u**11*v**2 + 6065677931947077405639189816*u**11*v + 819472536856675569383626248*u**11 + 28689781337302706176*u**10*v**20 + 1469086492973050473216*u**10*v**19 + 35193425076565077581064*u**10*v**18 + 521167442912802832547692*u**10*v**17 + 5310560526424213580279990*u**10*v**16 + 39180460184277614403398020*u**10*v**15 + 213921129665726182508239358*u**10*v**14 + 863136047606411998072367712*u**10*v**13 + 2486389331988052982182109066*u**10*v**12 + 4503466313349581969337643880*u**10*v**11 + 1894541262430070772354388084*u**10*v**10 - 16825516050414147249572436932*u**10*v**9 - 60191594655049580504632619218*u**10*v**8 - 112022223502638216646724947044*u**10*v**7 - 128331241226536145703073884810*u**10*v**6 - 82231444964314940610186399388*u**10*v**5 - 8157177969943238653024463574*u**10*v**4 + 33552753381061453207886808384*u**10*v**3 + 29173536282215553815128379832*u**10*v**2 + 10789812878905378872914244300*u**10*v + 1575893461049046424610983872*u**10 + 93498839754505694720*u**9*v**20 + 4737135621622694719456*u**9*v**19 + 112928000328916649591160*u**9*v**18 + 1674461374421572398781080*u**9*v**17 + 17211074821112150058870884*u**9*v**16 + 129348858729868238696426948*u**9*v**15 + 729906446022538923570664108*u**9*v**14 + 3119173107709560705085880700*u**9*v**13 + 10000656269992796847898317060*u**9*v**12 + 23147714059400039040749947792*u**9*v**11 + 34213695573253810987555313724*u**9*v**10 + 14219153465945561589543303048*u**9*v**9 - 71968335390619970485779988280*u**9*v**8 - 210846196634120456722434261420*u**9*v**7 - 308072459026918689812876269768*u**9*v**6 - 270262744581205935830460296316*u**9*v**5 - 128560539143695873892743109104*u**9*v**4 - 8344597125863522942029135320*u**9*v**3 + 26093451462716818269550902600*u**9*v**2 + 13560344478967761148450315824*u**9*v + 2270084006035581764305694688*u**9 + 240294278574849852144*u**8*v**20 + 12038881365626053615568*u**8*v**19 + 285076179477477369092522*u**8*v**18 + 4219028528185266507765112*u**8*v**17 + 43524111305756528814668630*u**8*v**16 + 330579726925275721073685508*u**8*v**15 + 1903120579751749508438152624*u**8*v**14 + 8415220246453875164937490036*u**8*v**13 + 28594607933538691701582589076*u**8*v**12 + 73610911598974954284459835840*u**8*v**11 + 137946922819278822852409393470*u**8*v**10 + 168133202063574748584101672344*u**8*v**9 + 72001362470008539318623407956*u**8*v**8 - 177482118106503727927899106884*u**8*v**7 - 437521207412462638047334477010*u**8*v**6 - 496251780716940199969697851708*u**8*v**5 - 324275635614153612405682703462*u**8*v**4 - 108323538371132866040848715808*u**8*v**3 - 2409543417726584772910034598*u**8*v**2 + 10169234999357603152736618280*u**8*v + 2322415862539889375265066936*u**8 + 484158188907187919712*u**7*v**20 + 23990109346605396686104*u**7*v**19 + 563759095280458611735000*u**7*v**18 + 8310796569949273585765012*u**7*v**17 + 85760741539098999011892920*u**7*v**16 + 654896685737005891834007832*u**7*v**15 + 3815455613976403626519071932*u**7*v**14 + 17229362309264607539386854340*u**7*v**13 + 60611781216037236969007839236*u**7*v**12 + 165314325255285221179057140920*u**7*v**11 + 343576920272132209204924317404*u**7*v**10 + 523138645009238377620876811252*u**7*v**9 + 528770328293273834719118443980*u**7*v**8 + 231020682866034197863115263136*u**7*v**7 - 232921218216575180922837319120*u**7*v**6 - 517256448905855561475215604140*u**7*v**5 - 449908832075975398077939819576*u**7*v**4 - 210720175992174259207255140360*u**7*v**3 - 45437790855428587032742451088*u**7*v**2 + 679795496331731525726102880*u**7*v + 1476376350054404965646256576*u**7 + 756187219382142505544*u**6*v**20 + 37090917951747492594668*u**6*v**19 + 864855745961467396841774*u**6*v**18 + 12685150124379612041919928*u**6*v**17 + 130653264239775973990217206*u**6*v**16 + 999607138646030616615551580*u**6*v**15 + 5862515230275051390908945394*u**6*v**14 + 26815831374158001267758267172*u**6*v**13 + 96392058551500160466501290544*u**6*v**12 + 272176198453602026139841054948*u**6*v**11 + 598553623477934642879284313206*u**6*v**10 + 1005771050773238683494090078584*u**6*v**9 + 1243963774788441116427829184222*u**6*v**8 + 1042815987931432013081989935104*u**6*v**7 + 447168278556978781460219967978*u**6*v**6 - 126610942170699714853402549852*u**6*v**5 - 325361573034532065836476665892*u**6*v**4 - 214706218907164635070122578676*u**6*v**3 - 67743152771568155521260085512*u**6*v**2 - 8022744013350646619827017264*u**6*v + 284403080115663825940741728*u**6 + 899220031735368259496*u**5*v**20 + 43737864279846093320276*u**5*v**19 + 1012546144601682832451008*u**5*v**18 + 14771437722034095632103484*u**5*v**17 + 151663351902828060252728784*u**5*v**16 + 1159920445309100550145999476*u**5*v**15 + 6823782978334756008514084568*u**5*v**14 + 31448730568048178711109006124*u**5*v**13 + 114575832812993451130879818572*u**5*v**12 + 330628682065701965720919804852*u**5*v**11 + 752335373717591111068976800292*u**5*v**10 + 1334764027933733572667468464708*u**5*v**9 + 1809554644911204301908327193524*u**5*v**8 + 1810721965504201644419379710692*u**5*v**7 + 1250891049299164701638300394052*u**5*v**6 + 499753228561085793318885124740*u**5*v**5 + 18737257317701958556210653416*u**5*v**4 - 94531843183979060506922984592*u**5*v**3 - 47742940051545903336132268896*u**5*v**2 - 9012092078642451153860630016*u**5*v - 380266070509905784680195072*u**5 + 792330160274721563135*u**4*v**20 + 38323989453676024940832*u**4*v**19 + 882195255683797419363930*u**4*v**18 + 12806819362385544509090760*u**4*v**17 + 131025874449928299037389793*u**4*v**16 + 1000423801869306018845609316*u**4*v**15 + 5890276206196597265006054226*u**4*v**14 + 27255755762988721398231322380*u**4*v**13 + 100117438249566354475502578245*u**4*v**12 + 292924789134384071124923958984*u**4*v**11 + 681122577242823144785075884938*u**4*v**10 + 1249162410841437769404640547856*u**4*v**9 + 1782836352175129358817901312570*u**4*v**8 + 1939417481253929746997009286360*u**4*v**7 + 1557093491154574876444868349564*u**4*v**6 + 873893634416245356928498921368*u**4*v**5 + 306591588704719392663390215087*u**4*v**4 + 45905008286698451656697664120*u**4*v**3 - 7638500013488573854935123000*u**4*v**2 - 3737192430717634550337022752*u**4*v - 309985448637458831443269264*u**4 + 496370871841934860668*u**3*v**20 + 23974454603036473236816*u**3*v**19 + 550183641460106919646824*u**3*v**18 + 7959180855339514955354244*u**3*v**17 + 81178639340281724818558380*u**3*v**16 + 618551251052069193419569536*u**3*v**15 + 3640309249767075928044271188*u**3*v**14 + 16875100526799108599104329612*u**3*v**13 + 62284581733207523406011151912*u**3*v**12 + 183834312598108611461206711440*u**3*v**11 + 433509162940677156827476230720*u**3*v**10 + 812211846708393391961117991528*u**3*v**9 + 1196741119212347962893045805152*u**3*v**8 + 1365666495789634435207115091192*u**3*v**7 + 1181044537086612212475781540140*u**3*v**6 + 750234226070513256305617861104*u**3*v**5 + 333832450695811712478712879656*u**3*v**4 + 96130619550441668569153644864*u**3*v**3 + 15334169985442057773182961024*u**3*v**2 + 871189206503221664562862080*u**3*v - 17738001873547443201253248*u**3 + 206892147657584998674*u**2*v**20 + 10036761880338905776668*u**2*v**19 + 230523473167926950982690*u**2*v**18 + 3331462872353283193192524*u**2*v**17 + 33920446796074032531034860*u**2*v**16 + 258048922966683062897798064*u**2*v**15 + 1517461903995010899326675694*u**2*v**14 + 7038760634826014056594907700*u**2*v**13 + 26049455502371099778356731872*u**2*v**12 + 77309647214208136038858771900*u**2*v**11 + 183999941152579482059412121608*u**2*v**10 + 349672126023539752525884935784*u**2*v**9 + 526117347590744322082162959930*u**2*v**8 + 618834643948157854875706881072*u**2*v**7 + 559150428542648385732290509320*u**2*v**6 + 378917777662586229225964353120*u**2*v**5 + 186226897010988876408587728008*u**2*v**4 + 63186880560710376495535729920*u**2*v**3 + 13706666950291236964880524224*u**2*v**2 + 1667762998403886657965537280*u**2*v + 86639097754925519423617152*u**2 + 50858358615534673908*u*v**20 + 2497343970290545791396*u*v**19 + 57717451835793450089928*u*v**18 + 836309146593249870408396*u*v**17 + 8520307694607768257629692*u*v**16 + 64798386618502675299640500*u*v**15 + 380909645910471299958754668*u*v**14 + 1767343517140515028498492884*u*v**13 + 6550920941362928385033635208*u*v**12 + 19510052638508035840420881336*u*v**11 + 46721793878957745125758672812*u*v**10 + 89653949392723489080403483248*u*v**9 + 136835118992059850395238259384*u*v**8 + 164255961497020444168585007328*u*v**7 + 152689549285977291410567228496*u*v**6 + 107636360150021424041433401856*u*v**5 + 55896706530761226649898594976*u*v**4 + 20504647298311667215980668928*u*v**3 + 4976238048682928732740118016*u*v**2 + 711337332344038381107044352*u*v + 45473551117685795707163136*u + 5510843761656428847*v**20 + 276632086052762979912*v**19 + 6478717463331333643620*v**18 + 94581083418134457016080*v**17 + 967345888509503742904002*v**16 + 7370025863584226538904128*v**15 + 43358120943437331572445396*v**14 + 201301918015167527741249040*v**13 + 747052847110859193124162335*v**12 + 2230253146194555594045120696*v**11 + 5363696572643722057846018992*v**10 + 10362384623330148313730300256*v**9 + 15975713676673983700176547320*v**8 + 19452343556242197470918681280*v**7 + 18439365108349415882408514336*v**6 + 13344578759203717757611903488*v**5 + 7176223707226916093759644272*v**4 + 2756555593336997173051862400*v**3 + 710453688752988551461046400*v**2 + 109609995046808660108539392*v + 7654919029916503885201152").homogenize('w');
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals(2, result.getDepth());
	}

	@Test
	public void testXiong23() {
		// ISBN 9787542878021, p112, §7.2, ex6
		LongPoly f = replaceAn("17*a1**12 + 156*a1**11*a2 + 156*a1**11*a3 + 108*a1**11*a4 + 642*a1**10*a2**2 + 1284*a1**10*a2*a3 + 900*a1**10*a2*a4 + 642*a1**10*a3**2 + 900*a1**10*a3*a4 + 258*a1**10*a4**2 + 1020*a1**9*a2**3 + 4692*a1**9*a2**2*a3 + 3348*a1**9*a2**2*a4 + 4692*a1**9*a2*a3**2 + 6696*a1**9*a2*a3*a4 + 2004*a1**9*a2*a4**2 + 1836*a1**9*a3**3 + 3348*a1**9*a3**2*a4 + 2004*a1**9*a3*a4**2 + 492*a1**9*a4**3 - 33*a1**8*a2**4 + 7500*a1**8*a2**3*a3 + 4044*a1**8*a2**3*a4 + 15066*a1**8*a2**2*a3**2 + 22068*a1**8*a2**2*a3*a4 + 7002*a1**8*a2**2*a4**2 + 10908*a1**8*a2*a3**3 + 22068*a1**8*a2*a3**2*a4 + 14004*a1**8*a2*a3*a4**2 + 3660*a1**8*a2*a4**3 + 4191*a1**8*a3**4 + 8268*a1**8*a3**3*a4 + 7002*a1**8*a3**2*a4**2 + 2844*a1**8*a3*a4**3 + 735*a1**8*a4**4 - 1800*a1**7*a2**5 + 4824*a1**7*a2**4*a3 - 2376*a1**7*a2**4*a4 + 23472*a1**7*a2**3*a3**2 + 29664*a1**7*a2**3*a3*a4 + 6192*a1**7*a2**3*a4**2 + 28272*a1**7*a2**2*a3**3 + 64080*a1**7*a2**2*a3**2*a4 + 43920*a1**7*a2**2*a3*a4**2 + 12336*a1**7*a2**2*a4**3 + 18648*a1**7*a2*a3**4 + 43488*a1**7*a2*a3**3*a4 + 43920*a1**7*a2*a3**2*a4**2 + 20448*a1**7*a2*a3*a4**3 + 5592*a1**7*a2*a4**4 + 7224*a1**7*a3**5 + 15672*a1**7*a3**4*a4 + 15216*a1**7*a3**3*a4**2 + 8112*a1**7*a3**2*a4**3 + 1368*a1**7*a3*a4**4 + 24*a1**7*a4**5 - 1636*a1**6*a2**6 + 1896*a1**6*a2**5*a3 - 8472*a1**6*a2**5*a4 + 22308*a1**6*a2**4*a3**2 + 15816*a1**6*a2**4*a3*a4 - 6492*a1**6*a2**4*a4**2 + 30192*a1**6*a2**3*a3**3 + 89808*a1**6*a2**3*a3**2*a4 + 55248*a1**6*a2**3*a3*a4**2 + 4656*a1**6*a2**3*a4**3 + 35364*a1**6*a2**2*a3**4 + 102864*a1**6*a2**2*a3**3*a4 + 123480*a1**6*a2**2*a3**2*a4**2 + 65808*a1**6*a2**2*a3*a4**3 + 18852*a1**6*a2**2*a4**4 + 23976*a1**6*a2*a3**5 + 59976*a1**6*a2*a3**4*a4 + 77328*a1**6*a2*a3**3*a4**2 + 56784*a1**6*a2*a3**2*a4**3 + 19656*a1**6*a2*a3*a4**4 + 4200*a1**6*a2*a4**5 + 8732*a1**6*a3**6 + 22632*a1**6*a3**5*a4 + 24612*a1**6*a3**4*a4**2 + 19056*a1**6*a3**3*a4**3 + 804*a1**6*a3**2*a4**4 - 4824*a1**6*a3*a4**5 - 1636*a1**6*a4**6 + 24*a1**5*a2**7 + 4200*a1**5*a2**6*a3 - 4824*a1**5*a2**6*a4 + 20664*a1**5*a2**5*a3**2 + 10224*a1**5*a2**5*a3*a4 - 10440*a1**5*a2**5*a4**2 + 10344*a1**5*a2**4*a3**3 + 84312*a1**5*a2**4*a3**2*a4 + 41112*a1**5*a2**4*a3*a4**2 - 9432*a1**5*a2**4*a4**3 + 24264*a1**5*a2**3*a3**4 + 109344*a1**5*a2**3*a3**3*a4 + 175536*a1**5*a2**3*a3**2*a4**2 + 67872*a1**5*a2**3*a3*a4**3 + 840*a1**5*a2**3*a4**4 + 32760*a1**5*a2**2*a3**5 + 108504*a1**5*a2**2*a3**4*a4 + 187632*a1**5*a2**2*a3**3*a4**2 + 170352*a1**5*a2**2*a3**2*a4**3 + 79128*a1**5*a2**2*a3*a4**4 + 20664*a1**5*a2**2*a4**5 + 22632*a1**5*a2*a3**6 + 65520*a1**5*a2*a3**5*a4 + 96408*a1**5*a2*a3**4*a4**2 + 93984*a1**5*a2*a3**3*a4**3 + 48024*a1**5*a2*a3**2*a4**4 + 10224*a1**5*a2*a3*a4**5 + 1896*a1**5*a2*a4**6 + 7224*a1**5*a3**7 + 23976*a1**5*a3**6*a4 + 32760*a1**5*a3**5*a4**2 + 24360*a1**5*a3**4*a4**3 + 5352*a1**5*a3**3*a4**4 - 10440*a1**5*a3**2*a4**5 - 8472*a1**5*a3*a4**6 - 1800*a1**5*a4**7 + 735*a1**4*a2**8 + 5592*a1**4*a2**7*a3 + 1368*a1**4*a2**7*a4 + 18852*a1**4*a2**6*a3**2 + 19656*a1**4*a2**6*a3*a4 + 804*a1**4*a2**6*a4**2 + 840*a1**4*a2**5*a3**3 + 79128*a1**4*a2**5*a3**2*a4 + 48024*a1**4*a2**5*a3*a4**2 + 5352*a1**4*a2**5*a4**3 - 1926*a1**4*a2**4*a3**4 + 76488*a1**4*a2**4*a3**3*a4 + 184860*a1**4*a2**4*a3**2*a4**2 + 68904*a1**4*a2**4*a3*a4**3 - 1926*a1**4*a2**4*a4**4 + 24360*a1**4*a2**3*a3**5 + 99144*a1**4*a2**3*a3**4*a4 + 238224*a1**4*a2**3*a3**3*a4**2 + 229584*a1**4*a2**3*a3**2*a4**3 + 76488*a1**4*a2**3*a3*a4**4 + 10344*a1**4*a2**3*a4**5 + 24612*a1**4*a2**2*a3**6 + 96408*a1**4*a2**2*a3**5*a4 + 202140*a1**4*a2**2*a3**4*a4**2 + 240912*a1**4*a2**2*a3**3*a4**3 + 184860*a1**4*a2**2*a3**2*a4**4 + 84312*a1**4*a2**2*a3*a4**5 + 22308*a1**4*a2**2*a4**6 + 15672*a1**4*a2*a3**7 + 59976*a1**4*a2*a3**6*a4 + 108504*a1**4*a2*a3**5*a4**2 + 99144*a1**4*a2*a3**4*a4**3 + 68904*a1**4*a2*a3**3*a4**4 + 41112*a1**4*a2*a3**2*a4**5 + 15816*a1**4*a2*a3*a4**6 + 4824*a1**4*a2*a4**7 + 4191*a1**4*a3**8 + 18648*a1**4*a3**7*a4 + 35364*a1**4*a3**6*a4**2 + 24264*a1**4*a3**5*a4**3 - 1926*a1**4*a3**4*a4**4 - 9432*a1**4*a3**3*a4**5 - 6492*a1**4*a3**2*a4**6 - 2376*a1**4*a3*a4**7 - 33*a1**4*a4**8 + 492*a1**3*a2**9 + 3660*a1**3*a2**8*a3 + 2844*a1**3*a2**8*a4 + 12336*a1**3*a2**7*a3**2 + 20448*a1**3*a2**7*a3*a4 + 8112*a1**3*a2**7*a4**2 + 4656*a1**3*a2**6*a3**3 + 65808*a1**3*a2**6*a3**2*a4 + 56784*a1**3*a2**6*a3*a4**2 + 19056*a1**3*a2**6*a4**3 - 9432*a1**3*a2**5*a3**4 + 67872*a1**3*a2**5*a3**3*a4 + 170352*a1**3*a2**5*a3**2*a4**2 + 93984*a1**3*a2**5*a3*a4**3 + 24360*a1**3*a2**5*a4**4 + 5352*a1**3*a2**4*a3**5 + 68904*a1**3*a2**4*a3**4*a4 + 229584*a1**3*a2**4*a3**3*a4**2 + 240912*a1**3*a2**4*a3**2*a4**3 + 99144*a1**3*a2**4*a3*a4**4 + 24264*a1**3*a2**4*a4**5 + 19056*a1**3*a2**3*a3**6 + 93984*a1**3*a2**3*a3**5*a4 + 240912*a1**3*a2**3*a3**4*a4**2 + 175040*a1**3*a2**3*a3**3*a4**3 + 238224*a1**3*a2**3*a3**2*a4**4 + 109344*a1**3*a2**3*a3*a4**5 + 30192*a1**3*a2**3*a4**6 + 15216*a1**3*a2**2*a3**7 + 77328*a1**3*a2**2*a3**6*a4 + 187632*a1**3*a2**2*a3**5*a4**2 + 238224*a1**3*a2**2*a3**4*a4**3 + 229584*a1**3*a2**2*a3**3*a4**4 + 175536*a1**3*a2**2*a3**2*a4**5 + 89808*a1**3*a2**2*a3*a4**6 + 23472*a1**3*a2**2*a4**7 + 8268*a1**3*a2*a3**8 + 43488*a1**3*a2*a3**7*a4 + 102864*a1**3*a2*a3**6*a4**2 + 109344*a1**3*a2*a3**5*a4**3 + 76488*a1**3*a2*a3**4*a4**4 + 67872*a1**3*a2*a3**3*a4**5 + 55248*a1**3*a2*a3**2*a4**6 + 29664*a1**3*a2*a3*a4**7 + 7500*a1**3*a2*a4**8 + 1836*a1**3*a3**9 + 10908*a1**3*a3**8*a4 + 28272*a1**3*a3**7*a4**2 + 30192*a1**3*a3**6*a4**3 + 10344*a1**3*a3**5*a4**4 + 840*a1**3*a3**4*a4**5 + 4656*a1**3*a3**3*a4**6 + 6192*a1**3*a3**2*a4**7 + 4044*a1**3*a3*a4**8 + 1020*a1**3*a4**9 + 258*a1**2*a2**10 + 2004*a1**2*a2**9*a3 + 2004*a1**2*a2**9*a4 + 7002*a1**2*a2**8*a3**2 + 14004*a1**2*a2**8*a3*a4 + 7002*a1**2*a2**8*a4**2 + 6192*a1**2*a2**7*a3**3 + 43920*a1**2*a2**7*a3**2*a4 + 43920*a1**2*a2**7*a3*a4**2 + 15216*a1**2*a2**7*a4**3 - 6492*a1**2*a2**6*a3**4 + 55248*a1**2*a2**6*a3**3*a4 + 123480*a1**2*a2**6*a3**2*a4**2 + 77328*a1**2*a2**6*a3*a4**3 + 24612*a1**2*a2**6*a4**4 - 10440*a1**2*a2**5*a3**5 + 41112*a1**2*a2**5*a3**4*a4 + 175536*a1**2*a2**5*a3**3*a4**2 + 187632*a1**2*a2**5*a3**2*a4**3 + 96408*a1**2*a2**5*a3*a4**4 + 32760*a1**2*a2**5*a4**5 + 804*a1**2*a2**4*a3**6 + 48024*a1**2*a2**4*a3**5*a4 + 184860*a1**2*a2**4*a3**4*a4**2 + 238224*a1**2*a2**4*a3**3*a4**3 + 202140*a1**2*a2**4*a3**2*a4**4 + 108504*a1**2*a2**4*a3*a4**5 + 35364*a1**2*a2**4*a4**6 + 8112*a1**2*a2**3*a3**7 + 56784*a1**2*a2**3*a3**6*a4 + 170352*a1**2*a2**3*a3**5*a4**2 + 229584*a1**2*a2**3*a3**4*a4**3 + 240912*a1**2*a2**3*a3**3*a4**4 + 187632*a1**2*a2**3*a3**2*a4**5 + 102864*a1**2*a2**3*a3*a4**6 + 28272*a1**2*a2**3*a4**7 + 7002*a1**2*a2**2*a3**8 + 43920*a1**2*a2**2*a3**7*a4 + 123480*a1**2*a2**2*a3**6*a4**2 + 175536*a1**2*a2**2*a3**5*a4**3 + 184860*a1**2*a2**2*a3**4*a4**4 + 170352*a1**2*a2**2*a3**3*a4**5 + 123480*a1**2*a2**2*a3**2*a4**6 + 64080*a1**2*a2**2*a3*a4**7 + 15066*a1**2*a2**2*a4**8 + 3348*a1**2*a2*a3**9 + 22068*a1**2*a2*a3**8*a4 + 64080*a1**2*a2*a3**7*a4**2 + 89808*a1**2*a2*a3**6*a4**3 + 84312*a1**2*a2*a3**5*a4**4 + 79128*a1**2*a2*a3**4*a4**5 + 65808*a1**2*a2*a3**3*a4**6 + 43920*a1**2*a2*a3**2*a4**7 + 22068*a1**2*a2*a3*a4**8 + 4692*a1**2*a2*a4**9 + 642*a1**2*a3**10 + 4692*a1**2*a3**9*a4 + 15066*a1**2*a3**8*a4**2 + 23472*a1**2*a3**7*a4**3 + 22308*a1**2*a3**6*a4**4 + 20664*a1**2*a3**5*a4**5 + 18852*a1**2*a3**4*a4**6 + 12336*a1**2*a3**3*a4**7 + 7002*a1**2*a3**2*a4**8 + 3348*a1**2*a3*a4**9 + 642*a1**2*a4**10 + 108*a1*a2**11 + 900*a1*a2**10*a3 + 900*a1*a2**10*a4 + 3348*a1*a2**9*a3**2 + 6696*a1*a2**9*a3*a4 + 3348*a1*a2**9*a4**2 + 4044*a1*a2**8*a3**3 + 22068*a1*a2**8*a3**2*a4 + 22068*a1*a2**8*a3*a4**2 + 8268*a1*a2**8*a4**3 - 2376*a1*a2**7*a3**4 + 29664*a1*a2**7*a3**3*a4 + 64080*a1*a2**7*a3**2*a4**2 + 43488*a1*a2**7*a3*a4**3 + 15672*a1*a2**7*a4**4 - 8472*a1*a2**6*a3**5 + 15816*a1*a2**6*a3**4*a4 + 89808*a1*a2**6*a3**3*a4**2 + 102864*a1*a2**6*a3**2*a4**3 + 59976*a1*a2**6*a3*a4**4 + 22632*a1*a2**6*a4**5 - 4824*a1*a2**5*a3**6 + 10224*a1*a2**5*a3**5*a4 + 84312*a1*a2**5*a3**4*a4**2 + 109344*a1*a2**5*a3**3*a4**3 + 108504*a1*a2**5*a3**2*a4**4 + 65520*a1*a2**5*a3*a4**5 + 23976*a1*a2**5*a4**6 + 1368*a1*a2**4*a3**7 + 19656*a1*a2**4*a3**6*a4 + 79128*a1*a2**4*a3**5*a4**2 + 76488*a1*a2**4*a3**4*a4**3 + 99144*a1*a2**4*a3**3*a4**4 + 96408*a1*a2**4*a3**2*a4**5 + 59976*a1*a2**4*a3*a4**6 + 18648*a1*a2**4*a4**7 + 2844*a1*a2**3*a3**8 + 20448*a1*a2**3*a3**7*a4 + 65808*a1*a2**3*a3**6*a4**2 + 67872*a1*a2**3*a3**5*a4**3 + 68904*a1*a2**3*a3**4*a4**4 + 93984*a1*a2**3*a3**3*a4**5 + 77328*a1*a2**3*a3**2*a4**6 + 43488*a1*a2**3*a3*a4**7 + 10908*a1*a2**3*a4**8 + 2004*a1*a2**2*a3**9 + 14004*a1*a2**2*a3**8*a4 + 43920*a1*a2**2*a3**7*a4**2 + 55248*a1*a2**2*a3**6*a4**3 + 41112*a1*a2**2*a3**5*a4**4 + 48024*a1*a2**2*a3**4*a4**5 + 56784*a1*a2**2*a3**3*a4**6 + 43920*a1*a2**2*a3**2*a4**7 + 22068*a1*a2**2*a3*a4**8 + 4692*a1*a2**2*a4**9 + 900*a1*a2*a3**10 + 6696*a1*a2*a3**9*a4 + 22068*a1*a2*a3**8*a4**2 + 29664*a1*a2*a3**7*a4**3 + 15816*a1*a2*a3**6*a4**4 + 10224*a1*a2*a3**5*a4**5 + 19656*a1*a2*a3**4*a4**6 + 20448*a1*a2*a3**3*a4**7 + 14004*a1*a2*a3**2*a4**8 + 6696*a1*a2*a3*a4**9 + 1284*a1*a2*a4**10 + 156*a1*a3**11 + 1284*a1*a3**10*a4 + 4692*a1*a3**9*a4**2 + 7500*a1*a3**8*a4**3 + 4824*a1*a3**7*a4**4 + 1896*a1*a3**6*a4**5 + 4200*a1*a3**5*a4**6 + 5592*a1*a3**4*a4**7 + 3660*a1*a3**3*a4**8 + 2004*a1*a3**2*a4**9 + 900*a1*a3*a4**10 + 156*a1*a4**11 + 17*a2**12 + 156*a2**11*a3 + 156*a2**11*a4 + 642*a2**10*a3**2 + 1284*a2**10*a3*a4 + 642*a2**10*a4**2 + 1020*a2**9*a3**3 + 4692*a2**9*a3**2*a4 + 4692*a2**9*a3*a4**2 + 1836*a2**9*a4**3 - 33*a2**8*a3**4 + 7500*a2**8*a3**3*a4 + 15066*a2**8*a3**2*a4**2 + 10908*a2**8*a3*a4**3 + 4191*a2**8*a4**4 - 1800*a2**7*a3**5 + 4824*a2**7*a3**4*a4 + 23472*a2**7*a3**3*a4**2 + 28272*a2**7*a3**2*a4**3 + 18648*a2**7*a3*a4**4 + 7224*a2**7*a4**5 - 1636*a2**6*a3**6 + 1896*a2**6*a3**5*a4 + 22308*a2**6*a3**4*a4**2 + 30192*a2**6*a3**3*a4**3 + 35364*a2**6*a3**2*a4**4 + 23976*a2**6*a3*a4**5 + 8732*a2**6*a4**6 + 24*a2**5*a3**7 + 4200*a2**5*a3**6*a4 + 20664*a2**5*a3**5*a4**2 + 10344*a2**5*a3**4*a4**3 + 24264*a2**5*a3**3*a4**4 + 32760*a2**5*a3**2*a4**5 + 22632*a2**5*a3*a4**6 + 7224*a2**5*a4**7 + 735*a2**4*a3**8 + 5592*a2**4*a3**7*a4 + 18852*a2**4*a3**6*a4**2 + 840*a2**4*a3**5*a4**3 - 1926*a2**4*a3**4*a4**4 + 24360*a2**4*a3**3*a4**5 + 24612*a2**4*a3**2*a4**6 + 15672*a2**4*a3*a4**7 + 4191*a2**4*a4**8 + 492*a2**3*a3**9 + 3660*a2**3*a3**8*a4 + 12336*a2**3*a3**7*a4**2 + 4656*a2**3*a3**6*a4**3 - 9432*a2**3*a3**5*a4**4 + 5352*a2**3*a3**4*a4**5 + 19056*a2**3*a3**3*a4**6 + 15216*a2**3*a3**2*a4**7 + 8268*a2**3*a3*a4**8 + 1836*a2**3*a4**9 + 258*a2**2*a3**10 + 2004*a2**2*a3**9*a4 + 7002*a2**2*a3**8*a4**2 + 6192*a2**2*a3**7*a4**3 - 6492*a2**2*a3**6*a4**4 - 10440*a2**2*a3**5*a4**5 + 804*a2**2*a3**4*a4**6 + 8112*a2**2*a3**3*a4**7 + 7002*a2**2*a3**2*a4**8 + 3348*a2**2*a3*a4**9 + 642*a2**2*a4**10 + 108*a2*a3**11 + 900*a2*a3**10*a4 + 3348*a2*a3**9*a4**2 + 4044*a2*a3**8*a4**3 - 2376*a2*a3**7*a4**4 - 8472*a2*a3**6*a4**5 - 4824*a2*a3**5*a4**6 + 1368*a2*a3**4*a4**7 + 2844*a2*a3**3*a4**8 + 2004*a2*a3**2*a4**9 + 900*a2*a3*a4**10 + 156*a2*a4**11 + 17*a3**12 + 156*a3**11*a4 + 642*a3**10*a4**2 + 1020*a3**9*a4**3 - 33*a3**8*a4**4 - 1800*a3**7*a4**5 - 1636*a3**6*a4**6 + 24*a3**5*a4**7 + 735*a3**4*a4**8 + 492*a3**3*a4**9 + 258*a3**2*a4**10 + 108*a3*a4**11 + 17*a4**12");
		SDS.Result<MutableBig> result = SDS.sds(new BigPoly("abcd", f.toString()), T_n);
		// A_4 works; Z_4 doesn't seem to work
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
		result = SDS.sds(new BigPoly("abcd", f.toString()), J_4);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
	}

	@Test
	public void testHan13() {
		// http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545
		// ex 4.1
		BigPoly f = new BigPoly("xyz", "9*x**2 + 6*x*y - 6*x*z + y**2 - 2*y*z + z**2");
		// T_3 works for 3e6 within 16 iterations, 3e7 within 18 iterations (73801 polynomials after 13th iteration); A_3 doesn't work
		SDS.Result<MutableBig> result = SDS.sds(new BigPoly("xyz", "z**2").add(3_000_000, f), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// H_3 works for 3e6 within 13 iterations, 3e7 within 15 iterations, Y_3 == H_3
		result = SDS.sds(new BigPoly("xyz", "z**2").add(3_000_000, f), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(13, result.getDepth());
		result = SDS.sds(new BigPoly("xyz", "z**2").add(30_000_000, f), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Z_3 works for 3e5 within 19 iterations, 3e6 within 22 iterations
		result = SDS.sds(new BigPoly("xyz", "z**2").add(300_000, f), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(19, result.getDepth());
		// ex 4.2
		f = new BigPoly("abcdefghij", replaceAn("a1**2 + a2**2 + a3**2 + a4**2 + a5**2 + a6**2 + a7**2 + a8**2 + a9**2 + a10**2 - 4*a1*a2").toString());
		result = SDS.sds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'a').signum() < 0);
		assertEquals(0, result.getDepth());
		// ex 4.3
		f = new BigPoly("xyz", "x**3 + y**3 + z**3 - 3*x*y*z");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
		// H_3 and Z_3 don't work
		// result = SDS.sds(f, H_3);
		f = new BigPoly("xyzw", "x**4 + y**4 + z**4 + w**4 - 4*x*y*z*w");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
		// J_4 and Z_4 don't work
		// result = SDS.sds(f, J_4);
		// ex 4.4
		f = new BigPoly("abc", "a**4 - 3*a**3*b + 2*a**2*b**2 + 2*a**2*c**2 - 3*a*c**3 + b**4 - 3*b**3*c + 2*b**2*c**2 + c**4");
		// zero at (1, 1, 1)
		assertEquals(0, subs(f, asList(f, 1, 1, 1), 'a').signum());
		// T_3 doesn't work (46455 polynomials after 50th iteration)
		// result = SDS.sds(f, T_n);
		// A_3 works for 1e9 but doesn't seem to work for 1e10
		String smallPos = "a**4 + b**4 + c**4";
		result = SDS.sds(new BigPoly("abc", smallPos).add(__().add(f.valueOf(1_000_000_000), f)));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(14, result.getDepth());
		// Z_3 needs 30 for 1e10, 33 for 1e11
		result = SDS.sds(new BigPoly("abc", smallPos).add(__().add(f.valueOf(10_000_000_000L), f)), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(30, result.getDepth());
		// 1e22
		f = __().add(f.valueOf("10000000000000000000000"), f);
		// T_3 needs 32
		result = SDS.sds(new BigPoly("abc", smallPos).add(f), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(32, result.getDepth());
		// H_3 needs 38, Y_3 == H_3
		result = SDS.sds(new BigPoly("abc", smallPos).add(f), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(38, result.getDepth());
		// both A_3 and T_3 find negative without iteration
		String smallNeg = "-a**4 - b**4 - c**4";
		result = SDS.sds(new BigPoly("abc", smallNeg).add(f));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// H_3 finds negative without iterations, Y_3 == H_3
		result = SDS.sds(new BigPoly("abc", smallNeg).add(f), H_3);
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// Z_3 finds negative without iterations
		result = SDS.sds(new BigPoly("abc", smallNeg).add(f), Z_n);
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// ex 4.5
		// result from han13-ex5.py
		f = new BigPoly("abcde", "a**2*b**2*c**2*d**2 + 3*a**2*b**2*c**2*e**2 + 3*a**2*b**2*d**2*e**2 + 9*a**2*b**2*e**4 + 3*a**2*c**2*d**2*e**2 + 9*a**2*c**2*e**4 + 9*a**2*d**2*e**4 + 11*a**2*e**6 - 32*a*b*e**6 - 32*a*c*e**6 - 32*a*d*e**6 + 3*b**2*c**2*d**2*e**2 + 9*b**2*c**2*e**4 + 9*b**2*d**2*e**4 + 11*b**2*e**6 - 32*b*c*e**6 - 32*b*d*e**6 + 9*c**2*d**2*e**4 + 11*c**2*e**6 - 32*c*d*e**6 + 11*d**2*e**6 + 81*e**8");
		// both A_5 and T_5 need 5; Z_5 and Y_5 dont work
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals(5, result.getDepth());
	}

	@Test
	public void testHan14() {
		// ISBN 9787560349800, p301, ex 12.9
		// f2 from han14-p301.py
		BigPoly f = new BigPoly("abc", "81*a**6*b**2 + 162*a**6*b*c + 81*a**6*c**2 - 412*a**5*b**3 + 1100*a**5*b**2*c + 2124*a**5*b*c**2 + 612*a**5*c**3 + 294*a**4*b**4 + 4314*a**4*b**3*c + 9320*a**4*b**2*c**2 + 5338*a**4*b*c**3 + 294*a**4*c**4 + 612*a**3*b**5 + 5338*a**3*b**4*c + 16090*a**3*b**3*c**2 + 16090*a**3*b**2*c**3 + 4314*a**3*b*c**4 - 412*a**3*c**5 + 81*a**2*b**6 + 2124*a**2*b**5*c + 9320*a**2*b**4*c**2 + 16090*a**2*b**3*c**3 + 9320*a**2*b**2*c**4 + 1100*a**2*b*c**5 + 81*a**2*c**6 + 162*a*b**6*c + 1100*a*b**5*c**2 + 4314*a*b**4*c**3 + 5338*a*b**3*c**4 + 2124*a*b**2*c**5 + 162*a*b*c**6 + 81*b**6*c**2 - 412*b**5*c**3 + 294*b**4*c**4 + 612*b**3*c**5 + 81*b**2*c**6");
		SDS.Result<MutableBig> result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		String zeroAt = "[[0, 0, 1], [0, 1, 0], [0, 3, 1], [1, 0, 0], [1, 0, 3], [3, 1, 0]]";
		assertEquals(zeroAt, result.getZeroAt().toString());
		// T_3 and H_3 need 2; Z_3 doesn't work
		assertEquals(3, result.getDepth());
		// f3 from han14-p301.py
		f = new BigPoly("abc", "6561*a**12*b**4 + 26244*a**12*b**3*c + 39366*a**12*b**2*c**2 + 26244*a**12*b*c**3 + 6561*a**12*c**4 - 66744*a**11*b**5 + 44712*a**11*b**4*c + 633744*a**11*b**3*c**2 + 965520*a**11*b**2*c**3 + 542376*a**11*b*c**4 + 99144*a**11*c**5 + 217372*a**10*b**6 - 112276*a**10*b**5*c + 2415028*a**10*b**4*c**2 + 8751816*a**10*b**3*c**3 + 9144756*a**10*b**2*c**4 + 3559788*a**10*b*c**5 + 422172*a**10*c**6 - 143112*a**9*b**7 - 1844892*a**9*b**6*c + 941668*a**9*b**5*c**2 + 23814912*a**9*b**4*c**3 + 45230848*a**9*b**3*c**4 + 32114276*a**9*b**2*c**5 + 8348004*a**9*b*c**6 + 293112*a**9*c**7 - 404730*a**8*b**8 - 145148*a**8*b**7*c + 1172710*a**8*b**6*c**2 + 30229204*a**8*b**5*c**3 + 90765272*a**8*b**4*c**4 + 100858580*a**8*b**3*c**5 + 46752998*a**8*b**2*c**6 + 6873348*a**8*b*c**7 - 404730*a**8*c**8 + 293112*a**7*b**9 + 6873348*a**7*b**8*c + 25171160*a**7*b**7*c**2 + 55499920*a**7*b**6*c**3 + 118778844*a**7*b**5*c**4 + 161741788*a**7*b**4*c**5 + 105045136*a**7*b**3*c**6 + 25171160*a**7*b**2*c**7 - 145148*a**7*b*c**8 - 143112*a**7*c**9 + 422172*a**6*b**10 + 8348004*a**6*b**9*c + 46752998*a**6*b**8*c**2 + 105045136*a**6*b**7*c**3 + 157443246*a**6*b**6*c**4 + 196665720*a**6*b**5*c**5 + 157443246*a**6*b**4*c**6 + 55499920*a**6*b**3*c**7 + 1172710*a**6*b**2*c**8 - 1844892*a**6*b*c**9 + 217372*a**6*c**10 + 99144*a**5*b**11 + 3559788*a**5*b**10*c + 32114276*a**5*b**9*c**2 + 100858580*a**5*b**8*c**3 + 161741788*a**5*b**7*c**4 + 196665720*a**5*b**6*c**5 + 196665720*a**5*b**5*c**6 + 118778844*a**5*b**4*c**7 + 30229204*a**5*b**3*c**8 + 941668*a**5*b**2*c**9 - 112276*a**5*b*c**10 - 66744*a**5*c**11 + 6561*a**4*b**12 + 542376*a**4*b**11*c + 9144756*a**4*b**10*c**2 + 45230848*a**4*b**9*c**3 + 90765272*a**4*b**8*c**4 + 118778844*a**4*b**7*c**5 + 157443246*a**4*b**6*c**6 + 161741788*a**4*b**5*c**7 + 90765272*a**4*b**4*c**8 + 23814912*a**4*b**3*c**9 + 2415028*a**4*b**2*c**10 + 44712*a**4*b*c**11 + 6561*a**4*c**12 + 26244*a**3*b**12*c + 965520*a**3*b**11*c**2 + 8751816*a**3*b**10*c**3 + 23814912*a**3*b**9*c**4 + 30229204*a**3*b**8*c**5 + 55499920*a**3*b**7*c**6 + 105045136*a**3*b**6*c**7 + 100858580*a**3*b**5*c**8 + 45230848*a**3*b**4*c**9 + 8751816*a**3*b**3*c**10 + 633744*a**3*b**2*c**11 + 26244*a**3*b*c**12 + 39366*a**2*b**12*c**2 + 633744*a**2*b**11*c**3 + 2415028*a**2*b**10*c**4 + 941668*a**2*b**9*c**5 + 1172710*a**2*b**8*c**6 + 25171160*a**2*b**7*c**7 + 46752998*a**2*b**6*c**8 + 32114276*a**2*b**5*c**9 + 9144756*a**2*b**4*c**10 + 965520*a**2*b**3*c**11 + 39366*a**2*b**2*c**12 + 26244*a*b**12*c**3 + 44712*a*b**11*c**4 - 112276*a*b**10*c**5 - 1844892*a*b**9*c**6 - 145148*a*b**8*c**7 + 6873348*a*b**7*c**8 + 8348004*a*b**6*c**9 + 3559788*a*b**5*c**10 + 542376*a*b**4*c**11 + 26244*a*b**3*c**12 + 6561*b**12*c**4 - 66744*b**11*c**5 + 217372*b**10*c**6 - 143112*b**9*c**7 - 404730*b**8*c**8 + 293112*b**7*c**9 + 422172*b**6*c**10 + 99144*b**5*c**11 + 6561*b**4*c**12");
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals(zeroAt, result.getZeroAt().toString());
		// T_3 and H_3 need 2; Z_3 doesn't work
		assertEquals(3, result.getDepth());

		// f3 from han14-p301.py, p302
		f = new BigPoly("uvw", "u**16 + 100*u**15*v + 84*u**15*w + 1570*u**14*v**2 + 2252*u**14*v*w + 746*u**14*w**2 + 11092*u**13*v**3 + 24064*u**13*v**2*w + 15336*u**13*v*w**2 + 2412*u**13*w**3 + 44619*u**12*v**4 + 134508*u**12*v**3*w + 133150*u**12*v**2*w**2 + 45604*u**12*v*w**3 + 1955*u**12*w**4 + 112268*u**11*v**5 + 443976*u**11*v**4*w + 614400*u**11*v**3*w**2 + 343744*u**11*v**2*w**3 + 55192*u**11*v*w**4 - 5876*u**11*w**5 + 182940*u**10*v**6 + 914032*u**10*v**5*w + 1651578*u**10*v**4*w**2 + 1301492*u**10*v**3*w**3 + 389122*u**10*v**2*w**4 - 1552*u**10*v*w**5 - 8708*u**10*w**6 + 191208*u**9*v**7 + 1183380*u**9*v**6*w + 2655284*u**9*v**5*w**2 + 2636292*u**9*v**4*w**3 + 1042044*u**9*v**3*w**4 + 49100*u**9*v**2*w**5 + 10564*u**9*v*w**6 + 30248*u**9*w**7 + 118413*u**8*v**8 + 917972*u**8*v**7*w + 2444248*u**8*v**6*w**2 + 2615728*u**8*v**5*w**3 + 605604*u**8*v**4*w**4 - 614856*u**8*v**3*w**5 - 16976*u**8*v**2*w**6 + 352132*u**8*v*w**7 + 118413*u**8*w**8 + 30248*u**7*v**9 + 352132*u**7*v**8*w + 1034596*u**7*v**7*w**2 + 419556*u**7*v**6*w**3 - 2502520*u**7*v**5*w**4 - 3924376*u**7*v**4*w**5 - 1407260*u**7*v**3*w**6 + 1034596*u**7*v**2*w**7 + 917972*u**7*v*w**8 + 191208*u**7*w**9 - 8708*u**6*v**10 + 10564*u**6*v**9*w - 16976*u**6*v**8*w**2 - 1407260*u**6*v**7*w**3 - 5548262*u**6*v**6*w**4 - 8702220*u**6*v**5*w**5 - 5548262*u**6*v**4*w**6 + 419556*u**6*v**3*w**7 + 2444248*u**6*v**2*w**8 + 1183380*u**6*v*w**9 + 182940*u**6*w**10 - 5876*u**5*v**11 - 1552*u**5*v**10*w + 49100*u**5*v**9*w**2 - 614856*u**5*v**8*w**3 - 3924376*u**5*v**7*w**4 - 8702220*u**5*v**6*w**5 - 8702220*u**5*v**5*w**6 - 2502520*u**5*v**4*w**7 + 2615728*u**5*v**3*w**8 + 2655284*u**5*v**2*w**9 + 914032*u**5*v*w**10 + 112268*u**5*w**11 + 1955*u**4*v**12 + 55192*u**4*v**11*w + 389122*u**4*v**10*w**2 + 1042044*u**4*v**9*w**3 + 605604*u**4*v**8*w**4 - 2502520*u**4*v**7*w**5 - 5548262*u**4*v**6*w**6 - 3924376*u**4*v**5*w**7 + 605604*u**4*v**4*w**8 + 2636292*u**4*v**3*w**9 + 1651578*u**4*v**2*w**10 + 443976*u**4*v*w**11 + 44619*u**4*w**12 + 2412*u**3*v**13 + 45604*u**3*v**12*w + 343744*u**3*v**11*w**2 + 1301492*u**3*v**10*w**3 + 2636292*u**3*v**9*w**4 + 2615728*u**3*v**8*w**5 + 419556*u**3*v**7*w**6 - 1407260*u**3*v**6*w**7 - 614856*u**3*v**5*w**8 + 1042044*u**3*v**4*w**9 + 1301492*u**3*v**3*w**10 + 614400*u**3*v**2*w**11 + 134508*u**3*v*w**12 + 11092*u**3*w**13 + 746*u**2*v**14 + 15336*u**2*v**13*w + 133150*u**2*v**12*w**2 + 614400*u**2*v**11*w**3 + 1651578*u**2*v**10*w**4 + 2655284*u**2*v**9*w**5 + 2444248*u**2*v**8*w**6 + 1034596*u**2*v**7*w**7 - 16976*u**2*v**6*w**8 + 49100*u**2*v**5*w**9 + 389122*u**2*v**4*w**10 + 343744*u**2*v**3*w**11 + 133150*u**2*v**2*w**12 + 24064*u**2*v*w**13 + 1570*u**2*w**14 + 84*u*v**15 + 2252*u*v**14*w + 24064*u*v**13*w**2 + 134508*u*v**12*w**3 + 443976*u*v**11*w**4 + 914032*u*v**10*w**5 + 1183380*u*v**9*w**6 + 917972*u*v**8*w**7 + 352132*u*v**7*w**8 + 10564*u*v**6*w**9 - 1552*u*v**5*w**10 + 55192*u*v**4*w**11 + 45604*u*v**3*w**12 + 15336*u*v**2*w**13 + 2252*u*v*w**14 + 100*u*w**15 + v**16 + 100*v**15*w + 1570*v**14*w**2 + 11092*v**13*w**3 + 44619*v**12*w**4 + 112268*v**11*w**5 + 182940*v**10*w**6 + 191208*v**9*w**7 + 118413*v**8*w**8 + 30248*v**7*w**9 - 8708*v**6*w**10 - 5876*v**5*w**11 + 1955*v**4*w**12 + 2412*v**3*w**13 + 746*v**2*w**14 + 84*v*w**15 + w**16");
		result = SDS.sds(f);
		// T_3 works; H_3 and Z_3 don't work
		assertTrue(result.isNonNegative());
		assertEquals("[[1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(1, result.getDepth());
	}

	@Test
	public void testHan23() {
		// ISBN 9787312056185, p341, ex 11.7
		// fn from han23-p341u.py, u = v = 1.001, T_3 needs 11 iterations; A_3 needs 376; H_3 and Z_3 don't work
		BigPoly f = new BigPoly("abc", "445779222889000000000000*a**5*b + 445779222889000000000000*a**5*c - 109550995776222000000000*a**4*b**2 + 222891003112778000000000*a**4*b*c - 113338226001000000000000*a**4*c**2 - 668666551996999111000000*a**3*b**3 - 221999887997443111000000*a**3*b**2*c - 223782118227223111000000*a**3*b*c**2 - 668666551996999111000000*a**3*c**3 - 113338226001000000000000*a**2*b**4 - 223782118227223111000000*a**2*b**3*c + 668664993324327999000000*a**2*b**2*c**2 - 221999887997443111000000*a**2*b*c**3 - 109550995776222000000000*a**2*c**4 + 445779222889000000000000*a*b**5 + 222891003112778000000000*a*b**4*c - 221999887997443111000000*a*b**3*c**2 - 223782118227223111000000*a*b**2*c**3 + 222891003112778000000000*a*b*c**4 + 445779222889000000000000*a*c**5 + 445779222889000000000000*b**5*c - 109550995776222000000000*b**4*c**2 - 668666551996999111000000*b**3*c**3 - 113338226001000000000000*b**2*c**4 + 445779222889000000000000*b*c**5");
		SDS.Result<MutableBig> result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		assertEquals(11, result.getDepth());

		// p352, ex 11.19
		// fn from han23-p352.py
		LongPoly fn = new LongPoly("abcd", "a**8*b**2*c**2*d + 2*a**7*b**3*c**3 + 2*a**7*b**3*c*d**2 - 2*a**7*b**2*c**2*d**2 + 2*a**7*b*c**3*d**2 + 5*a**6*b**4*c**2*d + 2*a**6*b**4*d**3 - 4*a**6*b**3*c**3*d - 2*a**6*b**3*c**2*d**2 - 4*a**6*b**3*c*d**3 + 5*a**6*b**2*c**4*d - 2*a**6*b**2*c**3*d**2 + 6*a**6*b**2*c**2*d**3 - 4*a**6*b*c**3*d**3 + 2*a**6*c**4*d**3 + 8*a**5*b**5*c*d**2 - 2*a**5*b**4*c**4 - 4*a**5*b**4*c**3*d - 8*a**5*b**4*c**2*d**2 - 4*a**5*b**4*c*d**3 - 2*a**5*b**4*d**4 - 4*a**5*b**3*c**4*d + 18*a**5*b**3*c**3*d**2 - 4*a**5*b**3*c**2*d**3 + 8*a**5*b**3*c*d**4 - 8*a**5*b**2*c**4*d**2 - 4*a**5*b**2*c**3*d**3 - 8*a**5*b**2*c**2*d**4 + 8*a**5*b*c**5*d**2 - 4*a**5*b*c**4*d**3 + 8*a**5*b*c**3*d**4 - 2*a**5*c**4*d**4 + 5*a**4*b**6*c**2*d + 2*a**4*b**6*d**3 - 2*a**4*b**5*c**4 - 4*a**4*b**5*c**3*d - 8*a**4*b**5*c**2*d**2 - 4*a**4*b**5*c*d**3 - 2*a**4*b**5*d**4 - 2*a**4*b**4*c**5 + 3*a**4*b**4*c**4*d - 8*a**4*b**4*c**3*d**2 + 30*a**4*b**4*c**2*d**3 - 2*a**4*b**4*c*d**4 + a**4*b**4*d**5 - 4*a**4*b**3*c**5*d - 8*a**4*b**3*c**4*d**2 - 16*a**4*b**3*c**3*d**3 - 8*a**4*b**3*c**2*d**4 - 4*a**4*b**3*c*d**5 + 5*a**4*b**2*c**6*d - 8*a**4*b**2*c**5*d**2 + 30*a**4*b**2*c**4*d**3 - 8*a**4*b**2*c**3*d**4 + 11*a**4*b**2*c**2*d**5 - 4*a**4*b*c**5*d**3 - 2*a**4*b*c**4*d**4 - 4*a**4*b*c**3*d**5 + 2*a**4*c**6*d**3 - 2*a**4*c**5*d**4 + a**4*c**4*d**5 + 2*a**3*b**7*c**3 + 2*a**3*b**7*c*d**2 - 4*a**3*b**6*c**3*d - 2*a**3*b**6*c**2*d**2 - 4*a**3*b**6*c*d**3 - 4*a**3*b**5*c**4*d + 18*a**3*b**5*c**3*d**2 - 4*a**3*b**5*c**2*d**3 + 8*a**3*b**5*c*d**4 - 4*a**3*b**4*c**5*d - 8*a**3*b**4*c**4*d**2 - 16*a**3*b**4*c**3*d**3 - 8*a**3*b**4*c**2*d**4 - 4*a**3*b**4*c*d**5 + 2*a**3*b**3*c**7 - 4*a**3*b**3*c**6*d + 18*a**3*b**3*c**5*d**2 - 16*a**3*b**3*c**4*d**3 + 42*a**3*b**3*c**3*d**4 - 4*a**3*b**3*c**2*d**5 + 2*a**3*b**3*c*d**6 - 2*a**3*b**2*c**6*d**2 - 4*a**3*b**2*c**5*d**3 - 8*a**3*b**2*c**4*d**4 - 4*a**3*b**2*c**3*d**5 - 2*a**3*b**2*c**2*d**6 + 2*a**3*b*c**7*d**2 - 4*a**3*b*c**6*d**3 + 8*a**3*b*c**5*d**4 - 4*a**3*b*c**4*d**5 + 2*a**3*b*c**3*d**6 + a**2*b**8*c**2*d - 2*a**2*b**7*c**2*d**2 + 5*a**2*b**6*c**4*d - 2*a**2*b**6*c**3*d**2 + 6*a**2*b**6*c**2*d**3 - 8*a**2*b**5*c**4*d**2 - 4*a**2*b**5*c**3*d**3 - 8*a**2*b**5*c**2*d**4 + 5*a**2*b**4*c**6*d - 8*a**2*b**4*c**5*d**2 + 30*a**2*b**4*c**4*d**3 - 8*a**2*b**4*c**3*d**4 + 11*a**2*b**4*c**2*d**5 - 2*a**2*b**3*c**6*d**2 - 4*a**2*b**3*c**5*d**3 - 8*a**2*b**3*c**4*d**4 - 4*a**2*b**3*c**3*d**5 - 2*a**2*b**3*c**2*d**6 + a**2*b**2*c**8*d - 2*a**2*b**2*c**7*d**2 + 6*a**2*b**2*c**6*d**3 - 8*a**2*b**2*c**5*d**4 + 11*a**2*b**2*c**4*d**5 - 2*a**2*b**2*c**3*d**6 + 2*a*b**7*c**3*d**2 - 4*a*b**6*c**3*d**3 + 8*a*b**5*c**5*d**2 - 4*a*b**5*c**4*d**3 + 8*a*b**5*c**3*d**4 - 4*a*b**4*c**5*d**3 - 2*a*b**4*c**4*d**4 - 4*a*b**4*c**3*d**5 + 2*a*b**3*c**7*d**2 - 4*a*b**3*c**6*d**3 + 8*a*b**3*c**5*d**4 - 4*a*b**3*c**4*d**5 + 2*a*b**3*c**3*d**6 + 2*b**6*c**4*d**3 - 2*b**5*c**4*d**4 + 2*b**4*c**6*d**3 - 2*b**4*c**5*d**4 + b**4*c**4*d**5");
		LongPoly fd = new LongPoly("abcd", "a**6*b**2*c**2*d**2 + 2*a**5*b**3*c**3*d + 2*a**5*b**3*c*d**3 + 2*a**5*b*c**3*d**3 + a**4*b**4*c**4 + 4*a**4*b**4*c**2*d**2 + a**4*b**4*d**4 + 4*a**4*b**2*c**4*d**2 + 4*a**4*b**2*c**2*d**4 + a**4*c**4*d**4 + 2*a**3*b**5*c**3*d + 2*a**3*b**5*c*d**3 + 2*a**3*b**3*c**5*d + 8*a**3*b**3*c**3*d**3 + 2*a**3*b**3*c*d**5 + 2*a**3*b*c**5*d**3 + 2*a**3*b*c**3*d**5 + a**2*b**6*c**2*d**2 + 4*a**2*b**4*c**4*d**2 + 4*a**2*b**4*c**2*d**4 + a**2*b**2*c**6*d**2 + 4*a**2*b**2*c**4*d**4 + a**2*b**2*c**2*d**6 + 2*a*b**5*c**3*d**3 + 2*a*b**3*c**5*d**3 + 2*a*b**3*c**3*d**5 + b**4*c**4*d**4");
		SDS.Result<MutableLong> longResult = SDS.sds(fn);
		assertTrue(longResult.isNonNegative());
		// general solution: (0, 1/2, 1/2) and (u, u, u)
		assertEquals("[[0, 1, 1, 2], [1, 0, 1, 2], [1, 1, 0, 2], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 3], [2, 2, 2, 1], [2, 2, 2, 3]]", getZeroAt(fn, fd, longResult.getZeroAt()).toString());
		// T_4 needs 6; J_4 and Z_4 don't work
		assertEquals(2, longResult.getDepth());

		// p354, ex 11.20, too slow, unable to prove
		/*
		// f from han23-p354u.py
		fn = new LongPoly("RStUVw", "4*R**4*S**4*U**2*V**2*t**2*w + 8*R**4*S**4*U**2*V**2*t*w + 4*R**4*S**4*U**2*V**2*w + R**4*S**2*U**2*V**4*t**2*w**2 + 2*R**4*S**2*U**2*V**4*t**2*w + R**4*S**2*U**2*V**4*t**2 + 2*R**4*S**2*U**2*V**4*t*w**2 + 4*R**4*S**2*U**2*V**4*t*w + 2*R**4*S**2*U**2*V**4*t + R**4*S**2*U**2*V**4*w**2 + 2*R**4*S**2*U**2*V**4*w + R**4*S**2*U**2*V**4 + 2*R**4*S**2*U**2*V**2*t**2*w**2 - 4*R**4*S**2*U**2*V**2*t**2*w + 2*R**4*S**2*U**2*V**2*t**2 + 4*R**4*S**2*U**2*V**2*t*w**2 - 8*R**4*S**2*U**2*V**2*t*w + 4*R**4*S**2*U**2*V**2*t + 2*R**4*S**2*U**2*V**2*w**2 - 4*R**4*S**2*U**2*V**2*w + 2*R**4*S**2*U**2*V**2 + R**4*S**2*U**2*t**2*w**2 + 2*R**4*S**2*U**2*t**2*w + R**4*S**2*U**2*t**2 + 2*R**4*S**2*U**2*t*w**2 + 4*R**4*S**2*U**2*t*w + 2*R**4*S**2*U**2*t + R**4*S**2*U**2*w**2 + 2*R**4*S**2*U**2*w + R**4*S**2*U**2 + 4*R**4*U**2*V**2*t**2*w + 8*R**4*U**2*V**2*t*w + 4*R**4*U**2*V**2*w - 2*R**3*S**3*U**3*V**3*t**2*w**2 + 2*R**3*S**3*U**3*V**3*t**2 + 2*R**3*S**3*U**3*V**3*w**2 - 2*R**3*S**3*U**3*V**3 + 2*R**3*S**3*U**3*V*t**2*w**2 - 2*R**3*S**3*U**3*V*t**2 - 2*R**3*S**3*U**3*V*w**2 + 2*R**3*S**3*U**3*V + 8*R**3*S**3*U**2*V**2*t**2*w**2 - 16*R**3*S**3*U**2*V**2*t**2*w + 8*R**3*S**3*U**2*V**2*t**2 - 8*R**3*S**3*U**2*V**2*w**2 + 16*R**3*S**3*U**2*V**2*w - 8*R**3*S**3*U**2*V**2 + 2*R**3*S**3*U*V**3*t**2*w**2 - 2*R**3*S**3*U*V**3*t**2 - 2*R**3*S**3*U*V**3*w**2 + 2*R**3*S**3*U*V**3 - 2*R**3*S**3*U*V*t**2*w**2 + 2*R**3*S**3*U*V*t**2 + 2*R**3*S**3*U*V*w**2 - 2*R**3*S**3*U*V + 2*R**3*S*U**3*V**3*t**2*w**2 - 2*R**3*S*U**3*V**3*t**2 - 2*R**3*S*U**3*V**3*w**2 + 2*R**3*S*U**3*V**3 - 2*R**3*S*U**3*V*t**2*w**2 + 2*R**3*S*U**3*V*t**2 + 2*R**3*S*U**3*V*w**2 - 2*R**3*S*U**3*V - 8*R**3*S*U**2*V**2*t**2*w**2 + 16*R**3*S*U**2*V**2*t**2*w - 8*R**3*S*U**2*V**2*t**2 + 8*R**3*S*U**2*V**2*w**2 - 16*R**3*S*U**2*V**2*w + 8*R**3*S*U**2*V**2 - 2*R**3*S*U*V**3*t**2*w**2 + 2*R**3*S*U*V**3*t**2 + 2*R**3*S*U*V**3*w**2 - 2*R**3*S*U*V**3 + 2*R**3*S*U*V*t**2*w**2 - 2*R**3*S*U*V*t**2 - 2*R**3*S*U*V*w**2 + 2*R**3*S*U*V + R**2*S**4*U**4*V**2*t**2*w**2 + 2*R**2*S**4*U**4*V**2*t**2*w + R**2*S**4*U**4*V**2*t**2 + 2*R**2*S**4*U**4*V**2*t*w**2 + 4*R**2*S**4*U**4*V**2*t*w + 2*R**2*S**4*U**4*V**2*t + R**2*S**4*U**4*V**2*w**2 + 2*R**2*S**4*U**4*V**2*w + R**2*S**4*U**4*V**2 + 2*R**2*S**4*U**2*V**2*t**2*w**2 - 4*R**2*S**4*U**2*V**2*t**2*w + 2*R**2*S**4*U**2*V**2*t**2 + 4*R**2*S**4*U**2*V**2*t*w**2 - 8*R**2*S**4*U**2*V**2*t*w + 4*R**2*S**4*U**2*V**2*t + 2*R**2*S**4*U**2*V**2*w**2 - 4*R**2*S**4*U**2*V**2*w + 2*R**2*S**4*U**2*V**2 + R**2*S**4*V**2*t**2*w**2 + 2*R**2*S**4*V**2*t**2*w + R**2*S**4*V**2*t**2 + 2*R**2*S**4*V**2*t*w**2 + 4*R**2*S**4*V**2*t*w + 2*R**2*S**4*V**2*t + R**2*S**4*V**2*w**2 + 2*R**2*S**4*V**2*w + R**2*S**4*V**2 + 4*R**2*S**2*U**4*V**4*t*w**2 + 8*R**2*S**2*U**4*V**4*t*w + 4*R**2*S**2*U**4*V**4*t + 2*R**2*S**2*U**4*V**2*t**2*w**2 + 4*R**2*S**2*U**4*V**2*t**2*w + 2*R**2*S**2*U**4*V**2*t**2 - 4*R**2*S**2*U**4*V**2*t*w**2 - 8*R**2*S**2*U**4*V**2*t*w - 4*R**2*S**2*U**4*V**2*t + 2*R**2*S**2*U**4*V**2*w**2 + 4*R**2*S**2*U**4*V**2*w + 2*R**2*S**2*U**4*V**2 + 4*R**2*S**2*U**4*t*w**2 + 8*R**2*S**2*U**4*t*w + 4*R**2*S**2*U**4*t + 8*R**2*S**2*U**3*V**3*t**2*w**2 - 8*R**2*S**2*U**3*V**3*t**2 - 16*R**2*S**2*U**3*V**3*t*w**2 + 16*R**2*S**2*U**3*V**3*t + 8*R**2*S**2*U**3*V**3*w**2 - 8*R**2*S**2*U**3*V**3 - 8*R**2*S**2*U**3*V*t**2*w**2 + 8*R**2*S**2*U**3*V*t**2 + 16*R**2*S**2*U**3*V*t*w**2 - 16*R**2*S**2*U**3*V*t - 8*R**2*S**2*U**3*V*w**2 + 8*R**2*S**2*U**3*V + 2*R**2*S**2*U**2*V**4*t**2*w**2 + 4*R**2*S**2*U**2*V**4*t**2*w + 2*R**2*S**2*U**2*V**4*t**2 - 4*R**2*S**2*U**2*V**4*t*w**2 - 8*R**2*S**2*U**2*V**4*t*w - 4*R**2*S**2*U**2*V**4*t + 2*R**2*S**2*U**2*V**4*w**2 + 4*R**2*S**2*U**2*V**4*w + 2*R**2*S**2*U**2*V**4 - 24*R**2*S**2*U**2*V**2*t**2*w**2 + 32*R**2*S**2*U**2*V**2*t**2*w - 24*R**2*S**2*U**2*V**2*t**2 + 32*R**2*S**2*U**2*V**2*t*w**2 - 32*R**2*S**2*U**2*V**2*t*w + 32*R**2*S**2*U**2*V**2*t - 24*R**2*S**2*U**2*V**2*w**2 + 32*R**2*S**2*U**2*V**2*w - 24*R**2*S**2*U**2*V**2 + 2*R**2*S**2*U**2*t**2*w**2 + 4*R**2*S**2*U**2*t**2*w + 2*R**2*S**2*U**2*t**2 - 4*R**2*S**2*U**2*t*w**2 - 8*R**2*S**2*U**2*t*w - 4*R**2*S**2*U**2*t + 2*R**2*S**2*U**2*w**2 + 4*R**2*S**2*U**2*w + 2*R**2*S**2*U**2 - 8*R**2*S**2*U*V**3*t**2*w**2 + 8*R**2*S**2*U*V**3*t**2 + 16*R**2*S**2*U*V**3*t*w**2 - 16*R**2*S**2*U*V**3*t - 8*R**2*S**2*U*V**3*w**2 + 8*R**2*S**2*U*V**3 + 8*R**2*S**2*U*V*t**2*w**2 - 8*R**2*S**2*U*V*t**2 - 16*R**2*S**2*U*V*t*w**2 + 16*R**2*S**2*U*V*t + 8*R**2*S**2*U*V*w**2 - 8*R**2*S**2*U*V + 4*R**2*S**2*V**4*t*w**2 + 8*R**2*S**2*V**4*t*w + 4*R**2*S**2*V**4*t + 2*R**2*S**2*V**2*t**2*w**2 + 4*R**2*S**2*V**2*t**2*w + 2*R**2*S**2*V**2*t**2 - 4*R**2*S**2*V**2*t*w**2 - 8*R**2*S**2*V**2*t*w - 4*R**2*S**2*V**2*t + 2*R**2*S**2*V**2*w**2 + 4*R**2*S**2*V**2*w + 2*R**2*S**2*V**2 + 4*R**2*S**2*t*w**2 + 8*R**2*S**2*t*w + 4*R**2*S**2*t + R**2*U**4*V**2*t**2*w**2 + 2*R**2*U**4*V**2*t**2*w + R**2*U**4*V**2*t**2 + 2*R**2*U**4*V**2*t*w**2 + 4*R**2*U**4*V**2*t*w + 2*R**2*U**4*V**2*t + R**2*U**4*V**2*w**2 + 2*R**2*U**4*V**2*w + R**2*U**4*V**2 + 2*R**2*U**2*V**2*t**2*w**2 - 4*R**2*U**2*V**2*t**2*w + 2*R**2*U**2*V**2*t**2 + 4*R**2*U**2*V**2*t*w**2 - 8*R**2*U**2*V**2*t*w + 4*R**2*U**2*V**2*t + 2*R**2*U**2*V**2*w**2 - 4*R**2*U**2*V**2*w + 2*R**2*U**2*V**2 + R**2*V**2*t**2*w**2 + 2*R**2*V**2*t**2*w + R**2*V**2*t**2 + 2*R**2*V**2*t*w**2 + 4*R**2*V**2*t*w + 2*R**2*V**2*t + R**2*V**2*w**2 + 2*R**2*V**2*w + R**2*V**2 + 2*R*S**3*U**3*V**3*t**2*w**2 - 2*R*S**3*U**3*V**3*t**2 - 2*R*S**3*U**3*V**3*w**2 + 2*R*S**3*U**3*V**3 - 2*R*S**3*U**3*V*t**2*w**2 + 2*R*S**3*U**3*V*t**2 + 2*R*S**3*U**3*V*w**2 - 2*R*S**3*U**3*V - 8*R*S**3*U**2*V**2*t**2*w**2 + 16*R*S**3*U**2*V**2*t**2*w - 8*R*S**3*U**2*V**2*t**2 + 8*R*S**3*U**2*V**2*w**2 - 16*R*S**3*U**2*V**2*w + 8*R*S**3*U**2*V**2 - 2*R*S**3*U*V**3*t**2*w**2 + 2*R*S**3*U*V**3*t**2 + 2*R*S**3*U*V**3*w**2 - 2*R*S**3*U*V**3 + 2*R*S**3*U*V*t**2*w**2 - 2*R*S**3*U*V*t**2 - 2*R*S**3*U*V*w**2 + 2*R*S**3*U*V - 2*R*S*U**3*V**3*t**2*w**2 + 2*R*S*U**3*V**3*t**2 + 2*R*S*U**3*V**3*w**2 - 2*R*S*U**3*V**3 + 2*R*S*U**3*V*t**2*w**2 - 2*R*S*U**3*V*t**2 - 2*R*S*U**3*V*w**2 + 2*R*S*U**3*V + 8*R*S*U**2*V**2*t**2*w**2 - 16*R*S*U**2*V**2*t**2*w + 8*R*S*U**2*V**2*t**2 - 8*R*S*U**2*V**2*w**2 + 16*R*S*U**2*V**2*w - 8*R*S*U**2*V**2 + 2*R*S*U*V**3*t**2*w**2 - 2*R*S*U*V**3*t**2 - 2*R*S*U*V**3*w**2 + 2*R*S*U*V**3 - 2*R*S*U*V*t**2*w**2 + 2*R*S*U*V*t**2 + 2*R*S*U*V*w**2 - 2*R*S*U*V + 4*S**4*U**2*V**2*t**2*w + 8*S**4*U**2*V**2*t*w + 4*S**4*U**2*V**2*w + S**2*U**2*V**4*t**2*w**2 + 2*S**2*U**2*V**4*t**2*w + S**2*U**2*V**4*t**2 + 2*S**2*U**2*V**4*t*w**2 + 4*S**2*U**2*V**4*t*w + 2*S**2*U**2*V**4*t + S**2*U**2*V**4*w**2 + 2*S**2*U**2*V**4*w + S**2*U**2*V**4 + 2*S**2*U**2*V**2*t**2*w**2 - 4*S**2*U**2*V**2*t**2*w + 2*S**2*U**2*V**2*t**2 + 4*S**2*U**2*V**2*t*w**2 - 8*S**2*U**2*V**2*t*w + 4*S**2*U**2*V**2*t + 2*S**2*U**2*V**2*w**2 - 4*S**2*U**2*V**2*w + 2*S**2*U**2*V**2 + S**2*U**2*t**2*w**2 + 2*S**2*U**2*t**2*w + S**2*U**2*t**2 + 2*S**2*U**2*t*w**2 + 4*S**2*U**2*t*w + 2*S**2*U**2*t + S**2*U**2*w**2 + 2*S**2*U**2*w + S**2*U**2 + 4*U**2*V**2*t**2*w + 8*U**2*V**2*t*w + 4*U**2*V**2*w");
		longResult = SDS.sds(fn.homogenize('q'));
		System.out.println(longResult);
		*/
	}
}