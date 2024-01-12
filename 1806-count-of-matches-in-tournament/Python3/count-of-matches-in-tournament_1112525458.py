class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1
        if n % 2: return (n - 1) // 2 + self.numberOfMatches((n - 1) // 2 + 1)
        return n // 2 + self.numberOfMatches(n // 2)