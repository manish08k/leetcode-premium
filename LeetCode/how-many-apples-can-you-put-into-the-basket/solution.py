class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        curr_sum=0
        for i,wt in enumerate(weight):
            curr_sum+=wt
            if curr_sum>5000:
                return i
        return i+1