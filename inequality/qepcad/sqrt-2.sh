#!/bin/bash

export qe=/usr/local/qepcad
$qe/bin/qepcad +N100000000 << END
[sum_cyc(sqrt(a/b)) >= 3]
(a, b, c, a1, b1, c1)
0
(A a)(A b)(A c)(A a1)(A b1)(A c1)[[a > 0 /\ b > 0 /\ c > 0 /\ a1 > 0 /\ b1 > 0 /\ c1 > 0 /\ a b1^2 = c /\ b c1^2 = a /\ c a1^2 = b] ==> a1 + b1 + c1 >= 3].
finish
END