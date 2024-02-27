package com.xqbase.math.inequality;

import java.util.List;
import java.util.Set;

import com.xqbase.math.polys.LongPoly;
import com.xqbase.math.polys.MutableLong;

public class DumpLattice {
	/** @param args */
	public static void main(String[] args) {
		// dump into sds-lattice.py
		SDS.Result<MutableLong> result = SDS.sds(new LongPoly("xyz", "-x - y - z"), SDS.Transform.Y_n, SDS.Find.DUMP_LATTICE, 5);
		// dump into sds-lattice-j4.py
		// SDS.Result<MutableLong> result = SDS.sds(new LongPoly("wxyz", "-w - x - y - z"), SDS.Transform.J_4, SDS.Find.DUMP_LATTICE, 2);
		for (Set<Set<List<MutableLong>>> simplices : result.getSimplices()) {
			for (Set<List<MutableLong>> simplex : simplices) {
				String s = simplex.toString();
				System.out.println("    [" + s.substring(1, s.length() - 1) + "],");
			}
			System.out.println("], [");
		}
	}

	/** @param args */
	public static void main3d(String[] args) {
		// dump into sds-lattice-3d.py
		SDS.Result<MutableLong> result = SDS.sds(new LongPoly("wxyz", "-w - x - y - z"), SDS.Transform.J_4, SDS.Find.DUMP_LATTICE, 5);
		for (List<MutableLong> zeroAt : result.getZeroAt()) {
			System.out.println("    " + zeroAt + ",");
		}
	}

	/** @param args */
	public static void mainDiameter(String[] args) {
		SDS.Result<MutableLong> result = SDS.sds(new LongPoly("wxyz", "-w - x - y - z"), SDS.Transform.Y_n, SDS.Find.DUMP_LATTICE, 9);
		@SuppressWarnings("unchecked")
		List<MutableLong>[] emptyList = new List[0];
		int depth = 0;
		for (Set<Set<List<MutableLong>>> simplices : result.getSimplices()) {
			double max = 0;
			for (Set<List<MutableLong>> simplex : simplices) {
				List<MutableLong>[] simplex_ = simplex.toArray(emptyList);
				double[][] vertices = new double[simplex_.length][];
				for (int i = 0; i < vertices.length; i ++) {
					List<MutableLong> vertice_ = simplex_[i];
					double[] vertice = new double[vertice_.size()];
					double one = 0;
					for (int j = 0; j < vertice.length; j ++) {
						one += vertice_.get(j).doubleValue();
					}
					for (int j = 0; j < vertice.length; j ++) {
						vertice[j] = vertice_.get(j).doubleValue()/one;
					}
					vertices[i] = vertice;
				}
				for (int i = 0; i < vertices.length; i ++) {
					for (int j = i + 1; j < vertices.length; j ++) {
						double d = 0;
						for (int k = 0; k < vertices.length; k ++) {
							double d0 = vertices[i][k] - vertices[j][k];
							d += d0*d0/2;
						}
						max = Math.max(max, Math.sqrt(d));
					}
				}
			}
			System.out.println("depth = " + depth +
					", simplices = " + simplices.size() +
					", max_diameter = " + max);
			depth ++;
		}
	}
}