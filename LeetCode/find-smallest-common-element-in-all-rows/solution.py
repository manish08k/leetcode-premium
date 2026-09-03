class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m=len(mat)
        counter=collections.Counter()
        for row in mat:
            for num in row:
                counter[num]+=1
                if counter[num]==m:
                    return num
        return -1