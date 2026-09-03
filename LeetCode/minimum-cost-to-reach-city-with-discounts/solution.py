from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adjDict = defaultdict(list)
        for u, v, toll in highways:
            adjDict[u].append((v, toll))
            adjDict[v].append((u, toll))

        q = deque([])

        q.append((0, 0, []))
        dp = [float("+inf")] * n
        dp[0] = 0
        res = float("+inf")
        while q:
            (effort, u, cost) = q.popleft()
            if u == n - 1:
                cost = sorted(cost, reverse=True)
                total = 0

                for i in range(min(discounts, len(cost))):
                    total += cost[i] // 2

                for i in range(discounts, len(cost)):
                    total += cost[i]

                res = min(res, total)

                continue

            for v, toll in adjDict[u]:
                nextEffort = toll + effort
                if nextEffort < dp[v]:
                    dp[v] = nextEffort
                    q.append((nextEffort, v, cost + [toll]))

        return res if res != float("+inf") else -1
