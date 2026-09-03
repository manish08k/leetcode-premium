class Solution:
    def lengthOfLongestSubstringKDistinct(self, line: str, k: int) -> int:
        left = 0
        res = 0
        curr = 0
        length = 0
        d = defaultdict(int)
        for x in line:
            if d[x] == 0:
                d[x] += 1
                length += 1
            else:
                d[x] += 1
            
            if length > k:
                res = max(res, curr)
                while length > k:
                    d[line[left]] -= 1
                    if d[line[left]] == 0:
                        length -= 1
                    left += 1
                    curr -= 1
            
            curr += 1
            
        return max(res, curr)