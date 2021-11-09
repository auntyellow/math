package com.xqbase.math.geometry;

import com.xqbase.math.polys.Poly;

public class Point {
	private Poly x, y, z;

	public Point(Poly x, Poly y, Poly z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public Poly getX() {
		return x;
	}

	public Poly getY() {
		return y;
	}

	public Poly getZ() {
		return z;
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ", " + z + ")";
	}
}