class Solution:
    def validSubarrays(self, nums: List[int], k: int) -> int:

        saddle = lambda x, y: y - x if y - x < k + 1 else k + 1
        lftSdle, midPk, ans, n  = 0, -1, 0, len(nums)

        for rgtPk in range(1, n - 1):
            if nums[rgtPk - 1] < nums[rgtPk] > nums[rgtPk + 1]:

                rgtSdle = saddle(midPk, rgtPk)
                ans+= lftSdle * rgtSdle
                lftSdle, midPk = rgtSdle, rgtPk
 
        ans+= lftSdle * saddle(midPk, n)

        return ans