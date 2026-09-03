# Count Univalue Subtrees

Problem: https://leetcode.com/problems/count-univalue-subtrees/

Solved on: 2026-09-03T06:13:30.000Z
Language: python3
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree, DP on Trees

---

Given the `root` of a binary tree, return *the number of **uni-value** **subtrees*.

A **uni-value subtree** means all nodes of the subtree have the same value.

**Example 1:**

```
**Input:** root = [5,1,5,5,5,null,5]
**Output:** 4
```

**Example 2:**

```
**Input:** root = []
**Output:** 0
```

**Example 3:**

```
**Input:** root = [5,5,5,5,5,null,5]
**Output:** 6
```

**Constraints:**

	- The number of the node in the tree will be in the range `[0, 1000]`.

	- `-1000 <= Node.val <= 1000`
