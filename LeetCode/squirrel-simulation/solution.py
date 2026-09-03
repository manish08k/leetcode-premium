class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        baseline = 0
        minExtra = float('inf')
        for nut in nuts:
            ds = dist(squirrel, nut)
            dt = dist(nut, tree)
            baseline += 2*dt
            extra = ds - dt
            if extra < minExtra:
                minExtra = extra
        return baseline + minExtra