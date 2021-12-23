package com.ogprover.api;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.ogprover.pp.GeoGebraOGPOutputProverProtocol;
import com.ogprover.pp.OGPInputProverProtocol;
import com.ogprover.pp.OGPOutputProverProtocol;

public class GeoGebraOGPInterface {
	private static final String CLASS = "com.ogprover.api.GeoGebraOGPInterface";
	private static final Logger log = LoggerFactory.getLogger(GeoGebraOGPInterface.class);

	/** @param proverInput */
	public OGPOutputProverProtocol prove(OGPInputProverProtocol proverInput) {
		log.debug(CLASS + ".prove(OGPInputProverProtocol)");
		return new GeoGebraOGPOutputProverProtocol();
	}
}