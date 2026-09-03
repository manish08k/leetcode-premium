class Solution:
    def earliestAcq(self, logs, n):
        par = list(range(n))

        def find(u):
            if u != par[u]:
                par[u] = find(par[u])
            return par[u]

        def join(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2: return False
            if p1 > p2: par[p1] = p2
            else: par[p2] = p1
            return True

        logs.sort()
        for timestamp, x, y in logs:
            if join(x, y): n -= 1
            if n == 1: return timestamp
        return -1