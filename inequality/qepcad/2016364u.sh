#!/bin/bash

$qe/bin/qepcad +N100000000 << END
[https://math.stackexchange.com/q/2016364]
(a, b, c, d)
0
(A a)(A b)(A c)(A d)[[a >= 0 /\ a <= 1 /\ b >= 0 /\ b <= 1 /\ c >= 0 /\ c <= 1 /\ d >= 0 /\ d <= 1] ==> a^4 + b^4 + c^4 + d^4 + a^2 b^2 + b^2 c^2 + c^2 d^2 + d^2 a^2 + 8 (1 - a) (1 - b) (1 - c) (1 - d) - 1 >= 0].
finish
END