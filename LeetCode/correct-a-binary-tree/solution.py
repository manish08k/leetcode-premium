class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = [(root, None)]
        seen = set()
        for node, prev in queue: 
            if node.right and node.right.val in seen: 
                if node == prev.left: prev.left = None
                if node == prev.right: prev.right = None
                return root 
            seen.add(node.val)
            if node.right: queue.append((node.right, node))
            if node.left: queue.append((node.left, node))