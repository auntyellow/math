package com.b.e;

import java.util.Vector;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class b extends d {
	private static final String CLASS = "com.ogprover.pp.GeoGebraOGPOutputProverProtocol";
	private static final Logger log = LoggerFactory.getLogger(b.class);

	private String result = null, message = null;

	public String getResult() {
		return result;
	}

	public void setResult(String result) {
		this.result = result;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public Vector<String> a() {
		log.info(CLASS + ".getNdgList()");
		return new Vector<>();
	}

	public String a(String resName) {
		log.info(CLASS + ".getOutputResult(\"{}\")", resName);
		switch (resName) {
		case "success":
			return result == null ? "false" : "true";
		case "failureMessage":
			return message;
		case "proverResult":
			return result == null ? "unknown" : result;
		case "proverMessage":
			return message;
		case "time":
			return "0";
		case "numTerms":
			return "0";
		default:
			return null;
		}
	}
}