package com.xqbase.math.inequality;

import java.io.InputStream;
import java.util.Properties;
import java.util.TreeMap;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogManager;

import com.xqbase.math.polys.Monom;
import com.xqbase.math.polys.Rational;
import com.xqbase.math.polys.RationalPoly;

public class _4741634 {
	private static final String VARS = "xyz";
	private static final Rational _1 = Rational.valueOf(1);
	// results from 4741634-sage.py, 15 positive real_roots excluding z = 1
	private static final String[][] ROOTS = {
		{"341764768953/140737488355328", "683585359749/281474976710656"},
		{"3941954899263/70368744177664", "7883965620369/140737488355328"},
		{"4534344391113/35184372088832", "18137433386295/140737488355328"},
		{"2143174263706503/9007199254740992", "1071587159764173/4503599627370496"},
		{"9795768552665919/18014398509481984", "78366148477149195/144115188075855872"},
		{"163938432168755415/288230376151711744", "81969216112288629/144115188075855872"},
		{"27656399156659227/36028797018963968", "13828199606240535/18014398509481984"},
		{"224012579530412151/288230376151711744", "1792100636299119051/2305843009213693952"},
		// {"1125885508536879/1125899906842624", "70370283000321/70368744177664"}, // z = 1
		// x0*x1 < 0, try max_interval = 1/2**20
		// {"10146491560867689/9007199254740992", "5073265290167973/4503599627370496"},
		// interval (z0', z1') from 1/2**20 is in interval (z0, z1) from 1/2**10 (z0 < z0' && z1' < z1), so not necessary to prove monotonicity
		{"16733659367247138098161565718810449569301176656904073109775142844241310183716377449974263104787881255286485246563176531377475918989328496131558411616204251551001515673918013120030332429670370887426706762366148172626608015153269012023975295586942105894462686116294017157386676115881627249693363700791070927334466638309175025641478393139847055565398222778303307799075982854517987659007185344616717470116733545459084409421432089160617/14854697210674840878452702602518793472677337256956052728495074709881270198835970389317941523857361850364017022304509376290207720256008405006732948566603224150355570649160734970971317472662883886882710614814271268791126075003240460905443226517895273532178042420821912448438361827154074519143312280745953993790296454424599373510880698854230081208336350999319647310951197954428577986844835456461284763259108363037860909493128802598912", "33467318734494276196323131437620899138602353313808146219550285688482620367432754899948526209575762510572970493126353062754951837978656992263116823232408503102003664820213051097255606464088972686892502699609303737761514568909452483649028891130585828498904127509752213359806972501525485971088450179016171702314177667392551215132197983829759014530149170143968683258414663244578319929693874015251222325332719954401600561605230005930609/29709394421349681756905405205037586945354674513912105456990149419762540397671940778635883047714723700728034044609018752580415440512016810013465897133206448300711141298321469941942634945325767773765421229628542537582252150006480921810886453035790547064356084841643824896876723654308149038286624561491907987580592908849198747021761397708460162416672701998639294621902395908857155973689670912922569526518216726075721818986257605197824"},
		{"17475801291296075579366967849873987356765544066402167481314715811362604803307371/14821387422376473014217086081112052205218558037201992197050570753012880593911808", "33332445700256491812680382193890751194292211713838440733087387133429107397/28269553036454149273332760011886696253239742350009903329945699220681916416"},
		{"1586669345901/1099511627776", "101585857605921/70368744177664"},
		{"32227587257378647666661432214880566702736917/22300745198530623141535718272648361505980416", "4755952434000056264199972156094093083851267563893786949822165911/3291009114642412084309938365114701009965471731267159726697218048"},
		// too slow, try max_interval = 1/30
		// {"5097073613930174266007562445934366605431690365432984793568805262885371503555139794193984678285292137750416620236153530317207779169838423422960376391562002933153595104806658226678562021535036990666551255698247596529421750655430524999454733806916701205617092606275916394569185054143512177555735644240088690517767054098581550322408087595598061784687322790714225879504500528855435518088557259117623483739671786077/3145604489732036216365934499989962674798357010864446456587433354871406554259603910562982278509976061426345669606916919050023073552094798197365051940034013220374740040055081652097235173818950351760556526782295529225647492265166563176224056468193867601341241139932514424678631640619420991797554613959413018797411482860385082575452023629082352121359010494594237996170134006011886429786342857901399557023436111872", "1274268403482543566501890611483591651357922591358246198392201315721342875888784948548496169571323034437604155059038382579301944792459605855740094097890500758176723058064379796112797313502301392280447754785371650970260461615911791093502188318015341316792334956289393090269089072889957867574297518229128698010856170514813253608628174886839389320504552227040325807896510962760968421258982084678535188014664318863/786401122433009054091483624997490668699589252716111614146858338717851638564900977640745569627494015356586417401729229762505768388023699549341262985008503305093685010013770413024308793454737587940139131695573882306411873066291640794056014117048466900335310284983128606169657910154855247949388653489853254699352870715096270643863005907270588030339752623648559499042533501502971607446585714475349889255859027968"},
		{"56977514521695/35184372088832", "890883343593/549755813888"},
		{"4141210728482469/2251799813685248", "2070624873975363/1125899906842624"},
		{"3112143487080470314627049815162167478645162640360062341496209/1606938044258990275541962092341162602522202993782792835301376", "24897147896643762517016445364212659575566375027002952902035281/12855504354071922204335696738729300820177623950262342682411008"},
	};
	private static final Monom CONSTANT = new Monom(VARS, "");

