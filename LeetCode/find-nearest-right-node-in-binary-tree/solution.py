# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:

        self.target_depth = -1
        self.ans = None

        def dfs(node,depth):
            if not node or self.ans:
                return
            
            if node == u:
                self.target_depth = depth

            elif self.target_depth == depth:
                self.ans = node
                return
            
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)

        dfs(root,0)

        return self.ans