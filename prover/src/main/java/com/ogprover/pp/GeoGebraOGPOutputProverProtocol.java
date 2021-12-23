package com.ogprover.pp;

import java.util.Vector;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GeoGebraOGPOutputProverProtocol extends OGPOutputProverProtocol {
	private static final String CLASS = "com.ogprover.pp.GeoGebraOGPOutputProverProtocol";
	private static final Logger log = LoggerFactory.getLogger(GeoGebraOGPOutputProverProtocol.class);

	public Vector<String> getNdgList() {
		log.debug(CLASS + ".getNdgList()");
		return new Vector<>();
	}

	public String getOutputResult(String resName) {
		log.debug(CLASS + ".getOutputResult(\"{}\")", resName);
		return null;
	}
}