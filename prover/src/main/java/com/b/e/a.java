package com.b.e;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.xqbase.math.geometry.prover.Prover;

public class a extends c {
	private static final String CLASS = "com.ogprover.pp.GeoGebraOGPInputProverProtocol";
	private static final Logger log = LoggerFactory.getLogger(a.class);

	private String geometryTheoremText = null;

	public String getGeometryTheoremText() {
		return geometryTheoremText;
	}

	public void a(String geometryTheoremText) {
		log.info(CLASS + ".setGeometryTheoremText(\"{}\")", geometryTheoremText);
		this.geometryTheoremText = geometryTheoremText;
	}

	public void b(String method) {
		log.info(CLASS + ".setMethod(\"{}\")", method);
	}

	public void a(double timeout) {
		log.info(CLASS + ".setTimeOut({})", "" + timeout);
	}

	public void a(int maxterms) {
		log.info(CLASS + ".setMaxTerms({})", "" + maxterms);
	}

	public void c(String reportFormat) {
		log.info(CLASS + ".setReportFormat(\"{}\")", "" + reportFormat);
	}
}