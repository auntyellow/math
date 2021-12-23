package a.c.a;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import a.c.e.b;
import a.c.e.c;
import a.c.e.d;

public class a {
	private static final String CLASS = "com.ogprover.api.GeoGebraOGPInterface";
	private static final Logger log = LoggerFactory.getLogger(a.class);

	/** @param proverInput */
	public d a(c proverInput) {
		log.info(CLASS + ".prove(OGPInputProverProtocol)");
		return new b();
	}
}