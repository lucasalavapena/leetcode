class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join([ w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue="")])