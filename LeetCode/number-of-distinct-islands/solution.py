class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        coords = ((0, 1), (1, 0), (-1, 0), (0, -1))
        res = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    curr = []
                    queue = deque([(i, j)])

                    while queue:
                        y, x = queue.popleft()
                        for dy, dx in coords:
                            dy += y
                            dx += x
                            if 0 <= dy < m and 0 <= dx < n and grid[dy][dx]:
                                grid[dy][dx] = 0
                                queue.append((dy, dx))
                                curr.append((dy - i, dx - j))
                        
                    res.add(tuple(curr))

        return len(res)