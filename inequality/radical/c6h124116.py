from sympy import *

# https://artofproblemsolving.com/community/c6h124116

def main():
    x, y, z, t = symbols('x, y, z, t', positive = True)
    # a**2 - b**2 <= 0 && a + b >= 0 => a - b <= 0
    f = (sqrt(578*x**2 + 1143*y*z) + sqrt(578*y**2 + 1143*z*x))**2 - (253*sqrt(527)*(x + y + z)/140 - sqrt(578*z**2 + 1143*x*y))**2
    # to prove: f1 = sqrt(578*x**2 + 1143*y*z) + sqrt(578*y**2 + 1143*z*x) + 253*sqrt(527)*(x + y + z)/140 - sqrt(578*z**2 + 1143*x*y) >= 0
    f1 = (253*sqrt(527)*(x + y + z)/140)**2 - (sqrt(578*z**2 + 1143*x*y))**2
    print('f1 =', factor(f1))
    print('f =', factor(f))
    # should prove positive:
    g = (22403943*x**2 + 89868286*x*y + 45062686*x*z + 22403943*y**2 + 45062686*y*z + 45061543*z**2)**2 - (70840*sqrt(527)*x*sqrt(1143*x*y + 578*z**2) + 70840*sqrt(527)*y*sqrt(1143*x*y + 578*z**2) + 70840*sqrt(527)*z*sqrt(1143*x*y + 578*z**2) + 39200*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*z + 578*y**2))**2
    # to prove: 22403943*x**2 + 89868286*x*y + 45062686*x*z + 22403943*y**2 + 45062686*y*z + 45061543*z**2 + 70840*sqrt(527)*x*sqrt(1143*x*y + 578*z**2) + 70840*sqrt(527)*y*sqrt(1143*x*y + 578*z**2) + 70840*sqrt(527)*z*sqrt(1143*x*y + 578*z**2) + 39200*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*z + 578*y**2) >= 0, which is obvious
    print('g =', factor(g))
    # should prove positive:
    h = (501936661947249*x**4 + 1003976334581796*x**3*y + 1003976334581796*x**3*z + 2521152155669094*x**2*y**2 + 4072913244850988*x**2*y*z + 2521152155669094*x**2*z**2 + 1003976334581796*x*y**3 + 4072913244850988*x*y**2*z + 4072913244850988*x*y*z**2 + 1003976334581796*x*z**3 + 501936661947249*y**4 + 1003976334581796*y**3*z + 2521152155669094*y**2*z**2 + 1003976334581796*y*z**3 + 501936661947249*z**4)**2 - (5553856000*sqrt(527)*x*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2) + 5553856000*sqrt(527)*y*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2) + 5553856000*sqrt(527)*z*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2))**2
    # to prove: 501936661947249*x**4 + 1003976334581796*x**3*y + 1003976334581796*x**3*z + 2521152155669094*x**2*y**2 + 4072913244850988*x**2*y*z + 2521152155669094*x**2*z**2 + 1003976334581796*x*y**3 + 4072913244850988*x*y**2*z + 4072913244850988*x*y*z**2 + 1003976334581796*x*z**3 + 501936661947249*y**4 + 1003976334581796*y**3*z + 2521152155669094*y**2*z**2 + 1003976334581796*y*z**3 + 501936661947249*z**4 + 5553856000*sqrt(527)*x*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2) + 5553856000*sqrt(527)*y*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2) + 5553856000*sqrt(527)*z*sqrt(578*x**2 + 1143*y*z)*sqrt(1143*x*y + 578*z**2)*sqrt(1143*x*z + 578*y**2) >= 0, which is obvious
    print('h =', factor(h))
    print('Is h cyclic?', h.subs(z, t).subs(y, z).subs(x, y).subs(t, x) == h)
    print('Is h symmetric?', h.subs(y, t).subs(x, y).subs(t, x) == h)
    m = Integer(51)/38
    print('h(m) =', h.subs(x, 1).subs(y, m).subs(z, m))
    u, v = symbols('u, v', positive = True)
    # 1 <= y <= z <= m
    print('h(1yzm) =', factor(h.subs(x, 1).subs(y, 1 + (m - 1)/(1 + u + v)).subs(z, 1 + (m - 1)/(1 + u))))
    # 1 <= y <= m <= z
    print('h(1ymz) =', factor(h.subs(x, 1).subs(y, 1 + (m - 1)/(1 + u)).subs(z, m + v)))
    j = 958341684427867715778131267128412489472*u**8*v**8 + 17957083532325434248700448915320732027904*u**8*v**7 + 123819948021979510847864243783778840627456*u**8*v**6 + 391591587582645102470951665748841829870848*u**8*v**5 + 596401164346194248469576435235778458414240*u**8*v**4 + 418610158508746306616451704884182941698368*u**8*v**3 + 127311588009230033986207325832403952257936*u**8*v**2 + 14162636050669462015445111084943185751984*u**8*v + 951673616555488685243445523279187096167*u**8 + 7666733475422941726225050137027299915776*u**7*v**8 + 144968217763715438724496532293244298667008*u**7*v**7 + 1004062106326872588295888704232270190808576*u**7*v**6 + 3163128469208960524653051832523944945009920*u**7*v**5 + 4729783618063048212231915589943183196332160*u**7*v**4 + 3159238333052829258472236563179643379251904*u**7*v**3 + 860852794650523587982108770354732117874592*u**7*v**2 + 71804976827438789815977190645600159020144*u**7*v + 5664353763134158085770967253644166869920*u**7 + 26833567163980296041787675479595549705216*u**6*v**8 + 511979185440895912107863156423729593887744*u**6*v**7 + 3563051664135073722721880000625045410215680*u**6*v**6 + 11186623864007530285713766080580899877230080*u**6*v**5 + 16427302696618362667213091130232270576098240*u**6*v**4 + 10426143946287395656704217840634073801869504*u**6*v**3 + 2531317207022691363718615221048021238047376*u**6*v**2 + 144337345638044746257225610285536540103360*u**6*v + 17046852469341347763811288990689216092800*u**6 + 53667134327960592083575350959191099410432*u**5*v**8 + 1033139217417575577359976899642208284881920*u**5*v**7 + 7226922841176970589598014866764213529451520*u**5*v**6 + 22623153359935738633929676978320713377057280*u**5*v**5 + 32635603248792078520431044420759376744556160*u**5*v**4 + 19653662644351878354510194834896334710920768*u**5*v**3 + 4244869091164169484967428451431977367022720*u**5*v**2 + 142635408278525807177353468906731140595200*u**5*v + 31809604928677444583092568547597071104000*u**5 + 67083917909950740104469188698988874263040*u**4*v**8 + 1302900079941699163130284358046196727485440*u**4*v**7 + 9163616603760721938167481907710324328400640*u**4*v**6 + 28614494131094200073832091218809213711223040*u**4*v**5 + 40562636554293639087419457995268013485307040*u**4*v**4 + 23146126405320685523917545770577481124908800*u**4*v**3 + 4472654558124080735267968264507081181632000*u**4*v**2 + 67264142973652270045797038558955118080000*u**4*v + 35688659492227454741422328510628881920000*u**4 + 53667134327960592083575350959191099410432*u**3*v**8 + 1051500910489143083648478073231706479094784*u**3*v**7 + 7438014653764968328251671979462228620238336*u**3*v**6 + 23178552687484527045823395847244788016341248*u**3*v**5 + 32296606232801214975808445103315879817203200*u**3*v**4 + 17439582879985017381795850377927639734784000*u**3*v**3 + 3068112510889839788789659848420781250560000*u**3*v**2 + 9628718050590584726531556823039160320000*u**3*v + 21533675563270133306425076720177152000000*u**3 + 26833567163980296041787675479595549705216*u**2*v**8 + 530340878512463418396364330013227788100608*u**2*v**7 + 3774143476723071461375537113323060501002496*u**2*v**6 + 11742002316206920896595360645407990002631680*u**2*v**5 + 16086714788917729098744751794654317631232000*u**2*v**4 + 8209378013103305539077277339785661132800000*u**2*v**3 + 1360548793439779978473781244560452587520000*u**2*v**2 - 1990781820891545760496421143748608000000*u**2*v + 5320628480574614285385812747354112000000*u**2 + 7666733475422941726225050137027299915776*u*v**8 + 152837514794387227133854178117314953329664*u*v**7 + 1094530026007443047718884609674276658288640*u*v**6 + 3401132894901986642879360714523423203123200*u*v**5 + 4582681020684369522998527290313734778880000*u*v**4 + 2207276400199448839737477194237056696320000*u*v**3 + 363459214541839445139902285191233536000000*u*v**2 - 295760315080249161890877589684224000000*u*v + 958341684427867715778131267128412489472*v**8 + 19268633037437398983593389885999174471680*v**7 + 138897934635407920751696894690779918540800*v**6 + 431255512639916488673315762065924120576000*v**5 + 571618916164786129623055048941794385920000*v**4 + 259501734369040808200266314359275520000000*v**3 + 45461464650590195432527299450765312000000*v**2
    w = symbols('w', positive = True)
    # u <= v
    print('j(uv) =', factor(j.subs(v, u*(1 + w))))
    # v <= u
    print('j(vu) =', factor(j.subs(u, v*(1 + w))))
    # 1 <= m <= y <= z
    print('h(1myz) =', factor(h.subs(x, 1).subs(y, m + u).subs(z, m + u + v)))

if __name__ == '__main__':
    main()