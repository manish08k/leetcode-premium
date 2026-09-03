class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
   
        if not maze or not maze[0]:
            return -1
            
        m,n = len(maze), len(maze[0])
        visited = set()

        pq = [(0, start[0], start[1])]

        while pq:
            dist, x, y = heapq.heappop(pq)

            if x == destination[0] and y == destination[1]:
                return dist

            if (x,y) in visited:
                continue
            visited.add((x,y))

            for dx, dy in[[0,1],[0,-1],[1,0],[-1,0]]:
                steps = 0 
                new_x, new_y = x, y 

                while (0 <= new_x + dx < m 
                    and 0 <= new_y + dy < n 
                    and maze[new_x + dx][new_y + dy] != 1):
             
                    steps += 1
                    new_x += dx
                    new_y += dy

                if (new_x, new_y) in visited:
                    continue

                heapq.heappush(pq, (steps + dist, new_x, new_y))

        return -1

 