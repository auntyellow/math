package com.xqbase.math.inequality;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.polys.BigPoly;
import com.xqbase.math.polys.Mono;
import com.xqbase.math.polys.MutableBig;

public class _1777075 {
	private static Logger log = LoggerFactory.getLogger(_1777075.class);

	static {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.WARNING);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.WARNING);
		}
	}

	private static double remove(BigPoly coeff, Mono mono) {
		MutableBig d = coeff.remove(mono);
		return d == null ? 0 : d.doubleValue();
	}

	public static void main(String[] args) throws Exception {
		String vars = "mnxyz";
		// fn from 1777075.py
		BigPoly fn = new BigPoly(vars, "m**3*x**5*z**2 - m**3*x**3*y**2*z**2 + m**3*x**2*y**5 - m**3*x**2*y**3*z**2 - m**3*x**2*y**2*z**3 + m**3*y**2*z**5 + m**2*n*x**5*y**2 + m**2*n*x**4*y**3 - m**2*n*x**4*y*z**2 - m**2*n*x**4*z**3 - m**2*n*x**3*y**4 + m**2*n*x**3*z**4 - m**2*n*x**2*y**4*z + m**2*n*x**2*z**5 - m**2*n*x*y**2*z**4 + m**2*n*y**5*z**2 + m**2*n*y**4*z**3 - m**2*n*y**3*z**4 - m*n**2*x**4*y**2*z + m*n**2*x**3*y**2*z**2 + m*n**2*x**2*y**3*z**2 + m*n**2*x**2*y**2*z**3 - m*n**2*x**2*y*z**4 - m*n**2*x*y**4*z**2");
		// A_3
		/*
		BigPoly xy = new BigPoly(vars, "x + y");
		BigPoly yz = new BigPoly(vars, "y + z");
		*/
		// T_3
		BigPoly xy = new BigPoly(vars, "6*x + y");
		BigPoly yz = new BigPoly(vars, "3*y + z");
		BigPoly z = new BigPoly(vars, "2*z");
		Mono m3 = new Mono("mn", new short[] {3, 0});
		Mono m2n = new Mono("mn", new short[] {2, 1});
		Mono mn2 = new Mono("mn", new short[] {1, 2});
		int[][] perms = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};
		Set<BigPoly> polys = Collections.singleton(fn);
		int depth = 1;
		while (!polys.isEmpty()) {
			System.out.println("depth = " + depth);
			// log.info("depth = " + depth + ", polynomials = " + polys.size());
			int traceCurr = 0;
			Set<BigPoly> polys1 = new HashSet<>();
			int trivials = 0;
			double minRatio = Double.MAX_VALUE;
			for (BigPoly f0 : polys) {
				traceCurr ++;
				log.info("depth = " + depth + ", polynomial: " + traceCurr + "/" + polys.size());

				for (int[] perm : perms) {
					// f1 = f0's permutation and substitution
					BigPoly f1 = new BigPoly();
					for (Map.Entry<Mono, MutableBig> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = exps.clone();
						for (int i = 0; i < 3; i ++) {
							// permute
							exps1[2 + perm[i]] = exps[2 + i];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// substitute
					f1 = f1.subs('x', xy).subs('y', yz).subs('z', z);
					boolean trivial = true;
					for (BigPoly coeff : f1.coeffsOf("xyz").values()) {
						// vars = "mnxyz" -> vars = "mn"
						BigPoly coeff1 = new BigPoly();
						for (Map.Entry<Mono, MutableBig> entry : coeff.entrySet()) {
							coeff1.put(new Mono("mn", Arrays.copyOfRange(entry.getKey().getExps(), 0, 2)),
									entry.getValue());
						}
						if (!SDS.sds(coeff1.homogenize('k'), SDS.Transform.T_n).isNonNegative()) {
							// each term of coeff1 has form a*m**3 + b*m**2*n - c*m*n**2 = m*(a*m**2 + b*m*n - c*n*2)
							trivial = false;
							trivials ++;
							BigPoly coeff2 = (BigPoly) coeff1.clone();
							double a = remove(coeff2, m3);
							double b = remove(coeff2, m2n);
							double c = remove(coeff2, mn2);
							assert coeff2.isEmpty() && a >= 0 && b >= 0 && c <= 0;
							if (a == 0) {
								continue;
							}
							double ratio = 2*a/(Math.sqrt(b*b - 4*a*c) - b);
							if (ratio < minRatio) {
								minRatio = ratio;
							}
						}
					}
					if (!trivial) {
						polys1.add(f1);
						log.info("after depth = " + depth + ": polynomials = " + polys1.size() + ", trivials = " + trivials);
					}
				}
			}
			System.out.println("n / m = " + minRatio);
			polys = polys1;
			depth ++;
		}
	}
}