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
        depth += 1
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
    # 1e-22, can be proved positive by tsds within 99 iterations (sds 72)
    f = (m*x - n*y)**2 + (x**2 + y**2)/10000000000000000000000
    print(sds(f, tsds = True))
    # 1e-22, can be found negative by tsds within 98 iterations (sds 71)
    f = (m*x - n*y)**2 - (x**2 + y**2)/10000000000000000000000
    non_negative, negative_ats = sds(f, tsds = True)
    print((non_negative, negative_ats))
    for negative_at in negative_ats:
        x0, y0 = negative_at
        print('f({},{}) = {}'.format(x0, y0, f.subs(x, x0).subs(y, y0)))
    # example 2:
    # zero at (3, 1, 3), not on sds or tsds's boundary
    # f = (3*x - y)**2 + (x - z)**2
    # 1e-8, can be proved positive by tsds within 16 iterations
    f = (3*x - y)**2 + (x - z)**2 + (x**2 + y**2 + z**2)/100000000
    print(sds(f, tsds = True))
    # 1e-8, can be found negative by tsds within 11 iterations
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

    # p174, 6-var Vasc's conjuction
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
    print(sds(f, tsds = True))

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
    # sds and tsds don't work
    '''

if __name__ == '__main__':
    main()