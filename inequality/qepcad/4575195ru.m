Resolve[
  ForAll[
    {x, y, z},
    x > 0 && y > 0 && z > 0,
    Sqrt[(4*x^2 + y^2)/(3*x^2 + y*z)] + Sqrt[(4*y^2 + z^2)/(3*y^2 + z*x)] + Sqrt[(4*z^2 + x^2)/(3*z^2 + x*y)] >= 3*Sqrt[5]/2
  ]
]