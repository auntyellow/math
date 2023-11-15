package com.xqbase.math.polys;

import java.math.BigInteger;

public class BigCircle {
	private static final BigInteger _1 = BigInteger.ONE;
	private static final BigInteger __1 = _1.negate();
	private static final BigInteger __2 = __1.add(__1);

	private BigPoly a, d, e, f;

	public BigCircle(BigPoly a, BigPoly d, BigPoly e, BigPoly f) {
		this.a = a;
		this.d = d;
		this.e = e;
		this.f = f;
	}

	public BigCircle(BigPoint p1, BigPoint p2, BigPoint p3) {
		BigPoly[] r1 = row(p1);
		BigPoly[] r2 = row(p2);
		BigPoly[] r3 = row(p3);
		a = BigPoly.det(r1[1], r1[2], r1[3], r2[1], r2[2], r2[3], r3[1], r3[2], r3[3]);
		d = new BigPoly().add(__1, BigPoly.det(r1[0], r1[2], r1[3], r2[0], r2[2], r2[3], r3[0], r3[2], r3[3]));
		e = BigPoly.det(r1[0], r1[1], r1[3], r2[0], r2[1], r2[3], r3[0], r3[1], r3[3]);
		f = new BigPoly().add(__1, BigPoly.det(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], r3[0], r3[1], r3[2]));
	}

	public BigPoint getCenter() {
		return new BigPoint(d, e, new BigPoly().add(__2, a));
	}

	public boolean passesThrough(BigPoint p) {
		BigPoly[] r = row(p);
		return new BigPoly().addMul(_1, a, r[0]).addMul(_1, d, r[1]).addMul(_1, e, r[2]).addMul(_1, f, r[3]).isEmpty();
	}

	/** pick the other point P1 lies on this circle, such that PP1's direction is (x, y) */
	public BigPoint pickPoint(BigPoint p, BigPoly x, BigPoly y) {
		return p.reflect(new BigPoint(new BigLine(p, x, y), new BigLine(getCenter(), y, new BigPoly().add(__1, x))));
	}

	@Override
	public String toString() {
		return "(" + a + ")*(x**2 + y**2) + (" + d + ")*x*z + (" + e + ")*y*z + (" + f + ")*z**2 = 0";
	}

	private static BigPoly[] row(BigPoint p) {
		BigPoly x = p.getX();
		BigPoly y = p.getY();
		BigPoly z = p.getZ();
		return new BigPoly[] {
			new BigPoly().addMul(_1, x, x).addMul(_1, y, y),
			new BigPoly().addMul(_1, x, z),
			new BigPoly().addMul(_1, y, z),
			new BigPoly().addMul(_1, z, z),
		};
	}

	public static boolean concyclic(BigPoint p1, BigPoint p2, BigPoint p3, BigPoint p4) {
		BigPoly[] r1 = row(p1);
		BigPoly[] r2 = row(p2);
		BigPoly[] r3 = row(p3);
		BigPoly[] r4 = row(p4);
		return BigPoly.det(
				r1[0], r1[1], r1[2], r1[3],
				r2[0], r2[1], r2[2], r2[3],
				r3[0], r3[1], r3[2], r3[3],
				r4[0], r4[1], r4[2], r4[3]).isEmpty();
	}
}