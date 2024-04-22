Resolve[
  ForAll[
    {a, b, c},
    a >= 1/d && a <= d && b >= 1/d && b <= d && c >= 1/d && c <= d && d >= 0,
    3/(b + 2*c) + 3/(c + 2*a) + 3/(a + 2*b) >= 2/(b + c) + 2/(c + a) + 2/(a + b)
  ]
]