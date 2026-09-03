class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total, cur_total = 0, 0
        queue = deque(nestedList)
        
        while queue:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.isInteger():
                    cur_total += ele.getInteger()
                else:
                    queue.extend(ele.getList())      
            total += cur_total
                
        return total