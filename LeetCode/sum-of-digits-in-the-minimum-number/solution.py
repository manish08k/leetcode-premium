class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        sum_ = 0
        while min_num > 0:
            sum_ += min_num % 10
            min_num = min_num // 10
        return 1 if sum_ % 2 == 0 else 0