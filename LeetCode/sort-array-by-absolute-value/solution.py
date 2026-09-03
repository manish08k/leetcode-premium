class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if abs(nums[j]) > abs(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums