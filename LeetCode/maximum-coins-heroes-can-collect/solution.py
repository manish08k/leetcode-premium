class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        comb = [[monsters[i], coins[i]] for i in range(len(monsters))]
        comb.sort()
        for i in range(1, len(comb)):
            comb[i][1] += comb[i - 1][1]
        res = []
        for hero in heroes:
            l = 0
            r = len(comb) - 1
            while l + 1 < r:
                m = (l + r) // 2
                if hero >= comb[m][0]:
                    l = m
                else:
                    r = m - 1
            if hero >= comb[r][0]:
                res.append(comb[r][1])
            elif hero >= comb[l][0]:
                res.append(comb[l][1])
            else:
                res.append(0)
        return res
