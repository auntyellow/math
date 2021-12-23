package com.ogprover.main;

import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;
import java.util.logging.Logger;

public class OpenGeoProver {
	static {
		Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINEST);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINEST);
		}
	}

	public static OGPConfigurationSettings settings = null;
}