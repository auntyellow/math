package com.xqbase.math.polys;

import java.util.HashMap;
import java.util.TreeMap;
import java.util.function.Function;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Poly extends HashMap<Mono, long[]> {
	private static final long serialVersionUID = 1L;
	private static final Function<Mono, long[]> ZERO_COEFF = k -> new long[] {0};

	private static Logger log = LoggerFactory.getLogger(Poly.class);

	private void append(String vars, String expr, boolean minus) {
		if (expr.isEmpty()) {
			return;
		}
		long c = 1;
		String s = expr;
		if (s.charAt(0) < 'a') {
			int i = s.indexOf('*');
			if (i < 0) {
				c = Long.parseLong(s);
				s = "";
			} else {
				c = Long.parseLong(s.substring(0, i));
				s = s.substring(i + 1);
			}
		}
		append(minus ? -c : c, new Mono(vars, s));
	}

	public void append(long n, Mono mono) {
		long[] coeff = computeIfAbsent(mono, ZERO_COEFF);
		coeff[0] += n;
		if (coeff[0] == 0) {
			remove(mono);
		}
	}

	public Poly() {/**/}

	public Poly(String vars, String expr) {
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
		TreeMap<Mono, long[]> sorted = new TreeMap<>(this);
		StringBuilder sb = new StringBuilder();
		sorted.forEach((k, v) -> {
			long c = v[0];
			if (sb.length() == 0) {
				if (c == -1) {
					sb.append('-');
				} else if (c != 1) {
					sb.append(c + "*");
				}
			} else if (c < 0) {
				sb.append(" - ");
				if (c < -1) {
					sb.append(-c + "*");
				}
			} else {
				sb.append(" + ");
				if (c != 1) {
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

	public Poly add(long n, Poly p) {
		p.forEach((k, v) -> {
			long[] coeff = computeIfAbsent(k, ZERO_COEFF);
			coeff[0] += n * v[0];
			if (coeff[0] == 0) {
				remove(k);
			}
		});
		return this;
	}

	public Poly addMul(long n, Poly p1, Poly p2) {
		p1.forEach((k1, v1) -> {
			p2.forEach((k2, v2) -> {
				Mono k = k1.mul(k2);
				long[] coeff = computeIfAbsent(k, ZERO_COEFF);
				coeff[0] += n * v1[0] * v2[0];
				if (coeff[0] == 0) {
					remove(k);
				}
			});
		});
		return this;
	}

	public TreeMap<Mono, Poly> coeffsOf(String gen) {
		TreeMap<Mono, Poly> coeffs = new TreeMap<>();
		forEach((mono, coeff) -> {
			String vars = mono.getVars();
			byte[] exps = mono.getExps();
			byte[] expsGen = new byte[exps.length];
			byte[] expsCoeff = exps.clone();
			for (int i = 0; i < gen.length(); i ++) {
				int j = vars.indexOf(gen.charAt(i));
				expsGen[j] = exps[j];
				expsCoeff[j] = 0;
			}
			coeffs.computeIfAbsent(new Mono(vars, expsGen), k -> new Poly()).
					append(coeff[0], new Mono(vars, expsCoeff));
		});
		return coeffs;
	}

	public static Poly det(Poly p11, Poly p12, Poly p21, Poly p22) {
		return new Poly().addMul(1, p11, p22).addMul(-1, p21, p12);
	}

	public static Poly det(
			Poly p11, Poly p12, Poly p13,
			Poly p21, Poly p22, Poly p23,
			Poly p31, Poly p32, Poly p33) {
		Poly p = new Poly().addMul(1, p11, det(p22, p23, p32, p33));
		log.trace("Det(1x3) Terms: " + p.size());
		p.addMul(-1, p21, det(p12, p13, p32, p33));
		log.trace("Det(2x3) Terms: " + p.size());
		p.addMul(1, p31, det(p12, p13, p22, p23));
		log.trace("Det(3x3) Terms: " + p.size());
		return p;
	}

	public static Poly det(
			Poly p11, Poly p12, Poly p13, Poly p14,
			Poly p21, Poly p22, Poly p23, Poly p24,
			Poly p31, Poly p32, Poly p33, Poly p34,
			Poly p41, Poly p42, Poly p43, Poly p44) {
		Poly p = new Poly().addMul(1, p11, det(p22, p23, p24, p32, p33, p34, p42, p43, p44));
		log.debug("Det(1x4) Terms: " + p.size());
		p.addMul(-1, p21, det(p12, p13, p14, p32, p33, p34, p42, p43, p44));
		log.debug("Det(2x4) Terms: " + p.size());
		p.addMul(1, p31, det(p12, p13, p14, p22, p23, p24, p42, p43, p44));
		log.debug("Det(3x4) Terms: " + p.size());
		p.addMul(-1, p41, det(p12, p13, p14, p22, p23, p24, p32, p33, p34));
		log.debug("Det(4x4) Terms: " + p.size());
		return p;
	}
}