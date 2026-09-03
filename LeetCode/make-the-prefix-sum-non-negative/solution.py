class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        cur,ans,heap=0,0,[]
        for num in nums:
            heapq.heappush(heap,num)
            cur+=num
            if cur<0:
                ans+=1
                cur-=heapq.heappop(heap)
        return ans