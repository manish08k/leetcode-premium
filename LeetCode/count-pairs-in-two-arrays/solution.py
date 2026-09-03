class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sorted(x - y for x, y in zip(nums1, nums2))
        ans, n = 0, len(diff)
        for i, x in enumerate(diff):
            idx = bisect_right(diff, -x, i+1)
            ans += n - idx
        return ans