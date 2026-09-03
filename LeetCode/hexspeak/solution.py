class Solution:
    def toHexspeak(self, num: str) -> str:
        hex = format(int(num), 'x')
        dict = {'0': 'O', '1': 'I', 'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
        res = ''

        for c in hex:
            if c not in dict:
                return "ERROR"
            res += dict[c]

        return res