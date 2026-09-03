class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        r, c = [[] for _ in range(m)], [[] for _ in range(n)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                h = heights[i][j]
                while r[i] and r[i][-1] < h:
                    r[i].pop()
                    res[i][j] += 1
                if r[i] and r[i][-1] >= h:
                    if r[i][-1] == h: r[i].pop()
                    res[i][j] += 1
                r[i].append(h)

                while c[j] and c[j][-1] < h:
                    c[j].pop()
                    res[i][j] += 1
                if c[j] and c[j][-1] >= h:
                    if c[j][-1] == h: c[j].pop()
                    res[i][j] += 1
                c[j].append(h)

        return res