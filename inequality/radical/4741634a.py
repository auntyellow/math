from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def z(u, v):
    # result from 4741634u.py, zero at u = 1 and v = sqrt(3) - 1
    U = sqrt(u*(u + 2))
    V = sqrt((1 + u)**2*(1 + v)**2 - u*(u + 2))
    f = (2*u**9*v**4 + 8*u**9*v**3 + 12*u**9*v**2 + 8*u**9*v + 2*u**9 + 13*u**8*v**4 + 52*u**8*v**3 + 78*u**8*v**2 + 52*u**8*v + 13*u**8 + 32*u**7*v**4 + 128*u**7*v**3 + 256*u**7*v**2 + 256*u**7*v + 32*u**7 + 28*u**6*v**4 + 112*u**6*v**3 + 552*u**6*v**2 + 880*u**6*v + 28*u**6 - 28*u**5*v**4 - 112*u**5*v**3 + 664*u**5*v**2 + 1552*u**5*v + 100*u**5 - 98*u**4*v**4 - 392*u**4*v**3 + 180*u**4*v**2 + 1144*u**4*v + 286*u**4 - 112*u**3*v**4 - 448*u**3*v**3 - 416*u**3*v**2 + 64*u**3*v - 112*u**3 - 68*u**2*v**4 - 272*u**2*v**3 - 408*u**2*v**2 - 272*u**2*v - 580*u**2 - 22*u*v**4 - 88*u*v**3 - 132*u*v**2 - 88*u*v - 22*u - 3*v**4 - 12*v**3 - 18*v**2 - 12*v - 3)*U*V + (-18*u**9*v**4 - 72*u**9*v**3 - 76*u**9*v**2 - 8*u**9*v - 2*u**9 - 157*u**8*v**4 - 628*u**8*v**3 - 654*u**8*v**2 - 52*u**8*v - 13*u**8 - 580*u**7*v**4 - 2320*u**7*v**3 - 2520*u**7*v**2 - 400*u**7*v - 36*u**7 - 1176*u**6*v**4 - 4704*u**6*v**3 - 5520*u**6*v**2 - 1632*u**6*v - 56*u**6 - 1416*u**5*v**4 - 5664*u**5*v**3 - 7056*u**5*v**2 - 2784*u**5*v - 184*u**5 - 1018*u**4*v**4 - 4072*u**4*v**3 - 4860*u**4*v**2 - 1576*u**4*v - 426*u**4 - 412*u**3*v**4 - 1648*u**3*v**3 - 1448*u**3*v**2 + 400*u**3*v - 28*u**3 - 80*u**2*v**4 - 320*u**2*v**3 - 96*u**2*v**2 + 448*u**2*v + 496*u**2 - 6*u*v**4 - 24*u*v**3 - 36*u*v**2 - 24*u*v - 6*u - v**4 - 4*v**3 - 6*v**2 - 4*v - 1)*U + (2*u**9*v**5 + 10*u**9*v**4 + 20*u**9*v**3 + 20*u**9*v**2 + 18*u**9*v + 10*u**9 + 14*u**8*v**5 + 70*u**8*v**4 + 144*u**8*v**3 + 152*u**8*v**2 + 138*u**8*v + 74*u**8 + 40*u**7*v**5 + 200*u**7*v**4 + 432*u**7*v**3 + 496*u**7*v**2 + 440*u**7*v + 216*u**7 + 60*u**6*v**5 + 300*u**6*v**4 + 692*u**6*v**3 + 876*u**6*v**2 + 720*u**6*v + 296*u**6 + 52*u**5*v**5 + 260*u**5*v**4 + 656*u**5*v**3 + 928*u**5*v**2 + 644*u**5*v + 164*u**5 + 32*u**4*v**5 + 160*u**4*v**4 + 476*u**4*v**3 + 788*u**4*v**2 + 460*u**4*v + 20*u**4 + 24*u**3*v**5 + 120*u**3*v**4 + 416*u**3*v**3 + 768*u**3*v**2 + 520*u**3*v + 72*u**3 + 20*u**2*v**5 + 100*u**2*v**4 + 332*u**2*v**3 + 596*u**2*v**2 + 464*u**2*v + 120*u**2 + 10*u*v**5 + 50*u*v**4 + 140*u*v**3 + 220*u*v**2 + 170*u*v + 50*u + 2*v**5 + 10*v**4 + 20*v**3 + 20*v**2 + 10*v + 2)*V + (-4*u**11*v**3 - 12*u**11*v**2 - 8*u**11*v + 2*u**10*v**5 + 10*u**10*v**4 - 24*u**10*v**3 - 112*u**10*v**2 - 78*u**10*v + 2*u**10 + 18*u**9*v**5 + 90*u**9*v**4 - 32*u**9*v**3 - 456*u**9*v**2 - 342*u**9*v + 10*u**9 + 84*u**8*v**5 + 420*u**8*v**4 + 240*u**8*v**3 - 960*u**8*v**2 - 848*u**8*v + 16*u**8 + 248*u**7*v**5 + 1240*u**7*v**4 + 1364*u**7*v**3 - 868*u**7*v**2 - 1216*u**7*v + 24*u**7 + 464*u**6*v**5 + 2320*u**6*v**4 + 3240*u**6*v**3 + 440*u**6*v**2 - 820*u**6*v + 124*u**6 + 532*u**5*v**5 + 2660*u**5*v**4 + 4180*u**5*v**3 + 1900*u**5*v**2 + 188*u**5*v + 340*u**5 + 348*u**4*v**5 + 1740*u**4*v**4 + 2912*u**4*v**3 + 1776*u**4*v**2 + 656*u**4*v + 400*u**4 + 104*u**3*v**5 + 520*u**3*v**4 + 848*u**3*v**3 + 464*u**3*v**2 + 200*u**3*v + 168*u**3 - 2*u**2*v**5 - 10*u**2*v**4 - 96*u**2*v**3 - 248*u**2*v**2 - 190*u**2*v - 30*u**2 - 6*u*v**5 - 30*u*v**4 - 84*u*v**3 - 132*u*v**2 - 102*u*v - 30*u)
    return -10 if f < 0 else np.log(1 + f)

def main():
    Z = [[z(i/100, j/100) for j in range(400)] for i in range(400)]
    plt.imshow(Z, origin='lower', extent = [0, 4, 0, 4], cmap=plt.cm.hsv)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    main()