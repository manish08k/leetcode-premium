# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        if s.isnumeric():
            return Node(s)
        if len(s) == 0:
            return None


        plus = s.find('+')
        paren = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                paren +=1
            elif s[i] == '(':
                paren -=1
            if paren > 0:
                continue
            if s[i] == '+':
                return Node('+', self.expTree(s[:i]), self.expTree(s[i+1:]))
            if s[i] == '-':
                return Node('-', self.expTree(s[:i]), self.expTree(s[i+1:]))
            
        paren = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                paren +=1
            elif s[i] == '(':
                paren -=1
            if paren > 0:
                continue
            if s[i] == '*':
                return Node('*', self.expTree(s[:i]), self.expTree(s[i+1:]))
            if s[i] == '/':
                return Node('/', self.expTree(s[:i]), self.expTree(s[i+1:]))
        if s[0] == '(' and s[-1] == ')':
            return self.expTree(s[1:-1])
        