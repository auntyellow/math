from math import sqrt

# https://math.stackexchange.com/a/2993922

def f(x):
    if x < 0:
        return -x
    if x == x + 1:
        return x**sqrt(2)
    y = sqrt(f(x**2 + 1) - 1)
    print(f'f({x})={y}')
    return y

if __name__ == '__main__':
    x = f(6.0)
    print('x =', x)
    f(x)