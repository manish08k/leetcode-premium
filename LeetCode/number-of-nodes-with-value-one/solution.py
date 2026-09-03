class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        flips = [0 for _ in range(n + 1)]
        nodes_with_ones = 0
        for q in queries: flips[q] += 1
        for i in range(1, n + 1): flips[i] += flips[i // 2]
        for i in range(1, n + 1): nodes_with_ones += flips[i] % 2

        return nodes_with_ones