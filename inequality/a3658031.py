# https://math.stackexchange.com/a/3658031

def main():
    # a, b, c = 1, 1, 1
    # a, b, c = 1.5, 1, .5
    a, b, c = .5, 1, 1.5
    f = 1/(2 + a**2 + b**2) - 3*(6*a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 4*b*c)/32/(a**2 + b**2 + c**2 + a*b + a*c + b*c)
    print('f =', f)

if __name__ == '__main__':
    main()