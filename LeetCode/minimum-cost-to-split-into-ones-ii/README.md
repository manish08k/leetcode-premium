# Minimum Cost to Split into Ones II

Problem: https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

Solved on: 2026-09-03T07:31:28.000Z
Language: python3
Difficulty: Medium
Tags: Math

---

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return the **minimum** total cost required to split the integer `n` into `n` ones.

**Example 1:**

**Input:** n = 3

**Output:** 3

**Explanation:**

One optimal set of operations is:

	
		
			`x`
			`a`
			`b`
			`a + b`
			`a * b`
			Cost
		
		
			3
			1
			2
			3
			2
			2
		
		
			2
			1
			1
			2
			1
			1
		
	

Thus, the minimum total cost is `2 + 1 = 3`.

**Example 2:**

**Input:** n = 4

**Output:** 6

**Explanation:​​​​​​​**

One optimal set of operations is:

	
		
			`x`
			`a`
			`b`
			`a + b`
			`a * b`
			Cost
		
		
			4
			2
			2
			4
			4
			4
		
		
			2
			1
			1
			2
			1
			1
		
	

Thus, the minimum total cost is `4 + 1 + 1 = 6`.

**Constraints:**

	- `1 <= n <= 5 * 10^7`
