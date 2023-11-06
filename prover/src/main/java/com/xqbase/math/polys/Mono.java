package com.xqbase.math.polys;

import java.util.Arrays;

public class Mono implements Comparable<Mono> {
	private transient String vars;
	private byte[] exps;

	private Mono(String vars) {
		this.vars = vars;
	}

	public Mono(String vars, byte[] exps) {
		this(vars);
		this.exps = exps;
	}

	public Mono(String vars, String expr) {
		this(vars);
		exps = new byte[vars.length()];
		if (!expr.isEmpty()) {
			for (String s : expr.replace("**", "^").split("\\*")) {
				exps[vars.indexOf(s.charAt(0))] = (s.length() == 1 ? 1 : Byte.parseByte(s.substring(2)));
			}
		}
	}

	public String getVars() {
		return vars;
	}

	public byte[] getExps() {
		return exps;
	}

	public Mono mul(Mono o) {
		Mono o2 = new Mono(vars);
		o2.exps = new byte[exps.length];
		for (int i = 0; i < exps.length; i ++) {
			o2.exps[i] = (byte) (exps[i] + o.exps[i]);
		}
		return o2;
	}

	@Override
	public boolean equals(Object o) {
		return Arrays.equals(exps, ((Mono) o).exps);
	}

	@Override
	public int hashCode() {
		return Arrays.hashCode(exps);
	}

	@Override
	public String toString() {
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

	@Override
	public int compareTo(Mono o) {
		for (int i = 0; i < exps.length; i ++) {
			int c = o.exps[i] - exps[i];
			if (c != 0) {
				return c;
			}
		}
		return 0;
	}
}