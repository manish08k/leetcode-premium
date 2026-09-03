class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        buffer = []
        idx = 0
        longest = max(words, key=lambda x: len(x))
        n = len(longest)
        for i in range(n):
            buffer.clear()
            for row in words:
                if i >= len(row):
                    continue
                buffer.append(row[i])
            if ''.join(buffer) != words[idx]:
                return False
            idx += 1

        return True