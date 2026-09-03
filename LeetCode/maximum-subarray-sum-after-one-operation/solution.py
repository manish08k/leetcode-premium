class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        res = 0
        a, b = 0, 0 

        for val in nums:
            x = b + val * val
            y = a + val

            a = max(x, y)
            b = max(0, b + val)

            res = max(res, a, b)

        return res