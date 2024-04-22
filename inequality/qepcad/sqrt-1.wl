CylindricalDecomposition[
  ForAll[{a, b, a1, b1},
    a > 0 && b > 0 && a1 > 0 && b1 > 0 &&
      a*a1^2 == b && b*b1^2 == a,
    a1 + b1 >= 2
  ], {}
]