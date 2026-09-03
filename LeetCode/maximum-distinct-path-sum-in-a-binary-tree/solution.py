class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        g = defaultdict(set); g[root] = set()
        def construct_graph(node):
            if node is None: return 
            if node.left:
                g[node].add(node.left); g[node.left].add(node)
                construct_graph(node.left)
            if node.right:
                g[node].add(node.right); g[node.right].add(node)                
                construct_graph(node.right)
        construct_graph(root)
        def dfs(node, p=None, seen = set()):
            if node is None or node.val in seen: return 0
            seen.add(node.val)
            ans = max((dfs(to, node, seen) for to in g[node] if to != p), default=-inf)
            seen.remove(node.val)
            return max(ans + node.val, node.val)
        return max(dfs(node) for node in g)
            