import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        emptyRoom = 2147483647
        wall = -1
        gate = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        m = len(rooms)
        n = len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    q.append([i, j])

        distance = 0
        while q:
            size = len(q)
            distance += 1
            while size > 0:
                size -= 1
                room = q.popleft()
                x, y = room
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and rooms[i][j] == emptyRoom:
                        rooms[i][j] = distance
                        q.append([i, j])
