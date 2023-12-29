import logging, itertools
from sympy import *

# successive difference substitution
# return (if non_negative, zero_at (non_negative) or negative_at)
# tsds = False (default): Use upper triangular matrix (A_n)
# tsds = True: Use column stochastic matrix (T_n)
# See https://arxiv.org/pdf/0904.4030v3.pdf
def sds(f, tsds = False):
    if not Poly(f).is_homogeneous:
        raise Exception('{} is not homogeneous'.format(f))

    vars = sorted(f.free_symbols, key = str)
    vars_l = len(vars)
    vars_r = range(vars_l)
    vars_r_1 = range(1, vars_l)
    vars_p = list(itertools.permutations(vars_r))
    vars_p01 = list(itertools.product([0, 1], repeat = vars_l))
    # all-zero is trivial
    vars_p01.pop(0)
    temp_vars = [Symbol('sds_temp_' + str(i)) for i in vars_r]

    eye_mat = eye(vars_l)
    upper_mat = zeros(vars_l)
    for i in vars_r:
        for j in range(i, vars_l):
            upper_mat[i, j] = S(1)/(j + 1) if tsds else 1
    poly_trans_list = {f: [eye_mat]}
    zero_at = set()

    for depth in range(100):
        logging.info('depth = {}, polynomials = {}'.format(depth, len(poly_trans_list)))
        poly_list_1 = []
        for f0 in poly_trans_list:
            trans_list = poly_trans_list[f0]
            # find negative or zero: try 0/1 for each var
            for perm in vars_p01:
                f1 = f0
                for i in vars_r:
                    f1 = f1.subs(vars[i], perm[i])
                if f1 <= 0:
                    col = []
                    for i in perm:
                        col.append([i])
                    col = Matrix(col)
                    non_positive_at = set()
                    for trans in trans_list:
                        # TODO reduce
                        non_positive_at.add(tuple(trans*col))
                    if f1 < 0:
                        return False, non_positive_at
                    zero_at.update(non_positive_at)

            # substitute and iterate if there are negative terms
            neg = False
            for coeff in Poly(f0, vars).coeffs():
                if coeff < 0:
                    neg = True
                    break
            if neg:
                poly_list_1.append(f0)
        if len(poly_list_1) == 0:
            return True, zero_at

        # substitution takes much time, so do it after negative check
        poly_trans_list_1 = {}
        for f0 in poly_list_1:
            trans_list = poly_trans_list[f0]
            for perm in vars_p:
                f1 = f0
                for i in vars_r:
                    f1 = f1.subs(vars[i], temp_vars[i])
                trans_1 = zeros(vars_l)
                for i in vars_r:
                    j = perm[i]
                    f1 = f1.subs(temp_vars[i], vars[j])
                    trans_1[i,:] = eye_mat[j,:]
                x = vars[0]
                for i in vars_r_1:
                    y = vars[i]
                    # much faster than f1 = f1.subs(...) ... expand(...)
                    f1 = expand(f1.subs(x, (x/i if tsds else x) + y))
                    x = y
                if tsds:
                    f1 = expand(f1.subs(x, x/vars_l))
                trans_1 *= upper_mat

                # update next poly_trans_list
                trans_list_1 = poly_trans_list_1.get(f1)
                if trans_list_1 == None:
                    trans_list_1 = []
                    poly_trans_list_1[f1] = trans_list_1
                for trans_0 in trans_list:
                    trans_list_1.append(trans_0*trans_1)

        poly_trans_list = poly_trans_list_1
    return None, zero_at

def cyc(f, vars):
    x, y, z = vars
    t = symbols('t', negative = False)
    return f.subs(z, t).subs(y, z).subs(x, y).subs(t, x)

def sum_cyc(f, vars):
    f1 = cyc(f, vars)
    return f + f1 + cyc(f1, vars)

