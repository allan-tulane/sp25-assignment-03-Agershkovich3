# CMPS 2200 Assignment 3
## Answers

**Name:** Aaron Gershkovich


Place all written answers from `assignment-03.md` here for easier grading.
**1a)** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.
The Greedy Algorithm for producing as few coins as possible is using as many coins of the largest denomination as possible before moving on to the next. Once a coin of the largest denomination cannot be used, we move down to the second largest denomination and continue. We repeat until adding up to exactly the right value, which is possible because there is a coin with a value of 1.


**1b)** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.
  The Greedy Algorithm is optimal because two coins of any denomination would just be unoptimal because you could instead replace them with a coin of a larger denomination. However, this is definition of a greedy algorithm because it is optimal to select the highest possible denomination.


**1c)** What is the work and span of your algorithm?
This algorithm has both a work and span of logn because for each addition of a coin we reduce the size by a factor of 2, which is effectively binary decomposition.

**2a)** You realize the greedy algorithm you devised above doesn't
  work in Fortuito. Give a simple counterexample that shows that the
  greedy algorithm does not produce the fewest number of coins.
  One potential counter example is a system with coins of a denomination of with coins of 4, 3 , and 1 because to get exactly 6 cents, if you use a greedy algorithm you would get one 4 cent coin and two 1 cent coins, but it would be optimal to use a two 3 cent coins.


**2b)** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.
It has the optimal substructure property because to find the smallest number of coins you can essentially break the problem down into a group of smaller problems which is the definition of an optimal substructure. If we use the current coin, the problem (let it be C(N,k)), becomes C(N-D_k, k) + 1, and if we do not use a give coin, it becomes C(N, k-1). We would recursively continue this in all directions, while storing and not repeating unique coin combinations (memoization), eventually taking the overall minimum. As this would work for this problem, it follows the optimal substructure property.

**2c)** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?
For the work, the number of distinct subproblems is Nk, and each subproblem is O(1) work for minimization, so the total for work and span is both O(Nk). This is true because we are computing all problems from 0 to N + 1 for each amount for 0 to K + 1 coin types, arriving at O(kN).


