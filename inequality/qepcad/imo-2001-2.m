CylindricalDecomposition[
  ForAll[
    {a, b, c, A, B, C},
    a > 0 && b > 0 && c > 0 && A > 0 && B > 0 && C > 0 &&
      A^2*(a^2 + 8*b*c) == a^2 && B^2*(b^2 + 8*a*c) == b^2 && C^2*(c^2 + 8*a*b) == c^2,
    A + B + C >= 1
  ], {}
]