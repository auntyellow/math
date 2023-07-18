from itertools import combinations

def powerset(s):
    result = []
    i = 0
    for _ in s:
        result.extend(combinations(s, i))
        i += 1
    result.extend(combinations(s, i))
    return result

def main():
    vertices = range(0, 6)
    edges = list(combinations(vertices, 2))
    colorings = powerset(edges)
    cliques = []
    for clique in combinations(vertices, 3):
        a, b, c = clique
        cliques.append(set([(a, b), (a, c), (b, c)]))
    non_monochromatic_count = 0
    for coloring in colorings:
        found = False
        for clique in cliques:
            l = len(clique.intersection(coloring))
            if l == 0 or l == 3:
                found = True
                break
        if not found:
            non_monochromatic_count += 1
            print(coloring)
    if non_monochromatic_count == 0:
        print("Monochromatic cliques found in all colorings")

if __name__ == '__main__':
    main()