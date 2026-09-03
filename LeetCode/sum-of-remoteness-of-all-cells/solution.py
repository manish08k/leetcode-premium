
class Solution:
    def __init__(self):
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]

    def dfs(self, x, y, g):
        if x < 0 or x >= len(g) or y < 0 or y >= len(g[0]) or g[x][y] < 0:
            return (0, 0)

        r = (g[x][y], 1)
        g[x][y] = -1

        for i in range(4):
            p = self.dfs(x + self.dx[i], y + self.dy[i], g)
            r = (r[0] + p[0], r[1] + p[1])

        return r

    def sumRemoteness(self, grid: List[List[int]]) -> int:
        s = 0
        for row in grid:
            for x in row:
                s += max(x, 0)

        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    p = self.dfs(i, j, grid)
                    r += (s - p[0]) * p[1]

        return r