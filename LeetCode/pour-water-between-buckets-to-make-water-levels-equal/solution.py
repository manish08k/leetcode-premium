class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:

        f = lambda x, y: (sum(b-x for b in buckets[:y]) + 
                          sum(b-x for b in buckets[y:])*(1-loss/100)) > 0
        buckets.sort()
        l, r = min(buckets), sum(buckets) / len(buckets)
        while  r - l >= 0.00001:
            m = (l + r) / 2
            cut = bisect_left(buckets, m)
            if f(m, cut): l = m
            else        : r = m
        return l