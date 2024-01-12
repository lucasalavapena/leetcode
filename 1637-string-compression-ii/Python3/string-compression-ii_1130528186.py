class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        if N == k: return 0
        if N == k-1: return 1

        # @cache
        def compute(x):
            return x if x < 2 else 2 + int(log10(x))

        @cache 
        def dfs(i, prev, cons, nk):
            if i == N:
                return compute(cons)

            if prev == s[i]:
                take = dfs(i + 1, s[i], cons+1, nk)
            else:
                take = compute(cons) + dfs(i + 1, s[i], 1, nk)
            not_take = float("inf")
            if nk > 0:
                not_take = dfs(i + 1, prev, cons, nk-1)
            return min(take, not_take)

        return dfs(0, "", 0, k)