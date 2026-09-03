class Solution:
    def expand(self, s: str) -> List[str]:
        if "," not in s and "{" not in s and "}" not in s: return [s]
        s = s.replace("{", " ").replace("}", " ").split()
        res = []
        for c in s:
            c = c.split(",")
            res.append("".join(c))
        y = []
        for p in product(*res):
            y.append("".join(p))
        y.sort()
        return y
        
        