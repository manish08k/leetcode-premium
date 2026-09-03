class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums[:k])
        cur = len(c)
        ans = [cur]
        for i in range(k, len(nums)):
            c[nums[i-k]] -= 1
            if c[nums[i-k]] == 0:
                cur -= 1
            if c[nums[i]] == 0:
                cur += 1
            c[nums[i]] += 1
            ans.append(cur)
        return ans