package com.xqbase.math.polys;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Factored {
	private Rational coeff;
	private Map<LongPoly, MutableLong> factors = new HashMap<>();

	private void clear() {
		coeff = new Rational(BigInteger.ZERO);
		factors.clear();
	}

	public Factored() {
		coeff = new Rational(BigInteger.ZERO);
	}

	public Factored(String coeff) {
		this.coeff = new Rational(coeff);
	}

	private void reduce() {
		Iterator<Map.Entry<LongPoly, MutableLong>> it = factors.entrySet().iterator();
		while (it.hasNext()) {
			Map.Entry<LongPoly, MutableLong> entry = it.next();
			if (entry.getKey().isEmpty()) {
				if (entry.getValue().signum() <= 0) {
					throw new ArithmeticException("/ by zero");
				}
				clear();
				return;
			}
			if (entry.getValue().signum() == 0) {
				it.remove();
			}
		}
	}

	private MutableLong getExp(LongPoly p) {
		return factors.computeIfAbsent(p, k -> new MutableLong(0));
	}

	public void mulPow(LongPoly p, long e) {
		getExp(p).add(MutableLong.valueOf(e));
	}

	public Factored mul(Factored f) {
		Factored result = new Factored();
		result.coeff.addMul(coeff, f.coeff);
		result.factors = new HashMap<>(factors);
		f.factors.forEach((p, e) -> {
			result.getExp(p).add(e);
		});
		result.reduce();
		return result;
	}

	public Factored div(Factored f) {
		Factored result = new Factored();
		result.coeff = coeff.div(f.coeff);
		f.factors.forEach((p, e) -> {
			result.getExp(p).add(e.negate());
		});
		result.reduce();
		return result;
	}

	public Factored gcd(Factored f) {
		Factored result = new Factored();
		result.coeff = coeff.gcd(f.coeff);
		Map<LongPoly, MutableLong> f0, f1;
		if (factors.size() < f.factors.size()) {
			f0 = factors;
			f1 = f.factors;
		} else {
			f0 = f.factors;
			f1 = factors;
		}
		f0.forEach((p, e) -> {
			MutableLong e1 = f1.get(p);
			if (e1 == null) {
				return;
			}
			if (e1.signum() > 0) {
				if (e.signum() > 0) {
					result.factors.put(p, new MutableLong(Long.min(e.longValue(), e1.longValue())));
				}
			} else if (e.signum() < 0) {
				result.factors.put(p, new MutableLong(Long.max(e.longValue(), e1.longValue())));
			}
		});
		return result;
	}
}