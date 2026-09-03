# Count Triplets with Even XOR Set Bits II

Problem: https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

Solved on: 2026-08-07T17:28:36.000Z
Language: python3
Difficulty: Medium
Tags: Array, Bit Manipulation

---

Given three integer arrays `a`, `b`, and `c`, return the number of triplets `(a[i], b[j], c[k])`, such that the bitwise `XOR` between the elements of each triplet has an **even** number of set bits.

**Example 1:**

**Input:** a = [1], b = [2], c = [3]

**Output:** 1

**Explanation:**

The only triplet is `(a[0], b[0], c[0])` and their `XOR` is: `1 XOR 2 XOR 3 = 002`.

**Example 2:**

**Input:** a = [1,1], b = [2,3], c = [1,5]

**Output:** 4

**Explanation:**

Consider these four triplets:

	- `(a[0], b[1], c[0])`: `1 XOR 3 XOR 1 = 0112`

	- `(a[1], b[1], c[0])`: `1 XOR 3 XOR 1 = 0112`

	- `(a[0], b[0], c[1])`: `1 XOR 2 XOR 5 = 1102`

	- `(a[1], b[0], c[1])`: `1 XOR 2 XOR 5 = 1102`

**Constraints:**

	- `1 <= a.length, b.length, c.length <= 10^5`

	- `0 <= a[i], b[i], c[i] <= 10^9`
