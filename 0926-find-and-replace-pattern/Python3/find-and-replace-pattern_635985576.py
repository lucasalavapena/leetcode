class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def mask(word):
            reference = {}
            res = ""
            increment = 97
            for letter in word:
                if letter not in reference:
                    reference[letter] = chr(increment)
                    increment += 1
                res += reference[letter]
            return res
            
        masked = [(mask(w), w) for w in words]
        masked_pattern = mask(pattern)
        res = []
        for masked_w, w in masked:
            if masked_w == masked_pattern:
                res.append(w)
            
        return res
        