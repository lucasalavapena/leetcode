class Solution:
    def numberOfWays(self, corridor: str) -> int:
        PRIME = 1_000_000_007
        s_idxs = [i for i, c in enumerate(corridor) if c == "S"]
        N = len(s_idxs)
        if N == 0 or N % 2: return 0
        res = 1
        for i in range(2, N, 2):
            res *=  s_idxs[i] - s_idxs[i-1]
        return res % PRIME