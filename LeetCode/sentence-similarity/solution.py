class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]]
    ) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        for sent1, sent2 in zip(sentence1, sentence2):

            if (
                sent1 == sent2
                or [sent1, sent2] in similarPairs
                or [sent2, sent1] in similarPairs
            ):
                continue
            else:
                return False

        return True