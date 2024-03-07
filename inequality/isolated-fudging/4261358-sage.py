from sage.all import *

# https://math.stackexchange.com/q/4261358

def main():
    u, v, x, y, z = var('u, v, x, y, z')
    xyz = (x + y + z)/3
    a, b, c = x/xyz, y/xyz, z/xyz
    f3 = a/(a*b + b*c + c*a)**3

    g = x + 2*(y + z)/5
    h = 9*(x + y + z)/5
    f = f3 - (g/h)**3
    U = 4
    # x <= y <= z <= U*a
    print('f(xyzU) =', factor(f.subs({z: x*(U + u)/(1 + u), y: x*(U + u + v)/(1 + u + v)})))
    print('f(zyxU) =', factor(f.subs({x: z*(U + u)/(1 + u), y: z*(U + u + v)/(1 + u + v)})))
    print('f(yxzU) =', factor(f.subs({z: y*(U + u)/(1 + u), x: y*(U + u + v)/(1 + u + v)})))

if __name__ == '__main__':
    main()