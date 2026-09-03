# Power Update After K-th Largest Insertion I

Problem: https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

Solved on: 2026-08-06T09:51:15.000Z
Language: python3
Difficulty: Medium
Tags: Array, Hash Table, Math, Segment Tree, Sorting, Heap (Priority Queue)

---

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each `queries[i] = [vali, ki]` and the difference between **consecutive** `ki` values is always **less** than 10.

For each query:

	- Insert `vali` into `nums`.

	- Let `x` be the `ki^th` **largest** element in the current `nums`.

	- **Update** `p` to `p^x % (10^9 + 7)`.

Return an array `ans` where the `ans[i]` represents the value of `p` after processing the `i^th` query.

**Example 1:**

**Input:** nums = [2], p = 4, queries = [[3,1],[1,2]]

**Output:** [64,4096]

**Explanation:**

	
		
			`i`
			`vali`
			Current

			`nums`
			`ki`
			`ki^th`

			largest
			p
			New `p = p^k % (10^9 + 7)`
		
	
	
		
			0
			3
			[2, 3]
			1
			3
			4
			4^3 % (10^9 + 7) = 64
		
		
			1
			1
			[2, 3, 1]
			2
			2
			64
			64^2 % (10^9 + 7) = 4096
		
	

Thus, `ans = [64, 4096]`.

**Example 2:**

**Input:** nums = [7,5], p = 6, queries = [[4,3],[7,2]]

**Output:** [1296,220296870]

**Explanation:**

	
		
			`i`
			`vali`
			Current​​​​​​​

			`nums`
			`ki`
			`ki^th`

			largest
			`p`
			New `p = p^k % (10^9 + 7)`
		
	
	
		
			0
			4
			[7, 5, 4]
			3
			4
			6
			6^4 % (10^9 + 7) = 1296
		
		
			1
			7
			[7, 5, 4, 7]
			2
			7
			1296
			1296^7 % (10^9 + 7) = 220296870
		
	

Thus, `ans = [1296, 220296870]`

**Constraints:**

	- `1 <= nums.length <= 2 × 10^4`

	- `1 <= nums[i] <= 10^6`

	- `​​​​​​​1 <= p <= 10^6`

	- `1 <= queries.length <= 2 × 10^4`

	- `^​​​​​​​1 <= vali <= 10^6`

	- `1 <= ki <= n + i + 1`

	- `|ki - ki - 1| < 10` for `i > 0`
