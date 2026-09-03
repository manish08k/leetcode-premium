class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mod = 1_000_000_007
        n = len(nums)
        r = isqrt(n)
        dp = [[0]*r for _ in range(n)]
        for i in range(n-1, -1, -1): 
            for j in range(r): 
                dp[i][j] = nums[i]
                if i+j < n: dp[i][j] = (dp[i][j] + dp[i+j][j]) % mod
        ans = []
        for x, y in queries: 
            if y < r: ans.append(dp[x][y])
            else: 
                val = 0 
                for j in range(x, n, y): 
                    val = (val + nums[j]) % mod
                ans.append(val) 
        return ans