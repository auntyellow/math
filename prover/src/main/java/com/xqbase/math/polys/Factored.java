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

	public Factored(Rational coeff) {
		this.coeff = coeff;
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

	public Factored negative() {
		Factored result = new Factored(coeff.negate());
		result.factors.putAll(factors);
		return result;
	}

	private static LongPoly mulPow(LongPoly p0, LongPoly p, long e) {
		LongPoly result = p0;
		for (long i = 0; i < e; i ++) {
			result = p.newPoly().addMul(result, p);
		}
		return result;
	}

	private static long mul(BigInteger n1, BigInteger n2) {
		return Math.multiplyExact(n1.longValueExact(), n2.longValueExact());
	}

	public Factored add(Factored f) {
		// just for newPoly()
		LongPoly anyPoly;
		if (factors.isEmpty()) {
			if (f.factors.isEmpty()) {
				Factored result = new Factored();
				result.coeff.addMul(coeff, f.coeff);
				return result;
			}
			anyPoly = f.factors.keySet().iterator().next();
		} else {
			anyPoly = factors.keySet().iterator().next();
		}
		LongPoly one = anyPoly.newPoly();
		one.put(new Monom(anyPoly.getVars().length), MutableLong.valueOf(1));
		// (g/h)*(p/q)
		Factored gcd = gcd(f);
		// (j/k)*(r/s)
		Factored f0 = div(gcd);
		// (m/n)*(t/u)
		Factored f1 = f.div(gcd);
		// result = (g/h/k/n)*(p*(j*n*r*u + k*m*s*t)/q/s/u)
		Factored result = new Factored();
		// g/h
		result.coeff = gcd.coeff;
		// .../k
		result.coeff = result.coeff.div(new Rational(f0.coeff.getQ()));
		// .../n
		result.coeff = result.coeff.div(new Rational(f1.coeff.getQ()));
		// ...*p/q
		result.factors.putAll(gcd.factors);
		// {r, s, t, u}
		LongPoly[] rstu = {one, one, one, one};
		f0.factors.forEach((p, e) -> {
			if (e.signum() < 0) {
				// .../s
				result.mulPow(p, e.longValue());
				rstu[1] = mulPow(rstu[1], p, -e.longValue());
			} else {
				rstu[0] = mulPow(rstu[0], p, e.longValue());
			}
		});
		f1.factors.forEach((p, e) -> {
			if (e.signum() < 0) {
				// .../u
				result.mulPow(p, e.longValue());
				rstu[3] = mulPow(rstu[3], p, -e.longValue());
			} else {
				rstu[2] = mulPow(rstu[2], p, e.longValue());
			}
		});
		LongPoly numerator = anyPoly.newPoly();
		// j*n*r*u
		numerator.addMul(mul(f0.coeff.getP(), f1.coeff.getQ()), rstu[0], rstu[3]);
		// k*m*s*t
		numerator.addMul(mul(f0.coeff.getQ(), f1.coeff.getP()), rstu[1], rstu[2]);
		// ...*(j*n*r*u + k*m*s*t)
		result.mulPow(numerator, 1);
		return result;
	}
}