class Solution:
    def stringShift(self, s, shift):
        return (lambda n, cc: ''.join(s[(i + cc) % n] for i in range(n)))(len(s), reduce(lambda p, a: p+(1 if a[0] == 0 else -1) * a[1], shift, 0))            