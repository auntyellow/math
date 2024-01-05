package com.xqbase.math.polys;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.function.Function;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public abstract class Poly<T extends MutableNumber<T>> extends HashMap<Mono, T> {
	private static final long serialVersionUID = 1L;

	public abstract T valueOf(long n);
	public abstract T valueOf(String s);
	public abstract T newZero();
	public abstract T[] newVector(int n);
	public abstract T[][] newMatrix(int n1, int n2);

	@SuppressWarnings("unchecked")
	public Poly<T> newPoly() {
		try {
			return getClass().getConstructor().newInstance();
		} catch (ReflectiveOperationException e) {
			throw new RuntimeException(e);
		}
	}

	private static Logger log = LoggerFactory.getLogger(Poly.class);

	private void append(String vars, String expr, boolean minus) {
		if (expr.isEmpty()) {
			return;
		}
		T c = valueOf(1);
		String s = expr;
		if (vars.indexOf(s.charAt(0)) < 0) {
			int i = s.indexOf('*');
			if (i < 0) {
				c = valueOf(s);
				s = "";
			} else {
				c = valueOf(s.substring(0, i));
				s = s.substring(i + 1);
			}
		}
		append(minus ? c.negate() : c, new Mono(vars, s));
	}

	public void append(T n, Mono mono) {
		T coeff = computeIfAbsent(mono, k -> newZero());
		coeff.add(n);
		if (coeff.signum() == 0) {
			remove(mono);
		}
	}

	protected Poly() {/**/}

	protected Poly(String vars, String expr) {
		for (String ss : expr.replace(" ", "").replace("**", "^").split("\\+")) {
			boolean minus = false;
			for (String s : ss.split("\\-")) {
				append(vars, s, minus);
				minus = true;
			}
		}
	}

	@Override
	public String toString() {
		if (isEmpty()) {
			return "0";
		}
		TreeMap<Mono, T> sorted = new TreeMap<>(this);
		StringBuilder sb = new StringBuilder();
		sorted.forEach((k, v) -> {
			T c = v;
			if (sb.length() == 0) {
				if (c.equals(valueOf(-1))) { // c == -1
					sb.append('-');
				} else if (!c.equals(valueOf(1))) { // c != 1
					sb.append(c + "*");
				}
			} else if (c.signum() < 0) { // c < 0
				sb.append(" - ");
				if (c.compareTo(valueOf(-1)) < 0) { // c < -1
					sb.append(c.negate() + "*");
				}
			} else {
				sb.append(" + ");
				if (!c.equals(valueOf(1))) { // c != -1
					sb.append(c + "*");
				}
			}
			String s = k.toString();
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

	/** @return this + p */
	public Poly<T> add(Poly<T> p) {
		return add(1, p);
	}

	/** @return this - p */
	public Poly<T> sub(Poly<T> p) {
		return add(-1, p);
	}

	/** @return this + n*p */
	public Poly<T> add(long n, Poly<T> p) {
		return add(valueOf(n), p);
	}

	/** @return this + n*p */
	public Poly<T> add(T n, Poly<T> p) {
		p.forEach((k, v) -> {
			T coeff = computeIfAbsent(k, k_ -> newZero());
			coeff.addMul(n, v);
			if (coeff.signum() == 0) {
				remove(k);
			}
		});
		return this;
	}

	/** @return this + p1*p2 */
	public Poly<T> addMul(Poly<T> p1, Poly<T> p2) {
		return addMul(1, p1, p2);
	}

	/** @return this - p1*p2 */
	public Poly<T> subMul(Poly<T> p1, Poly<T> p2) {
		return addMul(-1, p1, p2);
	}

	/** @return this + n*p1*p2 */
	public Poly<T> addMul(long n, Poly<T> p1, Poly<T> p2) {
		return addMul(valueOf(n), p1, p2);
	}

	/** @return this + n*p1*p2 */
	public Poly<T> addMul(T n, Poly<T> p1, Poly<T> p2) {
		p1.forEach((k1, v1) -> {
			p2.forEach((k2, v2) -> {
				Mono k = k1.mul(k2);
				T coeff = computeIfAbsent(k, k_ -> newZero());
				coeff.addMul(n, v1, v2);
				if (coeff.signum() == 0) {
					remove(k);
				}
			});
		});
		return this;
	}

	public TreeMap<Mono, Poly<T>> coeffsOf(String gen) {
		TreeMap<Mono, Poly<T>> coeffs = new TreeMap<>();
		forEach((mono, coeff) -> {
			String vars = mono.getVars();
			short[] exps = mono.getExps();
			short[] expsGen = new short[exps.length];
			short[] expsCoeff = exps.clone();
			for (int i = 0; i < gen.length(); i ++) {
				int j = vars.indexOf(gen.charAt(i));
				expsGen[j] = exps[j];
				expsCoeff[j] = 0;
			}
			coeffs.computeIfAbsent(new Mono(vars, expsGen), k -> newPoly()).
					append(coeff, new Mono(vars, expsCoeff));
		});
		return coeffs;
	}

	private Poly<T> subs(char from, Function<Poly<T>, Poly<T>> toFunc) {
		if (isEmpty()) {
			return this;
		}
		TreeMap<Mono, Poly<T>> ai = coeffsOf(String.valueOf(from));
		// a_0x^n+a_1x^{n-1}+a_2x^{n-2}+...+a_{n-1}x+a_n = (...((a_0x+a_1)x+a2)+...+a_{n-1})x+a_n
		Map.Entry<Mono, Poly<T>> lt = ai.firstEntry();
		Mono lm = lt.getKey();
		String vars = lm.getVars();
		Poly<T> p = lt.getValue();
		short[] exps = new short[vars.length()];
		int fromIndex = vars.indexOf(from);
		for (int i = lm.getExps()[fromIndex] - 1; i >= 0; i --) {
			exps[fromIndex] = (short) i;
			Poly<T> p1 = toFunc.apply(p);
			Poly<T> a = ai.get(new Mono(vars, exps));
			if (a != null) {
				p1.add(a);
			}
			p = p1;
		}
		return p;
	}

	public Poly<T> subs(char from, T to) {
		return subs(from, p -> {
			Poly<T> p1 = newPoly();
			p1.add(to, p);
			return p1;
		});
	}

	public Poly<T> subs(char from, Poly<T> to) {
		return subs(from, p -> {
			Poly<T> p1 = newPoly();
			p1.addMul(p, to);
			return p1;
		});
	}

	public Poly<T> homogenize(char newVar) {
		boolean homogeneous = true;
		int deg = 0;
		String vars = "";
		HashMap<Mono, Integer> expsMap = new HashMap<>();
		for (Mono mono : keySet()) {
			int exps = 0;
			for (int exp : mono.getExps()) {
				exps += exp;
			}
			if (deg == 0) {
				deg = exps;
				vars = mono.getVars();
			} else if (exps != deg) {
				homogeneous = false;
				if (exps > deg) {
					deg = exps;
				}
			}
			expsMap.put(mono, Integer.valueOf(exps));
		}
		if (homogeneous) {
			return this;
		}
		int numVars = vars.length();
		int numNewVars = numVars + 1;
		String newVars = vars + newVar;
		Poly<T> p = newPoly();
		for (Map.Entry<Mono, Integer> entry : expsMap.entrySet()) {
			Mono m = entry.getKey();
			short[] newExps = new short[numNewVars];
			System.arraycopy(m.getExps(), 0, newExps, 0, numVars);
			newExps[numVars] = (short) (deg - entry.getValue().intValue());
			p.put(new Mono(newVars, newExps), get(m));
		}
		return p;
	}

	@SuppressWarnings("unchecked")
	public static <T extends MutableNumber<T>, P extends Poly<T>> P
			det(P p11, P p12, P p21, P p22) {
		return (P) p11.newPoly().addMul(p11, p22).subMul(p21, p12);
	}

	@SuppressWarnings("unchecked")
	public static <T extends MutableNumber<T>, P extends Poly<T>> P
			det(P p11, P p12, P p13, P p21, P p22, P p23, P p31, P p32, P p33) {
		P p = (P) p11.newPoly().addMul(p11, det(p22, p23, p32, p33));
		log.trace("Det(1x3) Terms: " + p.size());
		p.subMul(p21, det(p12, p13, p32, p33));
		log.trace("Det(2x3) Terms: " + p.size());
		p.addMul(p31, det(p12, p13, p22, p23));
		log.trace("Det(3x3) Terms: " + p.size());
		return p;
	}

	@SuppressWarnings("unchecked")
	public static <T extends MutableNumber<T>, P extends Poly<T>> P
			det(P p11, P p12, P p13, P p14, P p21, P p22, P p23, P p24,
			P p31, P p32, P p33, P p34, P p41, P p42, P p43, P p44) {
		P p = (P) p11.newPoly().addMul(p11, det(p22, p23, p24, p32, p33, p34, p42, p43, p44));
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