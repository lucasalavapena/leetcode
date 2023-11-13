class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set(["a", "e", "i", "o", "u"])
        present_vowels = sorted([c for c in s if c.lower() in VOWELS], reverse=True)
        return "".join([present_vowels.pop() if c.lower() in VOWELS else c for c in s])