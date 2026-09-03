class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        dp=[0]*60000
        ans=[]
        for (start,end) in paint:
            ans.append(0)
            ind=start
            while ind<end:
                if dp[ind]==0:
                    dp[ind]=end
                    ans[-1]+=1
                    ind+=1
                else:
                    next=dp[ind]
                    dp[ind]=max(end,dp[ind])
                    ind=next
        return ans