"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
            
        def _to_doubly_list(node):
            # turns the tree into a doubly linked list and return head and tail
            if not node:
                return None, None
            head1, tail1 = _to_doubly_list(node.left)
            head2, tail2 = _to_doubly_list(node.right)
            
            if tail1:
                tail1.right = node
                node.left = tail1 
            if head2:
                head2.left = node
                node.right = head2
            
            head = head1 or node
            tail = tail2 or node
            return head, tail 

        head, tail = _to_doubly_list(root)
        head.left = tail
        tail.right = head
        return head