#!/bin/bash

$qe/bin/qepcad +N100000000 << END
[sqrt(a/b) + sqrt(a/b) >= 2]
(a, b, a1, b1)
0
(A a)(A b)(A a1)(A b1)[[a > 0 /\ b > 0 /\ a1 > 0 /\ b1 > 0 /\ a a1^2 = b /\ b b1^2 = a] ==> a1 + b1 >= 2].
finish
END