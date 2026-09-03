class Solution:
    def goodIndices(self, s: str) -> List[int]:  
        return [i for i in range(len(s)) if str(i)==s[i-(len(str(i))-1):i+1]]