def main():
    logging.basicConfig(level = 'INFO')

    x, y, z = symbols('x, y, z', negative = False)
    # only a trivial zero
    print(sds(x**2 + x*y + y**2))
    # zero at (1, 1)
    print(sds(x**2 - 2*x*y + y**2))
    # negative
    print(sds(x**2 - 3*x*y + y**2))
    # zero at (1, 0, 0) and (1, 1, 1)
    print(sds(x**2*y + y**2*z + z**2*x - 3*x*y*z))
    print()

    '''
    # sds vs tsds
    # example 1:
    m, n = 4660046610375530309, 7540113804746346429 # fibonacci 91, 92
    f = (m*x - n*y)**2
    # zero at (n, m), on sds's boundary but not on tsds's boundary
    print(sds(f))
    # 1e-22, tsds works within 99 iterations (sds 72)
    f = (m*x - n*y)**2 + (x**2 + y**2)/10000000000000000000000
    print(sds(f, tsds = True))
    # 1e-22, tsds finds negative within 98 iterations (sds 71)
    f = (m*x - n*y)**2 - (x**2 + y**2)/10000000000000000000000
    non_negative, negative_ats = sds(f, tsds = True)
    print((non_negative, negative_ats))
    for negative_at in negative_ats:
        x0, y0 = negative_at
        print('f({},{}) = {}'.format(x0, y0, f.subs(x, x0).subs(y, y0)))
    # example 2:
    # zero at (1, 3, 1), not on sds or tsds's boundary
    # f = (3*x - y)**2 + (x - z)**2
    # 1e-8, tsds works within 16 iterations
    f = (3*x - y)**2 + (x - z)**2 + (x**2 + y**2 + z**2)/100000000
    print(sds(f, tsds = True))
    # 1e-8, tsds finds negative within 11 iterations
    f = (3*x - y)**2 + (x - z)**2 - (x**2 + y**2 + z**2)/100000000
    non_negative, negative_ats = sds(f, tsds = True)
    print((non_negative, negative_ats))
    for negative_at in negative_ats:
        x0, y0, z0 = negative_at
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    # sds works for 1/6 but doesn't seem to work for 1/7
    f = (3*x - y)**2 + (x - z)**2 + (x**2 + y**2 + z**2)/6
    print(sds(f))
    # sds finds negative for 1e-22 (maybe smaller), why?
    f = (3*x - y)**2 + (x - z)**2 - (x**2 + y**2 + z**2)/10000000000000000000000
    non_negative, negative_ats = sds(f)
    print((non_negative, negative_ats))
    for negative_at in negative_ats:
        x0, y0, z0 = negative_at
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    print()
    '''

    # ISBN 9787030207210, p169, §7.3.2, problem 5
    a1, a2, a3, a4, a5, a6 = symbols('a1, a2, a3, a4, a5, a6', negative = False)
    '''
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) - S(5)/2
    fn, fd = fraction(cancel(f))
    # depth = 1
    non_neg, zero_ats = sds(fn)
    print('f =', f)
    print('Is f non-negative?', non_neg)
    print('f\'s numerator is zero at:', zero_ats)
    # remove extraneous solutions
    for zero_at in zero_ats:
        z1, z2, z3, z4, z5 = zero_at
        if fd.subs({a1: z1, a2: z2, a3: z3, a4: z4, a5: z5}) != 0:
            print('f is zero at:', zero_at)
    print()

    # p170, §7.3.3
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a1) + a4/(a1 + a2) - 2
    fn, fd = fraction(cancel(f))
    # depth = 1
    non_neg, zero_ats = sds(fn)
    print('f =', f)
    print('Is f non-negative?', non_neg)
    print('f\'s numerator is zero at:', zero_ats)
    # remove extraneous solutions
    for zero_at in zero_ats:
        z1, z2, z3, z4 = zero_at
        if fd.subs({a1: z1, a2: z2, a3: z3, a4: z4}) != 0:
            print('f is zero at:', zero_at)
    # can't find general solution (u, v, u, v)
    print()

    # p171, problem 8
    f = x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6
    # depth = 5
    non_negative, zero_ats = sds(f)
    print((non_negative, zero_ats))
    for zero_ats in zero_ats:
        x0, y0, z0 = zero_ats
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    print()

    # p171, problem 9
    f = 8*x**7 + (8*z + 6*y)*x**6 + 2*y*(31*y - 77*z)*x**5 - y*(69*y**2 - 2*z**2 - 202*y*z)*x**4 \
        + 2*y*(9*y**3 + 57*y*z**2 - 85*y**2*z + 9*z**3)*x**3 + 2*y**2*z*(-13*z**2 - 62*y*z + 27*y**2)*x**2 \
        + 2*y**3*z**2*(-11*z + 27*y)*x + y**3*z**3*(z + 18*y)
    # depth = 18
    non_negative, zero_ats = sds(f)
    print((non_negative, zero_ats))
    for zero_ats in zero_ats:
        x0, y0, z0 = zero_ats
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    print()

    # p172, problem 10
    a, b, c = symbols('a, b, c', negative = False)
    # only a trivial zero
    f = a*(a + b)**5 + b*(c + b)**5 + c*(a + c)**5
    # depth = 4
    print(sds(f.subs(c, -c)))
    # depth = 4
    print(sds(f.subs(c, -c).subs(b, -b)))
    print()

    # p172, problem 11
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    # depth = 46
    non_negative, zero_ats = sds(f)
    print((non_negative, zero_ats))
    for zero_ats in zero_ats:
        x0, y0, z0 = zero_ats
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    print()

    # p174, 6-var Vasc's conjecture
    # see also: https://math.stackexchange.com/a/4693459
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    f = fraction(cancel(f))[0]
    # TODO test if depth = 2 by tsds; sds may not work
    print(sds(f, tsds = True))

    # https://math.stackexchange.com/a/2120874
    # https://math.stackexchange.com/q/1775572
    f = sum_cyc(x**4/(8*x**3 + 5*y**3), (x, y, z)) - (x + y + z)/13
    # depth = 2 (tsds needs 3)
    # https://math.stackexchange.com/q/1777075
    f = sum_cyc(x**3/(13*x**2 + 5*y**2), (x, y, z)) - (x + y + z)/18
    # depth = 5 (tsds needs 4)
    # This is not always non-negative:
    f = sum_cyc(x**3/(8*x**2 + 3*y**2), (x, y, z)) - (x + y + z)/11
    f = fraction(cancel(f))[0]
    # depth = 2, negative
    non_negative, negative_ats = sds(f)
    print((non_negative, negative_ats))
    for negative_at in negative_ats:
        x0, y0, z0 = negative_at
        print('f({},{},{}) = {}'.format(x0, y0, z0, f.subs(x, x0).subs(y, y0).subs(z, z0)))
    # https://math.stackexchange.com/q/3526427
    f = 3 - sum_cyc((x + y)**2*x**2/(x**2 + y**2)**2, (x, y, z))
    # depth = 2
    # https://math.stackexchange.com/q/3757790
    f = sum_cyc((y + z)/x, (x, y, z)) + 1728*x**3*y**3*z**3/((x + y)**2*(y + z)**2*(z + x)**2*(x + y + z)**3) - 4*sum_cyc(x/(y + z), (x, y, z)) - 1
    # depth = 2 (tsds needs 4)
    f = fraction(cancel(f))[0]
    print(sds(f))
    print()

    # https://artofproblemsolving.com/community/c6h124116
    f = 220420308492342014250620007*x**8 + 881771706131270506700660856*x**7*y + 881771706131270506700660856*x**7*z + 3096138123320744208128844996*x**6*y**2 - 5398368991135052102868689208*x**6*y*z + 3096138123320744208128844996*x**6*z**2 - 119918369019191401348647608*x**5*y**3 - 6317290613092581261875578024*x**5*y**2*z - 6317290613092581261875578024*x**5*y*z**2 - 119918369019191401348647608*x**5*z**3 - 3095840712538537114054903510*x**4*y**4 + 6167413358885797384485337960*x**4*y**3*z - 3302116036095801486494237060*x**4*y**2*z**2 + 6167413358885797384485337960*x**4*y*z**3 - 3095840712538537114054903510*x**4*z**4 - 119918369019191401348647608*x**3*y**5 + 6167413358885797384485337960*x**3*y**4*z + 4218636235748732497452371920*x**3*y**3*z**2 + 4218636235748732497452371920*x**3*y**2*z**3 + 6167413358885797384485337960*x**3*y*z**4 - 119918369019191401348647608*x**3*z**5 + 3096138123320744208128844996*x**2*y**6 - 6317290613092581261875578024*x**2*y**5*z - 3302116036095801486494237060*x**2*y**4*z**2 + 4218636235748732497452371920*x**2*y**3*z**3 - 3302116036095801486494237060*x**2*y**2*z**4 - 6317290613092581261875578024*x**2*y*z**5 + 3096138123320744208128844996*x**2*z**6 + 881771706131270506700660856*x*y**7 - 5398368991135052102868689208*x*y**6*z - 6317290613092581261875578024*x*y**5*z**2 + 6167413358885797384485337960*x*y**4*z**3 + 6167413358885797384485337960*x*y**3*z**4 - 6317290613092581261875578024*x*y**2*z**5 - 5398368991135052102868689208*x*y*z**6 + 881771706131270506700660856*x*z**7 + 220420308492342014250620007*y**8 + 881771706131270506700660856*y**7*z + 3096138123320744208128844996*y**6*z**2 - 119918369019191401348647608*y**5*z**3 - 3095840712538537114054903510*y**4*z**4 - 119918369019191401348647608*y**3*z**5 + 3096138123320744208128844996*y**2*z**6 + 881771706131270506700660856*y*z**7 + 220420308492342014250620007*z**8
    # zero at (38, 51, 51), not on sds or tsds's boundary
    # print(sds(f))

    # ISBN 9787542878021, p112, §7.2, ex6
    abcd = (a1 + a2 + a3 + a4)/4
    a, b, c, d = a1/abcd, a2/abcd, a3/abcd, a4/abcd
    f = a/(b**3 + 4) + b/(c**3 + 4) + c/(d**3 + 4) + d/(a**3 + 4) - S(2)/3
    # cancel(f) is too slow, why?
    f = fraction(factor(f))[0]
    # depth = 1, show zero_at more clearly than xiong23_p112.py
    print(sds(f))

    # http://xbna.pku.edu.cn/CN/Y2013/V49/I4/545
    # ex 4.1
    # TODO test if depth = 16 by tsds; sds doesn't work
    f = (3*x + y - z)**2 + z**2/3000000
    print(sds(f, tsds = True))
    # ex 4.2
    a7, a8, a9, a10 = symbols('a7, a8, a9, a10', negative = False)
    f = a1**2 + a2**2 + a3**2 + a4**2 + a5**2 + a6**2 + a7**2 + a8**2 + a9**2 + a10**2 - 4*a1*a2
    print(sds(f))
    # ex 4.3
    f = x**3 + y**3 + z**3 - 3*x*y*z
    print(sds(f))
    # ex 4.4
    a, b, c = symbols('a, b, c', negative = False)
    f = (a**2 + b**2 + c**2)**2 - 3*(a**3*b + b**3*c + c**3*a)
    # sds and tsds don't work
    # ex 4.5
    x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5', negative = False)
    f = (x1**2 + 3*x5**2)*(x2**2 + 3*x5**2)*(x3**2 + 3*x5**2)*(x4**2 + 3*x5**2) - 16*(x1 + x2 + x3 + x4)**2*x5**6
    # equivalent to
    a, b, c, d = x1/x5, x2/x5, x3/x5, x4/x5
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*a**2 # - 81
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b)**2 # - S(704)/9
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b + c)**2 # - 48
    f = (a**2 + 3)*(b**2 + 3)*(c**2 + 3)*(d**2 + 3) - 16*(a + b + c + d)**2
    f = fraction(cancel(f))[0]
    # results from han13-ex5.py
    p, q, r, s, t = symbols('p, q, r, s, t', negative = False)
    g1 = 11*p**2*q**6 + 44*p**2*q**5*r + 22*p**2*q**5*s + 66*p**2*q**5*t + 66*p**2*q**4*r**2 + 66*p**2*q**4*r*s + 220*p**2*q**4*r*t + 11*p**2*q**4*s**2 + 110*p**2*q**4*s*t + 192*p**2*q**4*t**2 + 44*p**2*q**3*r**3 + 66*p**2*q**3*r**2*s + 264*p**2*q**3*r**2*t + 22*p**2*q**3*r*s**2 + 264*p**2*q**3*r*s*t + 512*p**2*q**3*r*t**2 + 44*p**2*q**3*s**2*t + 256*p**2*q**3*s*t**2 + 328*p**2*q**3*t**3 + 11*p**2*q**2*r**4 + 22*p**2*q**2*r**3*s + 132*p**2*q**2*r**3*t + 11*p**2*q**2*r**2*s**2 + 198*p**2*q**2*r**2*s*t + 468*p**2*q**2*r**2*t**2 + 66*p**2*q**2*r*s**2*t + 468*p**2*q**2*r*s*t**2 + 656*p**2*q**2*r*t**3 + 84*p**2*q**2*s**2*t**2 + 328*p**2*q**2*s*t**3 + 336*p**2*q**2*t**4 + 22*p**2*q*r**4*t + 44*p**2*q*r**3*s*t + 168*p**2*q*r**3*t**2 + 22*p**2*q*r**2*s**2*t + 252*p**2*q*r**2*s*t**2 + 408*p**2*q*r**2*t**3 + 84*p**2*q*r*s**2*t**2 + 408*p**2*q*r*s*t**3 + 448*p**2*q*r*t**4 + 80*p**2*q*s**2*t**3 + 224*p**2*q*s*t**4 + 192*p**2*q*t**5 + 20*p**2*r**4*t**2 + 40*p**2*r**3*s*t**2 + 80*p**2*r**3*t**3 + 20*p**2*r**2*s**2*t**2 + 120*p**2*r**2*s*t**3 + 144*p**2*r**2*t**4 + 40*p**2*r*s**2*t**3 + 144*p**2*r*s*t**4 + 128*p**2*r*t**5 + 32*p**2*s**2*t**4 + 64*p**2*s*t**5 + 48*p**2*t**6 + 22*p*q**6*t + 88*p*q**5*r*t + 44*p*q**5*s*t + 36*p*q**5*t**2 + 132*p*q**4*r**2*t + 132*p*q**4*r*s*t + 120*p*q**4*r*t**2 + 22*p*q**4*s**2*t + 60*p*q**4*s*t**2 - 96*p*q**4*t**3 + 88*p*q**3*r**3*t + 132*p*q**3*r**2*s*t + 144*p*q**3*r**2*t**2 + 44*p*q**3*r*s**2*t + 144*p*q**3*r*s*t**2 - 256*p*q**3*r*t**3 + 24*p*q**3*s**2*t**2 - 128*p*q**3*s*t**3 - 304*p*q**3*t**4 + 22*p*q**2*r**4*t + 44*p*q**2*r**3*s*t + 72*p*q**2*r**3*t**2 + 22*p*q**2*r**2*s**2*t + 108*p*q**2*r**2*s*t**2 - 216*p*q**2*r**2*t**3 + 36*p*q**2*r*s**2*t**2 - 216*p*q**2*r*s*t**3 - 608*p*q**2*r*t**4 - 24*p*q**2*s**2*t**3 - 304*p*q**2*s*t**4 - 288*p*q**2*t**5 + 12*p*q*r**4*t**2 + 24*p*q*r**3*s*t**2 - 48*p*q*r**3*t**3 + 12*p*q*r**2*s**2*t**2 - 72*p*q*r**2*s*t**3 - 336*p*q*r**2*t**4 - 24*p*q*r*s**2*t**3 - 336*p*q*r*s*t**4 - 384*p*q*r*t**5 - 32*p*q*s**2*t**4 - 192*p*q*s*t**5 - 96*p*q*t**6 + 8*p*r**4*t**3 + 16*p*r**3*s*t**3 - 32*p*r**3*t**4 + 8*p*r**2*s**2*t**3 - 48*p*r**2*s*t**4 - 96*p*r**2*t**5 - 16*p*r*s**2*t**4 - 96*p*r*s*t**5 - 64*p*r*t**6 - 32*p*s*t**6 + 92*q**6*t**2 + 368*q**5*r*t**2 + 184*q**5*s*t**2 + 456*q**5*t**3 + 552*q**4*r**2*t**2 + 552*q**4*r*s*t**2 + 1520*q**4*r*t**3 + 92*q**4*s**2*t**2 + 760*q**4*s*t**3 + 864*q**4*t**4 + 368*q**3*r**3*t**2 + 552*q**3*r**2*s*t**2 + 1824*q**3*r**2*t**3 + 184*q**3*r*s**2*t**2 + 1824*q**3*r*s*t**3 + 2304*q**3*r*t**4 + 304*q**3*s**2*t**3 + 1152*q**3*s*t**4 + 736*q**3*t**5 + 92*q**2*r**4*t**2 + 184*q**2*r**3*s*t**2 + 912*q**2*r**3*t**3 + 92*q**2*r**2*s**2*t**2 + 1368*q**2*r**2*s*t**3 + 2096*q**2*r**2*t**4 + 456*q**2*r*s**2*t**3 + 2096*q**2*r*s*t**4 + 1472*q**2*r*t**5 + 368*q**2*s**2*t**4 + 736*q**2*s*t**5 + 240*q**2*t**6 + 152*q*r**4*t**3 + 304*q*r**3*s*t**3 + 736*q*r**3*t**4 + 152*q*r**2*s**2*t**3 + 1104*q*r**2*s*t**4 + 928*q*r**2*t**5 + 368*q*r*s**2*t**4 + 928*q*r*s*t**5 + 320*q*r*t**6 + 192*q*s**2*t**5 + 160*q*s*t**6 + 80*r**4*t**4 + 160*r**3*s*t**4 + 192*r**3*t**5 + 80*r**2*s**2*t**4 + 288*r**2*s*t**5 + 128*r**2*t**6 + 96*r*s**2*t**5 + 128*r*s*t**6 + 48*s**2*t**6
    # depth = 2 (sds needs 4)
    print(sds(g1, tsds = True))
    g2 = 9*p**4*r**4 + 18*p**4*r**3*s + 36*p**4*r**3*t + 9*p**4*r**2*s**2 + 54*p**4*r**2*s*t + 60*p**4*r**2*t**2 + 18*p**4*r*s**2*t + 60*p**4*r*s*t**2 + 48*p**4*r*t**3 + 12*p**4*s**2*t**2 + 24*p**4*s*t**3 + 16*p**4*t**4 + 18*p**3*q*r**4 + 36*p**3*q*r**3*s + 72*p**3*q*r**3*t + 18*p**3*q*r**2*s**2 + 108*p**3*q*r**2*s*t + 120*p**3*q*r**2*t**2 + 36*p**3*q*r*s**2*t + 120*p**3*q*r*s*t**2 + 96*p**3*q*r*t**3 + 24*p**3*q*s**2*t**2 + 48*p**3*q*s*t**3 + 32*p**3*q*t**4 + 36*p**3*r**4*t + 72*p**3*r**3*s*t + 144*p**3*r**3*t**2 + 36*p**3*r**2*s**2*t + 216*p**3*r**2*s*t**2 + 240*p**3*r**2*t**3 + 72*p**3*r*s**2*t**2 + 240*p**3*r*s*t**3 + 192*p**3*r*t**4 + 48*p**3*s**2*t**3 + 96*p**3*s*t**4 + 64*p**3*t**5 + 9*p**2*q**2*r**4 + 18*p**2*q**2*r**3*s + 36*p**2*q**2*r**3*t + 9*p**2*q**2*r**2*s**2 + 54*p**2*q**2*r**2*s*t + 60*p**2*q**2*r**2*t**2 + 18*p**2*q**2*r*s**2*t + 60*p**2*q**2*r*s*t**2 + 48*p**2*q**2*r*t**3 + 12*p**2*q**2*s**2*t**2 + 24*p**2*q**2*s*t**3 + 16*p**2*q**2*t**4 + 54*p**2*q*r**4*t + 108*p**2*q*r**3*s*t + 216*p**2*q*r**3*t**2 + 54*p**2*q*r**2*s**2*t + 324*p**2*q*r**2*s*t**2 + 360*p**2*q*r**2*t**3 + 108*p**2*q*r*s**2*t**2 + 360*p**2*q*r*s*t**3 + 288*p**2*q*r*t**4 + 72*p**2*q*s**2*t**3 + 144*p**2*q*s*t**4 + 96*p**2*q*t**5 + 44*p**2*r**4*t**2 + 88*p**2*r**3*s*t**2 + 176*p**2*r**3*t**3 + 44*p**2*r**2*s**2*t**2 + 264*p**2*r**2*s*t**3 + 336*p**2*r**2*t**4 + 88*p**2*r*s**2*t**3 + 336*p**2*r*s*t**4 + 320*p**2*r*t**5 + 80*p**2*s**2*t**4 + 160*p**2*s*t**5 + 128*p**2*t**6 + 18*p*q**2*r**4*t + 36*p*q**2*r**3*s*t + 72*p*q**2*r**3*t**2 + 18*p*q**2*r**2*s**2*t + 108*p*q**2*r**2*s*t**2 + 120*p*q**2*r**2*t**3 + 36*p*q**2*r*s**2*t**2 + 120*p*q**2*r*s*t**3 + 96*p*q**2*r*t**4 + 24*p*q**2*s**2*t**3 + 48*p*q**2*s*t**4 + 32*p*q**2*t**5 + 44*p*q*r**4*t**2 + 88*p*q*r**3*s*t**2 + 176*p*q*r**3*t**3 + 44*p*q*r**2*s**2*t**2 + 264*p*q*r**2*s*t**3 + 336*p*q*r**2*t**4 + 88*p*q*r*s**2*t**3 + 336*p*q*r*s*t**4 + 320*p*q*r*t**5 + 80*p*q*s**2*t**4 + 160*p*q*s*t**5 + 128*p*q*t**6 + 16*p*r**4*t**3 + 32*p*r**3*s*t**3 - 64*p*r**3*t**4 + 16*p*r**2*s**2*t**3 - 96*p*r**2*s*t**4 - 192*p*r**2*t**5 - 32*p*r*s**2*t**4 - 192*p*r*s*t**5 - 128*p*r*t**6 - 64*p*s*t**6 + 20*q**2*r**4*t**2 + 40*q**2*r**3*s*t**2 + 80*q**2*r**3*t**3 + 20*q**2*r**2*s**2*t**2 + 120*q**2*r**2*s*t**3 + 144*q**2*r**2*t**4 + 40*q**2*r*s**2*t**3 + 144*q**2*r*s*t**4 + 128*q**2*r*t**5 + 32*q**2*s**2*t**4 + 64*q**2*s*t**5 + 48*q**2*t**6 + 8*q*r**4*t**3 + 16*q*r**3*s*t**3 - 32*q*r**3*t**4 + 8*q*r**2*s**2*t**3 - 48*q*r**2*s*t**4 - 96*q*r**2*t**5 - 16*q*r*s**2*t**4 - 96*q*r*s*t**5 - 64*q*r*t**6 - 32*q*s*t**6 + 80*r**4*t**4 + 160*r**3*s*t**4 + 192*r**3*t**5 + 80*r**2*s**2*t**4 + 288*r**2*s*t**5 + 128*r**2*t**6 + 96*r*s**2*t**5 + 128*r*s*t**6 + 48*s**2*t**6
    # depth = 1
    print(sds(g2, tsds = True))
    g3 = 3*p**6*s**2 + 6*p**6*s*t + 4*p**6*t**2 + 12*p**5*q*s**2 + 24*p**5*q*s*t + 16*p**5*q*t**2 + 6*p**5*r*s**2 + 12*p**5*r*s*t + 8*p**5*r*t**2 + 18*p**5*s**2*t + 36*p**5*s*t**2 + 24*p**5*t**3 + 18*p**4*q**2*s**2 + 36*p**4*q**2*s*t + 24*p**4*q**2*t**2 + 18*p**4*q*r*s**2 + 36*p**4*q*r*s*t + 24*p**4*q*r*t**2 + 60*p**4*q*s**2*t + 120*p**4*q*s*t**2 + 80*p**4*q*t**3 + 3*p**4*r**2*s**2 + 6*p**4*r**2*s*t + 4*p**4*r**2*t**2 + 30*p**4*r*s**2*t + 60*p**4*r*s*t**2 + 40*p**4*r*t**3 + 72*p**4*s**2*t**2 + 144*p**4*s*t**3 + 96*p**4*t**4 + 12*p**3*q**3*s**2 + 24*p**3*q**3*s*t + 16*p**3*q**3*t**2 + 18*p**3*q**2*r*s**2 + 36*p**3*q**2*r*s*t + 24*p**3*q**2*r*t**2 + 72*p**3*q**2*s**2*t + 144*p**3*q**2*s*t**2 + 96*p**3*q**2*t**3 + 6*p**3*q*r**2*s**2 + 12*p**3*q*r**2*s*t + 8*p**3*q*r**2*t**2 + 72*p**3*q*r*s**2*t + 144*p**3*q*r*s*t**2 + 96*p**3*q*r*t**3 + 192*p**3*q*s**2*t**2 + 384*p**3*q*s*t**3 + 256*p**3*q*t**4 + 12*p**3*r**2*s**2*t + 24*p**3*r**2*s*t**2 + 16*p**3*r**2*t**3 + 96*p**3*r*s**2*t**2 + 192*p**3*r*s*t**3 + 128*p**3*r*t**4 + 168*p**3*s**2*t**3 + 336*p**3*s*t**4 + 224*p**3*t**5 + 3*p**2*q**4*s**2 + 6*p**2*q**4*s*t + 4*p**2*q**4*t**2 + 6*p**2*q**3*r*s**2 + 12*p**2*q**3*r*s*t + 8*p**2*q**3*r*t**2 + 36*p**2*q**3*s**2*t + 72*p**2*q**3*s*t**2 + 48*p**2*q**3*t**3 + 3*p**2*q**2*r**2*s**2 + 6*p**2*q**2*r**2*s*t + 4*p**2*q**2*r**2*t**2 + 54*p**2*q**2*r*s**2*t + 108*p**2*q**2*r*s*t**2 + 72*p**2*q**2*r*t**3 + 180*p**2*q**2*s**2*t**2 + 360*p**2*q**2*s*t**3 + 240*p**2*q**2*t**4 + 18*p**2*q*r**2*s**2*t + 36*p**2*q*r**2*s*t**2 + 24*p**2*q*r**2*t**3 + 180*p**2*q*r*s**2*t**2 + 360*p**2*q*r*s*t**3 + 240*p**2*q*r*t**4 + 336*p**2*q*s**2*t**3 + 672*p**2*q*s*t**4 + 448*p**2*q*t**5 + 36*p**2*r**2*s**2*t**2 + 72*p**2*r**2*s*t**3 + 48*p**2*r**2*t**4 + 168*p**2*r*s**2*t**3 + 336*p**2*r*s*t**4 + 224*p**2*r*t**5 + 144*p**2*s**2*t**4 + 288*p**2*s*t**5 + 240*p**2*t**6 + 6*p*q**4*s**2*t + 12*p*q**4*s*t**2 + 8*p*q**4*t**3 + 12*p*q**3*r*s**2*t + 24*p*q**3*r*s*t**2 + 16*p*q**3*r*t**3 + 72*p*q**3*s**2*t**2 + 144*p*q**3*s*t**3 + 96*p*q**3*t**4 + 6*p*q**2*r**2*s**2*t + 12*p*q**2*r**2*s*t**2 + 8*p*q**2*r**2*t**3 + 108*p*q**2*r*s**2*t**2 + 216*p*q**2*r*s*t**3 + 144*p*q**2*r*t**4 + 216*p*q**2*s**2*t**3 + 432*p*q**2*s*t**4 + 288*p*q**2*t**5 + 36*p*q*r**2*s**2*t**2 + 72*p*q*r**2*s*t**3 + 48*p*q*r**2*t**4 + 216*p*q*r*s**2*t**3 + 432*p*q*r*s*t**4 + 288*p*q*r*t**5 + 192*p*q*s**2*t**4 + 384*p*q*s*t**5 + 320*p*q*t**6 + 48*p*r**2*s**2*t**3 + 96*p*r**2*s*t**4 + 64*p*r**2*t**5 + 96*p*r*s**2*t**4 + 192*p*r*s*t**5 + 160*p*r*t**6 - 96*p*s*t**6 + 12*q**4*s**2*t**2 + 24*q**4*s*t**3 + 16*q**4*t**4 + 24*q**3*r*s**2*t**2 + 48*q**3*r*s*t**3 + 32*q**3*r*t**4 + 48*q**3*s**2*t**3 + 96*q**3*s*t**4 + 64*q**3*t**5 + 12*q**2*r**2*s**2*t**2 + 24*q**2*r**2*s*t**3 + 16*q**2*r**2*t**4 + 72*q**2*r*s**2*t**3 + 144*q**2*r*s*t**4 + 96*q**2*r*t**5 + 80*q**2*s**2*t**4 + 160*q**2*s*t**5 + 128*q**2*t**6 + 24*q*r**2*s**2*t**3 + 48*q*r**2*s*t**4 + 32*q*r**2*t**5 + 80*q*r*s**2*t**4 + 160*q*r*s*t**5 + 128*q*r*t**6 - 64*q*s*t**6 + 32*r**2*s**2*t**4 + 64*r**2*s*t**5 + 48*r**2*t**6 - 32*r*s*t**6 + 48*s**2*t**6
    # depth = 2 (sds needs 4)
    print(sds(g3, tsds = True))

    # ISBN 9787560349800, p301, ex 12.9 (p147, ex 6.44; p335, ex 14.29)
    a, b, c = symbols('a, b, c', negative = False)
    # f2 from han14-p301.py
    f = 81*a**6*b**2 + 162*a**6*b*c + 81*a**6*c**2 - 412*a**5*b**3 + 1100*a**5*b**2*c + 2124*a**5*b*c**2 + 612*a**5*c**3 + 294*a**4*b**4 + 4314*a**4*b**3*c + 9320*a**4*b**2*c**2 + 5338*a**4*b*c**3 + 294*a**4*c**4 + 612*a**3*b**5 + 5338*a**3*b**4*c + 16090*a**3*b**3*c**2 + 16090*a**3*b**2*c**3 + 4314*a**3*b*c**4 - 412*a**3*c**5 + 81*a**2*b**6 + 2124*a**2*b**5*c + 9320*a**2*b**4*c**2 + 16090*a**2*b**3*c**3 + 9320*a**2*b**2*c**4 + 1100*a**2*b*c**5 + 81*a**2*c**6 + 162*a*b**6*c + 1100*a*b**5*c**2 + 4314*a*b**4*c**3 + 5338*a*b**3*c**4 + 2124*a*b**2*c**5 + 162*a*b*c**6 + 81*b**6*c**2 - 412*b**5*c**3 + 294*b**4*c**4 + 612*b**3*c**5 + 81*b**2*c**6
    # depth = 3, zero at (3, 1, 0)
    print(sds(f))
    # f3 from han14-p301.py
    f = 6561*a**12*b**4 + 26244*a**12*b**3*c + 39366*a**12*b**2*c**2 + 26244*a**12*b*c**3 + 6561*a**12*c**4 - 66744*a**11*b**5 + 44712*a**11*b**4*c + 633744*a**11*b**3*c**2 + 965520*a**11*b**2*c**3 + 542376*a**11*b*c**4 + 99144*a**11*c**5 + 217372*a**10*b**6 - 112276*a**10*b**5*c + 2415028*a**10*b**4*c**2 + 8751816*a**10*b**3*c**3 + 9144756*a**10*b**2*c**4 + 3559788*a**10*b*c**5 + 422172*a**10*c**6 - 143112*a**9*b**7 - 1844892*a**9*b**6*c + 941668*a**9*b**5*c**2 + 23814912*a**9*b**4*c**3 + 45230848*a**9*b**3*c**4 + 32114276*a**9*b**2*c**5 + 8348004*a**9*b*c**6 + 293112*a**9*c**7 - 404730*a**8*b**8 - 145148*a**8*b**7*c + 1172710*a**8*b**6*c**2 + 30229204*a**8*b**5*c**3 + 90765272*a**8*b**4*c**4 + 100858580*a**8*b**3*c**5 + 46752998*a**8*b**2*c**6 + 6873348*a**8*b*c**7 - 404730*a**8*c**8 + 293112*a**7*b**9 + 6873348*a**7*b**8*c + 25171160*a**7*b**7*c**2 + 55499920*a**7*b**6*c**3 + 118778844*a**7*b**5*c**4 + 161741788*a**7*b**4*c**5 + 105045136*a**7*b**3*c**6 + 25171160*a**7*b**2*c**7 - 145148*a**7*b*c**8 - 143112*a**7*c**9 + 422172*a**6*b**10 + 8348004*a**6*b**9*c + 46752998*a**6*b**8*c**2 + 105045136*a**6*b**7*c**3 + 157443246*a**6*b**6*c**4 + 196665720*a**6*b**5*c**5 + 157443246*a**6*b**4*c**6 + 55499920*a**6*b**3*c**7 + 1172710*a**6*b**2*c**8 - 1844892*a**6*b*c**9 + 217372*a**6*c**10 + 99144*a**5*b**11 + 3559788*a**5*b**10*c + 32114276*a**5*b**9*c**2 + 100858580*a**5*b**8*c**3 + 161741788*a**5*b**7*c**4 + 196665720*a**5*b**6*c**5 + 196665720*a**5*b**5*c**6 + 118778844*a**5*b**4*c**7 + 30229204*a**5*b**3*c**8 + 941668*a**5*b**2*c**9 - 112276*a**5*b*c**10 - 66744*a**5*c**11 + 6561*a**4*b**12 + 542376*a**4*b**11*c + 9144756*a**4*b**10*c**2 + 45230848*a**4*b**9*c**3 + 90765272*a**4*b**8*c**4 + 118778844*a**4*b**7*c**5 + 157443246*a**4*b**6*c**6 + 161741788*a**4*b**5*c**7 + 90765272*a**4*b**4*c**8 + 23814912*a**4*b**3*c**9 + 2415028*a**4*b**2*c**10 + 44712*a**4*b*c**11 + 6561*a**4*c**12 + 26244*a**3*b**12*c + 965520*a**3*b**11*c**2 + 8751816*a**3*b**10*c**3 + 23814912*a**3*b**9*c**4 + 30229204*a**3*b**8*c**5 + 55499920*a**3*b**7*c**6 + 105045136*a**3*b**6*c**7 + 100858580*a**3*b**5*c**8 + 45230848*a**3*b**4*c**9 + 8751816*a**3*b**3*c**10 + 633744*a**3*b**2*c**11 + 26244*a**3*b*c**12 + 39366*a**2*b**12*c**2 + 633744*a**2*b**11*c**3 + 2415028*a**2*b**10*c**4 + 941668*a**2*b**9*c**5 + 1172710*a**2*b**8*c**6 + 25171160*a**2*b**7*c**7 + 46752998*a**2*b**6*c**8 + 32114276*a**2*b**5*c**9 + 9144756*a**2*b**4*c**10 + 965520*a**2*b**3*c**11 + 39366*a**2*b**2*c**12 + 26244*a*b**12*c**3 + 44712*a*b**11*c**4 - 112276*a*b**10*c**5 - 1844892*a*b**9*c**6 - 145148*a*b**8*c**7 + 6873348*a*b**7*c**8 + 8348004*a*b**6*c**9 + 3559788*a*b**5*c**10 + 542376*a*b**4*c**11 + 26244*a*b**3*c**12 + 6561*b**12*c**4 - 66744*b**11*c**5 + 217372*b**10*c**6 - 143112*b**9*c**7 - 404730*b**8*c**8 + 293112*b**7*c**9 + 422172*b**6*c**10 + 99144*b**5*c**11 + 6561*b**4*c**12
    # depth = 3, zero at (3, 1, 0)
    print(sds(f))
    # f3 from han14-p301.py, p302
    u, v, w = symbols('u, v, w', negative = False)
    f = u**16 + 100*u**15*v + 84*u**15*w + 1570*u**14*v**2 + 2252*u**14*v*w + 746*u**14*w**2 + 11092*u**13*v**3 + 24064*u**13*v**2*w + 15336*u**13*v*w**2 + 2412*u**13*w**3 + 44619*u**12*v**4 + 134508*u**12*v**3*w + 133150*u**12*v**2*w**2 + 45604*u**12*v*w**3 + 1955*u**12*w**4 + 112268*u**11*v**5 + 443976*u**11*v**4*w + 614400*u**11*v**3*w**2 + 343744*u**11*v**2*w**3 + 55192*u**11*v*w**4 - 5876*u**11*w**5 + 182940*u**10*v**6 + 914032*u**10*v**5*w + 1651578*u**10*v**4*w**2 + 1301492*u**10*v**3*w**3 + 389122*u**10*v**2*w**4 - 1552*u**10*v*w**5 - 8708*u**10*w**6 + 191208*u**9*v**7 + 1183380*u**9*v**6*w + 2655284*u**9*v**5*w**2 + 2636292*u**9*v**4*w**3 + 1042044*u**9*v**3*w**4 + 49100*u**9*v**2*w**5 + 10564*u**9*v*w**6 + 30248*u**9*w**7 + 118413*u**8*v**8 + 917972*u**8*v**7*w + 2444248*u**8*v**6*w**2 + 2615728*u**8*v**5*w**3 + 605604*u**8*v**4*w**4 - 614856*u**8*v**3*w**5 - 16976*u**8*v**2*w**6 + 352132*u**8*v*w**7 + 118413*u**8*w**8 + 30248*u**7*v**9 + 352132*u**7*v**8*w + 1034596*u**7*v**7*w**2 + 419556*u**7*v**6*w**3 - 2502520*u**7*v**5*w**4 - 3924376*u**7*v**4*w**5 - 1407260*u**7*v**3*w**6 + 1034596*u**7*v**2*w**7 + 917972*u**7*v*w**8 + 191208*u**7*w**9 - 8708*u**6*v**10 + 10564*u**6*v**9*w - 16976*u**6*v**8*w**2 - 1407260*u**6*v**7*w**3 - 5548262*u**6*v**6*w**4 - 8702220*u**6*v**5*w**5 - 5548262*u**6*v**4*w**6 + 419556*u**6*v**3*w**7 + 2444248*u**6*v**2*w**8 + 1183380*u**6*v*w**9 + 182940*u**6*w**10 - 5876*u**5*v**11 - 1552*u**5*v**10*w + 49100*u**5*v**9*w**2 - 614856*u**5*v**8*w**3 - 3924376*u**5*v**7*w**4 - 8702220*u**5*v**6*w**5 - 8702220*u**5*v**5*w**6 - 2502520*u**5*v**4*w**7 + 2615728*u**5*v**3*w**8 + 2655284*u**5*v**2*w**9 + 914032*u**5*v*w**10 + 112268*u**5*w**11 + 1955*u**4*v**12 + 55192*u**4*v**11*w + 389122*u**4*v**10*w**2 + 1042044*u**4*v**9*w**3 + 605604*u**4*v**8*w**4 - 2502520*u**4*v**7*w**5 - 5548262*u**4*v**6*w**6 - 3924376*u**4*v**5*w**7 + 605604*u**4*v**4*w**8 + 2636292*u**4*v**3*w**9 + 1651578*u**4*v**2*w**10 + 443976*u**4*v*w**11 + 44619*u**4*w**12 + 2412*u**3*v**13 + 45604*u**3*v**12*w + 343744*u**3*v**11*w**2 + 1301492*u**3*v**10*w**3 + 2636292*u**3*v**9*w**4 + 2615728*u**3*v**8*w**5 + 419556*u**3*v**7*w**6 - 1407260*u**3*v**6*w**7 - 614856*u**3*v**5*w**8 + 1042044*u**3*v**4*w**9 + 1301492*u**3*v**3*w**10 + 614400*u**3*v**2*w**11 + 134508*u**3*v*w**12 + 11092*u**3*w**13 + 746*u**2*v**14 + 15336*u**2*v**13*w + 133150*u**2*v**12*w**2 + 614400*u**2*v**11*w**3 + 1651578*u**2*v**10*w**4 + 2655284*u**2*v**9*w**5 + 2444248*u**2*v**8*w**6 + 1034596*u**2*v**7*w**7 - 16976*u**2*v**6*w**8 + 49100*u**2*v**5*w**9 + 389122*u**2*v**4*w**10 + 343744*u**2*v**3*w**11 + 133150*u**2*v**2*w**12 + 24064*u**2*v*w**13 + 1570*u**2*w**14 + 84*u*v**15 + 2252*u*v**14*w + 24064*u*v**13*w**2 + 134508*u*v**12*w**3 + 443976*u*v**11*w**4 + 914032*u*v**10*w**5 + 1183380*u*v**9*w**6 + 917972*u*v**8*w**7 + 352132*u*v**7*w**8 + 10564*u*v**6*w**9 - 1552*u*v**5*w**10 + 55192*u*v**4*w**11 + 45604*u*v**3*w**12 + 15336*u*v**2*w**13 + 2252*u*v*w**14 + 100*u*w**15 + v**16 + 100*v**15*w + 1570*v**14*w**2 + 11092*v**13*w**3 + 44619*v**12*w**4 + 112268*v**11*w**5 + 182940*v**10*w**6 + 191208*v**9*w**7 + 118413*v**8*w**8 + 30248*v**7*w**9 - 8708*v**6*w**10 - 5876*v**5*w**11 + 1955*v**4*w**12 + 2412*v**3*w**13 + 746*v**2*w**14 + 84*v*w**15 + w**16
    print(sds(f))
    '''

if __name__ == '__main__':
    main()