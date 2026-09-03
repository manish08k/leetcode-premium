class Solution:
    def sumOfBlocks(self, n: int) -> int:
        return( lambda m: sum(reduce(lambda p, a: (p * a) % m, range(1 + (i - 1) * i // 2, 1 + (i - 1) * i // 2 + i)) for i in range(1, n + 1))%m)(1_000_000_007)
            