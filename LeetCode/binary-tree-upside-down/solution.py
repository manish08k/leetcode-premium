# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root

        newRoot = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return newRoot