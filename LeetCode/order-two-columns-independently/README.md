# Order Two Columns Independently

Problem: https://leetcode.com/problems/order-two-columns-independently/

Solved on: 2026-09-04T11:59:11.000Z
Language: mysql
Difficulty: Medium
Tags: Database

---

Table: `Data`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| first_col   | int  |
| second_col  | int  |
+-------------+------+
This table may contain duplicate rows.
```

Write a solution to independently:

	- order `first_col` in **ascending order**.

	- order `second_col` in **descending order**.

The result format is in the following example.

**Example 1:**

```
**Input:** 
Data table:
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 4         | 2          |
| 2         | 3          |
| 3         | 1          |
| 1         | 4          |
+-----------+------------+
**Output:** 
+-----------+------------+
| first_col | second_col |
+-----------+------------+
| 1         | 4          |
| 2         | 3          |
| 3         | 2          |
| 4         | 1          |
+-----------+------------+
```
