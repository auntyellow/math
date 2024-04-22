CylindricalDecomposition[
  ForAll[
    {x, y, z},
    x >= 0 && y >= 0 && z >= 0 && x^2 + y^2 + z^2 + x*y*z - 4 == 0,
    4*(x*y + y*z + z*x - x*y*z) - (x^2*y + z)*(y^2*z + x)*(z^2*x + y) >= 0
  ], {}
]