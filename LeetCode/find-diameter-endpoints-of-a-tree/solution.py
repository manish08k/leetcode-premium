class Solution:
    def treeit(self, edges):
        g = defaultdict(set)
        for a,b in edges:g[a].add(b);g[b].add(a);
        return g       
    def dist(self, n, g, source):
        dist, qu = [-1] * n, deque([source])
        dist[source] = 0
        while qu:
            node = qu.popleft()
            for to in g[node]:
                if dist[to] == -1: dist[to] = dist[node] +  1;qu.append(to);
        return dist, max(dist)
    def findSpecialNodes(self, n: int, edges: List[List[int]]) -> str:
        g = self.treeit(edges)
        a, ad = self.dist(n, g, 0)
        b, d = self.dist(n, g, a.index(ad))        
        c = self.dist(n, g, b.index(d))[0]
        return ''.join(d in (b[i], c[i]) and '1' or '0' for i in range(n))