# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node,prev_val,a):
            if node is None:
                return a
            if node.val==prev_val+1:
                a+=1
            else:
                a=1
            left_len=dfs(node.left,node.val,a)
            right_len=dfs(node.right,node.val,a)
            return max(a,left_len,right_len)
        return dfs(root,root.val-1,0)