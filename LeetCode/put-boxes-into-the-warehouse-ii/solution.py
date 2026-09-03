class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ans = lo = 0
        hi = len(warehouse)-1
        for box in sorted(boxes, reverse=True): 
            if lo <= hi: 
                if box <= warehouse[lo]: 
                    lo += 1
                    ans += 1
                elif box <= warehouse[hi]: 
                    hi -= 1
                    ans += 1
        return ans