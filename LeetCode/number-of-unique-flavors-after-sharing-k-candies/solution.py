class Solution:
    def shareCandies(self, A: List[int], k: int) -> int:
        hm = dict()
        
        for e in A:
            if e not in hm:
                hm[e] = 1
            else:
                hm[e] += 1
        
        for i in range(k):
            hm[A[i]] -= 1
            if hm[A[i]] == 0:
                del hm[A[i]]
        ans = len(hm)

        for i in range(k, len(A)):
            if A[i-k] not in hm:
                hm[A[i-k]] = 1
            else:
                hm[A[i-k]] += 1
            
            hm[A[i]] -= 1
            if hm[A[i]] == 0:
                del hm[A[i]]
            
            ans = max(ans, len(hm))
        
        return ans