class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        invert={
            '0':'0',
            '1':'1',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        for i in range((len(num))+1//2):
            if num[i]!=invert.get(num[~i]):
                return False
        return True