class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:
        cout = Counter(nums)
        return [k for k, v in cout.items() if v == 1]  + [k for k, v in cout.items() if v == 2]
       
        
        
            