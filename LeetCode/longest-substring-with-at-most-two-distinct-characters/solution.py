class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left = 0
        freq = {}
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > 2:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans