CylindricalDecomposition[
  ForAll[
    {a, b, c, a1, b1, c1},
    a > 0 && b > 0 && c > 0 && a1 > 0 && b1 > 0 && c1 > 0 &&
      a*b1^2 == c && b*c1^2 == a && c*a1^2 == b,
    a1 + b1 + c1 >= 3
  ], {}
]