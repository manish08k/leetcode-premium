# Number of Subsequences with Odd Sum

Problem: https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

Solved on: 2026-08-08T17:33:43.000Z
Language: python3
Difficulty: Medium
Tags: Array, Math, Dynamic Programming, Combinatorics

---

Given an array `nums`, return the number of subsequences with an odd sum of elements.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

**Input:** nums = [1,1,1]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[**1**, 1, 1]`, `[1, **1**, 1],` `[1, 1, **1**]`, `[**1, 1, 1**]`.

**Example 2:**

**Input:** nums = [1,2,2]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[**1**, 2, 2]`, `[**1, 2**, 2],` `[**1**, 2, **2**]`, `[**1, 2, 2**]`.

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
