class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        different = True
        while different:
            different = False
            last = 0
            for i, val in enumerate(arr):
                if i and i < len(arr) - 1:
                    if arr[i + 1] > val < arr[i - 1] + last :
                        different = True
                        arr[i] = val + 1
                        last = -1
                    elif arr[i + 1] < val > arr[i - 1] + last:
                        different = True
                        arr[i] = val - 1
                        last = 1
                    else:
                        arr[i] = val
                        last = 0
                else:
                    arr[i] = val
        return arr