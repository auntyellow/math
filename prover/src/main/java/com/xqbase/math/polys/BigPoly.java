package com.xqbase.math.polys;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.function.Function;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BigPoly extends HashMap<BigMono, BigInteger[]> {
	private static final long serialVersionUID = 1L;
	private static final BigInteger _0 = BigInteger.ZERO;
	private static final BigInteger _1 = BigInteger.ONE;
	private static final BigInteger __1 = _1.negate();
	private static final Function<BigMono, BigInteger[]> ZERO_COEFF = k -> new BigInteger[] {_0};

	private static Logger log = LoggerFactory.getLogger(BigPoly.class);

	private void append(String vars, String expr, boolean minus) {
		if (expr.isEmpty()) {
			return;
		}
		BigInteger c = _1;
		String s = expr;
		if (s.charAt(0) < 'a') {
			int i = s.indexOf('*');
			if (i < 0) {
				c = new BigInteger(s);
				s = "";
			} else {
				c = new BigInteger(s.substring(0, i));
				s = s.substring(i + 1);
			}
		}
		append(minus ? c.negate() : c, new BigMono(vars, s));
	}

	public void append(BigInteger n, BigMono mono) {
		BigInteger[] coeff = computeIfAbsent(mono, ZERO_COEFF);
		coeff[0] = coeff[0].add(n);
		if (coeff[0].signum() == 0) {
			remove(mono);
		}
	}

	public BigPoly() {/**/}

	public BigPoly(String vars, String expr) {
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
		TreeMap<BigMono, BigInteger[]> sorted = new TreeMap<>(this);
		StringBuilder sb = new StringBuilder();
		sorted.forEach((k, v) -> {
			BigInteger c = v[0];
			if (sb.length() == 0) {
				if (c.equals(__1)) { // c == -1
					sb.append('-');
				} else if (!c.equals(_1)) { // c != -1
					sb.append(c + "*");
				}
			} else if (c.signum() < 0) { // c < 0
				sb.append(" - ");
				if (c.compareTo(__1) < 0) { // c < -1
					sb.append(c.negate() + "*");
				}
			} else {
				sb.append(" + ");
				if (!c.equals(_1)) { // c != -1
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

	public BigPoly add(BigInteger n, BigPoly p) {
		p.forEach((k, v) -> {
			BigInteger[] coeff = computeIfAbsent(k, ZERO_COEFF);
			coeff[0] = coeff[0].add(n.multiply(v[0]));
			if (coeff[0].signum() == 0) {
				remove(k);
			}
		});
		return this;
	}

	public BigPoly addMul(BigInteger n, BigPoly p1, BigPoly p2) {
		p1.forEach((k1, v1) -> {
			p2.forEach((k2, v2) -> {
				BigMono k = k1.mul(k2);
				BigInteger[] coeff = computeIfAbsent(k, ZERO_COEFF);
				coeff[0] = coeff[0].add(n.multiply(v1[0]).multiply(v2[0]));
				if (coeff[0].signum() == 0) {
					remove(k);
				}
			});
		});
		return this;
	}

	public TreeMap<BigMono, BigPoly> coeffsOf(String gen) {
		TreeMap<BigMono, BigPoly> coeffs = new TreeMap<>();
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
			coeffs.computeIfAbsent(new BigMono(vars, expsGen), k -> new BigPoly()).
					append(coeff[0], new BigMono(vars, expsCoeff));
		});
		return coeffs;
	}

	public static BigPoly det(BigPoly p11, BigPoly p12, BigPoly p21, BigPoly p22) {
		return new BigPoly().addMul(_1, p11, p22).addMul(__1, p21, p12);
	}

	public static BigPoly det(
			BigPoly p11, BigPoly p12, BigPoly p13,
			BigPoly p21, BigPoly p22, BigPoly p23,
			BigPoly p31, BigPoly p32, BigPoly p33) {
		BigPoly p = new BigPoly().addMul(_1, p11, det(p22, p23, p32, p33));
		log.trace("Det(1x3) Terms: " + p.size());
		p.addMul(__1, p21, det(p12, p13, p32, p33));
		log.trace("Det(2x3) Terms: " + p.size());
		p.addMul(_1, p31, det(p12, p13, p22, p23));
		log.trace("Det(3x3) Terms: " + p.size());
		return p;
	}

	public static BigPoly det(
			BigPoly p11, BigPoly p12, BigPoly p13, BigPoly p14,
			BigPoly p21, BigPoly p22, BigPoly p23, BigPoly p24,
			BigPoly p31, BigPoly p32, BigPoly p33, BigPoly p34,
			BigPoly p41, BigPoly p42, BigPoly p43, BigPoly p44) {
		BigPoly p = new BigPoly().addMul(_1, p11, det(p22, p23, p24, p32, p33, p34, p42, p43, p44));
		log.debug("Det(1x4) Terms: " + p.size());
		p.addMul(__1, p21, det(p12, p13, p14, p32, p33, p34, p42, p43, p44));
		log.debug("Det(2x4) Terms: " + p.size());
		p.addMul(_1, p31, det(p12, p13, p14, p22, p23, p24, p42, p43, p44));
		log.debug("Det(3x4) Terms: " + p.size());
		p.addMul(__1, p41, det(p12, p13, p14, p22, p23, p24, p32, p33, p34));
		log.debug("Det(4x4) Terms: " + p.size());
		return p;
	}
}