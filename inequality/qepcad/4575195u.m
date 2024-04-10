CylindricalDecomposition[
  ForAll[
    {x, y, z, X, Y, Z},
    x > 0 && y > 0 && z > 0 && X > 0 && Y > 0 && Z > 0 &&
      X^2*(3*x^2 + y*z) == 4*x^2 + y^2 && Y^2*(3*y^2 + z*x) == 4*y^2 + z^2 && Z^2*(3*z^2 + x*y) == 4*z^2 + x^2,
    X + Y + Z >= 3*Sqrt[5]/2
  ], {}
]