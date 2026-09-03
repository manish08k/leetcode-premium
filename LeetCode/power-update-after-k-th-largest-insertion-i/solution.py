class Solution:
    def powerUpdate(self, A: list[int], p: int, queries: list[list[int]]) -> list[int]:
        maxHeap = []
        minHeap = []

        for e in A:
            heapq.heappush(minHeap, e)

        ans = []
        mod = 10**9 + 7

        for q in queries:
            val, k = q

            if val > minHeap[0]:
                heapq.heappush(minHeap, val)
            else:
                heapq.heappush(maxHeap, -val)

            while len(minHeap) < k:
                v = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, v)

            while len(minHeap) > k:
                v = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -v)

            kthLargest = minHeap[0]

            p = pow(p, kthLargest, mod)
            ans.append(p)

        return ans