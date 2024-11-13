package com.b.a;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.b.e.b;
import com.b.e.c;
import com.b.e.d;
import com.xqbase.math.geometry.prover.ProveException;
import com.xqbase.math.geometry.prover.Prover;

public class a {
	private static final String CLASS = "com.ogprover.api.GeoGebraOGPInterface";
	private static final Logger log = LoggerFactory.getLogger(a.class);

	public d a(c proverInput) {
		log.info(CLASS + ".prove(OGPInputProverProtocol)");
		b output = new b();
		if (proverInput instanceof com.b.e.a) {
			try {
				output.setResult(Prover.prove(((com.b.e.a) proverInput).getGeometryTheoremText()));
			} catch (ProveException e) {
				output.setMessage(e.getMessage());
			}
		} else {
			output.setMessage("proverInput is not com.ogprover.pp.GeoGebraOGPInputProverProtocol");
		}
		return output;
	}
}