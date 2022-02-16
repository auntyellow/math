from cartesian import *

def L(a, b):
    x, y = symbols('x, y')
    return Eq(y, a*x + b)

def main():
    # Lines abc and def are concurrent respectively, and G=a∩d, H=c∩f, J=a∩e, K=b∩f, M=b∩d, N=c∩e.
    # Prove GH, JK and MN are concurrent.
    # Put concurrent point of abc onto origin, and concurrent point of def onto y-axis
    g, h, j, k, m, n, p = symbols('g, h, j, k, m, n, p')
    a, b, c, d, e, f = L(h, 0), L(j, 0), L(k, 0), L(m, g), L(n, g), L(p, g)
    G, H = intersect(a, d), intersect(c, f)
    J, K = intersect(a, e), intersect(b, f)
    M, N = intersect(b, d), intersect(c, e)
    print('Are GH, JK and MN concurrent?', concurrency(line(G, H), line(J, K), line(M, N)) == 0)

if __name__ == '__main__':
    main()