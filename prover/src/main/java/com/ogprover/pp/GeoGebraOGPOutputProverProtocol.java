package com.ogprover.pp;

import java.util.Vector;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GeoGebraOGPOutputProverProtocol extends OGPOutputProverProtocol {
	private static Logger log = LoggerFactory.getLogger(GeoGebraOGPOutputProverProtocol.class);

	public Vector<String> getNdgList() {
		log.debug("");
		return new Vector<>();
	}

	public String getOutputResult(String resName) {
		log.debug("resName: {}", resName);
		return null;
	}
}