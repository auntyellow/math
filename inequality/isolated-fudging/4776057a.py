from math import sqrt
from scipy.optimize import minimize
from sympy import nsimplify

# https://math.stackexchange.com/q/4776057

def fun(X):
    p, q = X[0], X[1]
    non_negative_coeffs = [
        144*p**2 - 2016*p + 7056,
        36*p**2 - 504*p + 1764,
        360*p**2 - 5040*p + 17640,
        -7772*p**2 + 4480*p*q + 4872*p - 1280*q**2 + 9600*q + 19044,
        72*p**2 - 1008*p + 3528,
        -576*p**2 + 1152*p*q - 8064*q + 28224,
        -15544*p**2 + 8960*p*q + 9744*p - 2560*q**2 + 19200*q + 38088,
        -14736*p**2 + 19200*p*q + 7008*p + 19200*q + 21744,
        72*p**2 + 288*p*q - 1008*p - 2016*q + 3528,
        -1224*p**2 + 1728*p*q + 5040*p - 12096*q + 24696,
        -4080*p**2 - 6048*p*q + 33888*p - 3840*q**2 - 2208*q + 45648,
        -22104*p**2 + 28800*p*q + 10512*p + 28800*q + 32616,
        -6840*p**2 + 14400*p*q + 720*p + 14400*q + 7560,
        36*p**2 + 288*p*q - 504*p - 2016*q + 1764,
        -900*p**2 - 2880*p*q + 4536*p + 2304*q**2 - 12096*q + 12348,
        3692*p**2 - 10528*p*q + 29016*p - 2560*q**2 - 11808*q + 26604,
        12528*p**2 - 8640*p*q + 42336*p - 8640*q + 29808,
        -6840*p**2 + 14400*p*q + 720*p + 14400*q + 7560,
        9*p**2 + 144*p*q - 126*p + 576*q**2 - 1008*q + 441,
        -234*p**2 - 1728*p*q + 1260*p + 1152*q**2 - 4032*q + 2646,
        745*p**2 - 7952*p*q + 9762*p + 1600*q**2 - 8592*q + 6777,
        9948*p**2 - 9120*p*q + 19416*p - 9120*q + 9468,
        13140*p**2 - 7200*p*q + 19080*p - 7200*q + 5940,
        4180*p**2 - 4160*p*q + 8040*p + 1024*q**2 - 3648*q + 1044,
        9700*p**2 + 64*p*q + 18696*p - 2816*q**2 + 6720*q + 36,
        24440*p**2 - 15616*p*q + 36336*p + 2048*q**2 - 14592*q + 6264,
        5561*p**2 + 19664*p*q + 13410*p - 9664*q**2 + 41040*q - 4887,
        42822*p**2 + 17760*p*q + 61356*p - 4224*q**2 + 23136*q + 9702,
        49741*p**2 - 23792*p*q + 65994*p + 1600*q**2 - 24432*q + 14013,
        -464*p**2 + 28096*p*q - 960*p - 12800*q**2 + 67776*q - 12528,
        9988*p**2 + 101920*p*q + 17448*p - 12800*q**2 + 120864*q + 6948,
        52904*p**2 + 42752*p*q + 77040*p - 2560*q**2 + 41472*q + 25416,
        42612*p**2 - 19680*p*q + 56904*p - 19680*q + 14292,
        44*p**2 + 16640*p*q - 5832*p - 10240*q**2 + 55296*q - 14580,
        -11024*p**2 + 116992*p*q - 30240*p - 12800*q**2 + 154368*q - 5904,
        -19632*p**2 + 149472*p*q + 2784*p - 3840*q**2 + 153312*q + 30096,
        12672*p**2 + 37440*p*q + 36864*p + 37440*q + 24192,
        13140*p**2 - 7200*p*q + 19080*p - 7200*q + 5940,
        520*p**2 + 3520*p*q - 1392*p - 5120*q**2 + 24000*q - 8568,
        -1704*p**2 + 55680*p*q - 27792*p - 7680*q**2 + 86400*q - 10728,
        -28144*p**2 + 124160*p*q - 29856*p - 2560*q**2 + 134400*q + 11088,
        -32616*p**2 + 86400*p*q - 4752*p + 86400*q + 27864,
        -6840*p**2 + 14400*p*q + 720*p + 14400*q + 7560,
        -20*p**2 - 320*p*q + 600*p - 1280*q**2 + 4800*q - 2196,
        1160*p**2 + 8960*p*q - 6384*p - 2560*q**2 + 19200*q - 3960,
        -4604*p**2 + 33280*p*q - 11832*p - 1280*q**2 + 38400*q - 828,
        -12624*p**2 + 38400*p*q - 4128*p + 38400*q + 8496,
        -6840*p**2 + 14400*p*q + 720*p + 14400*q + 7560,
    ]
    v = 0
    for coeff in non_negative_coeffs:
        v += coeff**2 if coeff < 0 else 0
    return v

def main():
    res = minimize(fun, [0, 0], method = 'Nelder-Mead')
    print(res)
    p0 = nsimplify(res.x[0], tolerance = 0.001, rational = True)
    q0 = nsimplify(res.x[1], tolerance = 0.001, rational = True)
    print('f({},{}) ='.format(p0, q0), fun([p0, q0]))

if __name__ == '__main__':
    main()