class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count1 = sum(data) 
        n = len(data)
        i = 0
        j = count1-1
        ones,zeros = sum(data[i:j+1]), count1-sum(data[i:j+1])
        maxOnes = ones
        while j<n:
            if maxOnes<ones:
                maxOnes = max(maxOnes, ones)
            if 0<=i<n and data[i]==0:
                zeros-=1
            elif 0<=i<n and data[i]==1:
                ones-=1
            i+=1
            j+=1
            if j<n and data[j]==0:
                zeros+=1
            elif j<n and data[j]==1:
                ones+=1
        return count1-maxOnes