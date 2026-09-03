class Solution:
    def numWays(self, n: int, k: int) -> int:
        arr = [0, k, k*k]
        while len(arr) <= n:
            arr.append(arr[-2]*(k-1) + arr[-1]*(k-1))
        return arr[n]