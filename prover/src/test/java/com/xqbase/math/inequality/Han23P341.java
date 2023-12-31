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
import com.xqbase.math.polys.MutableBigInteger;
import com.xqbase.math.polys.Poly;

public class Han23P341 {
	private static Logger log = LoggerFactory.getLogger(Han23P341.class);

	static {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.INFO);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.INFO);
		}
	}

	public static void main(String[] args) throws Exception {
		String vars = "abcuvw";
		// result from han23-p341u.py
		BigPoly fn = new BigPoly(vars, "a**5*b*u**2*v**2*w**2 + a**5*b*u**2*v*w**3 + a**5*b*u*v**2*w**3 + a**5*b*u*v*w**4 + a**5*c*u**2*v**2*w**2 + a**5*c*u**2*v*w**3 + a**5*c*u*v**2*w**3 + a**5*c*u*v*w**4 + a**4*b**2*u**3*v**2*w + a**4*b**2*u**3*v*w**2 + a**4*b**2*u**2*v**3*w + 2*a**4*b**2*u**2*v**2*w**2 + a**4*b**2*u**2*v*w**3 + a**4*b**2*u*v**3*w**2 + a**4*b**2*u*v**2*w**3 - 9*a**4*b**2*u*v*w**4 + a**4*b*c*u**3*v**2*w + a**4*b*c*u**3*v*w**2 + a**4*b*c*u**2*v**3*w + 3*a**4*b*c*u**2*v**2*w**2 - 6*a**4*b*c*u**2*v*w**3 + a**4*b*c*u**2*w**4 + a**4*b*c*u*v**3*w**2 - 6*a**4*b*c*u*v**2*w**3 + 3*a**4*b*c*u*v*w**4 + a**4*b*c*u*w**5 + a**4*b*c*v**2*w**4 + a**4*b*c*v*w**5 - 9*a**4*c**2*u**2*v**2*w**2 + a**4*c**2*u**2*v*w**3 + a**4*c**2*u**2*w**4 + a**4*c**2*u*v**2*w**3 + 2*a**4*c**2*u*v*w**4 + a**4*c**2*u*w**5 + a**4*c**2*v**2*w**4 + a**4*c**2*v*w**5 + a**3*b**3*u**3*v**3 + a**3*b**3*u**3*v**2*w + a**3*b**3*u**2*v**3*w + 2*a**3*b**3*u**2*v**2*w**2 - 8*a**3*b**3*u**2*v*w**3 - 8*a**3*b**3*u*v**2*w**3 + 2*a**3*b**3*u*v*w**4 + a**3*b**3*u*w**5 + a**3*b**3*v*w**5 + a**3*b**3*w**6 + a**3*b**2*c*u**3*v**3 + 3*a**3*b**2*c*u**3*v**2*w - 6*a**3*b**2*c*u**3*v*w**2 + a**3*b**2*c*u**3*w**3 + 3*a**3*b**2*c*u**2*v**3*w - 10*a**3*b**2*c*u**2*v**2*w**2 + 7*a**3*b**2*c*u**2*v*w**3 + 2*a**3*b**2*c*u**2*w**4 - 6*a**3*b**2*c*u*v**3*w**2 + 7*a**3*b**2*c*u*v**2*w**3 + 6*a**3*b**2*c*u*v*w**4 - 7*a**3*b**2*c*u*w**5 + a**3*b**2*c*v**3*w**3 + 2*a**3*b**2*c*v**2*w**4 - 7*a**3*b**2*c*v*w**5 + a**3*b**2*c*w**6 + a**3*b*c**2*u**3*v**3 - 7*a**3*b*c**2*u**3*v**2*w + 2*a**3*b*c**2*u**3*v*w**2 + a**3*b*c**2*u**3*w**3 - 7*a**3*b*c**2*u**2*v**3*w + 6*a**3*b*c**2*u**2*v**2*w**2 + 7*a**3*b*c**2*u**2*v*w**3 - 6*a**3*b*c**2*u**2*w**4 + 2*a**3*b*c**2*u*v**3*w**2 + 7*a**3*b*c**2*u*v**2*w**3 - 10*a**3*b*c**2*u*v*w**4 + 3*a**3*b*c**2*u*w**5 + a**3*b*c**2*v**3*w**3 - 6*a**3*b*c**2*v**2*w**4 + 3*a**3*b*c**2*v*w**5 + a**3*b*c**2*w**6 + a**3*c**3*u**3*v**3 + a**3*c**3*u**3*v**2*w + a**3*c**3*u**2*v**3*w + 2*a**3*c**3*u**2*v**2*w**2 - 8*a**3*c**3*u**2*v*w**3 - 8*a**3*c**3*u*v**2*w**3 + 2*a**3*c**3*u*v*w**4 + a**3*c**3*u*w**5 + a**3*c**3*v*w**5 + a**3*c**3*w**6 - 9*a**2*b**4*u**2*v**2*w**2 + a**2*b**4*u**2*v*w**3 + a**2*b**4*u**2*w**4 + a**2*b**4*u*v**2*w**3 + 2*a**2*b**4*u*v*w**4 + a**2*b**4*u*w**5 + a**2*b**4*v**2*w**4 + a**2*b**4*v*w**5 + a**2*b**3*c*u**3*v**3 - 7*a**2*b**3*c*u**3*v**2*w + 2*a**2*b**3*c*u**3*v*w**2 + a**2*b**3*c*u**3*w**3 - 7*a**2*b**3*c*u**2*v**3*w + 6*a**2*b**3*c*u**2*v**2*w**2 + 7*a**2*b**3*c*u**2*v*w**3 - 6*a**2*b**3*c*u**2*w**4 + 2*a**2*b**3*c*u*v**3*w**2 + 7*a**2*b**3*c*u*v**2*w**3 - 10*a**2*b**3*c*u*v*w**4 + 3*a**2*b**3*c*u*w**5 + a**2*b**3*c*v**3*w**3 - 6*a**2*b**3*c*v**2*w**4 + 3*a**2*b**3*c*v*w**5 + a**2*b**3*c*w**6 - 9*a**2*b**2*c**2*u**3*v**3 + 3*a**2*b**2*c**2*u**3*v**2*w + 6*a**2*b**2*c**2*u**3*v*w**2 - 6*a**2*b**2*c**2*u**3*w**3 + 3*a**2*b**2*c**2*u**2*v**3*w + 12*a**2*b**2*c**2*u**2*v**2*w**2 - 12*a**2*b**2*c**2*u**2*v*w**3 + 6*a**2*b**2*c**2*u**2*w**4 + 6*a**2*b**2*c**2*u*v**3*w**2 - 12*a**2*b**2*c**2*u*v**2*w**3 + 12*a**2*b**2*c**2*u*v*w**4 + 3*a**2*b**2*c**2*u*w**5 - 6*a**2*b**2*c**2*v**3*w**3 + 6*a**2*b**2*c**2*v**2*w**4 + 3*a**2*b**2*c**2*v*w**5 - 9*a**2*b**2*c**2*w**6 + a**2*b*c**3*u**3*v**3 + 3*a**2*b*c**3*u**3*v**2*w - 6*a**2*b*c**3*u**3*v*w**2 + a**2*b*c**3*u**3*w**3 + 3*a**2*b*c**3*u**2*v**3*w - 10*a**2*b*c**3*u**2*v**2*w**2 + 7*a**2*b*c**3*u**2*v*w**3 + 2*a**2*b*c**3*u**2*w**4 - 6*a**2*b*c**3*u*v**3*w**2 + 7*a**2*b*c**3*u*v**2*w**3 + 6*a**2*b*c**3*u*v*w**4 - 7*a**2*b*c**3*u*w**5 + a**2*b*c**3*v**3*w**3 + 2*a**2*b*c**3*v**2*w**4 - 7*a**2*b*c**3*v*w**5 + a**2*b*c**3*w**6 + a**2*c**4*u**3*v**2*w + a**2*c**4*u**3*v*w**2 + a**2*c**4*u**2*v**3*w + 2*a**2*c**4*u**2*v**2*w**2 + a**2*c**4*u**2*v*w**3 + a**2*c**4*u*v**3*w**2 + a**2*c**4*u*v**2*w**3 - 9*a**2*c**4*u*v*w**4 + a*b**5*u**2*v**2*w**2 + a*b**5*u**2*v*w**3 + a*b**5*u*v**2*w**3 + a*b**5*u*v*w**4 + a*b**4*c*u**3*v**2*w + a*b**4*c*u**3*v*w**2 + a*b**4*c*u**2*v**3*w + 3*a*b**4*c*u**2*v**2*w**2 - 6*a*b**4*c*u**2*v*w**3 + a*b**4*c*u**2*w**4 + a*b**4*c*u*v**3*w**2 - 6*a*b**4*c*u*v**2*w**3 + 3*a*b**4*c*u*v*w**4 + a*b**4*c*u*w**5 + a*b**4*c*v**2*w**4 + a*b**4*c*v*w**5 + a*b**3*c**2*u**3*v**3 + 3*a*b**3*c**2*u**3*v**2*w - 6*a*b**3*c**2*u**3*v*w**2 + a*b**3*c**2*u**3*w**3 + 3*a*b**3*c**2*u**2*v**3*w - 10*a*b**3*c**2*u**2*v**2*w**2 + 7*a*b**3*c**2*u**2*v*w**3 + 2*a*b**3*c**2*u**2*w**4 - 6*a*b**3*c**2*u*v**3*w**2 + 7*a*b**3*c**2*u*v**2*w**3 + 6*a*b**3*c**2*u*v*w**4 - 7*a*b**3*c**2*u*w**5 + a*b**3*c**2*v**3*w**3 + 2*a*b**3*c**2*v**2*w**4 - 7*a*b**3*c**2*v*w**5 + a*b**3*c**2*w**6 + a*b**2*c**3*u**3*v**3 - 7*a*b**2*c**3*u**3*v**2*w + 2*a*b**2*c**3*u**3*v*w**2 + a*b**2*c**3*u**3*w**3 - 7*a*b**2*c**3*u**2*v**3*w + 6*a*b**2*c**3*u**2*v**2*w**2 + 7*a*b**2*c**3*u**2*v*w**3 - 6*a*b**2*c**3*u**2*w**4 + 2*a*b**2*c**3*u*v**3*w**2 + 7*a*b**2*c**3*u*v**2*w**3 - 10*a*b**2*c**3*u*v*w**4 + 3*a*b**2*c**3*u*w**5 + a*b**2*c**3*v**3*w**3 - 6*a*b**2*c**3*v**2*w**4 + 3*a*b**2*c**3*v*w**5 + a*b**2*c**3*w**6 + a*b*c**4*u**3*v**2*w + a*b*c**4*u**3*v*w**2 + a*b*c**4*u**2*v**3*w + 3*a*b*c**4*u**2*v**2*w**2 - 6*a*b*c**4*u**2*v*w**3 + a*b*c**4*u**2*w**4 + a*b*c**4*u*v**3*w**2 - 6*a*b*c**4*u*v**2*w**3 + 3*a*b*c**4*u*v*w**4 + a*b*c**4*u*w**5 + a*b*c**4*v**2*w**4 + a*b*c**4*v*w**5 + a*c**5*u**2*v**2*w**2 + a*c**5*u**2*v*w**3 + a*c**5*u*v**2*w**3 + a*c**5*u*v*w**4 + b**5*c*u**2*v**2*w**2 + b**5*c*u**2*v*w**3 + b**5*c*u*v**2*w**3 + b**5*c*u*v*w**4 + b**4*c**2*u**3*v**2*w + b**4*c**2*u**3*v*w**2 + b**4*c**2*u**2*v**3*w + 2*b**4*c**2*u**2*v**2*w**2 + b**4*c**2*u**2*v*w**3 + b**4*c**2*u*v**3*w**2 + b**4*c**2*u*v**2*w**3 - 9*b**4*c**2*u*v*w**4 + b**3*c**3*u**3*v**3 + b**3*c**3*u**3*v**2*w + b**3*c**3*u**2*v**3*w + 2*b**3*c**3*u**2*v**2*w**2 - 8*b**3*c**3*u**2*v*w**3 - 8*b**3*c**3*u*v**2*w**3 + 2*b**3*c**3*u*v*w**4 + b**3*c**3*u*w**5 + b**3*c**3*v*w**5 + b**3*c**3*w**6 - 9*b**2*c**4*u**2*v**2*w**2 + b**2*c**4*u**2*v*w**3 + b**2*c**4*u**2*w**4 + b**2*c**4*u*v**2*w**3 + 2*b**2*c**4*u*v*w**4 + b**2*c**4*u*w**5 + b**2*c**4*v**2*w**4 + b**2*c**4*v*w**5 + b*c**5*u**2*v**2*w**2 + b*c**5*u**2*v*w**3 + b*c**5*u*v**2*w**3 + b*c**5*u*v*w**4");
		BigPoly ab = new BigPoly(vars, "a + b");
		BigPoly bc = new BigPoly(vars, "b + c");
		// BigPoly c = new BigPoly(vars, "c");
		int[][] perms = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};
		Set<BigPoly> polys = Collections.singleton(fn);
		int depth = 1;
		while (!polys.isEmpty()) {
			log.info("depth = " + depth + ", polynomials = " + polys.size());
			int traceCurr = 0;
			Set<BigPoly> polys1 = new HashSet<>();
			int trivials = 0;
			for (BigPoly f0 : polys) {
				traceCurr ++;
				log.info("depth = " + depth + ", polynomial: " + traceCurr + "/" + polys.size());

				for (int[] perm : perms) {
					// f1 = f0's permutation and substitution
					BigPoly f1 = new BigPoly();
					for (Map.Entry<Mono, MutableBigInteger> term : f0.entrySet()) {
						short[] exps = term.getKey().getExps();
						short[] exps1 = exps.clone();
						for (int i = 0; i < 3; i ++) {
							// permute
							exps1[perm[i]] = exps[i];
						}
						f1.put(new Mono(vars, exps1), term.getValue());
					}
					// substitute
					f1 = (BigPoly) f1.subs('a', ab);
					f1 = (BigPoly) f1.subs('b', bc);
					// f1 = (BigPoly) f1.subs('c', c);
					boolean trivial = true;
					for (Poly<MutableBigInteger> coeff : f1.coeffsOf("abc").values()) {
						// vars = "abcuvw" -> vars = "uvw"
						BigPoly coeff1 = new BigPoly();
						for (Map.Entry<Mono, MutableBigInteger> entry : coeff.entrySet()) {
							coeff1.put(new Mono("uvw", Arrays.copyOfRange(entry.getKey().getExps(), 3, 6)),
									entry.getValue());
						}
						if (!SDS.tsds(coeff1).isNonNegative()) {
							trivial = false;
							trivials ++;
							break;
						}
					}
					if (!trivial) {
						polys1.add(f1);
						log.info("after depth = " + depth + ": polynomials = " + polys1.size() + ", trivials = " + trivials);
					}
				}
			}
			polys = polys1;
			depth ++;
		}
	}
}