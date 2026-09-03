class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i, j):
            if i < 0:
                return 0 if j == 1 else -inf
            if j == 0:
                return max(nums[i], dfs(i - 1, 1) + nums[i])
            else:
                return dfs(i - 1, 0) - nums[i]
        ans = -inf
        for i in range(n):
            ans = max(ans, dfs(i, 1), dfs(i, 0))
        return ans