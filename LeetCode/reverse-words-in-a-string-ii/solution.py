class Solution:
    def reverseWords(self, s: List[str]) -> None:

        def rev(left: int, rght: int)-> None:
            s[left: rght] = s[left: rght][::-1]


        prevSpace = 0
        for curr, ch in enumerate(s):
            if ch == ' ':
                rev(prevSpace, curr)
                prevSpace = curr + 1
                
        rev(prevSpace, len(s))
        s.reverse()