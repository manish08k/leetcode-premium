class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        from sortedcontainers import SortedList
        sl, d = SortedList([0, 100001]), { 0 : 0, 100001 : 0 }
        for i in order:
            j = sl.bisect_left(i)
            d[i] = 1 + max(d[sl[j - 1]], d[sl[j]])
            sl.add(i)
        return max(d.values())