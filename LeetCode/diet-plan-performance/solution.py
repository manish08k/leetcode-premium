class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pref = [0] + list(accumulate(calories))
        res = 0
        for i in range(k, len(pref)):
            sum = pref[i] - pref[i - k]
            if sum < lower:
                res -= 1
            elif sum > upper:
                res += 1

        return res