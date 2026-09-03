# Sort Array Using Prefix Reversals

Problem: https://leetcode.com/problems/sort-array-using-prefix-reversals/

Solved on: 2026-09-03T07:31:32.000Z
Language: python3
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Breadth-First Search, Hash Function

---

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers in the range `[0, n - 1]`.

You are also given an integer array `pre`, where each `pre[i]` is a valid prefix length.

In one operation, you may choose any length `x` from `pre` and reverse the first `x` elements of `nums`.

For example, applying a prefix reversal of length `3` on `[4, 1, 2, 3]` results in `[2, 1, 4, 3]`.

Return the minimum number of operations required to sort `nums` in ascending order. If it is impossible to sort `nums`, return `-1`.

**Example 1:**

**Input:** nums = [2,0,1], pre = [2,3]

**Output:** 2

**Explanation:**

	- Reverse `pre[1] = 3` elements to get `nums = [1, 0, 2]`.

	- Then reverse `pre[0] = 2` elements to get `nums = [0, 1, 2]`.

	- Thus, the minimum number of prefix reversal required is 2.

**Example 2:**

**Input:** nums = [1,0,2], pre = [1,3]

**Output:** -1

**Explanation:**

It is impossible to sort the array using the given prefix lengths, so the answer is -1.

**Example 3:**

**Input:** nums = [0,1], pre = [2]

**Output:** 0

**Explanation:**

Since `nums` is already sorted, no prefix reversals are needed. Thus, the answer is 0.

**Constraints:**

	- `1 <= n == nums.length <= 8`

	- `0 <= nums[i] <= n - 1`

	- `1 <= pre.length <= n`

	- `1 <= pre[i] <= n`

	- `​​​​​​​nums` is a permutation of integers from 0 to `n - 1`.

	- `pre` consists of **unique** integers.
