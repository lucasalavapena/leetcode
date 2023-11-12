class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        curr_count = 0

        for i, c in enumerate(s):
            is_vowel = c in vowels
            delta = is_vowel - (s[i-k] in vowels) if i >= k else is_vowel
            curr_count += delta
            max_vowels = max(max_vowels, curr_count)

        
        return max_vowels
