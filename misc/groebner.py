from sympy import diff, factor, groebner, resultant, solve, symbols

# https://www.johndcook.com/blog/2017/05/13/grobner-bases/

def main():
    l, x, y, z = symbols('l, x, y, z')
    F = x**3 + 2*x*y*z - z**2
    G = x**2 + y**2 + z**2 - 1
    L = F + l*G
    Lx, Ly, Lz = diff(L, x), diff(L, y), diff(L, z)
    s = solve([Lx, Ly, Lz, G])
    print(s, len(s))
    B = groebner([Lx, Ly, Lz, G], l, x, y, z)
    print(B, len(B))
    for f in B:
        print(f, '= 0', f.free_symbols)
    print()
    solutions = 0
    fz = factor(B[7])
    print(fz, '= 0')
    for z0 in solve(fz, dict = True):
        z0 = z0[z]
        print('z =', z0)
        fy1 = factor(B[6].subs(z, z0))
        print(' ', fy1, '= 0')
        fy2 = factor(B[5].subs(z, z0))
        print(' ', fy2, '= 0')
        fy3 = factor(B[4].subs(z, z0))
        print(' ', fy3, '= 0')
        for y0 in solve([fy1, fy2, fy3], dict = True):
            y0 = y0[y]
            print('  y =', y0)
            fx1 = factor(B[3].subs(z, z0).subs(y, y0))
            print('   ', fx1, '= 0')
            fx2 = factor(B[2].subs(z, z0).subs(y, y0))
            print('   ', fx2, '= 0')
            fx3 = factor(B[1].subs(z, z0).subs(y, y0))
            print('   ', fx3, '= 0')
            for x0 in solve([fx1, fx2, fx3], dict = True):
                x0 = x0[x]
                print('    x =', x0)
                fl = factor(B[0].subs(z, z0).subs(y, y0).subs(x, x0))
                print('     ', fl, '= 0')
                for l0 in solve(fl, dict = True):
                    l0 = l0[l]
                    print('      l =', l0)
                    solutions += 1
    print(solutions, 'solutions')
    print()

    h1 = resultant(Lx, Ly, l) # xyz
    h2 = resultant(Lx, Lz, l) # xyz
    h3 = resultant(h1, h2, x) # yz
    h4 = resultant(h1, G, x) # yz
    h5 = resultant(h3, h4, y) # z
    solutions = 0
    print(factor(h5), '= 0')
    for z0 in solve(h5, dict = True):
        z0 = z0[z]
        print('z =', z0)
        fy1 = factor(h4.subs(z, z0))
        print(' ', fy1, '= 0')
        fy2 = factor(h3.subs(z, z0))
        print(' ', fy2, '= 0')
        for y0 in solve([fy1, fy2], dict = True):
            y0 = y0[y]
            print('  y =', y0)
            fx1 = factor(h1.subs(z, z0).subs(y, y0))
            print('   ', fx1, '= 0')
            fx2 = factor(h2.subs(z, z0).subs(y, y0))
            print('   ', fx2, '= 0')
            fx3 = factor(G.subs(z, z0).subs(y, y0))
            print('   ', fx3, '= 0')
            for x0 in solve([fx1, fx2, fx3], dict = True):
                x0 = x0[x]
                print('    x =', x0)
                fl1 = factor(Lx.subs(z, z0).subs(y, y0).subs(x, x0))
                print('     ', fl, '= 0')
                fl2 = factor(Ly.subs(z, z0).subs(y, y0).subs(x, x0))
                print('     ', fl, '= 0')
                fl3 = factor(Lz.subs(z, z0).subs(y, y0).subs(x, x0))
                print('     ', fl, '= 0')
                for l0 in solve([fl1, fl2, fl3], dict = True):
                    l0 = l0[l]
                    print('      l =', l0)
                    solutions += 1
    print(solutions, 'solutions')

if __name__ == '__main__':
    main()