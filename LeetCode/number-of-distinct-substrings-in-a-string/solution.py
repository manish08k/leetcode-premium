class Solution:
    def countDistinct(self, s: str) -> int:
        trie = {}
        res = 0
        for i in range(len(s)):
            node = trie
            for j in range(i, len(s)):
                if s[j] not in node:
                    node[s[j]] = {'end': True} 
                node = node[s[j]]
                if node['end'] == True:
                    node['end'] = False
                    res += 1
        return res