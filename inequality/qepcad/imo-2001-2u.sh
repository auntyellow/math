#!/bin/bash

export qe=/usr/local/qepcad
$qe/bin/qepcad +N100000000 << END
[IMO 2001 problem 2]
(a, b, c, a1, b1, c1)
0
(A a)(A b)(A c)(A a1)(A b1)(A c1)[[a > 0 /\ b > 0 /\ c > 0 /\ a1 > 0 /\ b1 > 0 /\ c1 > 0 /\ a1^2 (a^2 + 8 b c) = a^2 /\ b1^2 (b^2 + 8 a c) = b^2 /\ c1^2 (c^2 + 8 a b) = c^2] ==> a1 + b1 + c1 >= 1].
finish
END