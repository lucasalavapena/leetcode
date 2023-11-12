class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s): return False
        for i, w in enumerate(words):
            if w[0] != s[i]:
                return False
        return True