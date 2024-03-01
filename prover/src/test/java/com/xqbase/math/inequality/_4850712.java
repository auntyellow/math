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
import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.MutableBig;

public class _4850712 {
	private static Logger log = LoggerFactory.getLogger(_4850712.class);

	static {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.WARNING);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.WARNING);
		}
	}

	private static double remove(BigPoly coeff, Monom mono) {
		MutableBig d = coeff.remove(mono);
		return d == null ? 0 : d.doubleValue();
	}

	public static void main(String[] args) throws Exception {
		String vars = "nxyz";
		// fn from 4850712u.py
		BigPoly fn = new BigPoly(vars, "x**5*z**2 - x**3*y**2*z**2 + x**2*y**5 - x**2*y**3*z**2 - x**2*y**2*z**3 + y**2*z**5 + n*x**5*y**2 + n*x**4*y**3 - n*x**4*y*z**2 - n*x**4*z**3 - n*x**3*y**4 + n*x**3*z**4 - n*x**2*y**4*z + n*x**2*z**5 - n*x*y**2*z**4 + n*y**5*z**2 + n*y**4*z**3 - n*y**3*z**4 - n**2*x**4*y**2*z + n**2*x**3*y**2*z**2 + n**2*x**2*y**3*z**2 + n**2*x**2*y**2*z**3 - n**2*x**2*y*z**4 - n**2*x*y**4*z**2");
		Monom n2 = new Monom(new short[] {2});
		Monom n1 = new Monom(new short[] {1});
		Monom n0 = new Monom(new short[] {0});
		int[][][] perms = {{{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}}};
		// A_3
		/*
		BigPoly[][] subs = {{
			new BigPoly(vars, "x + y"),
			new BigPoly(vars, "y + z"),
		}};
		*/
		// T_3
		BigPoly[][] subs = {{
			new BigPoly(vars, "6*x + y"),
			new BigPoly(vars, "3*y + z"),
			new BigPoly(vars, "2*z")
		}};
		// H_3 doesn't seem to work
		/*
		int[][][] perms = {{{0, 1, 2}, {1, 2, 0}, {2, 0, 1}}, {{0, 1, 2}}};
		BigPoly[][] subs = {{
			new BigPoly(vars, "2*x + y + z"),
		}, {
			new BigPoly(vars, "2*x + y - z"),
			new BigPoly(vars, "y + z - x"),
			new BigPoly(vars, "z + x"),
		}};
		*/
		Set<BigPoly> polys = Collections.singleton(fn);
		int depth = 1;
		while (!polys.isEmpty()) {
			System.out.println("depth = " + depth);
			// log.info("depth = " + depth + ", polynomials = " + polys.size());
			int traceCurr = 0;
			Set<BigPoly> polys1 = new HashSet<>();
			double min = Double.MAX_VALUE;
			for (BigPoly f0 : polys) {
				traceCurr ++;
				log.info("depth = " + depth + ", polynomial: " + traceCurr + "/" + polys.size());

				for (int i = 0; i < perms.length; i ++) {
					for (int[] perm : perms[i]) {
						// f1 = f0's permutation and substitution
						BigPoly f1 = new BigPoly(vars);
						for (Map.Entry<Monom, MutableBig> term : f0.entrySet()) {
							short[] exps = term.getKey().getExps();
							short[] exps1 = exps.clone();
							for (int j = 0; j < 3; j ++) {
								// permute
								exps1[1 + perm[j]] = exps[1 + j];
							}
							f1.put(new Monom(exps1), term.getValue());
						}
						// substitute
						BigPoly[] subs_ = subs[i];
						for (int j = 0; j < subs_.length; j ++) {
							f1 = f1.subs(vars.charAt(1 + j), subs_[j]);
						}
						boolean trivial = true;
						for (BigPoly coeff : f1.coeffsOf("xyz").values()) {
							// vars = "nxyz" -> vars = "n"
							BigPoly coeff1 = new BigPoly("n");
							for (Map.Entry<Monom, MutableBig> entry : coeff.entrySet()) {
								coeff1.put(new Monom(Arrays.copyOfRange(entry.getKey().getExps(), 0, 1)),
										entry.getValue());
							}
							double a = remove(coeff1, n2);
							double b = remove(coeff1, n1);
							double c = remove(coeff1, n0);
							if (!coeff1.isEmpty()) {
								System.out.println("Doesn't match a*n**2 + b*n + c: " + coeff);
								return;
							}
							if (a > 0 || c < 0) {
								System.out.println("a > 0 || c < 0: " + coeff);
								return;
							}
							double n;
							if (a == 0) {
								if (b >= 0) {
									// trivial
									continue;
								}
								n = -c / b;
							} else {
								n = (-b - Math.sqrt(b*b - 4*a*c))/2/a;
							}
							trivial = false;
							if (n < min) {
								min = n;
							}
						}
						if (!trivial) {
							polys1.add(f1);
							log.info("after depth = " + depth + ": polynomials = " + polys1.size());
						}
					}
				}
			}
			System.out.println("n = " + min);
			polys = polys1;
			depth ++;
		}
	}
}