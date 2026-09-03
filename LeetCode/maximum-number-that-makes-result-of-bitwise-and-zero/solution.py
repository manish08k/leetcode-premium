class Solution:
    def maxNumber(self, n: int) -> int:
        return 2 ** floor(log2(n)) - 1