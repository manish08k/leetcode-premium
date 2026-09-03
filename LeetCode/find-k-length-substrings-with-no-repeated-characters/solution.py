class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        ans = 0
        c = Counter(S[:K])
        for i in range(K, len(S)):
            if len(c) == K:
                ans += 1
            c[S[i]] += 1
            c[S[i-K]] -= 1
            if c[S[i-K]] == 0:
                del c[S[i-K]]
        return ans + int(len(c) == K)