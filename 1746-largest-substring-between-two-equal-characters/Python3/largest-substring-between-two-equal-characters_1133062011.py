class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occ = {}
        max_occurance = -1
        for i, c in enumerate(s):
            if c in first_occ:
                max_occurance = max(i - first_occ[c]-1, max_occurance)
            else:
                first_occ[c] = i
        return max_occurance
        
