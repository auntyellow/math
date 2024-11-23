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
import org.w3c.dom.Text;
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

	private static void skipBlank(Node node) {
		if (!(node instanceof Text) || !isBlank(((Text) node).getData())) {
			log.warn("skip unknown node {}, {}", toXml(node), node.getClass());
		}
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

	private static final LongPoly ONE = new LongPoly("1");

	private static LongPoly newCoord(int[] vars) {
		vars[0] ++;
		String var = "u" + vars[0];
		return new LongPoly(var, var);
	}

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
		int[] vars = {0};

		NodeList nodes = pom.getChildNodes();
		int len = nodes.getLength();
		for (int i = 0; i < len; i ++) {
			Node node = nodes.item(i);
			if (!(node instanceof Element)) {
				skipBlank(node);
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
					// free point TODO: 1st (0, 0, 1), 2nd (1, 0, 1)
					// projective: 1st (1, 0, 0), 2nd (0, 1, 0), 3rd (0, 0, 1), 4th (1, 1, 1)
					Point point = new Point(newCoord(vars), newCoord(vars), ONE);
					points.put(label, point);
					log.info("construct a free point {}: {}", label, point);
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
						skipBlank(nodeJ);
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
						outputLabel = elementJ.getAttribute("a0");
						break;
					default:
						log.warn("skip unknown input or output {}", toXml(elementJ));
					}
				}
				if (isBlank(outputLabel) && !"Prove".equals(name)) {
					// command "Prove" has an empty output
					log.warn("missing output: {}", toXml(element));
					continue;
				}

				switch (name) {
				case "Line":
					if (inputLabels.size() != 2) {
						log.warn("unable to construct a line with less or more than 2 points: {}", inputLabels);
						continue;
					}
					Point p1 = points.get(inputLabels.get(0));
					Point p2 = points.get(inputLabels.get(1));
					if (p1 == null || p2 == null) {
						log.warn("points not found: {}", inputLabels);
						continue;
					}
					Line line = new Line(p1, p2);
					lines.put(outputLabel, line);
					log.info("construct a line {} by {}: {}", outputLabel, inputLabels, line);
					break;

				case "Point":
					if (inputLabels.size() != 1) {
						log.warn("unable to construct a semi-free point with less or more than 1 line: {}", inputLabels);
						continue;
					}
					label = inputLabels.get(0);
					line = lines.get(label);
					if (line == null) {
						log.warn("line not found: {}", label);
						continue;
					}
					Point point = new Point(line, newCoord(vars));
					points.put(outputLabel, point);
					log.info("construct a semi-free point {} on {}: {}", outputLabel, label, point);
					break;

				case "Intersect":
					if (inputLabels.size() != 2) {
						log.warn("unable to construct an intersect with less or more than 2 lines: {}", inputLabels);
						continue;
					}
					Line l1 = lines.get(inputLabels.get(0));
					Line l2 = lines.get(inputLabels.get(1));
					if (l1 == null || l2 == null) {
						log.warn("lines not found: {}", inputLabels);
						continue;
					}
					point = new Point(l1, l2);
					points.put(outputLabel, point);
					log.info("construct an intersect {} by {}: {}", outputLabel, inputLabels, point);
					break;

				case "Prove":
					if (inputLabels.size() != 1) {
						log.warn("unable to prove less or more than 1 statement: {}", inputLabels);
						continue;
					}
					String statement = inputLabels.get(0);
					// TODO parse function name as statement
					if (statement.startsWith("AreCollinear[") && statement.endsWith("]")) {
						String[] args = statement.substring(13, statement.length() - 1).split(",");
						if (args.length != 3) {
							log.warn("AreCollinear should have 3 arguments: {}", statement);
							continue;
						}
						p1 = points.get(args[0].trim());
						p2 = points.get(args[1].trim());
						Point p3 = points.get(args[2].trim());
						if (p1 == null || p2 == null || p3 == null) {
							log.warn("points not found: {}", Arrays.asList(args));
							continue;
						}
						log.info("proving collinear of {} ...", Arrays.asList(args));
						return Point.collinear(p1, p2, p3) ? "true" : "false";
					}
					log.warn("not implemented: {}", statement);
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
