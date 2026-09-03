class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        return self.kpletCount([a,b,c])

    def kpletCount(self, arrs: List[List[int]]) -> int:
        odd, even = 0, 1
        for arr in arrs:
            oddA, evenA = self.cnts(arr)
            odd, even = odd*evenA + even*oddA, odd*oddA + even*evenA
        return even
        
    def cnts(self, arr: List[int]) -> (int, int):
        odd = sum(num.bit_count() & 1 for num in arr)
        even = len(arr) - odd
        return odd, even