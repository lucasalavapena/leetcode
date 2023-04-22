class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        state = 0
        if word[0] == word[0].upper():
            state = 1
        if len(word) > 1 and state == 1 and word[1] == word[1].upper():
            state = 2
        if state == 0 or state == 1:
            for w in word[1:]:
                if w == w.upper():
                    return False
        elif state == 2:
            for w in word[2:]:
                if w != w.upper():
                    return False
            
        return True