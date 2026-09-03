class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        out=""
        k+=1
        while k!=1:
            out=('7' if k&1 else '4')+out
            k//=2
        return out