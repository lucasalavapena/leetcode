class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        arrSet = set(arr)
        
        @lru_cache(None)
        def dp(root):
            ans = 1
            for cand in arrSet:
                if root % cand == 0 and (root // cand) in arrSet:
                    ans += (dp(cand) * dp(root // cand) ) % MOD
            return ans
        
        return sum(dp(x) for x in arrSet) % MOD