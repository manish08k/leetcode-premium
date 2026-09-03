class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        deque = collections.deque([(val,0) for val in windows])
        dct = collections.Counter()
        for num in queries:
            dct[num] += 1
            deque.appendleft((num,dct[num]))
        return [val for val,count in deque if count == dct[val]]

