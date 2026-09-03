class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_value = max_index = nums[0]
        min_index = max_value = 0
        for i, n in enumerate(nums):
            if n < min_value:
                min_value = n
                min_index = i
            
            if n >= max_value:
                max_value = n
                max_index = i
                
        return min_index + len(nums) - 1 - max_index - (min_index > max_index)