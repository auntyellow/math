(* ISBN 9787030207210, p169, §7.3.2, problem 7 *)

Cyc4[f_, a_, b_, c_, d_] := (
    t = Symbol["Cyc4Temp"];
    f /. (d -> t) /. (c -> d) /. (b -> c) /. (a -> b) /. (t -> a)
)

Cyc3[f_, a_, b_, c_, d_] := (
    t = Symbol["Cyc3Temp"];
    f /. (d -> t) /. (c -> d) /. (b -> c) /. (t -> b)
)

SumComb4[f_, a_, b_, c_, d_] := (
    f1 = Cyc4[f, a, b, c, d];
    f2 = Cyc4[f1, a, b, c, d];
    f3 = Cyc3[f2, a, b, c, d];
    f + f1 + f2 + Cyc4[f2, a, b, c, d] + f3 + Cyc4[f3, a, b, c, d]
)

n = 1000
f = SumComb4[(-x3^2 - 2*x4*x1 + 6*x1^2 + 6*x2^2 + 4*x2*x1 - x4^2 - 2*x2*x3 - 2*x3*x1 - 2*x4*x2)*(x1 - x2)^n, x1, x2, x3, x4]
Print["f = ", ExpandAll[f /. (x1 -> a) /. (x2 -> a + u) /. (x3 -> a + u + v) /. (x4 -> a + u + v + w)]]