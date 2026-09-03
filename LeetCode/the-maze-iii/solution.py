class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        directions = [(1, 0, 'd'),  (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
        queue = collections.deque([(ball[0], ball[1], "", 0)])
        M, N, visited = len(maze), len(maze[0]), {}
        result = collections.defaultdict(list)
        res_length = float('inf')
        while(queue):
            i, j, path, distance = queue.popleft()
            visited[(i,j)] = (path, distance)
            for x, y, d in directions:
                row, col, dist = i, j, distance    
                while 0 <= row + x < M and 0 <= col + y < N and maze[row + x][col + y] == 0:
                    row, col, dist = row + x, col + y, dist + 1
                    if [row, col] == hole:       
                        res_length = min(res_length, dist)
                        result[dist].append(path + d)
                if(row, col) not in visited: 
                    queue.append((row, col, path + d, dist))
                elif visited[(row, col)][1] >= dist and visited[(row, col)][0] > path + d:  # edge case
                        visited[(row, col)] = (path + d, dist)     
                        queue.append((row, col, path + d, dist))  
        return "impossible" if( not result ) else sorted(result[res_length])[0]
    
        directions = [("l", 0,-1),("r", 0, 1),("u", -1, 0),("d",1,0)]
        
        rolling_directions = {
            "l" : (0,-1),
            "r" : (0, 1),
            "u": (-1, 0),
            "d":(1,0)
        }
        def dfs( i, j, path, distance, dir, visited ):            
            
            if( self.result and distance > self.result[1]):
                return False
                        
            if(dir): 
                dx, dy = rolling_directions[dir]
                
                while( 0 <= i + dx < len(maze) and 0 <= j +dy < len(maze[0]) and not (maze[i+dx][j+dy] == 1)):
                    i = i +dx
                    j = j +dy
                    
                    distance += 1
                    
                    if( i == hole[0] and j == hole[1] ):
                        if(self.result and self.result[1] >= distance or (not self.result) ):
                            if(self.result and self.result[1] == distance):
                                self.result =  (path[:], distance) if("".join(self.result[0]) > "".join(path[:]) ) else (self.result[0], distance)
                            else:
                                self.result = (path[:], distance)
                    
                    if( (i,j) in visited) : 
                        return False
                    
            if( i == hole[0] and j == hole[1] ):
                if(self.result and self.result[1] >= distance or (not self.result) ):
                    if(self.result and self.result[1] == distance):
                        self.result =  (path[:], distance) if("".join(self.result[0]) > "".join(path[:]) ) else (self.result[0], distance)
                    else:
                        self.result = (path[:], distance)
                        
            for new_dir, x, y in directions:
                if( (i+x, j+y) not in visited and 0 <= i + x < len(maze) and 0 <= j + y < len(maze[0]) and not maze[i+x][j+y] == 1 ):
                    
                    visited.add((i,j))
                    
                    dfs( i, j, path+[new_dir], distance, new_dir , visited )
                    
                    visited.remove((i,j))
        
        visited = set()
        path = []
        self.result = []
        dfs(ball[0], ball[1], path, 0, None, visited)
        return "".join(self.result[0]) if(self.result) else "impossible"
                