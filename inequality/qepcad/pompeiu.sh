#!/bin/bash

export qe=/usr/local/qepcad
$qe/bin/qepcad +N100000000 << END
[Pompeiu's Theorem]
(s3, x, y, a, b, c)
0
(A s3)(A x)(A y)(A a)(A b)(A c)[[s3 >= 0 /\ s3^2 - 3 = 0 /\ a >= 0 /\ b >= 0 /\ c >= 0 /\ (x - 2)^2 + y^2 - a^2 = 0 /\ (x + 1)^2 + (y - s3)^2 - b^2 = 0 /\ (x + 1)^2 + (y + s3)^2 - c^2 = 0 /\ x^2 + y^2 - 4 /= 0] ==> a + b - c > 0].
finish
END