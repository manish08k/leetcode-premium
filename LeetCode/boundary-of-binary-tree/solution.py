# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        def preorder(node, is_leftb):
            if is_leftb or not (node.left or node.right):
                ans.append(node.val)
            if node.left:
                preorder(node.left, is_leftb)
            if node.right:
                preorder(node.right, not node.left and is_leftb)
        def postorder(node, is_rightb):
            if node.left:
                postorder(node.left, not node.right and is_rightb)
            if node.right:
                postorder(node.right, is_rightb)
            if is_rightb or not (node.left or node.right):
                ans.append(node.val)
        if root.left:
            preorder(root.left, True)
        if root.right:
            postorder(root.right, True)
        return ans
