class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        ROWS,COLS = len(grid),len(grid[0])

        pq = [(-grid[0][0],0,0)]

        visited = set()
        visited.add((0,0))

        result = grid[0][0]

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        while pq:
            val,r,c = heapq.heappop(pq)
            val = -val

            result = min(result,val)

            if r == ROWS-1 and c == COLS-1:
                return result

            for dr,dc in directions:
                nr,nc = r + dr,c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(pq,(-grid[nr][nc],nr,nc))

        return result
        