from cartesian import *

def pair(p1, p2, p3):
    return p1[0] - p2[0], p2[0] - p3[0]

def main():
    # https://en.wikipedia.org/wiki/Ceva%27s_theorem
    # AD, BE, CF are concurrent => (AF/FB)*(BD/DC)*(CE/EA)=1
    # Put AB onto x-axis and C onto y-axis
    a, b, c, g, h = symbols('a, b, c, g, h')
    A, B, C, O = (a, 0), (b, 0), (0, c), (g, h)
    D = intersect(line(O, A), line(B, C))
    E = intersect(line(O, B), line(C, A))
    F = intersect(line(O, C), line(A, B))
    (AF, FB), (BD, DC), (CE, EA) = pair(A, F, B), pair(B, D, C), pair(C, E, A)
    print('AF*BD*CE - FB*DC*EA =', cancel(AF*BD*CE - FB*DC*EA))

if __name__ == '__main__':
    main()