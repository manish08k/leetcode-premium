# Maximum Number of Accepted Invitations

Problem: https://leetcode.com/problems/maximum-number-of-accepted-invitations/

Solved on: 2026-09-03T06:47:18.000Z
Language: python3
Difficulty: Medium
Tags: Array, Depth-First Search, Graph Theory, Matrix, Maximum Flow, Maximum Matching, Bipartite Graph, Edmonds–Karp Algorithm, MPM Algorithm, Push-Relabel Algorithm, Matching (Graph), Flow Network, Dinic's Algorithm

---

There are `m` boys and `n` girls in a class attending an upcoming party.

You are given an `m x n` integer matrix `grid`, where `grid[i][j]` equals `0` or `1`. If `grid[i][j] == 1`, then that means the `i^th` boy can invite the `j^th` girl to the party. A boy can invite at most** one girl**, and a girl can accept at most **one invitation** from a boy.

Return *the **maximum** possible number of accepted invitations.*

**Example 1:**

```
**Input:** grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
**Output:** 3**
Explanation:** The invitations are sent as follows:
- The 1^st boy invites the 2^nd girl.
- The 2^nd boy invites the 1^st girl.
- The 3^rd boy invites the 3^rd girl.
```

**Example 2:**

```
**Input:** grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
**Output:** 3
**Explanation:** The invitations are sent as follows:
-The 1^st boy invites the 3^rd girl.
-The 2^nd boy invites the 1^st girl.
-The 3^rd boy invites no one.
-The 4^th boy invites the 2^nd girl.
```

**Constraints:**

	- `grid.length == m`

	- `grid[i].length == n`

	- `1 <= m, n <= 200`

	- `grid[i][j]` is either `0` or `1`.
