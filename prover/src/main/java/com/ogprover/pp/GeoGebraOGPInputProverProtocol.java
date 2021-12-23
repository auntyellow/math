package com.ogprover.pp;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GeoGebraOGPInputProverProtocol extends OGPInputProverProtocol {
	private static final String CLASS = "com.ogprover.pp.GeoGebraOGPInputProverProtocol";
	private static final Logger log = LoggerFactory.getLogger(GeoGebraOGPInputProverProtocol.class);

	public void setGeometryTheoremText(String geometryTheoremText) {
		log.debug(CLASS + ".setGeometryTheoremText(\"{}\")", geometryTheoremText);
	}

	public void setMethod(String method) {
		log.debug(CLASS + ".setMethod(\"{}\")", method);
	}

	public void setTimeOut(double timeout) {
		log.debug(CLASS + ".setTimeOut({})", "" + timeout);
	}

	public void setMaxTerms(int maxterms) {
		log.debug(CLASS + ".setMaxTerms({})", "" + maxterms);
	}

	public void setReportFormat(String reportFormat) {
		log.debug(CLASS + ".setReportFormat({})", "" + reportFormat);
	}
}