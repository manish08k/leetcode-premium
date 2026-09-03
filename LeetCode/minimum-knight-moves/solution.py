class Solution:
    def minKnightMoves(self, s: int, e: int) -> int:
        q = collections.deque()
        q.append([0,0,0])
        visited = set()
        visited.add((0,0))
        while q:
            x,y,steps = q.popleft()
            if x==s and y==e:
                return steps
            dirs = [(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y-2),(x+2,y-1),(x+1,y+2),(x+2,y+1)]
            for i,j in dirs:
                if (i,j) not in visited:
                    q.append([i,j,steps+1])
                    visited.add((i,j))
        return -1