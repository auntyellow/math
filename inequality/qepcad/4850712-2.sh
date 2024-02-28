#!/bin/bash

export saclib=/usr/local/saclib
export qe=/usr/local/qepcad
$qe/bin/qepcad << END
[https://math.stackexchange.com/q/4850712 m, n = 121, 315]
(x, y)
0
(A x)(A y)[[x >= 0 /\ y >= 0] ==> 4611915 x^5 y^2 + 1771561 x^5 + 4611915 x^4 y^3 - 12006225 x^4 y^2 - 4611915 x^4 y - 4611915 x^4 - 4611915 x^3 y^4 + 10234664 x^3 y^2 + 4611915 x^3 + 1771561 x^2 y^5 - 4611915 x^2 y^4 + 10234664 x^2 y^3 + 10234664 x^2 y^2 - 12006225 x^2 y + 4611915 x^2 - 12006225 x y^4 - 4611915 x y^2 + 4611915 y^5 + 4611915 y^4 - 4611915 y^3 + 1771561 y^2 >= 0].
finish
END