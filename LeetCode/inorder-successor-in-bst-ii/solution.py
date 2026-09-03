"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        found = None
        ready = False
        def r(n):
            nonlocal found, node, ready
            if n is None or found is not None:
                return
            r(n.left)
            if found is not None:
                return
            if ready:
                found = n
                return
            if n == node:
                ready = True
            r(n.right)
        root = node
        print(node.val)
        while root.parent is not None:
            root = root.parent
        r(root)
        return found