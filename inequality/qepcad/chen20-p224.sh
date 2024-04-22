#!/bin/bash

# b <= 0 doesn't work: a = 0 /\ b = 0 causes degenerate
$qe/bin/qepcad +N100000000 << END
[ISBN 9787030655189, p224, ex 8.5.3]
(r, a, b, c, d)
1
(E a)(E b)(E c)(E d)[a >= 0 /\ b < 0 /\ c >= 1 /\ d <= -1 /\ a^2 + b^2 <= r^2 /\ d - (1 - a) (d - b) = 0 /\ c - (1 + b) (c - a) = 0].
finish
END