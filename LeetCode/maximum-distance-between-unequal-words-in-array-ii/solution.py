class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n=len(words)
        for i in range((n+1)//2):
            if words[i]==words[0]==words[~i]:
                continue
            return n-i
        return 0