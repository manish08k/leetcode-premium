class FileSharing:
    def __init__(self, m):
        self.available = []
        self.dict1 = defaultdict(set)

        for i in range(1,m+1):
            heapq.heappush(self.available,i)

    def join(self, ownedChunks):
        userId = heapq.heappop(self.available)
        self.dict1[userId] = set(ownedChunks)
        return userId

    def leave(self, userID):
        if userID in self.dict1:
            del self.dict1[userID]
            heapq.heappush(self.available,userID)
    
    def request(self, userID, chunkID):
        ans = []

        for a in self.dict1:
            if chunkID in self.dict1[a]:
                ans.append(a)

        if len(ans) > 0:
            self.dict1[userID].add(chunkID)

        return sorted(ans) 