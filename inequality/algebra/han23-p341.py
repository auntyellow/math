from sympy import *

# ISBN 9787312056185, p341, ex 11.7

def main():
    a, b, c, u, v, w = symbols('a, b, c, u, v, w', negative = False)
    f = 1/(a + u*b)/(a + v*b) + 1/(b + u*c)/(b + v*c) + 1/(c + u*a)/(c + v*a) - 9/(1 + u)/(1 + v)/(a*b + b*c + c*a)
    print('Are u and v symmetric?', f.subs(u, w).subs(v, u).subs(w, v) == f)
    print('f(acb,1uv) =', factor(f.subs(c, a*(1 + c)).subs(b, a*(1 + b + c)).subs(u, 1 + u).subs(v, 1 + u + v))) # trivially positive
    print('f(abc,u1v) =', factor(f.subs(b, a*(1 + b)).subs(c, a*(1 + b + c)).subs(u, 1/(1 + u)).subs(v, 1 + v)))
    print('f(acb,v1u) =', factor(f.subs(c, a*(1 + c)).subs(b, a*(1 + b + c)).subs(v, 1/(1 + v)).subs(u, 1 + u)).subs(b, w).subs(c, b).subs(w, c)) # similar to f(abc,u1v)
    print('f(abc,1uv) =', factor(f.subs(b, a*(1 + b)).subs(c, a*(1 + b + c)).subs(u, 1 + u).subs(v, 1 + u + v)))
    print('f(acb,uv1) =', factor(f.subs(c, a*(1 + c)).subs(b, a*(1 + b + c)).subs(u, 1/(1 + u)).subs(v, 1/(1 + u + v))).subs(b, w).subs(c, b).subs(w, c)) # similar to f(abc,1uv)
    # so only need to prove when a = max(a, b, c)
    print('f(uv1) =', factor(f.subs(b, a*b).subs(c, a*c))) # proved by BinarySearch
    print('f(u1v) =', factor(f.subs(b, a*b).subs(c, a*c).subs(v, 1/v))) # proved by BinarySearch
    print('f(1uv) =', factor(f.subs(b, a*b).subs(c, a*c).subs(u, 1/u).subs(v, 1/v)).subs(b, w).subs(c, b).subs(w, c)) # similar to f(abc,uv1)

if __name__ == '__main__':
    main()