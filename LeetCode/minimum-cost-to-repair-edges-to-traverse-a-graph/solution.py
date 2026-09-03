class Solution:
    def minCost(self, n: int, edges: list[list[int]], k: int) -> int:

        def bfs(wgt: int)-> bool:
            queue, seen = deque([(0, k)]), [False] * n

            while queue:
                if queue[-1][0] == n - 1: return True
                node, steps = queue.pop()

                if steps > 0:
                    for nxt, w in graph[node]:
                        if seen[nxt] or w > wgt: continue
                        queue.appendleft((nxt, steps - 1))
                        seen[nxt] = True           
            return False 


        graph = defaultdict(list)
        mxWgt = 0

        for u, v, wgt in edges:
            graph[u].append((v, wgt))
            graph[v].append((u, wgt))
            if wgt > mxWgt: mxWgt = wgt

        mnWgt = bisect_left(range(mxWgt + 1), True, key = bfs)
        return -1 if mnWgt > mxWgt else mnWgt