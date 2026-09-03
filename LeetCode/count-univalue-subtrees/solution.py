# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return None
            left=dfs(node.left)
            right=dfs(node.right)
            if node.left and left!=node.val:
                return float('inf')
            if node.right and right!=node.val:
                return float('inf')
            ans+=1
            return node.val
        dfs(root)
        return ans