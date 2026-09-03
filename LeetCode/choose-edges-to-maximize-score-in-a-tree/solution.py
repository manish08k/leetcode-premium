class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, [par, weight] in enumerate(edges):
            if i == 0: continue
            g[par].append(i)
        def dfs(node):
            if len(g[node]) == 0:
                return edges[node][1], 0
            if node == 0:
                cur_choose = 0
            else:
                cur_choose = edges[node][1]
            sub_choose, sub_skip = [], []
            for nei in g[node]:
                c, s = dfs(nei)
                sub_choose.append(c)
                sub_skip.append(s)
            max_sub_choose, max_sub_skip = -float('inf'), sum(sub_skip)
            for i, c in enumerate(sub_choose):
                max_sub_choose = max(max_sub_choose, sub_choose[i] + max_sub_skip - sub_skip[i])
            return cur_choose + max_sub_skip, max(max_sub_choose, max_sub_skip)
        return max(dfs(0))