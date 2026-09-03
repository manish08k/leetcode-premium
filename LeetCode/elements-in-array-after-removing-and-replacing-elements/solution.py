class Solution:
    def elementInNums(self, n: List[int], queries: List[List[int]]) -> List[int]:
        return [-1 if i >= abs(t - len(n)) else n[i + (t if t < len(n) else 0)] for t, i in [(t % (2 * len(n)), i) for t, i in queries]]