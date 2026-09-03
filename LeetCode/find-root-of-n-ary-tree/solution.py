"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ans=0
        for x in tree:
            ans=ans^x.val
            for ch in x.children:
                ans=ans^ch.val
        for node in tree:
            if node.val==ans:
                return node