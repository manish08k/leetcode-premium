class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        ans = sum(nums[0:k])
        if ans%2 == 0:
            return ans
        lastEven = None
        lastOdd = None
        for i in range(k):
            if nums[i]%2 == 0:
                lastEven = nums[i]
            else:
                lastOdd = nums[i]
        nextEven = None
        nextOdd = None
        i = k
        while (nextEven is None or nextOdd is None) and (i < len(nums)):
            if nums[i]%2 == 0:
                if nextEven is None:
                    nextEven = nums[i]
            else:
                if nextOdd is None:
                    nextOdd = nums[i]
            i += 1
        if nextEven is not None and lastOdd is not None:
            ans1 = ans - lastOdd + nextEven
        else:
            ans1 = -1
        if nextOdd is not None and lastEven is not None:
            ans2 = ans - lastEven + nextOdd
        else:
            ans2 = -1
        return max(ans1, ans2)