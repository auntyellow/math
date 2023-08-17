import numpy as np
import scipy.optimize as optimize

# https://math.stackexchange.com/q/4746804

def g(X):
    u, w = X[0], X[1]
    return u**8*w**6 + 12*u**8*w**5 + 60*u**8*w**4 + 160*u**8*w**3 + 240*u**8*w**2 + 192*u**8*w + 64*u**8 + u**6*w**6 - 6*u**6*w**5 - 63*u**6*w**4 - 176*u**6*w**3 - 228*u**6*w**2 - 144*u**6*w - 32*u**6 + 2*u**4*w**5 + 18*u**4*w**4 + 70*u**4*w**3 + 112*u**4*w**2 + 60*u**4*w + 8*u**4 + u**2*w**4 - 10*u**2*w**3 - 27*u**2*w**2 - 28*u**2*w - 8*u**2 + w**2 + 4*w + 4

def main():
    result = optimize.minimize(g, [1, 1], bounds=((0, 10), (0, 10)), \
            method = 'Nelder-Mead', options={'xatol': 1e-14, 'maxiter': 10000})
            # method = 'CG', options={'gtol': .5e-14, 'eps': .5e-14})
    print(result)

if __name__ == '__main__':
    main()