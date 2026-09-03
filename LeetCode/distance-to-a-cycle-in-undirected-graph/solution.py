class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        
        s = set(list(range(n)))
        dq = collections.deque()
        for i in range(n):
            if in_degree[i] == 1: dq.append(i)
        
        while dq:
            u = dq.popleft()
            in_degree[u] -= 1
            s.remove(u)
            for v in g[u]:
                in_degree[v] -= 1
                if in_degree[v] == 1: dq.append(v)
        
        res = [-1 for _ in range(n)]
        distance = 0
        dq = collections.deque(list(s))
        while dq:
            l = len(dq)
            for _ in range(l):
                u = dq.popleft()
                if res[u] != -1: continue
                res[u] = distance
                for v in g[u]:
                    if res[v] == -1: dq.append(v)
            distance += 1
        return res