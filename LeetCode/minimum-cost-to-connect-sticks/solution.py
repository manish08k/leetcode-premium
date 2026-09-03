class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        if len(sticks) <= 1:
            return 0

        heapq.heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            cost = x + y
            total_cost += cost
            heapq.heappush(sticks,cost)

        return total_cost