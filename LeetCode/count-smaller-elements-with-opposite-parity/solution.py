class Solution:
    def countSmallerOppositeParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        odd=SortedList()
        even=SortedList()
        for i in range(n-1,-1,-1):
            cnt=0
            if nums[i]%2==0:
                even.add(nums[i])
                cnt=odd.bisect_left(nums[i])
            else:
                odd.add(nums[i])
                cnt=even.bisect_left(nums[i])
            ans[i]=cnt
        return ans