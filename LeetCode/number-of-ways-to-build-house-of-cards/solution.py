class Solution:
    def houseOfCards(self, n: int) -> int:
        @lru_cache(None)
        def dp(n, prev):
            if n <= 2:
                return int(n != 1)
            if prev < 2:
                return 0
            ans = 0
            for i in range(2, min(prev, (n+1)//3+1)):
                ans += dp(n - 3*i + 1, i)
            return ans
        return dp(n, 10**5)