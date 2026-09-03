# Convex Polygon

Problem: https://leetcode.com/problems/convex-polygon/

Solved on: 2026-08-06T18:45:30.000Z
Language: python3
Difficulty: Medium
Tags: Array, Math, Geometry, Polygons

---

You are given an array of points on the **X-Y** plane `points` where `points[i] = [xi, yi]`. The points form a polygon when joined sequentially.

Return `true` if this polygon is convex and `false` otherwise.

You may assume the polygon formed by given points is always a simple polygon. In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.

**Example 1:**

```
**Input:** points = [[0,0],[0,5],[5,5],[5,0]]
**Output:** true
```

**Example 2:**

```
**Input:** points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
**Output:** false
```

**Constraints:**

	- `3 <= points.length <= 10^4`

	- `points[i].length == 2`

	- `-10^4 <= xi, yi <= 10^4`

	- All the given points are **unique**.
