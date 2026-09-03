class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        res = 0
        state = 0
        mod = 10**9 + 7
        ct = Counter()
        n = len(nums)

        def qmi(a, b, mod):
            res = 1
            mi = a
            while b:
                if b & 1: res = ( res * mi) % mod
                b >>= 1
                mi = (mi * mi) % mod
            return res
        for i in range(k):
            ct[nums[i]] += 1
        
        for key in ct:
            # state = (state + key ** ct[key]) % mod
            state = (state + qmi(key, ct[key], mod)) % mod
        res = state

        for i in range(k, n):
            delnum = nums[i - k]
            newnum = nums[i]
            if delnum == newnum: continue
            precnt = ct[delnum]
            newcnt = ct[newnum] + 1
            diff1 = qmi(delnum, precnt, mod) - [0, qmi(delnum, precnt - 1, mod)][precnt - 1 != 0]
            diff2 = qmi(newnum, newcnt, mod) - [0, qmi(newnum, newcnt - 1, mod)][newcnt - 1 != 0]
            ct[delnum] -= 1
            ct[newnum] += 1
            state = (state + diff2 - diff1) % mod
            if state > res: res = state
        return res
