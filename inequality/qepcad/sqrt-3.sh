#!/bin/bash

$qe/bin/qepcad +N100000000 << END
[sum_cyc(sqrt(a/(b + c))) >= 2]
(a, b, c, a1, b1, c1)
0
(A a)(A b)(A c)(A a1)(A b1)(A c1)[[a > 0 /\ b > 0 /\ c > 0 /\ a1 > 0 /\ b1 > 0 /\ c1 > 0 /\ (b + c) a1^2 = a /\ (a + c) b1^2 = b /\ (a + b) c1^2 = c] ==> a1 + b1 + c1 > 2].
finish
END