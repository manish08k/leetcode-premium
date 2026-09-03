# Meeting Rooms

Problem: https://leetcode.com/problems/meeting-rooms/

Solved on: 2026-08-21T17:50:48.000Z
Language: python3
Difficulty: Easy
Tags: Array, Sorting, Quicksort

---

You are given an array of meeting times `intervals` where `intervals[i] = [starti, endi]`.

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time `t` and starting at time `t` **do not** overlap.

​​​​​​​Return `true` if a person can attend all meetings. Otherwise, return `false`.

**Example 1:**

```
**Input:** intervals = [[0,30],[5,10],[15,20]]
**Output:** false
```

**Example 2:**

```
**Input:** intervals = [[7,10],[2,4]]
**Output:** true
```

**Constraints:**

	- `0 <= intervals.length <= 10^4`

	- `intervals[i].length == 2`

	- `0 <= starti < endi <= 10^6`
