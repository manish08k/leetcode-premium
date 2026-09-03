"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        a,b=[node.val],[]
        l,r=node.prev,node.next
        while l:
            a.append(l.val)
            l=l.prev
        while r:
            b.append(r.val)
            r=r.next
        return a[::-1]+b