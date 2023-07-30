from cartesian import *

def main():
    # https://math.stackexchange.com/q/4744474
    a, b, x, y = symbols('a, b, x, y')
    A, B, C, M = (30, 0), (0, 0), (0, 2), (0, 1)
    P8, P12, P20, P24 = (22, 0), (18, 0), (10, 0), (6, 0)
    AM = line(A, M)
    CP8, CP12, CP20, CP24 = line(C, P8), line(C, P12), line(C, P20), line(C, P24)
    Q8, Q12, Q20, Q24 = intersect(AM, CP8), intersect(AM, CP12), intersect(AM, CP20), intersect(AM, CP24)
    print('Q8Q20/Q12Q24 = ', cancel((Q8[0] - Q20[0])/(Q12[0] - Q24[0])))

if __name__ == '__main__':
    main()