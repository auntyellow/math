from cartesian import *

def pair(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

def main():
    # https://en.wikipedia.org/wiki/Ceva%27s_theorem
    # (AF/FB)*(BD/DC)*(CE/EA)=1 => AD, BE, CF are concurrent
    # Put AB onto x-axis and C onto y-axis
    a, b, c, d, e, f = symbols('a, b, c, d, e, f')
    A, B, C, D, E, F = (a, 0), (b, 0), (0, c), (d, (1 - d/b)*c), (e, (1 - e/a)*c), (f, 0)
    (AF, FB), (BD, DC), (CE, EA) = pair(A, F, B), pair(B, D, C), pair(C, E, A)
    F = (solve(Eq(AF*BD*CE, FB*DC*EA), f)[0], 0)
    print('Are AD, BE and CF concurrent?', concurrency(line(A, D), line(B, E), line(C, F)) == 0)

if __name__ == '__main__':
    main()