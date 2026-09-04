# The read4 API is already defined for you.
# def read4(buf4):

class Solution(object):

    def __init__(self):
        self.buf4 = [""] * 4
        self.ptr = 0
        self.cnt = 0

    def read(self, buf, n):
        i = 0

        while i < n:
            if self.ptr == self.cnt:
                self.cnt = read4(self.buf4)
                self.ptr = 0
                if self.cnt == 0:
                    break

            while i < n and self.ptr < self.cnt:
                buf[i] = self.buf4[self.ptr]
                i += 1
                self.ptr += 1

        return i