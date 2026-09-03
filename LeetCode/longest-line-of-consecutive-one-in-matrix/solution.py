class Solution:
    def draw_right(self, mat, r, c):
        cols = len(mat[0])
        for c_right in range(c + 1, cols + 1):
            if c_right == cols or mat[r][c_right] == 0:
                break
        return c_right - c

    def draw_down(self, mat, r, c):
        rows = len(mat)
        for r_down in range(r + 1, rows + 1):
            if r_down == rows or mat[r_down][c] == 0:
                break
        return r_down - r

    def draw_diagonal(self, mat, r, c):
        rows, cols = len(mat), len(mat[0])
        new_r, new_c = r, c
        while 1:
            new_r += 1
            new_c += 1
            if new_r == rows or new_c == cols or mat[new_r][new_c] == 0:
                break
        return new_r - r

    def draw_anti_diagonal(self, mat, r, c):
        rows = len(mat)
        new_r, new_c = r, c
        while 1:
            new_r += 1
            new_c -= 1
            if new_r == rows or new_c < 0 or mat[new_r][new_c] == 0:
                break
        return new_r - r

    def longestLine(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue
                right = self.draw_right(mat, r, c) if c == 0 or mat[r][c - 1] == 0 else 1
                down = self.draw_down(mat, r, c) if r == 0 or mat[r - 1][c] == 0 else 1
                diagonal = self.draw_diagonal(mat, r, c) if r == 0 or c == 0 or mat[r - 1][c - 1] == 0 else 1
                anti_diagonal = self.draw_anti_diagonal(mat, r, c) if r == 0 or c == cols - 1 or mat[r - 1][c + 1] == 0 else 1
                res = max(res, right, down, diagonal, anti_diagonal)
        return res