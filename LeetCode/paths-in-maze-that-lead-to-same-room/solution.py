class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        s = set()
        for r1, r2 in corridors:
            if r1 < r2:
                graph[r1].append(r2)
                s.add((r2, r1))
            else:    
                graph[r2].append(r1)
                s.add((r1, r2))
        ans = 0        
        for node in range(1, n+1):
            for nei in graph[node]:
                for nei_nei in graph[nei]:
                    ans += 1 if (nei_nei, node) in s else 0
        return ans