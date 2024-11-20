package com.xqbase.math.polys;

import java.util.Arrays;
import java.util.List;

public class Monom implements Comparable<Monom> {
	private short[] exps;

	public Monom(short[] exps) {
		this.exps = exps;
	}

	public Monom(int len) {
		exps = new short[len];
		Arrays.fill(exps, (short) 0);
	}

	public Monom(String expr, String... vars) {
		this(vars.length);
		String expr_ = expr.trim();
		if (expr_.isEmpty()) {
			return;
		}
		List<String> varList = Arrays.asList(vars);
		for (String s : expr_.replaceAll("\\s+","").replace("**", "^").split("\\*")) {
			String var;
			short exp;
			int pow = s.indexOf('^');
			if (pow < 0) {
				var = s;
				exp = 1;
			} else {
				var = s.substring(0, pow);
				exp = Short.parseShort(s.substring(pow + 1));
			}
			int i = varList.indexOf(var);
			if (i < 0) {
				throw new IllegalArgumentException("unrecognized variable \"" + var + "\"");
			}
			exps[i] = exp;
		}
	}

	public short[] getExps() {
		return exps;
	}

	@Override
	public boolean equals(Object o) {
		return Arrays.equals(exps, ((Monom) o).exps);
	}

	@Override
	public int hashCode() {
		return Arrays.hashCode(exps);
	}

	@Override
	public int compareTo(Monom o) {
		for (int i = 0; i < exps.length; i ++) {
			int c = o.exps[i] - exps[i];
			if (c != 0) {
				return c;
			}
		}
		return 0;
	}

	@Override
	public String toString() {
		return Arrays.toString(exps);
	}

	public String toString(String... vars) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < exps.length; i ++) {
			int exp = exps[i];
			if (exp <= 0) {
				continue;
			}
			sb.append("*" + vars[i]);
			if (exp > 1) {
				sb.append("**" + exp);
			}
		}
		return sb.length() == 0 ? "" : sb.substring(1);
	}
}