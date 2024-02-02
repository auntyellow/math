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
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class SDSTest {
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

	private static RationalPoly addMul(RationalPoly f, Rational n, RationalPoly pos) {
		return new RationalPoly().add(f).add(n, pos);
	}

	@Test
	public void testTransform() {
		// A_n vs T_n vs H_3 vs J_4 vs Z_n
		// example 1:
		// fibonacci 91, 92
		String vars = "xy";
		long m = 4660046610375530309L;
		long n = 7540113804746346429L;
		RationalPoly f = new RationalPoly(vars, m + "*x - " + n + "*y");
		f = new RationalPoly().addMul(f, f);
		SDS.Result<Rational> result;/* = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals("[[" + n + ", " + m + "]]", result.getZeroAt().toString());
		assertEquals(91, result.getDepth());*/
		// 1e-22
		Rational e_22 = f.valueOf("1/10000000000000000000000");
		RationalPoly pos = new RationalPoly(vars, "x**2 + y**2");
		// T_2 works within 99 iterations (A_2 72)
		result = SDS.sds(addMul(f, e_22, pos), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// Z_2 == T_2
		result = SDS.sds(addMul(f, e_22, pos), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(99, result.getDepth());
		// T_2 finds negative within 98 iterations (A_2 71)
		RationalPoly f1 = addMul(f, e_22.negate(), pos);
		result = SDS.sds(f1, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(98, result.getDepth());
		// Z_2 == T_2
		result = SDS.sds(f1, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(98, result.getDepth());

		// example 2
		// (3*x - y)**2 + (x - z)**2
		vars = "xyz";
		f = new RationalPoly(vars, "10*x**2 - 6*x*y - 2*x*z + y**2 + z**2");
		// zero at (1, 3, 1), not on A_3 or T_3's lattice?
		assertEquals(0, subs(f, asList(f, 1, 3, 1), 'x').signum());
		// A_3 works for 1/6 but doesn't seem to work for 1/7
		pos = new RationalPoly(vars, "x**2 + y**2 + z**2");
		result = SDS.sds(addMul(f, f.valueOf("1/6"), pos));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(9, result.getDepth());
		// A_3 finds negative for 1e-22 (maybe larger)
		result = SDS.sds(addMul(f, e_22.negate(), pos));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 3, 1]", result.getNegativeAt().toString());
		assertEquals(2, result.getDepth());
		// 1e-8
		f1 = addMul(f, f.valueOf("1/100000000"), pos);
		// T_3 works within 16 iterations (A_3 doesn't work)
		result = SDS.sds(f1, T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// H_3 works within 15 iterations
		result = SDS.sds(f1, H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Y_3 == H3
		result = SDS.sds(f1, Y_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Z_3 works within 26 iterations
		result = SDS.sds(f1, Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(26, result.getDepth());
		// T_3 finds negative within 11 iterations
		f1 = addMul(f, f.valueOf("-1/100000000"), pos);
		result = SDS.sds(f1, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(11, result.getDepth());
		// H_3 finds negative within 13 iterations
		result = SDS.sds(f1, H_3);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(13, result.getDepth());
		// Y_3 == H_3
		result = SDS.sds(f1, Y_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(13, result.getDepth());
		// Z_3 finds negative within 16 iterations
		result = SDS.sds(f1, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(16, result.getDepth());

		// example 3
		// (2*w - x)**2 + (w - y)**2 + (w - z)**2
		vars = "wxyz";
		f = new RationalPoly(vars, "6*w**2 - 4*w*x - 2*w*y - 2*w*z + x**2 + y**2 + z**2");
		// zero at (1, 2, 1, 1), not on A_4 or T_4's lattice?
		assertEquals(0, subs(f, asList(f, 1, 2, 1, 1), 'w').signum());
		// A_4 works for 1/8 but doesn't seem to work for 1/9
		pos = new RationalPoly(vars, "w**2 + x**2 + y**2 + z**2");
		result = SDS.sds(addMul(f, f.valueOf("1/8"), pos));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(6, result.getDepth());
		// T_4 needs 9 for 1e-4, 12 for 1e-5 (19991 polynomials at 10th iteration); A_4 doesn't work
		result = SDS.sds(addMul(f, f.valueOf("1/10000"), pos), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(9, result.getDepth());
		// J_4 needs 16 for 1e-5, 21 for 1e-7, 27 for 1e-9
		result = SDS.sds(addMul(f, f.valueOf("1/100000"), pos), J_4);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// Y_4 works within 47 iterations for 1e-22
		result = SDS.sds(addMul(f, e_22, pos), Y_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(47, result.getDepth());
		// Z_4 works within 16 iterations for 1e-3, within 20 iterations for 1e-4 (374376 polynomials at 19th iteration)
		result = SDS.sds(addMul(f, f.valueOf("1/1000"), pos), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// A_4 finds negative for 1e-22 (maybe larger)
		result = SDS.sds(addMul(f, e_22.negate(), pos));
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 2, 1, 1]", result.getNegativeAt().toString());
		assertEquals(1, result.getDepth());
		// 1e-5
		f1 = addMul(f, f.valueOf("-1/100000"), pos);
		// T_4 finds negative within 11 iterations
		result = SDS.sds(f1, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(7, result.getDepth());
		// J_4 finds negative within 9 iterations
		result = SDS.sds(f1, J_4);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(9, result.getDepth());
		// Z_4 finds negative within 13 iterations
		result = SDS.sds(f1, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'w').signum() < 0);
		assertEquals(13, result.getDepth());
		// Y_4 finds negative within 5 iterations
		result = SDS.sds(f1, Y_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f1, result.getNegativeAt(), 'w').signum() < 0);
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
	public void testYang08() {
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
		// https://math.stackexchange.com/q/4850712
		// from 4850712u.py
		// m, n = 5, 13, non-negative, https://math.stackexchange.com/q/1777075
		f = new BigPoly("xyz", "325*x**5*y**2 + 125*x**5*z**2 + 325*x**4*y**3 - 845*x**4*y**2*z - 325*x**4*y*z**2 - 325*x**4*z**3 - 325*x**3*y**4 + 720*x**3*y**2*z**2 + 325*x**3*z**4 + 125*x**2*y**5 - 325*x**2*y**4*z + 720*x**2*y**3*z**2 + 720*x**2*y**2*z**3 - 845*x**2*y*z**4 + 325*x**2*z**5 - 845*x*y**4*z**2 - 325*x*y**2*z**4 + 325*y**5*z**2 + 325*y**4*z**3 - 325*y**3*z**4 + 125*y**2*z**5");
		result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 5; H_3 and Z_3 don't work
		assertEquals(4, result.getDepth());
		// m, n = 63, 164, non-negative
		f = new BigPoly("xyz", "650916*x**5*y**2 + 250047*x**5*z**2 + 650916*x**4*y**3 - 1694448*x**4*y**2*z - 650916*x**4*y*z**2 - 650916*x**4*z**3 - 650916*x**3*y**4 + 1444401*x**3*y**2*z**2 + 650916*x**3*z**4 + 250047*x**2*y**5 - 650916*x**2*y**4*z + 1444401*x**2*y**3*z**2 + 1444401*x**2*y**2*z**3 - 1694448*x**2*y*z**4 + 650916*x**2*z**5 - 1694448*x*y**4*z**2 - 650916*x*y**2*z**4 + 650916*y**5*z**2 + 650916*y**4*z**3 - 650916*y**3*z**4 + 250047*y**2*z**5");
		result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 9; H_3 and Z_3 don't work
		assertEquals(7, result.getDepth());
		// m, n = 121, 315, negative
		f = new BigPoly("xyz", "4611915*x**5*y**2 + 1771561*x**5*z**2 + 4611915*x**4*y**3 - 12006225*x**4*y**2*z - 4611915*x**4*y*z**2 - 4611915*x**4*z**3 - 4611915*x**3*y**4 + 10234664*x**3*y**2*z**2 + 4611915*x**3*z**4 + 1771561*x**2*y**5 - 4611915*x**2*y**4*z + 10234664*x**2*y**3*z**2 + 10234664*x**2*y**2*z**3 - 12006225*x**2*y*z**4 + 4611915*x**2*z**5 - 12006225*x*y**4*z**2 - 4611915*x*y**2*z**4 + 4611915*y**5*z**2 + 4611915*y**4*z**3 - 4611915*y**3*z**4 + 1771561*y**2*z**5");
		result = SDS.sds(f);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(4, result.getDepth());
		result = SDS.sds(f, T_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(7, result.getDepth());
		result = SDS.sds(f, H_3); // Y_3 == H_3
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(8, result.getDepth());
		result = SDS.sds(f, Z_n);
		assertTrue(!result.isNonNegative());
		assertTrue(subs(f, result.getNegativeAt(), 'x').signum() < 0);
		assertEquals(10, result.getDepth());
		// https://math.stackexchange.com/q/3526427
		f = new BigPoly("xyz", "x**9*y**3 - x**9*y**2*z - x**9*y*z**2 + x**9*z**3 + 6*x**8*y**4 + x**8*y**3*z - 10*x**8*y**2*z**2 + x**8*y*z**3 + 6*x**8*z**4 + 15*x**7*y**5 + 19*x**7*y**4*z - 26*x**7*y**3*z**2 - 26*x**7*y**2*z**3 + 19*x**7*y*z**4 + 15*x**7*z**5 + 20*x**6*y**6 + 45*x**6*y**5*z - 30*x**6*y**4*z**2 - 110*x**6*y**3*z**3 - 30*x**6*y**2*z**4 + 45*x**6*y*z**5 + 20*x**6*z**6 + 15*x**5*y**7 + 45*x**5*y**6*z - 26*x**5*y**5*z**2 - 202*x**5*y**4*z**3 - 202*x**5*y**3*z**4 - 26*x**5*y**2*z**5 + 45*x**5*y*z**6 + 15*x**5*z**7 + 6*x**4*y**8 + 19*x**4*y**7*z - 30*x**4*y**6*z**2 - 202*x**4*y**5*z**3 + 1410*x**4*y**4*z**4 - 202*x**4*y**3*z**5 - 30*x**4*y**2*z**6 + 19*x**4*y*z**7 + 6*x**4*z**8 + x**3*y**9 + x**3*y**8*z - 26*x**3*y**7*z**2 - 110*x**3*y**6*z**3 - 202*x**3*y**5*z**4 - 202*x**3*y**4*z**5 - 110*x**3*y**3*z**6 - 26*x**3*y**2*z**7 + x**3*y*z**8 + x**3*z**9 - x**2*y**9*z - 10*x**2*y**8*z**2 - 26*x**2*y**7*z**3 - 30*x**2*y**6*z**4 - 26*x**2*y**5*z**5 - 30*x**2*y**4*z**6 - 26*x**2*y**3*z**7 - 10*x**2*y**2*z**8 - x**2*y*z**9 - x*y**9*z**2 + x*y**8*z**3 + 19*x*y**7*z**4 + 45*x*y**6*z**5 + 45*x*y**5*z**6 + 19*x*y**4*z**7 + x*y**3*z**8 - x*y**2*z**9 + y**9*z**3 + 6*y**8*z**4 + 15*y**7*z**5 + 20*y**6*z**6 + 15*y**5*z**7 + 6*y**4*z**8 + y**3*z**9");
		result = SDS.sds(f, T_n);
		assertTrue(result.isNonNegative());
		assertEquals("[[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1]]", result.getZeroAt().toString());
		// A_3 needs 2; H_3 and Z_3 don't work
		assertEquals(4, result.getDepth());
		// https://math.stackexchange.com/q/4575195
		// f4 from 4575195.py when x, y <= z <= 6x, 6y
		// A_3 doesn't seem to work; T_3 needs 4; H_3 needs 3; Z_3 needs 5
		f = new BigPoly("uv", "65229815808*u**20*v**18 + 4377746079744*u**20*v**17 + 138309861900288*u**20*v**16 + 2738384736878592*u**20*v**15 + 38154737887477760*u**20*v**14 + 398229498393001984*u**20*v**13 + 3234945554633940992*u**20*v**12 + 20969275043700383744*u**20*v**11 + 110264513517565085696*u**20*v**10 + 475240632024438776320*u**20*v**9 + 1687777530304549730544*u**20*v**8 + 4941717745103586545952*u**20*v**7 + 11874605542918629309224*u**20*v**6 + 23165217668337851286216*u**20*v**5 + 35980334620703559639935*u**20*v**4 + 43049089265818514857368*u**20*v**3 + 37463096884257551761704*u**20*v**2 + 21220341305982040428768*u**20*v + 5906573325552857936112*u**20 - 65229815808*u**19*v**19 + 1806755168256*u**19*v**18 + 279441454399488*u**19*v**17 + 10552488625176576*u**19*v**16 + 226947523663101952*u**19*v**15 + 3324006446662025216*u**19*v**14 + 35915800796847669248*u**19*v**13 + 299432594060295819264*u**19*v**12 + 1980540375319698843648*u**19*v**11 + 10578595462678514498816*u**19*v**10 + 46120802072594315820256*u**19*v**9 + 164992510268872575085328*u**19*v**8 + 484431684331134327189464*u**19*v**7 + 1161541580536996719426668*u**19*v**6 + 2248967536438573628946676*u**19*v**5 + 3447226022780305076561732*u**19*v**4 + 4046559920875573645134336*u**19*v**3 + 3435109720553513114294688*u**19*v**2 + 1887839767861541231772096*u**19*v + 507453680772262315317312*u**19 + 65229815808*u**18*v**20 - 198055034880*u**18*v**19 + 108588023414784*u**18*v**18 + 11816511555502080*u**18*v**17 + 444929611019911168*u**18*v**16 + 9691784697467633664*u**18*v**15 + 143660273181775165440*u**18*v**14 + 1567007973593110474752*u**18*v**13 + 13155578705457631861760*u**18*v**12 + 87416953530132895316864*u**18*v**11 + 467995209558578127933704*u**18*v**10 + 2040303975505580740148120*u**18*v**9 + 7280848904464360129331802*u**18*v**8 + 21268559222225751804668880*u**18*v**7 + 50596460331186770111234874*u**18*v**6 + 96909127507538786113298248*u**18*v**5 + 146485708720583119191814050*u**18*v**4 + 169024118856148647244045584*u**18*v**3 + 140571968199573037136389200*u**18*v**2 + 75434360340357136776212928*u**18*v + 19734824687583015318362400*u**18 + 4377746079744*u**17*v**20 + 133090309570560*u**17*v**19 + 6252390676168704*u**17*v**18 + 367699555559276544*u**17*v**17 + 12523393915277541376*u**17*v**16 + 266096786629106522112*u**17*v**15 + 3913311732446660628480*u**17*v**14 + 42533066811017349189632*u**17*v**13 + 356041998364333222988992*u**17*v**12 + 2357495002390418321079688*u**17*v**11 + 12561899250624151983692492*u**17*v**10 + 54431172556452587574010680*u**17*v**9 + 192746437633021535515205752*u**17*v**8 + 557775989222274111107604252*u**17*v**7 + 1312165495169865654628088348*u**17*v**6 + 2480723059083325992939685524*u**17*v**5 + 3694236233970365773214820260*u**17*v**4 + 4191201099091877560300549824*u**17*v**3 + 3420327495906843041418374304*u**17*v**2 + 1797255402559428304131097536*u**17*v + 459425932222832862175310400*u**17 + 138309861900288*u**16*v**20 + 5523808513425408*u**16*v**19 + 192468133300469760*u**16*v**18 + 8048618007499898880*u**16*v**17 + 247041884549939986432*u**16*v**16 + 5078400398450615054336*u**16*v**15 + 73666602075778932025344*u**16*v**14 + 794126798910557509856640*u**16*v**13 + 6601330082602245088529775*u**16*v**12 + 43391963012072722232181816*u**16*v**11 + 229317593607996513411284980*u**16*v**10 + 984316965604229719237775064*u**16*v**9 + 3448340751272695708705370275*u**16*v**8 + 9858921475120937500423610260*u**16*v**7 + 22882550046725248107296187236*u**16*v**6 + 42622424390321993374040770204*u**16*v**5 + 62449103406631406853035994503*u**16*v**4 + 69611159009901173244414326520*u**16*v**3 + 55736649607968422395699251240*u**16*v**2 + 28694674992268663655862104352*u**16*v + 7176223707226916093759644272*u**16 + 2738384736878592*u**15*v**20 + 118770666814570496*u**15*v**19 + 3644479186205147136*u**15*v**18 + 124764703085273176064*u**15*v**17 + 3528305414599011696640*u**15*v**16 + 70513130124696846905344*u**15*v**15 + 1010162890504047567604288*u**15*v**14 + 10798149401417651716781108*u**15*v**13 + 89045797480512825738720452*u**15*v**12 + 580189111148128398179455440*u**15*v**11 + 3035635621438796856811308540*u**15*v**10 + 12882953258128571381522874688*u**15*v**9 + 44562078257000200229414048408*u**15*v**8 + 125624813257877654309515221912*u**15*v**7 + 287126840408285058341117921460*u**15*v**6 + 525995889160015966296515932216*u**15*v**5 + 757034156176616803026438388896*u**15*v**4 + 827943364014227711147380383936*u**15*v**3 + 649676021984379439570415433024*u**15*v**2 + 327418106136835204270378892160*u**15*v + 80067472555222306545671420928*u**15 + 38154737887477760*u**14*v**20 + 1689479792626630656*u**14*v**19 + 47250187656254814208*u**14*v**18 + 1408240099772436373504*u**14*v**17 + 37498809342110760798208*u**14*v**16 + 735415594471607862380096*u**14*v**15 + 10452093676259639918955338*u**14*v**14 + 111013506707043820302264864*u**14*v**13 + 908674429106314240332996612*u**14*v**12 + 5866865507029662109044732184*u**14*v**11 + 30364060178726750010150775808*u**14*v**10 + 127250263780087415995134810908*u**14*v**9 + 433955872057979926995338875654*u**14*v**8 + 1204318835193619771724080748412*u**14*v**7 + 2705927231012429617330089127044*u**14*v**6 + 4866622324410547636732785937068*u**14*v**5 + 6867867463971817402189702139976*u**14*v**4 + 7356194677826914097970889681248*u**14*v**3 + 5646805086064283898443941250304*u**14*v**2 + 2780903204434284928188693605568*u**14*v + 663817143900578971766706516096*u**14 + 398229498393001984*u**13*v**20 + 17471466941692313600*u**13*v**19 + 446666261795714363392*u**13*v**18 + 11867027448777864888320*u**13*v**17 + 302733594020332227947904*u**13*v**16 + 5893334798417658548905652*u**13*v**15 + 83641961403958814509151840*u**13*v**14 + 885703147502968777698839076*u**13*v**13 + 7206884035440686138851481820*u**13*v**12 + 46126028886864599752974601992*u**13*v**11 + 236055697529324815255235088532*u**13*v**10 + 976057940596362153728435730680*u**13*v**9 + 3277788598317651489682808649176*u**13*v**8 + 8942041893543256751695492343480*u**13*v**7 + 19718730610211495857576378505472*u**13*v**6 + 34755022804596495151044103351344*u**13*v**5 + 47999690198350684150256587297440*u**13*v**4 + 50248844861957732810917244500992*u**13*v**3 + 37651557884220515190111963252480*u**13*v**2 + 18077378132780279612978845296384*u**13*v + 4201706208148314653718435156480*u**13 + 3234945554633940992*u**12*v**20 + 138135813473700024320*u**12*v**19 + 3198101157351811054592*u**12*v**18 + 75822551305478350397632*u**12*v**17 + 1879579762973753352454223*u**12*v**16 + 36838405379167403089178436*u**12*v**15 + 526639244562346799794507060*u**12*v**14 + 5585733301351814592820252636*u**12*v**13 + 45283880020254971481657028551*u**12*v**12 + 287544951838072021236250417024*u**12*v**11 + 1455021046508023495134695590666*u**12*v**10 + 5932272678203325954076705202360*u**12*v**9 + 19597353780319511968617442796171*u**12*v**8 + 52484975763165302689109190880656*u**12*v**7 + 113413123431527860926463683082554*u**12*v**6 + 195550605575189531731209266061192*u**12*v**5 + 263788119436682459715008433972120*u**12*v**4 + 269318491138163210248821889858752*u**12*v**3 + 196520872968004971405869421494112*u**12*v**2 + 91749804971194784458761443584128*u**12*v + 20704524924969482875428805326720*u**12 + 20969275043700383744*u**11*v**20 + 861292252173261973504*u**11*v**19 + 17753671095346140945280*u**11*v**18 + 368401031476764915929160*u**11*v**17 + 8996432489958319876292056*u**11*v**16 + 181070674934226389837866688*u**11*v**15 + 2638454834655234000231921672*u**11*v**14 + 28202119152668563285411400120*u**11*v**13 + 228478518046686595767159332560*u**11*v**12 + 1441135671330641956214380510928*u**11*v**11 + 7211819922940400957640946041500*u**11*v**10 + 28978843543063140454110797787132*u**11*v**9 + 94086199101456115801441715105100*u**11*v**8 + 247058411058319783908065363398440*u**11*v**7 + 522343066803698380963140123501888*u**11*v**6 + 879539099228096427721790465471712*u**11*v**5 + 1156603225830795796694051347006464*u**11*v**4 + 1149179332284921698299485843557760*u**11*v**3 + 814681367407950731923208599895040*u**11*v**2 + 368878789409032611862182900758016*u**11*v + 80577902831015233287566814790656*u**11 + 110264513517565085696*u**10*v**20 + 4322697035922948857088*u**10*v**19 + 77485923442099026406280*u**10*v**18 + 1339453508996999429391788*u**10*v**17 + 32793487642913068539066052*u**10*v**16 + 700194655897353318395753180*u**10*v**15 + 10581779256389368193803916304*u**10*v**14 + 114931185527482314721491019380*u**10*v**13 + 934048085065454174498104619034*u**10*v**12 + 5861688056692107741021168562236*u**10*v**11 + 29020071055094239150621240629974*u**10*v**10 + 114882559758621678115389599321844*u**10*v**9 + 366261029419648459195595204309970*u**10*v**8 + 941833734477088678639345352438604*u**10*v**7 + 1945441207508767001540085423672216*u**10*v**6 + 3193646359947892149550831933714992*u**10*v**5 + 4086307485114372240666360588052128*u**10*v**4 + 3942995904557789519545298376621120*u**10*v**3 + 2709535545990012506592720534484608*u**10*v**2 + 1186853546286542552523303028684032*u**10*v + 250248627293265496330863862090752*u**10 + 475240632024438776320*u**9*v**20 + 17705961394788513095136*u**9*v**19 + 267895824037635098628248*u**9*v**18 + 3436890522405486260005944*u**9*v**17 + 87272147469453721503971288*u**9*v**16 + 2110001112854018734559591936*u**9*v**15 + 34007516885705203602986279228*u**9*v**14 + 379635224910697382471701405784*u**9*v**13 + 3110212249410088785977382082632*u**9*v**12 + 19457800145680323981718492949724*u**9*v**11 + 95349801966100703610108884155668*u**9*v**10 + 371746752835381081905620922677748*u**9*v**9 + 1162795347470313958152170111474124*u**9*v**8 + 2924645069450767422459013202275632*u**9*v**7 + 5893472340703448372168306486580384*u**9*v**6 + 9416500685828258541865049598643008*u**9*v**5 + 11701878810984814720685901748678656*u**9*v**4 + 10944148172955865911320860290809088*u**9*v**3 + 7274280228148933315560746548498944*u**9*v**2 + 3075345764043013033449596828264448*u**9*v + 624328144733119114774614907155456*u**9 + 1687777530304549730544*u**8*v**20 + 59721447901610251703440*u**8*v**19 + 736514834925058798721082*u**8*v**18 + 4933504535385440531009000*u**8*v**17 + 147230206208803719838324579*u**8*v**16 + 4824187534367249000148579912*u**8*v**15 + 87186738563200222349600725910*u**8*v**14 + 1016896086523781164731584781096*u**8*v**13 + 8450393590067793861753407221035*u**8*v**12 + 52824058733985752672146695112092*u**8*v**11 + 256356682273124029710790531162002*u**8*v**10 + 983969212697231933201647636914300*u**8*v**9 + 3016910513301456717322698443588271*u**8*v**8 + 7412689300194851405696984328981120*u**8*v**7 + 14550680440491023871191491222696272*u**8*v**6 + 22590793319136020551770335981679744*u**8*v**5 + 27217056449456446436527713340978080*u**8*v**4 + 24624750249749196993422809479877632*u**8*v**3 + 15799736295741136922472096067080960*u**8*v**2 + 6433475542585483713573026668944384*u**8*v + 1254761914852952874518433044463360*u**8 + 4941717745103586545952*u**7*v**20 + 166653103543057644894360*u**7*v**19 + 1617481545429868079698672*u**7*v**18 - 3270329721407772273094468*u**7*v**17 + 42431579983221101414579668*u**7*v**16 + 7816861826390769450957489736*u**7*v**15 + 176333589030624619496981748380*u**7*v**14 + 2201898933292034940371976293176*u**7*v**13 + 18702959385661421232704039328576*u**7*v**12 + 117114854074128001615110251489784*u**7*v**11 + 563137961349005316803930011569756*u**7*v**10 + 2126860812994838281063997097314880*u**7*v**9 + 6385451128457567330256418959983136*u**7*v**8 + 15305819595283168760271745950368256*u**7*v**7 + 29220822069424960721251905132084864*u**7*v**6 + 44007765840733259783617268198925312*u**7*v**5 + 51309803486892421772674890526863360*u**7*v**4 + 44825571944466962382194256158533632*u**7*v**3 + 27710780963157291121996275857267712*u**7*v**2 + 10846965541517328860956165144117248*u**7*v + 2028659533973781733647874485411840*u**7 + 11874605542918629309224*u**6*v**20 + 384726286826731508119884*u**6*v**19 + 2879304624477185270037930*u**6*v**18 - 40518661944504092400709220*u**6*v**17 - 614122893440847068565196284*u**6*v**16 + 7068539333782681813557392868*u**6*v**15 + 275701449180829749298981784612*u**6*v**14 + 3827914196362104455426396471520*u**6*v**13 + 33540852764029516396578116534970*u**6*v**12 + 210907003551571761459043166500608*u**6*v**11 + 1004987308023083237098133321409960*u**6*v**10 + 3731854585171447237471145634223872*u**6*v**9 + 10956915297873612247739473202821200*u**6*v**8 + 25581460330967209682457331572278400*u**6*v**7 + 47417574030254155806142921283328768*u**6*v**6 + 69146976530211989209707261533824512*u**6*v**5 + 77873998967779925892416693755014144*u**6*v**4 + 65568454594754594753870416868751360*u**6*v**3 + 38981345866437552988876720531752960*u**6*v**2 + 14642192242785913976321835504869376*u**6*v + 2621699771995167735829840064925696*u**6 + 23165217668337851286216*u**5*v**20 + 730137294400849995585588*u**5*v**19 + 4328094342974369640270984*u**5*v**18 - 121439109601746903382261740*u**5*v**17 - 2162592161445183113050494564*u**5*v**16 - 2685053543358073386916944504*u**5*v**15 + 322172970315984985253830589484*u**5*v**14 + 5286934160384004772913856630672*u**5*v**13 + 48268253374344046747082070749880*u**5*v**12 + 305336371838602934767058708336928*u**5*v**11 + 1441167207258528179905249855860912*u**5*v**10 + 5254735449931658662865455699231104*u**5*v**9 + 15062315891081197823625532153704192*u**5*v**8 + 34188691754116278016993241644884480*u**5*v**7 + 61406264641518505981634980619893248*u**5*v**6 + 86529307818235167082410692751820800*u**5*v**5 + 93940204738932144562729820682590208*u**5*v**4 + 76080041053761971039843200928661504*u**5*v**3 + 43416046896053995969150126459023360*u**5*v**2 + 15621855519490973450625535182176256*u**5*v + 2673823685952214996351487104647168*u**5 + 35980334620703559639935*u**4*v**20 + 1121378821200971343361172*u**4*v**19 + 5896895300125862522238546*u**4*v**18 - 219649397088267861885710572*u**4*v**17 - 4193873312242424432743150969*u**4*v**16 - 20522470301833638872244938208*u**4*v**15 + 266252978607965451930192092856*u**4*v**14 + 5720276182342797527823639435168*u**4*v**13 + 54878652070077489438237985277784*u**4*v**12 + 349253810897428085664618384818688*u**4*v**11 + 1630168484423298726669291060718176*u**4*v**10 + 5823994191093034950665810975412096*u**4*v**9 + 16260853134040240435876334078790048*u**4*v**8 + 35798362987075956406806334916189184*u**4*v**7 + 62155461953526575433820762818475008*u**4*v**6 + 84435934082695195850984431052015616*u**4*v**5 + 88164196060291728181880124164262912*u**4*v**4 + 68529950506943644848202346544562176*u**4*v**3 + 37462413689525116249004621588963328*u**4*v**2 + 12889141081939162638985430649470976*u**4*v + 2105701442909713115679316897308672*u**4 + 43049089265818514857368*u**3*v**20 + 1351572167268716152254960*u**3*v**19 + 7549213950581082807736224*u**3*v**18 - 258241278219066126643992240*u**3*v**17 - 5263260892786481591533699032*u**3*v**16 - 34132675303391866860028032576*u**3*v**15 + 142975107468862251123821945760*u**3*v**14 + 4762965907072193505053767414272*u**3*v**13 + 48068329961612449156736364321600*u**3*v**12 + 306675385894339437136554846094464*u**3*v**11 + 1410497714294227908200884015151424*u**3*v**10 + 4921080914653971563136565558794240*u**3*v**9 + 13340995263591645118063933318390272*u**3*v**8 + 28399805746382402261413595416811520*u**3*v**7 + 47527153878661104793308405344999424*u**3*v**6 + 62066889194600496016839735697563648*u**3*v**5 + 62163009211030795351736002417213440*u**3*v**4 + 46258619366812319776614354061492224*u**3*v**3 + 24168062763501309762235083827527680*u**3*v**2 + 7934836132464439557125465341820928*u**3*v + 1235294590226025528633325271777280*u**3 + 37463096884257551761704*u**2*v**20 + 1207380446222922285825600*u**2*v**19 + 8283496779312931792232784*u**2*v**18 - 186211278414303642383173056*u**2*v**17 - 4198216648896033244624721304*u**2*v**16 - 30489560944624855646822801088*u**2*v**15 + 47839365979805081449117324800*u**2*v**14 + 2973066251015065645053840252672*u**2*v**13 + 31022858798388372297110373463392*u**2*v**12 + 196515505278176603290363604072448*u**2*v**11 + 884867626998151485269915618024832*u**2*v**10 + 2999550206079568177014433198003200*u**2*v**9 + 7860991793188496613304559184974592*u**2*v**8 + 16116410622637716547166392879844352*u**2*v**7 + 25898569821791916868868939101329408*u**2*v**6 + 32398916397883844886625869537030144*u**2*v**5 + 31022142782879443199571765955584000*u**2*v**4 + 22033024182722772725872951238344704*u**2*v**3 + 10971175839851433369189025925627904*u**2*v**2 + 3429009104234352961035175881670656*u**2*v + 507699278428117492467163263467520*u**2 + 21220341305982040428768*u*v**20 + 714162447978570556524288*u*v**19 + 6353398511758523987516160*u*v**18 - 65853253884947036221872000*u*v**17 - 1868439727642606407348549408*u*v**16 - 14156979826347591881992089984*u*v**15 + 18479730198727282222923470784*u*v**14 + 1306004306598400764814212983040*u*v**13 + 13439683257034601618754395506560*u*v**12 + 83013434447988584341990769066496*u*v**11 + 362177595019863893986571892061440*u*v**10 + 1184019071769751633126884103394304*u*v**9 + 2981398004241657155407443157632000*u*v**8 + 5855043789525434065186754925342720*u*v**7 + 8990278552129251116192382681071616*u*v**6 + 10724488474919531835723551673237504*u*v**5 + 9775689828876684029864638678007808*u*v**4 + 6600946855137519087692395465605120*u*v**3 + 3121769635557314184244997091164160*u*v**2 + 926012791203993231961173523955712*u*v + 130068253113945066432107517837312*u + 5906573325552857936112*v**20 + 210525699618915720866496*v**19 + 2406641604303486650656032*v**18 - 2956333645591240533542208*v**17 - 309985448637458831443269264*v**16 - 2281596423059434708081170432*v**15 + 10238510884163897733866702208*v**14 + 318897291611751472579591420416*v**13 + 3009850957851696630343526749056*v**12 + 17652173230932683799241081893888*v**11 + 73524885318704309986650063532032*v**10 + 229399864077510332190974797360128*v**9 + 550316226514856972883554610798336*v**8 + 1027610014825799905945979434254336*v**7 + 1497652158274012975752387854880768*v**6 + 1693269942159264299458294227959808*v**5 + 1461259528285827351999799052476416*v**4 + 933416538397930498016425858301952*v**3 + 417400799036806731090924396675072*v**2 + 117053405816296970465966958575616*v + 15546695934451042905827618783232").homogenize('w');
		result = SDS.sds(f, H_3);
		assertTrue(result.isNonNegative());
		assertEquals(3, result.getDepth());
		// https://math.stackexchange.com/q/4765187
		f = new BigPoly("xyz", "x**7*y**7*z**7 + 7*x**7*y**7*z**6 + 21*x**7*y**7*z**5 + 35*x**7*y**7*z**4 + 35*x**7*y**7*z**3 + 21*x**7*y**7*z**2 + 7*x**7*y**7*z + x**7*y**7 + 7*x**7*y**6*z**7 + 49*x**7*y**6*z**6 + 147*x**7*y**6*z**5 + 245*x**7*y**6*z**4 + 245*x**7*y**6*z**3 + 147*x**7*y**6*z**2 + 49*x**7*y**6*z + 7*x**7*y**6 + 21*x**7*y**5*z**7 + 147*x**7*y**5*z**6 + 441*x**7*y**5*z**5 + 735*x**7*y**5*z**4 + 735*x**7*y**5*z**3 + 441*x**7*y**5*z**2 + 147*x**7*y**5*z + 21*x**7*y**5 + 35*x**7*y**4*z**7 + 245*x**7*y**4*z**6 + 735*x**7*y**4*z**5 + 1225*x**7*y**4*z**4 + 1225*x**7*y**4*z**3 + 735*x**7*y**4*z**2 + 245*x**7*y**4*z + 35*x**7*y**4 + 35*x**7*y**3*z**7 + 245*x**7*y**3*z**6 + 735*x**7*y**3*z**5 + 1225*x**7*y**3*z**4 + 1225*x**7*y**3*z**3 + 735*x**7*y**3*z**2 + 245*x**7*y**3*z + 35*x**7*y**3 + 21*x**7*y**2*z**7 + 147*x**7*y**2*z**6 + 441*x**7*y**2*z**5 + 735*x**7*y**2*z**4 + 735*x**7*y**2*z**3 + 441*x**7*y**2*z**2 + 147*x**7*y**2*z + 21*x**7*y**2 + 7*x**7*y*z**7 + 49*x**7*y*z**6 + 147*x**7*y*z**5 + 245*x**7*y*z**4 + 245*x**7*y*z**3 + 147*x**7*y*z**2 + 49*x**7*y*z + 7*x**7*y + x**7*z**7 + 7*x**7*z**6 + 21*x**7*z**5 + 35*x**7*z**4 + 35*x**7*z**3 + 21*x**7*z**2 + 7*x**7*z + x**7 + 7*x**6*y**7*z**7 + 49*x**6*y**7*z**6 + 147*x**6*y**7*z**5 + 245*x**6*y**7*z**4 + 245*x**6*y**7*z**3 + 147*x**6*y**7*z**2 + 49*x**6*y**7*z + 7*x**6*y**7 + 49*x**6*y**6*z**7 + 343*x**6*y**6*z**6 + 1029*x**6*y**6*z**5 + 1715*x**6*y**6*z**4 + 1715*x**6*y**6*z**3 + 1029*x**6*y**6*z**2 + 343*x**6*y**6*z + 49*x**6*y**6 + 147*x**6*y**5*z**7 + 1029*x**6*y**5*z**6 + 3087*x**6*y**5*z**5 + 5145*x**6*y**5*z**4 + 5145*x**6*y**5*z**3 + 3087*x**6*y**5*z**2 + 1029*x**6*y**5*z + 147*x**6*y**5 + 245*x**6*y**4*z**7 + 1715*x**6*y**4*z**6 + 5145*x**6*y**4*z**5 + 8575*x**6*y**4*z**4 + 8575*x**6*y**4*z**3 + 5145*x**6*y**4*z**2 + 1715*x**6*y**4*z + 245*x**6*y**4 + 245*x**6*y**3*z**7 + 1715*x**6*y**3*z**6 + 5145*x**6*y**3*z**5 + 8575*x**6*y**3*z**4 + 8575*x**6*y**3*z**3 + 5145*x**6*y**3*z**2 + 1715*x**6*y**3*z + 245*x**6*y**3 + 147*x**6*y**2*z**7 + 1029*x**6*y**2*z**6 + 3087*x**6*y**2*z**5 + 5145*x**6*y**2*z**4 + 5145*x**6*y**2*z**3 + 3087*x**6*y**2*z**2 + 1029*x**6*y**2*z + 147*x**6*y**2 + 49*x**6*y*z**7 + 343*x**6*y*z**6 + 1029*x**6*y*z**5 + 1715*x**6*y*z**4 + 1715*x**6*y*z**3 + 1029*x**6*y*z**2 + 343*x**6*y*z + 49*x**6*y + 7*x**6*z**7 + 49*x**6*z**6 + 147*x**6*z**5 + 245*x**6*z**4 + 245*x**6*z**3 + 147*x**6*z**2 + 49*x**6*z + 7*x**6 + 21*x**5*y**7*z**7 + 147*x**5*y**7*z**6 + 441*x**5*y**7*z**5 + 735*x**5*y**7*z**4 + 735*x**5*y**7*z**3 + 441*x**5*y**7*z**2 + 147*x**5*y**7*z + 21*x**5*y**7 + 147*x**5*y**6*z**7 + 1029*x**5*y**6*z**6 + 3087*x**5*y**6*z**5 + 5145*x**5*y**6*z**4 + 5145*x**5*y**6*z**3 + 3087*x**5*y**6*z**2 + 1029*x**5*y**6*z + 147*x**5*y**6 + 441*x**5*y**5*z**7 + 3087*x**5*y**5*z**6 + 9261*x**5*y**5*z**5 + 15435*x**5*y**5*z**4 + 15435*x**5*y**5*z**3 + 9261*x**5*y**5*z**2 + 3087*x**5*y**5*z + 441*x**5*y**5 + 735*x**5*y**4*z**7 + 5145*x**5*y**4*z**6 + 15435*x**5*y**4*z**5 + 25725*x**5*y**4*z**4 + 25725*x**5*y**4*z**3 + 15435*x**5*y**4*z**2 + 5145*x**5*y**4*z + 735*x**5*y**4 + 735*x**5*y**3*z**7 + 5145*x**5*y**3*z**6 + 15435*x**5*y**3*z**5 + 25725*x**5*y**3*z**4 + 25725*x**5*y**3*z**3 + 15435*x**5*y**3*z**2 + 5145*x**5*y**3*z + 735*x**5*y**3 + 441*x**5*y**2*z**7 + 3087*x**5*y**2*z**6 + 9261*x**5*y**2*z**5 + 15435*x**5*y**2*z**4 + 15435*x**5*y**2*z**3 + 9261*x**5*y**2*z**2 + 3087*x**5*y**2*z + 441*x**5*y**2 + 147*x**5*y*z**7 + 1029*x**5*y*z**6 + 3087*x**5*y*z**5 + 5145*x**5*y*z**4 + 5145*x**5*y*z**3 + 3087*x**5*y*z**2 + 1029*x**5*y*z + 147*x**5*y + 21*x**5*z**7 + 147*x**5*z**6 + 441*x**5*z**5 + 735*x**5*z**4 + 735*x**5*z**3 + 441*x**5*z**2 + 147*x**5*z + 21*x**5 + 35*x**4*y**7*z**7 + 245*x**4*y**7*z**6 + 735*x**4*y**7*z**5 + 1225*x**4*y**7*z**4 + 1225*x**4*y**7*z**3 + 735*x**4*y**7*z**2 + 245*x**4*y**7*z + 35*x**4*y**7 + 245*x**4*y**6*z**7 + 1715*x**4*y**6*z**6 + 5145*x**4*y**6*z**5 + 8575*x**4*y**6*z**4 + 8575*x**4*y**6*z**3 + 5145*x**4*y**6*z**2 + 1715*x**4*y**6*z + 245*x**4*y**6 + 735*x**4*y**5*z**7 + 5145*x**4*y**5*z**6 + 15435*x**4*y**5*z**5 + 25725*x**4*y**5*z**4 + 25725*x**4*y**5*z**3 + 15435*x**4*y**5*z**2 + 5145*x**4*y**5*z + 735*x**4*y**5 + 1225*x**4*y**4*z**7 + 8575*x**4*y**4*z**6 + 25725*x**4*y**4*z**5 - 780668*x**4*y**4*z**4 + 42875*x**4*y**4*z**3 + 25725*x**4*y**4*z**2 + 8575*x**4*y**4*z + 1225*x**4*y**4 + 1225*x**4*y**3*z**7 + 8575*x**4*y**3*z**6 + 25725*x**4*y**3*z**5 + 42875*x**4*y**3*z**4 + 42875*x**4*y**3*z**3 + 25725*x**4*y**3*z**2 + 8575*x**4*y**3*z + 1225*x**4*y**3 + 735*x**4*y**2*z**7 + 5145*x**4*y**2*z**6 + 15435*x**4*y**2*z**5 + 25725*x**4*y**2*z**4 + 25725*x**4*y**2*z**3 + 15435*x**4*y**2*z**2 + 5145*x**4*y**2*z + 735*x**4*y**2 + 245*x**4*y*z**7 + 1715*x**4*y*z**6 + 5145*x**4*y*z**5 + 8575*x**4*y*z**4 + 8575*x**4*y*z**3 + 5145*x**4*y*z**2 + 1715*x**4*y*z + 245*x**4*y + 35*x**4*z**7 + 245*x**4*z**6 + 735*x**4*z**5 + 1225*x**4*z**4 + 1225*x**4*z**3 + 735*x**4*z**2 + 245*x**4*z + 35*x**4 + 35*x**3*y**7*z**7 + 245*x**3*y**7*z**6 + 735*x**3*y**7*z**5 + 1225*x**3*y**7*z**4 + 1225*x**3*y**7*z**3 + 735*x**3*y**7*z**2 + 245*x**3*y**7*z + 35*x**3*y**7 + 245*x**3*y**6*z**7 + 1715*x**3*y**6*z**6 + 5145*x**3*y**6*z**5 + 8575*x**3*y**6*z**4 + 8575*x**3*y**6*z**3 + 5145*x**3*y**6*z**2 + 1715*x**3*y**6*z + 245*x**3*y**6 + 735*x**3*y**5*z**7 + 5145*x**3*y**5*z**6 + 15435*x**3*y**5*z**5 + 25725*x**3*y**5*z**4 + 25725*x**3*y**5*z**3 + 15435*x**3*y**5*z**2 + 5145*x**3*y**5*z + 735*x**3*y**5 + 1225*x**3*y**4*z**7 + 8575*x**3*y**4*z**6 + 25725*x**3*y**4*z**5 + 42875*x**3*y**4*z**4 + 42875*x**3*y**4*z**3 + 25725*x**3*y**4*z**2 + 8575*x**3*y**4*z + 1225*x**3*y**4 + 1225*x**3*y**3*z**7 + 8575*x**3*y**3*z**6 + 25725*x**3*y**3*z**5 + 42875*x**3*y**3*z**4 + 42875*x**3*y**3*z**3 + 25725*x**3*y**3*z**2 + 8575*x**3*y**3*z + 1225*x**3*y**3 + 735*x**3*y**2*z**7 + 5145*x**3*y**2*z**6 + 15435*x**3*y**2*z**5 + 25725*x**3*y**2*z**4 + 25725*x**3*y**2*z**3 + 15435*x**3*y**2*z**2 + 5145*x**3*y**2*z + 735*x**3*y**2 + 245*x**3*y*z**7 + 1715*x**3*y*z**6 + 5145*x**3*y*z**5 + 8575*x**3*y*z**4 + 8575*x**3*y*z**3 + 5145*x**3*y*z**2 + 1715*x**3*y*z + 245*x**3*y + 35*x**3*z**7 + 245*x**3*z**6 + 735*x**3*z**5 + 1225*x**3*z**4 + 1225*x**3*z**3 + 735*x**3*z**2 + 245*x**3*z + 35*x**3 + 21*x**2*y**7*z**7 + 147*x**2*y**7*z**6 + 441*x**2*y**7*z**5 + 735*x**2*y**7*z**4 + 735*x**2*y**7*z**3 + 441*x**2*y**7*z**2 + 147*x**2*y**7*z + 21*x**2*y**7 + 147*x**2*y**6*z**7 + 1029*x**2*y**6*z**6 + 3087*x**2*y**6*z**5 + 5145*x**2*y**6*z**4 + 5145*x**2*y**6*z**3 + 3087*x**2*y**6*z**2 + 1029*x**2*y**6*z + 147*x**2*y**6 + 441*x**2*y**5*z**7 + 3087*x**2*y**5*z**6 + 9261*x**2*y**5*z**5 + 15435*x**2*y**5*z**4 + 15435*x**2*y**5*z**3 + 9261*x**2*y**5*z**2 + 3087*x**2*y**5*z + 441*x**2*y**5 + 735*x**2*y**4*z**7 + 5145*x**2*y**4*z**6 + 15435*x**2*y**4*z**5 + 25725*x**2*y**4*z**4 + 25725*x**2*y**4*z**3 + 15435*x**2*y**4*z**2 + 5145*x**2*y**4*z + 735*x**2*y**4 + 735*x**2*y**3*z**7 + 5145*x**2*y**3*z**6 + 15435*x**2*y**3*z**5 + 25725*x**2*y**3*z**4 + 25725*x**2*y**3*z**3 + 15435*x**2*y**3*z**2 + 5145*x**2*y**3*z + 735*x**2*y**3 + 441*x**2*y**2*z**7 + 3087*x**2*y**2*z**6 + 9261*x**2*y**2*z**5 + 15435*x**2*y**2*z**4 + 15435*x**2*y**2*z**3 + 9261*x**2*y**2*z**2 + 3087*x**2*y**2*z + 441*x**2*y**2 + 147*x**2*y*z**7 + 1029*x**2*y*z**6 + 3087*x**2*y*z**5 + 5145*x**2*y*z**4 + 5145*x**2*y*z**3 + 3087*x**2*y*z**2 + 1029*x**2*y*z + 147*x**2*y + 21*x**2*z**7 + 147*x**2*z**6 + 441*x**2*z**5 + 735*x**2*z**4 + 735*x**2*z**3 + 441*x**2*z**2 + 147*x**2*z + 21*x**2 + 7*x*y**7*z**7 + 49*x*y**7*z**6 + 147*x*y**7*z**5 + 245*x*y**7*z**4 + 245*x*y**7*z**3 + 147*x*y**7*z**2 + 49*x*y**7*z + 7*x*y**7 + 49*x*y**6*z**7 + 343*x*y**6*z**6 + 1029*x*y**6*z**5 + 1715*x*y**6*z**4 + 1715*x*y**6*z**3 + 1029*x*y**6*z**2 + 343*x*y**6*z + 49*x*y**6 + 147*x*y**5*z**7 + 1029*x*y**5*z**6 + 3087*x*y**5*z**5 + 5145*x*y**5*z**4 + 5145*x*y**5*z**3 + 3087*x*y**5*z**2 + 1029*x*y**5*z + 147*x*y**5 + 245*x*y**4*z**7 + 1715*x*y**4*z**6 + 5145*x*y**4*z**5 + 8575*x*y**4*z**4 + 8575*x*y**4*z**3 + 5145*x*y**4*z**2 + 1715*x*y**4*z + 245*x*y**4 + 245*x*y**3*z**7 + 1715*x*y**3*z**6 + 5145*x*y**3*z**5 + 8575*x*y**3*z**4 + 8575*x*y**3*z**3 + 5145*x*y**3*z**2 + 1715*x*y**3*z + 245*x*y**3 + 147*x*y**2*z**7 + 1029*x*y**2*z**6 + 3087*x*y**2*z**5 + 5145*x*y**2*z**4 + 5145*x*y**2*z**3 + 3087*x*y**2*z**2 + 1029*x*y**2*z + 147*x*y**2 + 49*x*y*z**7 + 343*x*y*z**6 + 1029*x*y*z**5 + 1715*x*y*z**4 + 1715*x*y*z**3 + 1029*x*y*z**2 + 343*x*y*z + 49*x*y + 7*x*z**7 + 49*x*z**6 + 147*x*z**5 + 245*x*z**4 + 245*x*z**3 + 147*x*z**2 + 49*x*z + 7*x + y**7*z**7 + 7*y**7*z**6 + 21*y**7*z**5 + 35*y**7*z**4 + 35*y**7*z**3 + 21*y**7*z**2 + 7*y**7*z + y**7 + 7*y**6*z**7 + 49*y**6*z**6 + 147*y**6*z**5 + 245*y**6*z**4 + 245*y**6*z**3 + 147*y**6*z**2 + 49*y**6*z + 7*y**6 + 21*y**5*z**7 + 147*y**5*z**6 + 441*y**5*z**5 + 735*y**5*z**4 + 735*y**5*z**3 + 441*y**5*z**2 + 147*y**5*z + 21*y**5 + 35*y**4*z**7 + 245*y**4*z**6 + 735*y**4*z**5 + 1225*y**4*z**4 + 1225*y**4*z**3 + 735*y**4*z**2 + 245*y**4*z + 35*y**4 + 35*y**3*z**7 + 245*y**3*z**6 + 735*y**3*z**5 + 1225*y**3*z**4 + 1225*y**3*z**3 + 735*y**3*z**2 + 245*y**3*z + 35*y**3 + 21*y**2*z**7 + 147*y**2*z**6 + 441*y**2*z**5 + 735*y**2*z**4 + 735*y**2*z**3 + 441*y**2*z**2 + 147*y**2*z + 21*y**2 + 7*y*z**7 + 49*y*z**6 + 147*y*z**5 + 245*y*z**4 + 245*y*z**3 + 147*y*z**2 + 49*y*z + 7*y + z**7 + 7*z**6 + 21*z**5 + 35*z**4 + 35*z**3 + 21*z**2 + 7*z + 1").homogenize('w');
		// A_4 and T_4 need 1; J_4 and Y_4 need 2; Z_4 needs 3
		result = SDS.sds(f);
		assertTrue(result.isNonNegative());
		assertEquals(1, result.getDepth());
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
		RationalPoly f = new RationalPoly("xyz", "9*x**2 + 6*x*y - 6*x*z + y**2 - 2*y*z + z**2");
		// T_3 works for 1/3e6 within 16 iterations, 1/3e7 within 18 iterations (73801 polynomials after 13th iteration); A_3 doesn't work
		RationalPoly pos = new RationalPoly("xyz", "z**2");
		RationalPoly f1 = addMul(f, f.valueOf("1/3000000"), pos);
		SDS.Result<Rational> result = SDS.sds(f1, T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(16, result.getDepth());
		// H_3 works for 1/3e6 within 13 iterations, 1/3e7 within 15 iterations, Y_3 == H_3
		result = SDS.sds(f1, H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(13, result.getDepth());
		result = SDS.sds(addMul(f, f.valueOf("1/30000000"), pos), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(15, result.getDepth());
		// Z_3 works for 1/3e5 within 19 iterations, 1/3e6 within 22 iterations
		result = SDS.sds(addMul(f, f.valueOf("1/300000"), pos), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(19, result.getDepth());
		// ex 4.2
		BigPoly g = new BigPoly("abcdefghij", replaceAn("a1**2 + a2**2 + a3**2 + a4**2 + a5**2 + a6**2 + a7**2 + a8**2 + a9**2 + a10**2 - 4*a1*a2").toString());
		SDS.Result<MutableBig> bigResult = SDS.sds(g);
		assertTrue(!bigResult.isNonNegative());
		assertTrue(subs(g, bigResult.getNegativeAt(), 'a').signum() < 0);
		assertEquals(0, bigResult.getDepth());
		// ex 4.3
		g = new BigPoly("xyz", "x**3 + y**3 + z**3 - 3*x*y*z");
		bigResult = SDS.sds(g);
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(1, bigResult.getDepth());
		// H_3 and Z_3 don't work
		// result = SDS.sds(f, H_3);
		g = new BigPoly("xyzw", "x**4 + y**4 + z**4 + w**4 - 4*x*y*z*w");
		bigResult = SDS.sds(g);
		assertTrue(bigResult.isNonNegative());
		assertEquals("[[1, 1, 1, 1]]", bigResult.getZeroAt().toString());
		assertEquals(1, bigResult.getDepth());
		// J_4 and Z_4 don't work
		// result = SDS.sds(f, J_4);
		// ex 4.4
		f = new RationalPoly("abc", "a**4 - 3*a**3*b + 2*a**2*b**2 + 2*a**2*c**2 - 3*a*c**3 + b**4 - 3*b**3*c + 2*b**2*c**2 + c**4");
		// zero at (1, 1, 1)
		assertEquals(0, subs(f, asList(f, 1, 1, 1), 'a').signum());
		// T_3 doesn't work (46455 polynomials after 50th iteration)
		// result = SDS.sds(f, T_n);
		// A_3 works for 1e-9 but doesn't seem to work for 1e-10
		pos = new RationalPoly("abc", "a**4 + b**4 + c**4");
		result = SDS.sds(addMul(f, f.valueOf("1/1000000000"), pos));
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(14, result.getDepth());
		// Z_3 needs 30 for 1e-10, 33 for 1e-11
		result = SDS.sds(addMul(f, f.valueOf("1/10000000000"), pos), Z_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(30, result.getDepth());
		// 1e-22
		Rational e_22 = f.valueOf("1/10000000000000000000000");
		// T_3 needs 32
		result = SDS.sds(addMul(f, e_22, pos), T_n);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(32, result.getDepth());
		// H_3 needs 38, Y_3 == H_3
		result = SDS.sds(addMul(f, e_22, pos), H_3);
		assertTrue(result.isNonNegative());
		assertTrue(result.getZeroAt().isEmpty());
		assertEquals(38, result.getDepth());
		// both A_3 and T_3 find negative without iteration
		f1 = addMul(f, e_22.negate(), pos);
		result = SDS.sds(f1);
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// H_3 finds negative without iterations, Y_3 == H_3
		result = SDS.sds(f1, H_3);
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// Z_3 finds negative without iterations
		result = SDS.sds(f1, Z_n);
		assertTrue(!result.isNonNegative());
		assertEquals("[1, 1, 1]", result.getNegativeAt().toString());
		assertEquals(0, result.getDepth());
		// ex 4.5
		// result from han13-ex5.py
		g = new BigPoly("abcde", "a**2*b**2*c**2*d**2 + 3*a**2*b**2*c**2*e**2 + 3*a**2*b**2*d**2*e**2 + 9*a**2*b**2*e**4 + 3*a**2*c**2*d**2*e**2 + 9*a**2*c**2*e**4 + 9*a**2*d**2*e**4 + 11*a**2*e**6 - 32*a*b*e**6 - 32*a*c*e**6 - 32*a*d*e**6 + 3*b**2*c**2*d**2*e**2 + 9*b**2*c**2*e**4 + 9*b**2*d**2*e**4 + 11*b**2*e**6 - 32*b*c*e**6 - 32*b*d*e**6 + 9*c**2*d**2*e**4 + 11*c**2*e**6 - 32*c*d*e**6 + 11*d**2*e**6 + 81*e**8");
		// both A_5 and T_5 need 5; Z_5 and Y_5 dont work
		bigResult = SDS.sds(g);
		assertTrue(bigResult.isNonNegative());
		assertEquals(5, bigResult.getDepth());
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