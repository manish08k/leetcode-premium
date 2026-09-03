class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        counter=Counter(s)
        a=[]
        for i in s:
            if counter[i]<k:
                a.append(i)
        return ''.join(a)