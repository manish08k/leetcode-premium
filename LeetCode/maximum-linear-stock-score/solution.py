class Solution:
    def maxScore(self, prices: List[int]) -> int:

        hm = defaultdict(int)

        for i, p in enumerate(prices):
            hm[p-i] += p

        return max(hm.values())
        