package com.ogprover.pp;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GeoGebraOGPInputProverProtocol extends OGPInputProverProtocol {
	private static Logger log = LoggerFactory.getLogger(GeoGebraOGPInputProverProtocol.class);

	public void setGeometryTheoremText(String geometryTheoremText) {
		log.debug("geometryTheoremText: {}", geometryTheoremText);
	}

	public void setMethod(String method) {
		log.debug("method: {}", method);
	}

	public void setTimeOut(double timeout) {
		log.debug("timeout: {}", "" + timeout);
	}

	public void setMaxTerms(int maxterms) {
		log.debug("maxterms: {}", "" + maxterms);
	}

	public void setReportFormat(String reportFormat) {
		log.debug("reportFormat: {}", "" + reportFormat);
	}
}