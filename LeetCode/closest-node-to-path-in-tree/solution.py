from collections import defaultdict
class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        #1. Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #2. Set up for binary listing
        LOG = 11
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n

        #3. Precompute depths and the 'up' table via DFS
        def dfs(node, parent, d):
            up[node][0] = parent
            depth[node] = d

            #compute 2 power i ancestor
            for i in range(1, LOG):
                up[node][i] = up[up[node][i - 1]][i - 1]

            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
        
        dfs(0, 0, 0)

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG - 1, -1, -1):
                #diff can be written to the power of i
                if (diff >> i) & 1:
                    u = up[u][i]
                
            if u == v:
                return u
                
            #Climb together
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
                
            return up[u][0]

        ans = []
        for start, end, target in query:
            lca2 = get_lca(start, target)
            lca1 = get_lca(start, end)
            lca3 = get_lca(end, target)

            closest = lca1
            if depth[lca2] > depth[closest]:
                closest = lca2
            if depth[lca3] > depth[closest]:
                closest = lca3
            ans.append(closest)
        return ans

                