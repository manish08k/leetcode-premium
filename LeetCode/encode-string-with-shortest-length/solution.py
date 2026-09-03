class Solution:

    def encode(self, s):
        
        @cache
        def calc(s):
            i = (s + s).find(s, 1)
            res = s
            if i < len(s):
                res = str(len(s) // i) + "[" + calc(s[:i]) + "]"
            
            ans = []
            for i in range(1, len(s)):
                ans.append(calc(s[:i]) + calc(s[i:]))

            ans.append(res)

            return min(ans, key = len)


        return calc(s)





        