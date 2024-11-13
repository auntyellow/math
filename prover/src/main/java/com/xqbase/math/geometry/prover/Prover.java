package com.xqbase.math.geometry.prover;

import java.io.ByteArrayInputStream;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Prover {
	private static final Logger log = LoggerFactory.getLogger(Prover.class);
	private static final DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

	public static String prove(String input) throws ProveException {
		DocumentBuilder builder;
		try {
			builder = dbf.newDocumentBuilder();
		} catch (ParserConfigurationException e) {
			throw new RuntimeException(e);
		}
		Document doc;
		try {
			doc = builder.parse(new ByteArrayInputStream(input.getBytes()));
		} catch (SAXException | IOException e) {
			throw new ProveException(e.getMessage());
		}
		Element pom = (Element) doc.getFirstChild();
		if (!pom.getTagName().equals("construction")) {
			throw new ProveException("Expect XML Root <construction>");
		}
		NodeList nodes = pom.getChildNodes();
		int len = nodes.getLength();
		for (int i = 0; i < len; i ++) {
			Node node = nodes.item(i);
			if (!(node instanceof Element)) {
				continue;
			}
			Element element = (Element) node;
			switch (element.getTagName()) {
			case "element":
				log.info("element type {} label {}", element.getAttribute("type"), element.getAttribute("label"));
				// TODO save label
				break;
			case "command":
				log.info("command name {}", element.getAttribute("name"));
				// TODO input and output
				break;
			default:
				break;
			}
		}
		return "unknown";
	}
}
