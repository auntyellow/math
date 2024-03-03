#!/bin/bash

# G (all_but_finitely_many) gets correct result?
export qe=/usr/local/qepcad
$qe/bin/qepcad +N100000000 << END
[https://math.stackexchange.com/q/4850712]
(k, x, y)
1
(G x)(G y)[[x >= 0 /\ y >= 0] ==> -k^2 x^4 y^2 + k^2 x^3 y^2 + k^2 x^2 y^3 + k^2 x^2 y^2 - k^2 x^2 y - k^2 x y^4 + k x^5 y^2 + k x^4 y^3 - k x^4 y - k x^4 - k x^3 y^4 + k x^3 - k x^2 y^4 + k x^2 - k x y^2 + k y^5 + k y^4 - k y^3 + x^5 - x^3 y^2 + x^2 y^5 - x^2 y^3 - x^2 y^2 + y^2 >= 0].
finish
END