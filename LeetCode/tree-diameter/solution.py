class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for a, b in edges: 
            adj[a].add(b)
            adj[b].add(a)
            
        counter = 0 
        toRemove = []
        while len(adj) > 2: 
            for u in adj: 
                if len(adj[u]) == 1: 
                    toRemove.append(u)
            for u in toRemove: 
                v = adj[u].pop()
                adj.pop(u)
                adj[v].remove(u)
            toRemove = []
            counter += 2
            
        return counter + 1 if len(adj) == 2 else counter 