class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def f(t):
            ans=False
            l=list(t)
            for i in range(len(l)):
                for j in range(1,l[i]+1):
                    l[i]-=j
                    ans=ans or not f(tuple(l))
                    l[i]+=j
            
            return ans
        
        return f(tuple(piles))