class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for w1, w2 in zip_longest(word1, word2, fillvalue=""):
            res += w1
            res += w2
        return res