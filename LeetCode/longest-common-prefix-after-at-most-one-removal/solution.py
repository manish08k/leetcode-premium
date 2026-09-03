class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        # Greedy. When I meet different character from s for the first time. I should remove it.

        ans = 0
        chance = 1
        sIdx = 0
        tIdx = 0
        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] != t[tIdx]:
                if chance > 0:
                    sIdx += 1
                    chance -= 1
                    continue
                else:
                    break
            sIdx+=1
            tIdx+=1
            ans += 1
        
        return ans