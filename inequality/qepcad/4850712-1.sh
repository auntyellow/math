#!/bin/bash

export qe=/usr/local/qepcad
$qe/bin/qepcad << END
[https://math.stackexchange.com/q/4850712 m, n = 63, 164]
(x, y)
0
(A x)(A y)[[x >= 0 /\ y >= 0] ==> 650916 x^5 y^2 + 250047 x^5 + 650916 x^4 y^3 - 1694448 x^4 y^2 - 650916 x^4 y - 650916 x^4 - 650916 x^3 y^4 + 1444401 x^3 y^2 + 650916 x^3 + 250047 x^2 y^5 - 650916 x^2 y^4 + 1444401 x^2 y^3 + 1444401 x^2 y^2 - 1694448 x^2 y + 650916 x^2 - 1694448 x y^4 - 650916 x y^2 + 650916 y^5 + 650916 y^4 - 650916 y^3 + 250047 y^2 >= 0].
finish
END