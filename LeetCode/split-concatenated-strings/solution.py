class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [max(i, "".join(reversed(i))) for i in strs]
        whole_string = "".join(chain.from_iterable(strs))
        la = [len(i) for i in strs]
        lacc = [0] + list(accumulate(la))
        def left_right(i):
            left = whole_string[0:lacc[i]]
            right = whole_string[lacc[i+1]:]
            return left, right
        best = whole_string
        for i in range(len(strs)):
            for adj_str in [strs[i], "".join(reversed(strs[i]))]:
                for sp in range(len(adj_str)):
                    left, right = left_right(i)
                    constructed_string = adj_str[sp:] + right + left + adj_str[:sp]
                    best=max(best, constructed_string)
        return best