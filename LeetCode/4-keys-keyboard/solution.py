class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(7, n + 1):
            dp[i] = max(
                2 * dp[i - 3],
                3 * dp[i - 4],
                4 * dp[i - 5],
            )
        return dp[n]