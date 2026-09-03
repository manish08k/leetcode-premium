class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        m, n = len(pattern), len(s)
        
        def dfs(i, j, mapping, mapped_to):
            if i == m:
                return j == n
            
            for k in range(j, len(s) - (m - i) + 1):
                substr = s[j:k+1]
                if not mapping[pattern[i]] and substr not in mapped_to:
                    mapping[pattern[i]] = substr
                    mapped_to.add(substr)
                    if dfs(i + 1, k + 1, mapping, mapped_to):
                        return True
                    mapping[pattern[i]] = ""
                    mapped_to.remove(substr)
                elif mapping[pattern[i]] == substr:
                    if dfs(i + 1, k + 1, mapping, mapped_to):
                        return True

            return False
        
        return dfs(0, 0, defaultdict(str), set())