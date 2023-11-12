class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = int(n/2 * (n + 1))
        no_ms = n//m
        dm_sum =  no_ms * (m + m * no_ms)
        return total - dm_sum