package com.xqbase.math.geometry.prover;

import java.io.File;
import java.io.InputStream;
import java.util.zip.ZipFile;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.junit.Assert;
import org.junit.Test;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class ProverTest {
	private static final DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

	@Test
	public void test() throws Exception {
		DocumentBuilder builder = dbf.newDocumentBuilder();
		for (File file : new File(ProverTest.class.getResource("").toURI()).listFiles()) {
			if (!file.getName().endsWith(".ggb")) {
				continue;
			}
			NodeList nodes;
			try (
				ZipFile ggb = new ZipFile(file);
				InputStream in = ggb.getInputStream(ggb.getEntry("geogebra.xml"));
			) {
				nodes = builder.parse(in).getFirstChild().getChildNodes();
			}
			Element input = null;
			int len = nodes.getLength();
			for (int i = 0; i < len; i ++) {
				Node node = nodes.item(i);
				if ((node instanceof Element) &&
						((Element) node).getTagName().equals("construction")) {
					input = (Element) node;
					break;
				}
			}
			if (input == null) {
				Assert.fail("unable to find \"construction\" in geogebra.xml in " + file);
			} else {
				Assert.assertEquals(file.getName(), "true", Prover.prove(input));
			}
		}
	}
}
