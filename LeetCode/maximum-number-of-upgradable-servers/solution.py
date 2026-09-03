class Solution:
    def maxUpgrades(self, C: List[int], U: List[int], S: List[int], M: List[int]) -> List[int]:
        return [min(c, (s * c + m) // (u + s)) for c, u, s, m in zip(C, U, S, M)]