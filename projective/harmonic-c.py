from cartesian import *

def main():
    # Given diagram from https://en.wikipedia.org/wiki/Projective_harmonic_conjugate, prove (A,B;C,D)=-1
    # Put MN∩KL onto origin and rotate MN onto x-axis
    h, k, l, m, n = symbols('h, k, l, m, n')
    K, L, M, N = (k, h*k), (l, h*l), (0, m), (0, n)
    LMA, LNB, NKA, MKB, LKD, MNC = line(L, M), line(L, N), line(N, K), line(M, K), line(L, K), line(M, N)
    A, B = intersect(LMA, NKA), intersect(LNB, MKB)
    ADBC = line(A, B)
    D, C = intersect(ADBC, LKD), intersect(ADBC, MNC)
    print('(A,B;C,D) =', cross_ratio(A[0], B[0], C[0], D[0]))
    print('(A,B;C,D) =', cross_ratio(A[1], B[1], C[1], D[1]))

if __name__ == '__main__':
    main()