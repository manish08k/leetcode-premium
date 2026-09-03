class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        
        def fn(node, prev=None): 
            """Return updated node."""
            if node == root: 
                if prev == node.left: node.left = None
                else: node.right = None
            else: 
                if prev == node.right: node.right = node.left
                node.left = fn(node.parent, node)
            node.parent = prev
            return node 
        
        return fn(leaf)