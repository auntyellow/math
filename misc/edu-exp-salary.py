from numpy import array, linalg

def main():
    # The Book of Why, Table 8.1
    # name, exp, edu, salary
    data = \
        ['Alice', 6, 0, 81000], \
        ['Bert', 9, 1, 92500], \
        ['Caroline', 9, 2, 97000], \
        ['David', 8, 1, 91000], \
        ['Ernest', 12, 1, 100000], \
        ['Francis', 13, 0, 97000]

    # Exp and Edu are independent: salary = x1*exp + x2*edu + x3 + error
    A, B = [], []
    for i in data:
        A.append([i[1], i[2], 1])
        B.append(i[3])
    x1, x2, x3 = linalg.lstsq(array(A), array(B), rcond=None)[0]
    print(f'salary = {x1:.0f}*exp + {x2:.0f}*edu + {x3:.0f} + error')
    # In the book, Eq 8.1: salary = 2500*ex + 5000*ed + 65000
    print('Name: S(edu=0), S(edu=1), S(edu=2), error')
    for i in data:
        name, exp, edu, salary = i[0], i[1], i[2], i[3]
        base = salary - x2*edu
        error = base - x1*exp - x3
        print(f'{name}: {base:.0f}, {base + x2:.0f}, {base + x2*2:.0f}, {error:.0f}')

    # Adjust Exp by Edu: salary = x1*(exp + 4*edu) + x2*edu + x3 + error
    A, B = [], []
    for i in data:
        A.append([i[1] + i[2]*4, i[2], 1])
        B.append(i[3])
    x1, x2, x3 = linalg.lstsq(array(A), array(B), rcond=None)[0]
    print(f'salary = {x1:.0f}*(exp + 4*edu) + {x2:.0f}*edu + {x3:.0f} + error')
    print('Name: S(edu=0), S(edu=1), S(edu=2), error')
    for i in data:
        name, exp, edu, salary = i[0], i[1], i[2], i[3]
        base = salary - x2*edu
        error = base - x1*(exp + 4*edu) - x3
        print(f'{name}: {base:.0f}, {base + x2:.0f}, {base + x2*2:.0f}, {error:.0f}')
        # In the book, Alice: S(edu=1) = 76000

if __name__ == '__main__':
    main()