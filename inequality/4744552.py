from sympy import *

# https://math.stackexchange.com/q/4744552

def main():
    x, y, z = symbols('x, y, z', positive = True)
    a = sqrt(x/(x + y + z))
    b = sqrt(y/(x + y + z))
    c = sqrt(z/(x + y + z))
    print('a*a + b*b + c*c =', factor(a*a + b*b + c*c))

    f = a*b/c + b*c/a + c*a/b
    u, v = symbols('u, v', positive = True)
    # assume x <= y <= z
    print('f =', factor(f.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # so we guess maximum or minimum is sqrt(3) when u = v = 0 (x = y = z)
    f23 = f*f - 3
    print('f^2 - 3 =', factor(f23.subs(y, z*(1 + u)).subs(x, z*(1 + u + v))))
    # f23 >= 0 so sqrt(3) is minimum

if __name__ == '__main__':
    main()