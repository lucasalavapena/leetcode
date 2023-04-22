class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:
        return min(t.count('b'), t.count('a'), t.count('l') // 2, t.count('o') // 2, t.count('n'))        