CylindricalDecomposition[
  ForAll[
    {s3, x, y, a, b, c},
    s3 >= 0 && s3^2 - 3 == 0 &&
      a > 0 && b > 0 && c > 0 &&
      (x - 2)^2 + y^2 - a^2 == 0 &&
      (x + 1)^2 + (y - s3)^2 - b^2 == 0 &&
      (x + 1)^2 + (y + s3)^2 - c^2 == 0 &&
      x^2 + y^2 - 4 != 0,
    a + b - c > 0
  ], {}
]