class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        mp, stack = {None: (0, 0)}, []
        node, prev = root, None
        while node or stack: 
            if node: 
                stack.append(node)
                node = node.left
            else: 
                node = stack[-1]
                if node.right and node.right != prev: node = node.right
                else: 
                    mp[node] = [1, 1]
                    if node.left:
                        if node.left.val + 1 == node.val: mp[node][0] = 1 + mp[node.left][0]
                        if node.left.val - 1 == node.val: mp[node][1] = 1 + mp[node.left][1]
                    if node.right: 
                        if node.right.val + 1 == node.val: mp[node][0] = max(mp[node][0], 1 + mp[node.right][0])
                        if node.right.val - 1 == node.val: mp[node][1] = max(mp[node][1], 1 + mp[node.right][1])
                    ans = max(ans, sum(mp[node]) - 1)
                    stack.pop()
                    prev = node
                    node = None
        return ans 