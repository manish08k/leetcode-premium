# Find the Index of Permutation

Problem: https://leetcode.com/problems/find-the-index-of-permutation/

Solved on: 2026-08-08T17:30:21.000Z
Language: python3
Difficulty: Medium
Tags: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set

---

Given an array `perm` of length `n` which is a permutation of `[1, 2, ..., n]`, return the index of `perm` in the lexicographically sorted array of all of the permutations of `[1, 2, ..., n]`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

**Input:** perm = [1,2]

**Output:** 0

**Explanation:**

There are only two permutations in the following order:

`[1,2]`, `[2,1]`

And `[1,2]` is at index 0.

**Example 2:**

**Input:** perm = [3,1,2]

**Output:** 4

**Explanation:**

There are only six permutations in the following order:

`[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`

And `[3,1,2]` is at index 4.

**Constraints:**

	- `1 <= n == perm.length <= 10^5`

	- `perm` is a permutation of `[1, 2, ..., n]`.
