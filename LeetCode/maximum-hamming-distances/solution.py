class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        dp = [-inf] * (1<<m)
        for num in nums:
            dp[num] = 0
        
        for bit in range(m):
            prev = dp[:] 
            for num in range(1<<m):
                dp[num] = max(dp[num], prev[num ^ (1<<bit)] + 1)

        return [dp[num] for num in nums]