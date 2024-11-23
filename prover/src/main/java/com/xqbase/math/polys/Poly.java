package com.xqbase.math.polys;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.function.Function;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public abstract class Poly<T extends MutableNumber<T>, P extends Poly<T, P>> extends HashMap<Monom, T> {
	private static final long serialVersionUID = 1L;

	public abstract T valueOf(long n);
	public abstract T valueOf(String s) throws NumberFormatException;
	public abstract T newZero();
	public abstract T[] newVector(int n);
	public abstract T[][] newMatrix(int n1, int n2);

	private String[] vars;

	public P newPoly() {
		try {
			return unchecked(getClass().
					getConstructor(String[].class).newInstance((Object) vars));
		} catch (ReflectiveOperationException e) {
			throw new RuntimeException(e);
		}
	}

	public P newPoly(String[] newVars) {
		try {
			return unchecked(getClass().
					getConstructor(String[].class).newInstance((Object) newVars));
		} catch (ReflectiveOperationException e) {
			throw new RuntimeException(e);
		}
	}

	public P newPoly(String expr, String... newVars) {
		try {
			return unchecked(getClass().
					getConstructor(String.class, String[].class).newInstance(expr, newVars));
		} catch (ReflectiveOperationException e) {
			throw new RuntimeException(e);
		}
	}

	private static Logger log = LoggerFactory.getLogger(Poly.class);

	private void append(boolean minus, String expr) {
		if (expr.isEmpty()) {
			return;
		}
		T c = valueOf(1);
		int times = expr.indexOf('*');
		String expr_ = expr;
		try {
			if (times < 0) {
				c = valueOf(expr_);
				expr_ = "";
			} else {
				c = valueOf(expr.substring(0, times));
				expr_ = expr.substring(times + 1);
			}
		} catch (NumberFormatException e) {
			// no coeff: expr unchanged
		}
		append(new Monom(expr_, vars), minus ? c.negate() : c);
	}

	public void append(Monom mono, T n) {
		T coeff = computeIfAbsent(mono, k -> newZero());
		coeff.add(n);
		if (coeff.signum() == 0) {
			remove(mono);
		}
	}

	protected Poly(String[] vars) {
		this.vars = vars;
	}

	protected Poly(String expr, String... vars) {
		this(vars);
		for (String ss : expr.replaceAll("\\s+", "").split("\\+")) {
			boolean minus = false;
			for (String s : ss.split("\\-")) {
				append(minus, s);
				minus = true;
			}
		}
	}

	public String[] getVars() {
		return vars;
	}

	@Override
	public String toString() {
		if (isEmpty()) {
			return "0";
		}
		TreeMap<Monom, T> sorted = new TreeMap<>(this);
		StringBuilder sb = new StringBuilder();
		sorted.forEach((m, c) -> {
			if (sb.length() == 0) {
				if (c.equals(valueOf(-1))) { // c == -1
					sb.append('-');
				} else if (!c.equals(valueOf(1))) { // c != 1
					sb.append(c + "*");
				}
			} else if (c.signum() < 0) { // c < 0
				sb.append(" - ");
				if (!c.equals(valueOf(-1))) { // c != -1
					sb.append(c.negate() + "*");
				}
			} else {
				sb.append(" + ");
				if (!c.equals(valueOf(1))) { // c != 1
					sb.append(c + "*");
				}
			}
			String s = m.toString(vars);
			int len = sb.length();
			if (s.isEmpty()) {
				if (len == 0) {
					sb.append("1");
				} else {
					switch (sb.charAt(len - 1)) {
					case ' ':
					case '-':
						sb.append('1');
						break;
					case '*':
						sb.setLength(len - 1);
						break;
					default:
					}
				}
			} else {
				sb.append(s);
			}
		});
		return sb.toString();
	}

	@SuppressWarnings("unchecked")
	private P unchecked(Poly<?, ?> p) {
		return (P) p;
	}

	private static final Monom[] EMPTY_MONOMS = {};
	private static final String[] EMPTY_STRINGS = {};

	/**
	 * align with other polys' vars
	 *
	 * @return newVars' indices in aligned poly, <code>null</code>
	 *         if nothing to align (all newVars equal to this vars)
	 */
	public int[][] align(String[]... newVarss) {
		boolean needAlign = false;
		outerLoop:
		for (String[] newVars : newVarss) {
			if (newVars.length != vars.length) {
				needAlign = true;
				break;
			}
			for (int i = 0; i < vars.length; i ++) {
				if (!newVars[i].equals(vars[i])) {
					needAlign = true;
					break outerLoop;
				}
			}
		}
		if (!needAlign) {
			return null;
		}

		int[][] newVarsIndices = new int[newVarss.length][];
		List<String> alignedVars = new ArrayList<>();
		for (String var : vars) {
			alignedVars.add(var);
		}
		for (int i = 0; i < newVarsIndices.length; i ++) {
			String[] newVars = newVarss[i];
			int[] newVarsIndex = new int[newVars.length];
			for (int j = 0; j < newVarsIndex.length; j ++) {
				String newVar = newVars[j];
				int index = alignedVars.indexOf(newVar);
				if (index < 0) {
					index = alignedVars.size();
					alignedVars.add(newVar);
				}
				newVarsIndex[j] = index;
			}
			newVarsIndices[i] = newVarsIndex;
		}
		// no new var added, so this poly is unchanged
		int originalLen = vars.length;
		int alignedLen = alignedVars.size();
		if (alignedLen == originalLen) {
			return newVarsIndices;
		}

		vars = alignedVars.toArray(EMPTY_STRINGS);
		// iterate a copy of keySet and modify original map
		for (Monom originalMonom : keySet().toArray(EMPTY_MONOMS)) {
			short[] alignedExps = new short[alignedLen];
			System.arraycopy(originalMonom.getExps(), 0, alignedExps, 0, originalLen);
			Arrays.fill(alignedExps, originalLen, alignedLen, (short) 0);
			put(new Monom(alignedExps), remove(originalMonom));
		}
		return newVarsIndices;
	}

	/** @return this + p */
	public P add(P p) {
		return add(1, p);
	}

	/** @return this - p */
	public P sub(P p) {
		return add(-1, p);
	}

	/** @return this + n*p */
	public P add(long n, P p) {
		return add(valueOf(n), p);
	}

	/** @return this + n*p */
	public P add(T n, P p) {
		int[][] pVarsIndices = align(p.getVars());
		p.forEach((m, c) -> {
			Monom alignedMono = m;
			if (pVarsIndices != null) {
				short[] exps = m.getExps();
				short[] alignedExps = new short[vars.length];
				Arrays.fill(alignedExps, (short) 0);
				for (int i = 0; i < exps.length; i ++) {
					alignedExps[pVarsIndices[0][i]] = exps[i];
				}
				alignedMono = new Monom(alignedExps);
			}
			T c1 = computeIfAbsent(alignedMono, k -> newZero());
			c1.addMul(n, c);
			if (c1.signum() == 0) {
				remove(alignedMono);
			}
		});
		return unchecked(this);
	}

	/** @return this + p1*p2 */
	public P addMul(P p1, P p2) {
		return addMul(1, p1, p2);
	}

	/** @return this - p1*p2 */
	public P subMul(P p1, P p2) {
		return addMul(-1, p1, p2);
	}

	/** @return this + n*p1*p2 */
	public P addMul(long n, P p1, P p2) {
		return addMul(valueOf(n), p1, p2);
	}

	/** @return this + n*p1*p2 */
	public P addMul(T n, P p1, P p2) {
		int[][] pVarsIndices = align(p1.getVars(), p2.getVars());
		p1.forEach((m1, c1) -> {
			p2.forEach((m2, c2) -> {
				short[] exps1 = m1.getExps();
				short[] exps2 = m2.getExps();
				short[] exps = new short[vars.length];
				if (pVarsIndices == null) {
					for (int i = 0; i < exps.length; i ++) {
						exps[i] = (short) (exps1[i] + exps2[i]);
					}
				} else {
					Arrays.fill(exps, (short) 0);
					for (int i = 0; i < exps1.length; i ++) {
						exps[pVarsIndices[0][i]] += exps1[i];
					}
					for (int i = 0; i < exps2.length; i ++) {
						exps[pVarsIndices[1][i]] += exps2[i];
					}
				}
				Monom m = new Monom(exps);
				T coeff = computeIfAbsent(m, k -> newZero());
				coeff.addMul(n, c1, c2);
				if (coeff.signum() == 0) {
					remove(m);
				}
			});
		});
		return unchecked(this);
	}

	/** like sympy.polys.polytools.poly(expr, *gens) */
	public TreeMap<Monom, P> collect(int... gens) {
		TreeMap<Monom, P> coeffs = new TreeMap<>();
		forEach((m, c) -> {
			short[] exps = m.getExps();
			short[] expsGen = new short[exps.length];
			short[] expsCoeff = exps.clone();
			for (int i = 0; i < gens.length; i ++) {
				int j = gens[i];
				expsGen[j] = exps[j];
				expsCoeff[j] = 0;
			}
			coeffs.computeIfAbsent(new Monom(expsGen), k -> newPoly()).
					append(new Monom(expsCoeff), c);
		});
		return coeffs;
	}

	private int indexOfVar(String var) {
		for (int i = 0; i < vars.length; i ++) {
			if (vars[i].equals(var)) {
				return i;
			}
		}
		return -1;
	}

	private int[] toInts(String... ss) {
		int[] ints = new int[ss.length];
		for (int i = 0; i < ss.length; i ++) {
			ints[i] = indexOfVar(ss[i]);
		}
		return ints;
	}

	/** like sympy.polys.polytools.poly(expr, *gens) */
	public TreeMap<Monom, P> collect(String... gens) {
		return collect(toInts(gens));
	}

	/** exclude variables by setting them to 1 */
	public P exclude(int... ex) {
		boolean[] excluded = new boolean[vars.length];
		Arrays.fill(excluded, false);
		for (int i = 0; i < ex.length; i ++) {
			excluded[ex[i]] = true;
		}
		int newLen = vars.length - ex.length;
		int[] iExp = new int[newLen];
		int j = 0;
		String[] newVars = new String[newLen];
		for (int i = 0; i < vars.length; i ++) {
			if (excluded[i]) {
				continue;
			}
			iExp[j] = i;
			newVars[j] = vars[i];
			j ++;
		}
		P p = newPoly(newVars);
		forEach((m, c) -> {
			short[] exps = m.getExps();
			short[] newExps = new short[newLen];
			for (int i = 0; i < newLen; i ++) {
				newExps[i] = exps[iExp[i]];
			}
			p.append(new Monom(newExps), c);
		});
		return p;
	}

	/** exclude variables by setting them to 1 */
	public P exclude(String... ex) {
		return exclude(toInts(ex));
	}

	public int degree(int var) {
		int degree = 0;
		for (Monom m : keySet()) {
			int exp = m.getExps()[var];
			if (exp > degree) {
				degree = exp;
			}
		}
		return degree;
	}

	public int degree(String var) {
		return degree(indexOfVar(var));
	}

	public int[] degrees() {
		int[] degrees = new int[vars.length];
		Arrays.fill(degrees, 0);
		for (Monom m : keySet()) {
			short[] exps = m.getExps();
			for (int i = 0; i < vars.length; i ++) {
				if (exps[i] > degrees[i]) {
					degrees[i] = exps[i];
				}
			}
		}
		return degrees;
	}

	/** x -> 1/x and remove denominator */
	public P reciprocal(int var) {
		return reciprocal(var, degree(var));
	}

	/** x -> 1/x and remove denominator */
	public P reciprocal(String var) {
		return reciprocal(indexOfVar(var));
	}

	/** x -> 1/x and remove denominator */
	public P reciprocal(int var, int degree) {
		P p = newPoly();
		forEach((m, c) -> {
			short[] exps = m.getExps();
			short[] exps1 = exps.clone();
			exps1[var] = (short) (degree - exps[var]);
			p.put(new Monom(exps1), c);
		});
		return p;
	}

	/** x -> 1/x and remove denominator */
	public P reciprocal(String var, int degree) {
		return reciprocal(indexOfVar(var), degree);
	}

	private P subs(int fromVar, Function<P, P> toFunc) {
		if (isEmpty()) {
			return unchecked(this);
		}
		TreeMap<Monom, P> ai = collect(fromVar);
		// a_0x^n+a_1x^{n-1}+a_2x^{n-2}+...+a_{n-1}x+a_n = (...((a_0x+a_1)x+a2)+...+a_{n-1})x+a_n
		Map.Entry<Monom, P> lt = ai.firstEntry();
		Monom lm = lt.getKey();
		P p = lt.getValue();
		short[] exps = new short[vars.length];
		for (int i = lm.getExps()[fromVar] - 1; i >= 0; i --) {
			exps[fromVar] = (short) i;
			P p1 = toFunc.apply(p);
			P a = ai.get(new Monom(exps));
			if (a != null) {
				p1.add(a);
			}
			p = p1;
		}
		return p;
	}

	public P subs(int fromVar, T to) {
		return subs(fromVar, p -> {
			P p1 = newPoly();
			p1.add(to, p);
			return p1;
		});
	}

	public P subs(String fromVar, T to) {
		return subs(indexOfVar(fromVar), to);
	}

	public P subs(int fromVar, P to) {
		return subs(fromVar, p -> {
			P p1 = newPoly();
			p1.addMul(p, to);
			return p1;
		});
	}

	public P subs(String fromVar, P to) {
		return subs(indexOfVar(fromVar), to);
	}

	public P homogenize(String newVar) {
		boolean homogeneous = true;
		int deg = 0;
		HashMap<Monom, Integer> expsMap = new HashMap<>();
		for (Monom m : keySet()) {
			int exps = 0;
			for (int exp : m.getExps()) {
				exps += exp;
			}
			if (deg == 0) {
				deg = exps;
			} else if (exps != deg) {
				homogeneous = false;
				if (exps > deg) {
					deg = exps;
				}
			}
			expsMap.put(m, Integer.valueOf(exps));
		}
		if (homogeneous) {
			return unchecked(this);
		}
		String[] newVars = new String[vars.length + 1];
		System.arraycopy(vars, 0, newVars, 0, vars.length);
		newVars[vars.length] = newVar;
		P p = newPoly(newVars);
		int deg_ = deg;
		expsMap.forEach((m, n) -> {
			short[] newExps = new short[newVars.length];
			System.arraycopy(m.getExps(), 0, newExps, 0, vars.length);
			newExps[vars.length] = (short) (deg_ - n.intValue());
			p.put(new Monom(newExps), get(m));
		});
		return p;
	}

	public P diff(int var) {
		P p = newPoly();
		forEach((m, c) -> {
			short[] exps = m.getExps().clone();
			T c1 = newZero();
			int exp = exps[var];
			if (exp == 0) {
				return;
			}
			c1.addMul(valueOf(exp), c);
			exps[var] --;
			Monom m1 = new Monom(exps);
			p.put(m1, c1);
		});
		return p;
	}

	public P diff(String var) {
		return diff(indexOfVar(var));
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> P
			det(P p11, P p12, P p21, P p22) {
		return p11.newPoly().addMul(p11, p22).subMul(p21, p12);
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> P
			det(P p11, P p12, P p13, P p21, P p22, P p23, P p31, P p32, P p33) {
		P p = p11.newPoly().addMul(p11, det(p22, p23, p32, p33));
		log.trace("Det(1x3) Terms: " + p.size());
		p.subMul(p21, det(p12, p13, p32, p33));
		log.trace("Det(2x3) Terms: " + p.size());
		p.addMul(p31, det(p12, p13, p22, p23));
		log.trace("Det(3x3) Terms: " + p.size());
		return p;
	}

	public static <T extends MutableNumber<T>, P extends Poly<T, P>> P
			det(P p11, P p12, P p13, P p14, P p21, P p22, P p23, P p24,
			P p31, P p32, P p33, P p34, P p41, P p42, P p43, P p44) {
		P p = p11.newPoly().addMul(p11, det(p22, p23, p24, p32, p33, p34, p42, p43, p44));
		log.debug("Det(1x4) Terms: " + p.size());
		p.subMul(p21, det(p12, p13, p14, p32, p33, p34, p42, p43, p44));
		log.debug("Det(2x4) Terms: " + p.size());
		p.addMul(p31, det(p12, p13, p14, p22, p23, p24, p42, p43, p44));
		log.debug("Det(3x4) Terms: " + p.size());
		p.subMul(p41, det(p12, p13, p14, p22, p23, p24, p32, p33, p34));
		log.debug("Det(4x4) Terms: " + p.size());
		return p;
	}
}