	static {
		java.util.logging.Logger rootLogger = LogManager.getLogManager().getLogger("");
		rootLogger.setLevel(Level.FINE);
		for (Handler h : rootLogger.getHandlers()) {
			h.setLevel(Level.FINE);
		}
	}

	private static RationalPoly solve(RationalPoly f, String var) {
		TreeMap<Monom, RationalPoly> poly = f.coeffsOf(var);
		RationalPoly a1 = poly.remove(new Monom(VARS, var));
		RationalPoly a0 = poly.remove(CONSTANT);
		if (!poly.isEmpty()) {
			throw new RuntimeException("Should be empty: " + poly);
		}
		Rational denominator = a1.remove(new Monom(VARS, "")).negate();
		if (!a1.isEmpty()) {
			throw new RuntimeException("Should be empty: " + a1);
		}
		RationalPoly ret = new RationalPoly(VARS);
		a0.forEach((m, c) -> {
			ret.put(m, c.div(denominator));
		});
		return ret;
	}

	private static Rational subs(RationalPoly f, char from, Rational to) {
		RationalPoly poly = f.subs(from, to);
		Rational ret = poly.remove(CONSTANT);
		if (!poly.isEmpty()) {
			throw new RuntimeException("Should be empty: " + poly);
		}
		return ret;
	}

	private static Rational[] subsInterval(RationalPoly f, char var, Rational to0, Rational to1) {
		Rational x0 = subs(f, var, to0);
		Rational x1 = subs(f, var, to1);
		if (x0.compareTo(x1) > 0) {
			Rational t = x0;
			x0 = x1;
			x1 = t;
		}
		return new Rational[] {x0, x1};
	}

	public static void main(String[] args) throws Exception {
		Properties p = new Properties();
		// results from 4741634-sage.py, B[1] and B[2]
		try (InputStream in = _4741634.class.getResourceAsStream("4741634.properties")) {
			p.load(in);
		}
		RationalPoly f = new RationalPoly(VARS, "-x**4*y*z**2 - x**3*y**3*z**3 - x**3*y**2 - x**2*y**4*z - x**2*z**3 - x*y**2*z**4 - 5*x*y*z + 4*x*y + 4*x*z - y**3*z**2 + 4*y*z");
		RationalPoly b1 = new RationalPoly(VARS, p.getProperty("B1"));
		RationalPoly b2 = new RationalPoly(VARS, p.getProperty("B2"));
		RationalPoly x = solve(b1, "x");
		RationalPoly y = solve(b2, "y");
		System.out.println("x(z = 1) = " + x.subs('z', _1));
		System.out.println("y(z = 1) = " + y.subs('z', _1));
		for (int i = 0; i < ROOTS.length; i++) {
			String[] roots = ROOTS[i];
			Rational z0 = new Rational(roots[0]);
			Rational z1 = new Rational(roots[1]);
			// TODO exists z0' < z0 < z1 < z1' such that z0' and z1''s denominators are not too large
			System.out.println(z0 + " <= z <= " + z1);
			// too slow to prove monotonicity
			/*
			z1.add(z0.negate());
			System.out.print("prove x is monotonic: ");
			RationalPoly x1 = x.subs('z', new RationalPoly(VARS, z1 + "*z + " + z0)).diff('z');
			if (x1.get(CONSTANT).signum() < 0) {
				x1 = new RationalPoly(VARS, "").add(-1, x1);
			}
			System.out.println(Bisection.search01(x1).length == 0);
			System.out.print("prove y is monotonic: ");
			RationalPoly y1 = y.subs('z', new RationalPoly(VARS, z1 + "*z + " + z0)).diff('z');
			if (y1.get(CONSTANT).signum() < 0) {
				y1 = new RationalPoly(VARS, "").add(-1, y1);
			}
			System.out.println(Bisection.search01(y1).length == 0);
			*/
			Rational[] x01 = subsInterval(x, 'z', z0, z1);
			Rational x0 = x01[0], x1 = x01[1];
			Rational[] y01 = subsInterval(y, 'z', z0, z1);
			Rational y0 = y01[0], y1 = y01[1];
			if ((x0.signum() < 0 && x1.signum() < 0) || (y0.signum() < 0 && y1.signum() < 0)) {
				System.out.println("x or y is negative: x = " + x0.doubleValue() + ", y = " + y0.doubleValue());
				continue;
			}
			if ((x0.signum() < 0 && x1.signum() > 0) || (y0.signum() < 0 && y1.signum() > 0)) {
				System.out.println("x0*x1 < 0 or y0*y1 < 0: x = " + x0.doubleValue() + ", y = " + y0.doubleValue());
				break;
			}
			x1.add(x0.negate());
			y1.add(y0.negate());
			z1.add(z0.negate());
			System.out.println("width: [" + x1.doubleValue() + ", " + y1.doubleValue() + ", " + z1.doubleValue() + "]");
			System.out.print("prove positive: ");
			RationalPoly f1 = f.
					subs('x', new RationalPoly(VARS, x1 + "*x + " + x0)).
					subs('y', new RationalPoly(VARS, y1 + "*y + " + y0)).
					subs('z', new RationalPoly(VARS, z1 + "*z + " + z0));
			System.out.println(Bisection.search01(f1).length == 0);
		}
	}
}