import logging, itertools
from sympy import *

# successive difference substitution
# return (if non_negative, zero_at (non_negative) or negative_at)
def sds(f, vars):
    deg = Poly(f).homogeneous_order()
    if deg == None:
        raise Exception('{} is not homogeneous'.format(f))

    vars_l = len(vars)
    vars_r = range(vars_l)
    vars_r_1 = range(1, vars_l)
    vars_p = list(itertools.permutations(vars_r))
    vars_p01 = list(itertools.product([0, 1], repeat = vars_l))
    # all-zero is trivial
    vars_p01.pop(0)
    t_vars = []
    for i in vars_r:
        t_vars.append(Symbol('sds_t' + str(i)))

    eye_mat = eye(vars_l)
    upper_mat = zeros(vars_l)
    for i in vars_r:
        for j in range(i, vars_l):
            upper_mat[i, j] = S(1)/(j + 1)
    poly_trans_list = {f: [eye_mat]}
    zero_at = set()

    for depth in range(1000):
        logging.info('depth = {}, polynomials = {}'.format(depth, len(poly_trans_list)))
        poly_trans_list_1 = {}
        for f0 in poly_trans_list:
            p = Poly(f0, vars)
            neg = False
            for coeff in p.coeffs():
                if coeff < 0:
                    neg = True
                    break
            trans_list = poly_trans_list[f0]
            if not neg:
                # find zero: try 0/1 for each var
                # so this approach can't find all non-trivial general solutions
                for perm in vars_p01:
                    f1 = f0
                    for i in vars_r:
                        f1 = f1.subs(vars[i], perm[i])
                    if f1 == 0:
                        col = []
                        for i in perm:
                            col.append([i])
                        col = Matrix(col)
                        for trans in trans_list:
                            zero_at.add(tuple(trans*col))
                continue

            # there is negative term
            # if a*x**deg < 0: the polynomial is negative
            for i in vars_r:
                if p.coeff_monomial(vars[i]**deg) < 0:
                    negative_at = set()
                    # [[0]]*vars_l doesn't work ([0] is a shallow copy)
                    col = [[0] for _ in vars_r]
                    col[i][0] = 1
                    col = Matrix(col)
                    for trans in trans_list:
                        negative_at.add(tuple(trans*col))
                    return False, negative_at

            # else: iterate
            for perm in vars_p:
                f1 = f0
                for i in vars_r:
                    f1 = f1.subs(vars[i], t_vars[i])
                trans_1 = zeros(vars_l)
                for i in vars_r:
                    j = perm[i]
                    f1 = f1.subs(t_vars[i], vars[j])
                    trans_1[i,:] = eye_mat[j,:]
                x = vars[0]
                for i in vars_r_1:
                    y = vars[i]
                    # much faster than f1 = f1.subs(...) ... expand(...)
                    f1 = expand(f1.subs(x, x/i + y))
                    x = y
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
        if len(poly_trans_list) == 0:
            return True, zero_at
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
    print(sds(x**2 + x*y + y**2, [x, y]))
    # zero at (0, 0, 1)
    print(sds(x**2 + x*y + y**2, [x, y, z]))
    # zero at (1, 1)
    print(sds(x**2 - 2*x*y + y**2, [x, y]))
    # negative
    print(sds(x**2 - 3*x*y + y**2, [x, y]))
    f = x**2*y + y**2*z + z**2*x - 3*x*y*z
    # zero at (1, 0, 0) and (1, 1, 1)
    print(sds(f, [x, y, z]))
    m, n = 4660046610375530309, 7540113804746346429 # fibonacci 91, 92
    f = (m*x - n*y)**2
    # zero at (n, m)
    print(sds(f, [x, y]))
    # TODO why doesn't work?
    f = (3*x - y)**2 + (x - z)**2
    # zero at (3, 1, 3)
    print(sds(f, [x, y, z]))

    # ISBN 9787030207210, p169, §7.3.2, problem 5
    a1, a2, a3, a4, a5, a6 = symbols('a1, a2, a3, a4, a5, a6', negative = False)
    '''
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a5) + a4/(a5 + a1) + a5/(a1 + a2) - S(5)/2
    fn, fd = fraction(cancel(f))
    # depth = 1
    non_neg, zero_ats = sds(fn, [a1, a2, a3, a4, a5])
    print('f =', f)
    print('Is f non-negative?', non_neg)
    print('f\'s numerator is zero at:', zero_ats)
    # remove extraneous solutions
    for zero_at in zero_ats:
        z1, z2, z3, z4, z5 = zero_at
        if fd.subs({a1: z1, a2: z2, a3: z3, a4: z4, a5: z5}) != 0:
            print('f is zero at:', zero_at)

    # p170, §7.3.3
    f = a1/(a2 + a3) + a2/(a3 + a4) + a3/(a4 + a1) + a4/(a1 + a2) - 2
    fn, fd = fraction(cancel(f))
    # depth = 1
    non_neg, zero_ats = sds(fn, [a1, a2, a3, a4])
    print('f =', f)
    print('Is f non-negative?', non_neg)
    print('f\'s numerator is zero at:', zero_ats)
    # remove extraneous solutions
    for zero_at in zero_ats:
        z1, z2, z3, z4 = zero_at
        if fd.subs({a1: z1, a2: z2, a3: z3, a4: z4}) != 0:
            print('f is zero at:', zero_at)
    # can't find general solution (u, v, u, v)

    # p171, problem 8
    f = x**4*y**2 - 2*x**4*y*z + x**4*z**2 + 3*x**3*y**2*z - 2*x**3*y*z**2 - 2*x**2*y**4 - 2*x**2*y**3*z + x**2*y**2*z**2 + 2*x*y**4*z + y**6
    # depth = 5
    print(sds(f, [x, y, z]))

    # p171, problem 9
    f = 8*x**7 + (8*z + 6*y)*x**6 + 2*y*(31*y - 77*z)*x**5 - y*(69*y**2 - 2*z**2 - 202*y*z)*x**4 \
        + 2*y*(9*y**3 + 57*y*z**2 - 85*y**2*z + 9*z**3)*x**3 + 2*y**2*z*(-13*z**2 - 62*y*z + 27*y**2)*x**2 \
        + 2*y**3*z**2*(-11*z + 27*y)*x + y**3*z**3*(z + 18*y)
    # depth = 18
    print(sds(f, [x, y, z]))

    # p172, problem 10
    a, b, c = symbols('a, b, c', negative = False)
    # only a trivial zero
    f = a*(a + b)**5 + b*(c + b)**5 + c*(a + c)**5
    # depth = 4
    print(sds(f.subs(c, -c), [a, b, c]))
    # depth = 4
    print(sds(f.subs(c, -c).subs(b, -b), [a, b, c]))

    # p172, problem 11
    f = 2572755344*x**4 - 20000000*x**3*y - 6426888360*x**3*z + 30000000*x**2*y**2 \
        + 5315682897*x**2*z**2 - 20000000*x*y**3 - 1621722090*x*z**3 + 170172209*y**4 \
        - 1301377672*y**3*z + 3553788598*y**2*z**2 - 3864133016*y*z**3 \
        + 1611722090*z**4
    # depth = 46
    print(sds(f, [x, y, z]))

    # p174, 6-var Vasc's conjuction
    # see also: https://math.stackexchange.com/a/4693459
    f = (a1 - a2)/(a2 + a3) + (a2 - a3)/(a3 + a4) + (a3 - a4)/(a4 + a5) + \
        (a4 - a5)/(a5 + a6) + (a5 - a6)/(a6 + a1) + (a6 - a1)/(a1 + a2)
    f = fraction(cancel(f))[0]
    # TODO test if depth = 2
    print(sds(f, [a1, a2, a3, a4, a5, a6]))

    # https://math.stackexchange.com/a/2120874
    # https://math.stackexchange.com/q/1775572
    f = sum_cyc(x**4/(8*x**3 + 5*y**3), (x, y, z)) - (x + y + z)/13
    # depth = 2
    # https://math.stackexchange.com/q/1777075
    f = sum_cyc(x**3/(13*x**2 + 5*y**2), (x, y, z)) - (x + y + z)/18
    # depth = 5
    # This is not always non-negative:
    f = sum_cyc(x**3/(8*x**2 + 3*y**2), (x, y, z)) - (x + y + z)/11
    f = fraction(cancel(f))[0]
    # depth = 3, negative
    print(sds(f, [x, y, z]))
    print('f(2,3,5) =', f.subs(x, 2).subs(y, 3).subs(z, 5))
    # https://math.stackexchange.com/q/3526427
    f = 3 - sum_cyc((x + y)**2*x**2/(x**2 + y**2)**2, (x, y, z))
    # depth = 2
    # https://math.stackexchange.com/q/3757790
    f = sum_cyc((y + z)/x, (x, y, z)) + 1728*x**3*y**3*z**3/((x + y)**2*(y + z)**2*(z + x)**2*(x + y + z)**3) - 4*sum_cyc(x/(y + z), (x, y, z)) - 1
    # depth = 2
    f = fraction(cancel(f))[0]
    print(sds(f, [x, y, z]))
    '''

    # https://artofproblemsolving.com/community/c6h124116
    f = 220420308492342014250620007*x**8 + 881771706131270506700660856*x**7*y + 881771706131270506700660856*x**7*z + 3096138123320744208128844996*x**6*y**2 - 5398368991135052102868689208*x**6*y*z + 3096138123320744208128844996*x**6*z**2 - 119918369019191401348647608*x**5*y**3 - 6317290613092581261875578024*x**5*y**2*z - 6317290613092581261875578024*x**5*y*z**2 - 119918369019191401348647608*x**5*z**3 - 3095840712538537114054903510*x**4*y**4 + 6167413358885797384485337960*x**4*y**3*z - 3302116036095801486494237060*x**4*y**2*z**2 + 6167413358885797384485337960*x**4*y*z**3 - 3095840712538537114054903510*x**4*z**4 - 119918369019191401348647608*x**3*y**5 + 6167413358885797384485337960*x**3*y**4*z + 4218636235748732497452371920*x**3*y**3*z**2 + 4218636235748732497452371920*x**3*y**2*z**3 + 6167413358885797384485337960*x**3*y*z**4 - 119918369019191401348647608*x**3*z**5 + 3096138123320744208128844996*x**2*y**6 - 6317290613092581261875578024*x**2*y**5*z - 3302116036095801486494237060*x**2*y**4*z**2 + 4218636235748732497452371920*x**2*y**3*z**3 - 3302116036095801486494237060*x**2*y**2*z**4 - 6317290613092581261875578024*x**2*y*z**5 + 3096138123320744208128844996*x**2*z**6 + 881771706131270506700660856*x*y**7 - 5398368991135052102868689208*x*y**6*z - 6317290613092581261875578024*x*y**5*z**2 + 6167413358885797384485337960*x*y**4*z**3 + 6167413358885797384485337960*x*y**3*z**4 - 6317290613092581261875578024*x*y**2*z**5 - 5398368991135052102868689208*x*y*z**6 + 881771706131270506700660856*x*z**7 + 220420308492342014250620007*y**8 + 881771706131270506700660856*y**7*z + 3096138123320744208128844996*y**6*z**2 - 119918369019191401348647608*y**5*z**3 - 3095840712538537114054903510*y**4*z**4 - 119918369019191401348647608*y**3*z**5 + 3096138123320744208128844996*y**2*z**6 + 881771706131270506700660856*y*z**7 + 220420308492342014250620007*z**8
    # depth = ?, zero at (38, 51, 51)
    print(sds(f, [x, y, z]))

if __name__ == '__main__':
    main()