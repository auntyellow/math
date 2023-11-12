package com.xqbase.math.polys;

import java.math.BigInteger;

import com.xqbase.math.polys.BigPoly;

public class BigPoint {
	private static final BigInteger _1 = BigInteger.ONE;
	private static final BigInteger _2 = _1.add(_1);
	private static final BigInteger __1 = _1.negate();

	private BigPoly x, y, z;

	public BigPoint(BigPoly x, BigPoly y,BigPoly z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public BigPoint(BigLine l1, BigLine l2) {
		x = BigPoly.det(l1.getV(), l1.getW(), l2.getV(), l2.getW());
		y = BigPoly.det(l1.getW(), l1.getU(), l2.getW(), l2.getU());
		z = BigPoly.det(l1.getU(), l1.getV(), l2.getU(), l2.getV());
	}

	public BigPoly getX() {
		return x;
	}

	public BigPoly getY() {
		return y;
	}

	public BigPoly getZ() {
		return z;
	}

	public boolean liesOn(BigLine l) {
		return new BigPoly().addMul(_1, x, l.getU()).addMul(_1, y, l.getV()).addMul(_1, z, l.getW()).isEmpty();
	}

	/** reflect this about p */
	public BigPoint reflect(BigPoint p) {
		return new BigPoint(
				new BigPoly().addMul(_2, z, p.getX()).addMul(__1, x, p.getZ()),
				new BigPoly().addMul(_2, z, p.getY()).addMul(__1, y, p.getZ()),
				new BigPoly().addMul(_1, z, p.getZ()));
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ", " + z + ")";
	}

	public static BigPoint midpoint(BigPoint p1, BigPoint p2) {
		return new BigPoint(
				new BigPoly().addMul(_1, p1.getX(), p2.getZ()).addMul(_1, p1.getZ(), p2.getX()),
				new BigPoly().addMul(_1, p1.getY(), p2.getZ()).addMul(_1, p1.getZ(), p2.getY()),
				new BigPoly().addMul(_2, p1.getZ(), p2.getZ()));
	}

	public static boolean collinear(BigPoint p1, BigPoint p2, BigPoint p3) {
		return BigPoly.det(
				p1.getX(), p1.getY(), p1.getZ(),
				p2.getX(), p2.getY(), p2.getZ(),
				p3.getX(), p3.getY(), p3.getZ()).isEmpty();
	}
}