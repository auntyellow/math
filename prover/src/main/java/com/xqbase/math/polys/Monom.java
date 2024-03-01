package com.xqbase.math.polys;

import java.util.Arrays;

public class Monom implements Comparable<Monom> {
	private short[] exps;

	public Monom(short[] exps) {
		this.exps = exps;
	}

	public Monom(String vars, String expr) {
		exps = new short[vars.length()];
		if (!expr.isEmpty()) {
			for (String s : expr.replace("**", "^").split("\\*")) {
				exps[vars.indexOf(s.charAt(0))] = (s.length() == 1 ? 1 : Byte.parseByte(s.substring(2)));
			}
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

	public String toString(String vars) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < exps.length; i ++) {
			int exp = exps[i];
			if (exp <= 0) {
				continue;
			}
			sb.append("*" + vars.charAt(i));
			if (exp > 1) {
				sb.append("**" + exp);
			}
		}
		return sb.length() == 0 ? "" : sb.substring(1);
	}
}