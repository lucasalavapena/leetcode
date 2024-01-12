ordering = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        for i, c in enumerate(s):
            if i > 0 and ordering[s[i-1]] < ordering[c]:
                val += ordering[c] - 2 * ordering[s[i-1]] 
            else:
                val += ordering[c]
        return val
            