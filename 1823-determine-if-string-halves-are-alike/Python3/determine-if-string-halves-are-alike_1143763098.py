ALPHA = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count(i, j) -> int:
            return sum(1 for k in range(i, j) if s[k] in ALPHA)
        N = len(s)
        return count(0, N//2) == count(N//2, N)
