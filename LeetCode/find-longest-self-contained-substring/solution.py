class Solution:
    def maxSubstringLength(self, s: str) -> int:
        
        loc = defaultdict(list)
        for i, x in enumerate(s):
            loc[x].append(i)
        
        def check(l, r):
            for k in loc:
                x, y = bisect.bisect_left(loc[k], l), bisect.bisect(loc[k], r)
				
                if not (y - x == len(loc[k]) or x == y):
                    return False
            return True
        
        ans = -1
        for k1 in loc:
            a = loc[k1][0]
            for k2 in loc:
                b = loc[k2][-1]
                if a > b or b - a + 1 == len(s): continue
                if check(a, b):
                    ans = max(ans, b - a + 1)
        
        return ans