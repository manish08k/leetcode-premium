class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = m = len(matrix)
        self.n = n = len(matrix[0])

        self.tree = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        self.aux = [
            [0] * n
            for _ in range(m)
        ]

        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.aux[row][col]  
        self.aux[row][col] += delta

        i = row + 1
        while i <= self.m:
            j = col + 1 
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & -j 
            i += i & -i

        
    def sumRegion(self, a: int, b: int, c: int, d: int) -> int:
        def query(i, j):
            acc = 0
            while i > 0:
                k = j
                while k > 0:
                    acc += self.tree[i][k]
                    k -= k & -k 
                i -= i & -i
            return acc 

        region =  query(c + 1, d + 1)
        region -= query(c + 1, b)
        region -= query(a, d + 1)
        region += query(a, b)

        return region 


        