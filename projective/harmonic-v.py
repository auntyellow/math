from homogeneous import *

def main():
    # Given diagram from https://en.wikipedia.org/wiki/Projective_harmonic_conjugate, prove (A,B;C,D)=-1
    K, L, M, N = (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)
    LMA, LNB, NKA, MKB, LKD, MNC = cross(L, M), cross(L, N), cross(N, K), cross(M, K), cross(L, K), cross(M, N)
    A, B = cross(LMA, NKA), cross(LNB, MKB)
    print('A:', A)
    print('B:', B)
    ADBC = cross(A, B)
    D, C = cross(ADBC, LKD), cross(ADBC, MNC)
    print('C:', C)
    print('D:', D)
    print('(A,B;C,D) =', cross_ratio(A, B, C, D))

if __name__ == '__main__':
    main()