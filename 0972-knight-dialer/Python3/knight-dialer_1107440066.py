class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        PRIME = 10**9 + 7
        a = b = c = d = e = g = h = i = j = 1
        for _ in range(1, n):
            # how to get zeros in the ith step
            # either start from 4, 6
            a, b, c, d, e, g, h, i, j = (
                (e + g) % PRIME,
                (g + i) % PRIME,
                (h + j) % PRIME,
                (e + i) % PRIME,
                (a + d + j) % PRIME,
                (a + b + h) % PRIME,
                (c + g) % PRIME,
                (b + d) % PRIME,
                (c + e) % PRIME
            )
        return (a + b + c + d + e + g + h + i + j) % PRIME
