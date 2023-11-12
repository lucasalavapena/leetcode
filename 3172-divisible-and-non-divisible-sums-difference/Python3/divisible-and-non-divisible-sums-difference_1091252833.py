class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(i for i in range(1, n + 1) if i % m) - sum(i for i in range(1, n + 1) if i % m == 0)
