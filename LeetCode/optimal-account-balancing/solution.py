class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        bank = defaultdict(int)
        for a, b, amount in transactions:
            bank[a] += amount
            bank[b] -= amount

        balances = [balance for balance in bank.values() if balance]
        n = len(balances)

        def dfs(i) -> int:
            while i < n and balances[i] == 0:
                i += 1
            if i == n: return 0

            transaction = 101
            for nxt in range(i + 1, n):
                if balances[i] * balances[nxt] < 0:
                    balances[nxt] += balances[i]                   
                    transaction = min(transaction, 1 + dfs(i + 1))  
                    balances[nxt] -= balances[i]                    

            return transaction


        return dfs(0)