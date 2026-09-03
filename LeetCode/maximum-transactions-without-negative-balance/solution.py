class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        amt, cnt = 0, 0
        heap = []
        for i, x in enumerate(transactions):
            amt += x
            cnt += 1
            if x < 0: 
                heapq.heappush(heap, x)

            if amt < 0:
                val = heapq.heappop(heap)
                amt -= val
                cnt -= 1
        return cnt 