class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max((i for i in counter if counter[i] == 1), default=-1)