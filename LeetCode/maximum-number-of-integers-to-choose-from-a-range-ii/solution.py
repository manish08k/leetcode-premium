class Solution:
    def maxCount(self, banned: List[int], n: int, max_sum: int) -> int:
        k = min(n, int((-1 + math.sqrt(1 + 8 * max_sum)) / 2))
        current_sum = int(k * (k + 1) / 2)
        count = k

        banned_set = set(banned)
        for b in banned_set:
            if b <= k:
                current_sum -= b
                count -= 1

        for i in range(k + 1, n + 1):
            if current_sum + i > max_sum:
                return count

            if i not in banned_set:
                current_sum += i
                count += 1

        return count