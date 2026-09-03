class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        dp = [[-1] * n for _ in range(m)]

        for j in range(n):
            if s1[j] == s2[0]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if s1[j] == s2[i]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        start, minLen = 0, float('inf')
        for j in range(n):
            if dp[m-1][j] != -1:
                if j - dp[m-1][j] + 1 < minLen:
                    minLen = j - dp[m-1][j] + 1
                    start = dp[m-1][j]

        return "" if minLen == float('inf') else s1[start:start+minLen]