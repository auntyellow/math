package com.b.a;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.b.e.b;
import com.b.e.c;
import com.b.e.d;

public class a {
	private static final String CLASS = "com.ogprover.api.GeoGebraOGPInterface";
	private static final Logger log = LoggerFactory.getLogger(a.class);

	/** @param proverInput */
	public d a(c proverInput) {
		log.info(CLASS + ".prove(OGPInputProverProtocol)");
		return new b();
	}
}