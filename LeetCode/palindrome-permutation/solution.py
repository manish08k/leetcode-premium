class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_dict = {}
        for c in s:
            if c in freq_dict:
                freq_dict[c] += 1
            else:
                freq_dict[c] = 1
        num_odds = len([
            i for i in freq_dict.values()
            if i % 2 == 1
        ])

        return num_odds <= 1