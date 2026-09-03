class Solution:
    def missingNumber(self, arr):
        diff = (arr[-1] - arr[0]) // len(arr)

        for i in range(1, len(arr)):
            exp = arr[0] + diff * i
            if arr[i] != exp:
                return exp

        return arr[0]