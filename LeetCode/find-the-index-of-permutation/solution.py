from sortedcontainers import SortedList

class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        ans = 0
        M = 10 ** 9 + 7
        n = len(perm)
        prev = SortedList()
        f = {0: 0}
        tmp = 1
        for i in range(1, n+1):            
            tmp = (tmp * i) % M
            f[i] = tmp
        for i, x in enumerate(perm, 1):
            loc = bisect.bisect(prev, x)
            ans = (ans + max(x - loc - 1, 0) * f[n-i]) % M
            prev.add(x)
            
        return ans