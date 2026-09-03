class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        penality=0
        for days in daysLate:
            if days<=5 and days>=2:
                penality+=days*2
            elif days>5:
                penality+=days*3
            else:
                penality+=days
        return penality