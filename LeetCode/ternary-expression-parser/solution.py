class Solution:
    def parseTernary(self, expression: str) -> str:
        def helper(s):
            N = len(s)

            if N == 1:
                return s

            idx = N-1
            idx2 = N-1
            for i in range(N-1, -1, -1):
                if s[i] == ':':
                    idx2 = i
                if s[i] == '?':
                    idx = i
                    break
            ch = s[idx-1]
            ret = ''
            if ch == 'T':
                ret = s[idx+1:idx2]
            else:
                ret = s[idx2+1]

            return helper(s[:idx-1] + ret + s[idx2+2:])
            
        return helper(expression)