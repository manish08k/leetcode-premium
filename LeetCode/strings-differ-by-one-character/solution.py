class Solution:
    def differByOne(self, dictionary: List[str]) -> bool:

        L = len(dictionary[0])
        N = len(dictionary)
        
        if L < N:
            for i in range(L):
                seen = set()
                for word in dictionary:
                    mask = word[:i] + "*" + word[i + 1:]
                    if mask in seen:
                        return True
                    seen.add(mask)
            return False
        
        for i in range(N):
            for j in range(i + 1, N):
                word1, word2 = dictionary[i], dictionary[j]
                diff = 0
                for idx in range(L):
                    if word1[idx] != word2[idx]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    return True
        
        return False

        