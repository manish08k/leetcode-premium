class StringIterator:
    def __init__(self, compressedString: str):
        self.q = deque()
        r = 0
        while r < len(compressedString):
            n = ""
            c = compressedString[r]
            r += 1
            while r < len(compressedString) and compressedString[r].isnumeric():
                n += compressedString[r]
                r += 1
            self.q.append([c, int(n)])
    def next(self) -> str:
        if self.hasNext():
            c = self.q[0][0]
            self.q[0][1] -= 1
            if self.q[0][1] == 0:
                self.q.popleft()
            return c
        else:
            return " "
    def hasNext(self) -> bool:
        return len(self.q) > 0

        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()