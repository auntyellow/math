package com.b.e;

import java.util.Vector;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class b extends d {
	private static final String CLASS = "com.ogprover.pp.GeoGebraOGPOutputProverProtocol";
	private static final Logger log = LoggerFactory.getLogger(b.class);

	public Vector<String> a() {
		log.info(CLASS + ".getNdgList()");
		return new Vector<>();
	}

	public String a(String resName) {
		log.info(CLASS + ".getOutputResult(\"{}\")", resName);
		return null;
	}
}