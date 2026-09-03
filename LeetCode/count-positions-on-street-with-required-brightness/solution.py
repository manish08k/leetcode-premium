class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:        
        switch = defaultdict(int)

        for pos, sz in lights:
            up = max(0, pos-sz)
            down = min(n-1, pos+sz) + 1

            switch[up] += 1
            switch[down] -= 1

        cur = 0
        ans = 0

        for i in range(n):
            cur += switch[i]
            if cur >= requirement[i]:
                ans += 1
        
        return ans