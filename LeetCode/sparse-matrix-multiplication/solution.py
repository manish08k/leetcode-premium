class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(mat1)):
            ans.append([0] * len(mat2[0]))
            
        for i in range(len(mat1)):
            for h in range(len(mat2)):

                if mat1[i][h] == 0: continue
                for j in range(len(mat2[0])):
                    ans[i][j] += (mat1[i][h] * mat2[h][j])
        return (ans)