from typing import List
from collections import Counter

class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for a in range(1, 101):
            if freq[a] == 0:
                continue

            for b in range(a, 101):
                if freq[b] == 0:
                    continue

                for c in range(b, 101):
                    if freq[c] == 0:
                        continue

                    s = a + b + c

                    # Exactly one of a, b, c divides the sum
                    if (
                        (s % a == 0)
                        + (s % b == 0)
                        + (s % c == 0)
                    ) != 1:
                        continue

                    if a == b == c:
                        # Cannot choose 3 distinct indices
                        continue

                    elif a == b:
                        # Choose 2 from freq[a], 1 from freq[c]
                        ways = freq[a] * (freq[a] - 1) // 2 * freq[c]

                    elif b == c:
                        # Choose 1 from freq[a], 2 from freq[b]
                        ways = freq[a] * freq[b] * (freq[b] - 1) // 2

                    else:
                        # All values different
                        ways = freq[a] * freq[b] * freq[c]

                    # 6 permutations of (a,b,c)
                    ans += ways * 6

        return ans