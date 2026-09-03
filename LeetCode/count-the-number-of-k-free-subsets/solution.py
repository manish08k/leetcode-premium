class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        size = defaultdict(int)
        for x in sorted(nums): 
            size[x] = size[x-k] + 1
            size.pop(x-k)
        m = max(size.values())
        fib = [1]*(m+2)
        for i in range(2, m+2): fib[i] = fib[i-2] + fib[i-1]
        return reduce(mul, (fib[v+1] for v in size.values()))