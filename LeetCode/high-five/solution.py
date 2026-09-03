class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heaps = defaultdict(list)

        for sid, score in items:
            heap = heaps[sid]
            if len(heap) < 5:
                heappush(heap, score)
            else:
                heappushpop(heap, score)

        return [[sid, sum(heap) // 5] for sid, heap in sorted(heaps.items())]