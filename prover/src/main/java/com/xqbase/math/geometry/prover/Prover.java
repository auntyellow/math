package com.xqbase.math.geometry.prover;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import com.xqbase.math.geometry.Line;
import com.xqbase.math.geometry.Point;
import com.xqbase.math.polys.LongPoly;

public class Prover {
	private static final Logger log = LoggerFactory.getLogger(Prover.class);
	private static final DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
	private static final TransformerFactory tf = TransformerFactory.newInstance();

	private static boolean isBlank(String s) {
		return s == null || s.trim().isEmpty();
	}

	private static String toXml(Node node) {
		StringWriter writer = new StringWriter();
		try {
			Transformer transformer = tf.newTransformer();
			transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
			transformer.transform(new DOMSource(node), new StreamResult(writer));
		} catch (TransformerException e) {
			throw new RuntimeException(e);
		}
		return writer.toString();
	}

	private static LongPoly newCoord(List<String> vars) {
		String newVar = "u" + (vars.size() + 1);
		vars.add(newVar);
		return new LongPoly(vars, newVar);
	}

	private static final LongPoly ONE = new LongPoly(Arrays.asList(), "1");

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

		Map<String, Point> points = new HashMap<>();
		Map<String, Line> lines = new HashMap<>();
		List<String> vars = new ArrayList<>();

		NodeList nodes = pom.getChildNodes();
		int len = nodes.getLength();
		for (int i = 0; i < len; i ++) {
			Node node = nodes.item(i);
			if (!(node instanceof Element)) {
				log.warn("skip unknown node {}", toXml(node));
				continue;
			}
			Element element = (Element) node;

			switch (element.getTagName()) {
			case "element":
				String type = element.getAttribute("type");
				String label = element.getAttribute("label");
				if (isBlank(type) || isBlank(label)) {
					log.warn("type or label not found in {}", toXml(element));
					continue;
				}
				switch (type) {
				case "point":
					if (points.containsKey(label)) {
						log.info("point {} already constructed", label);
						break;
					}
					// free point
					Point point = new Point(newCoord(vars), newCoord(vars), ONE);
					points.put(label, point);
					log.info("construct a free point {} {}", label, point);
					break;
				case "line":
					if (lines.containsKey(label)) {
						log.info("line {} already constructed", label);
					} else {
						log.warn("unable to construct free line {}", label);
					}
					break;
				default:
					log.warn("skip unknown element {}", toXml(element));
				}
				break;

			case "command":
				String name = element.getAttribute("name");
				if (isBlank(name)) {
					log.warn("name not found in {}", toXml(element));
					continue;
				}
				List<String> inputLabels = new ArrayList<>();
				String outputLabel = null;
				NodeList nodesJ = element.getChildNodes();
				int lenJ = nodesJ.getLength();
				for (int j = 0; j < lenJ; j ++) {
					Node nodeJ = nodesJ.item(j);
					if (!(nodeJ instanceof Element)) {
						log.warn("skip unknown node {}", toXml(nodeJ));
						continue;
					}
					Element elementJ = (Element) nodeJ;
					switch (elementJ.getTagName()) {
					case "input":
						NamedNodeMap nodeMap = elementJ.getAttributes();
						int lenK = nodeMap.getLength();
						for (int k = 0; k < lenK; k ++) {
							Node nodeK = nodeMap.item(k);
							if (!(nodeK instanceof Attr)) {
								log.warn("skip unknown attr {}", toXml(nodeK));
								continue;
							}
							// is attr's name (a0, a1, ...) useful?
							inputLabels.add(((Attr) nodeK).getValue());
						}
						break;
					case "output":
						outputLabel = elementJ.getAttribute("a1");
						break;
					default:
						log.warn("skip unknown input or output {}", toXml(elementJ));
					}
				}
				if (isBlank(outputLabel)) {
					log.warn("missing output: {}", toXml(element));
					continue;
				}

				switch (name) {
				case "Line":
					break;

				case "Point":
					break;

				case "Intersect":
					break;

				default:
					log.warn("skip unknown command {}", toXml(element));
					break;
				}
				break;

			default:
				log.warn("skip unknown element or command {}", toXml(node));
				break;
			}
		}
		return "unknown";
	}
}
