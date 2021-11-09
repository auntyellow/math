package com.xqbase.math.polys;

import java.util.Arrays;

public class Term implements Comparable<Term> {
	private byte[] orders;

	private Term() {/**/}

	public Term(int vars, String expr) {
		orders = new byte[vars];
		if (expr.isEmpty()) {
			return;
		}
		for (String s : expr.replace("**", "^").split("\\*")) {
			orders[s.charAt(0) - 'a'] = (s.length() == 1 ? 1 : Byte.parseByte(s.substring(2)));
		}
	}

	public Term mul(Term o) {
		Term o2 = new Term();
		o2.orders = new byte[orders.length];
		for (int i = 0; i < orders.length; i ++) {
			o2.orders[i] = (byte) (orders[i] + o.orders[i]);
		}
		return o2;
	}

	@Override
	public boolean equals(Object o) {
		return Arrays.equals(orders, ((Term) o).orders);
	}

	@Override
	public int hashCode() {
		return Arrays.hashCode(orders);
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < orders.length; i ++) {
			int order = orders[i];
			if (order <= 0) {
				continue;
			}
			sb.append("*" + (char) ('a' + i));
			if (order > 1) {
				sb.append("**" + order);
			}
		}
		return sb.length() == 0 ? "" : sb.substring(1);
	}

	@Override
	public int compareTo(Term o) {
		for (int i = 0; i < orders.length; i ++) {
			int c = o.orders[i] - orders[i];
			if (c != 0) {
				return c;
			}
		}
		return 0;
	}
}