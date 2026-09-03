class Solution:
    def removeOnes(self, A: List[List[int]]) -> int:

        m = len(A)
        n = len(A[0])
        lst = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    lst.append((i, j))

        def check(A):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        return False
            return True

        self.ans = float('inf')
        def helper(idx, cnt):
            if check(A):
                self.ans = min(self.ans, cnt)
                return
            if idx >= len(lst) or self.ans <= cnt:
                return

            r = lst[idx][0]
            c = lst[idx][1]

            removedCells = []
            for i in range(m):
                if A[i][c] == 1:
                    removedCells.append((i,c))
                    A[i][c] = 0
            for j in range(n):
                if A[r][j] == 1:
                    removedCells.append((r,j))
                    A[r][j] = 0
            helper(idx+1, cnt+1)
            for e in removedCells:
                i, j = e
                A[i][j] = 1

            helper(idx+1, cnt)
        
        helper(0, 0)

        return self.ans