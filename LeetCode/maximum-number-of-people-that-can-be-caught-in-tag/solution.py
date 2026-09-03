class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        nonItIndex = -1
        count = 0
        def helper(index, arr) -> int:
            while index + 1 < len(arr):
                index += 1
                if arr[index] == 0:
                    return index
            return -1
        for i in range(len(team)):
            if team[i] == 1:
                while max(i - dist, 0) > nonItIndex:
                    nonItIndex = helper(nonItIndex, team)
                    if nonItIndex == -1:
                        return count
                if i - dist <= nonItIndex <= i + dist:
                    count += 1
                    nonItIndex = helper(nonItIndex, team)
                if nonItIndex == -1:
                    return count
        return count