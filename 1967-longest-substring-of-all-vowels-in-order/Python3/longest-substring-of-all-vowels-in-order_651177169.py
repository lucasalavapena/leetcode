class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        start, longest = -1, 0
        for i, c in enumerate(word):
            if i > 0 and c < word[i - 1]:
                seen = set()
                start = i - 1    
            seen.add(c)    
            if len(seen) == 5:
                longest = max(longest, i - start)
        return longest