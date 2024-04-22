#!/bin/bash

$qe/bin/qepcad +N1000000000 << END
[ISBN 9787560349800, p226, ex 9.5]
(a, b, c)
0
(A a)(A b)(A c)[[a >= 0 /\ a <= 1 /\ b >= 0 /\ b <= 1 /\ c >= 0 /\ c <= 1] ==> 8 a^3 b^2 c - 8 a^3 b^2 + 8 a^3 b c^2 - 8 a^3 b c - 8 a^3 c^2 + 8 a^2 b^3 c - 8 a^2 b^3 + 16 a^2 b^2 c^2 - 8 a^2 b^2 c - 8 a^2 b^2 + 8 a^2 b c^3 - 8 a^2 b c^2 - 8 a^2 b c + 7 a^2 b - 8 a^2 c^3 - 8 a^2 c^2 + 7 a^2 c - a^2 + 8 a b^3 c^2 - 8 a b^3 c + 8 a b^2 c^3 - 8 a b^2 c^2 - 8 a b^2 c + 7 a b^2 - 8 a b c^3 - 8 a b c^2 + 6 a b c + 5 a b + 7 a c^2 + 5 a c - 2 a - 8 b^3 c^2 - 8 b^2 c^3 - 8 b^2 c^2 + 7 b^2 c - b^2 + 7 b c^2 + 5 b c - 2 b - c^2 - 2 c - 1 <= 0].
finish
END