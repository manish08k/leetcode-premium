class Solution:
    def maxCaloriesBurnt(self, heights: List[int]) -> int:

        heights.sort()
        ans = heights[~0]**2
        queue = deque(heights)

        while len(queue) > 1:
            ans+= (queue.pop() - queue[0])**2
            if len(queue) > 1:
                ans+= (queue.popleft() - queue[~0])**2

        return ans         