class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        lookup = defaultdict(list)
        for u, v in roads:
            lookup[u].append(v)
            lookup[v].append(u)

        convert = defaultdict(int)
        for index, x in enumerate(names):
            convert[x] |= (1 << index)

        A = []

      
        for x in targetPath:
            A.append(convert[x])
        N = len(A)
        @cache
        def calc(index, u):
            if index == N - 1:
                return (1-int((A[index] & (1<<u)) > 0)), [u]

            best = 10 ** 10
            L = []

            for v in lookup[u]:
                val, X = calc(index + 1, v)
                if val < best:
                    best = val
                    L = X
           
            return best +  (1-int((A[index] & (1<<u)) > 0)), [u] + L 


        
        best = 10 ** 10
        ans = []
        for i in range(n):
            val, X = calc(0, i)
        

            if val < best:
                best = val
                ans = X

        return ans