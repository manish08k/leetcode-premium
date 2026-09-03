class Solution:
    def countSubranges(self, n1: List[int], n2: List[int]) -> int:
        @cache
        def dfs(i: int, bal: int) -> int:
            return (bal == 0) + (0 if i >= len(n1) else dfs(i + 1, bal + n1[i]) + dfs(i + 1, bal - n2[i]))
        return sum(dfs(i, 0) - 1 for i in range(len(n1))) % 1000000007 