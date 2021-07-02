## Friends and Strangers

> In any party of six people either at least three of them are (pairwise) mutual strangers or at least three of them are (pairwise) mutual acquaintances.

The simple proof by pigeonhole principle is shown [here](https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers#Sketch_of_a_proof) and [here](https://en.wikipedia.org/wiki/Ramsey's_theorem#R%283,_3%29_=_6).

However, I'd like to prove it with by brute force. As mentioned [here](https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers#Conversion_to_a_graph-theoretic_setting), the only thing is to exhaust 2<sup>15</sup> cases and to find mutual friends / strangers in each case. Considering the symmetry, only 78 cases are necessary to check.<sup>*How to prove?*</sup>

### Proof by Program

[ramsey.py](ramsey.py) tries to find out cases (where mutual friends / strangers are not found) for `R(3,3)=N`. It has three big nested loops:

1. Loop for 2<sup>M</sup> cases by recursion, where `M=N*(N-1)/2` is the number of total edges (function [test_edges](ramsey.py#L73));
2. Loop for `L=C(N,3)` cliques (vertices in cliques stored in [vertex_combinations](ramsey.py#L38));
3. Loop for `K=L*(L-1)/2` edges to check if the clique is monochromatic.

The program found no case (without monochromatic cliques) for `R(3,3)=6`, and found 12 cases for `R(3,3)=5` (change [N](ramsey.py#L5) to 5), which matched our expectation.