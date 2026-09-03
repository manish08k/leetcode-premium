class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_positions = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            self.word_positions[word].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        min_dist = float('inf')
        i, j = 0, 0
        word1_positions = self.word_positions[word1]
        word2_positions = self.word_positions[word2]
        max_word1 = len(word1_positions)
        max_word2 = len(word2_positions)

        while i < max_word1 and j < max_word2:
            min_dist = min(min_dist, abs(word1_positions[i] - word2_positions[j]))
            if word2_positions[j] < word1_positions[i]:
                j += 1
            else:
                i += 1
        
        return min_dist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)