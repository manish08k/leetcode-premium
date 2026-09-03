# Longest Line of Consecutive One in Matrix

Problem: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Solved on: 2026-08-06T19:11:46.000Z
Language: python3
Difficulty: Medium
Tags: Array, Dynamic Programming, Matrix

---

Given an `m x n` binary matrix `mat`, return *the length of the longest line of consecutive one in the matrix*.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

**Example 1:**

```
**Input:** mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
**Output:** 3
```

**Example 2:**

```
**Input:** mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
**Output:** 4
```

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^4`

	- `1 <= m * n <= 10^4`

	- `mat[i][j]` is either `0` or `1`.
