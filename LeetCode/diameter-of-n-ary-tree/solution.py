"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        def dfs(node):
            if not node.children:
                return 1
            maxDepth = 0
            for nextnode in node.children:
                d = dfs(nextnode)
                self.ans = max(self.ans,maxDepth+d)
                maxDepth = max(maxDepth,d)
            return maxDepth+1
        dfs(root)
        return self.ans