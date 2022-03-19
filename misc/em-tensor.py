from sympy import *

def main():
    Bx, By, Bz, Ex, Ey, Ez = symbols('Bx, By, Bz, Ex, Ey, Ez')
    eta = diag(1, -1, -1, -1)
    F = Matrix([[0, Ex, Ey, Ez], [-Ex, 0, -Bz, By], [-Ey, Bz, 0, -Bx], [-Ez, -By, Bx, 0]])
    print('F^{μν} =', F)
    # F_{\mu\nu}=\eta_{\alpha\nu}F^{\beta\alpha}\eta_{\mu\beta}
    F1 = [[0] * 4 for i in range(4)]
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    F1[mu][nu] += eta[alpha, nu]*F[beta, alpha]*eta[mu, beta]
    F1 = Matrix(F1)
    print('F_{μν} =', F1)
    detF = F.det()
    print('det F =', detF)
    BE, B2, E2 = Bx*Ex + By*Ey + Bz*Ez, Bx**2 + By**2 + Bz**2, Ex**2 + Ey**2 + Ez**2
    print('det F = (B·E)² ?', detF == expand(BE**2))
    FF = 0
    for mu in range(4):
        for nu in range(4):
            FF += F[mu, nu]*F1[mu, nu]
    FF = expand(FF)
    print('F_{μν}F^{μν} =', FF)
    print('F_{μν}F^{μν} = 2(B²-E²) ?', FF == 2*(B2 - E2))
    # G^{\alpha\beta}=\frac{1}2\epsilon^{\alpha\beta\gamma\delta}F_{\gamma\delta}
    G = [[0] * 4 for i in range(4)]
    for alpha in range(4):
        for beta in range(4):
            for gamma in range(4):
                for delta in range(4):
                    G[alpha][beta] += LeviCivita(alpha, beta, gamma, delta)*F[gamma, delta]/2
    G = Matrix(G)
    print('G^{μν} =', G)
    # G_{\mu\nu}=\eta_{\alpha\nu}G^{\beta\alpha}\eta_{\mu\beta}
    G1 = [[0] * 4 for i in range(4)]
    for mu in range(4):
        for nu in range(4):
            for alpha in range(4):
                for beta in range(4):
                    G1[mu][nu] += eta[alpha, nu]*G[beta, alpha]*eta[mu, beta]
    G1 = Matrix(G1)
    print('G_{μν} =', G1)
    GF = 0
    for gamma in range(4):
        for delta in range(4):
            GF += G[gamma, delta]*F[gamma, delta]
    print('G_{γδ}F^{γδ} =', GF)
    print('G_{γδ}F^{γδ} = -4B·E ?', GF == -4*BE)

if __name__ == '__main__':
    main()