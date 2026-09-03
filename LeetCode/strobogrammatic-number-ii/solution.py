class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.dfs(n,n)
    
    def dfs(self,k,total):
        if k==0:
            return [""]
        if k==1:return ["0","1","8"]
        sub=self.dfs(k-2,total)
        res=[]
        for s in sub:
            if k!=total:
                res.append(f"0{s}0")
            res.append(f"1{s}1")
            res.append(f"6{s}9")
            res.append(f"8{s}8")
            res.append(f"9{s}6")
        return res
    