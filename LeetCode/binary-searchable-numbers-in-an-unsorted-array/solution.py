class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        from collections import deque

        stack = deque()
        stack.append(nums[0])
        largest = nums[0]
        for i in range(1, len(nums)):
            is_invalid = False

            while stack and nums[i] < stack[-1]:
                stack.pop()
                is_invalid = True

            if not is_invalid and nums[i] > largest:
                stack.append(nums[i])
                largest = nums[i]

        return len(stack)

            