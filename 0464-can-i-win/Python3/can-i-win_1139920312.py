class Solution:
    def canIWin(self, c: int, t: int) -> bool:
        if c >= t: return True 
        # impossible for either
        max_poss = (c + 1) * c//2
        if max_poss < t: return False
        @cache
        def dp(mask, left):
            for i in range(c):
                if mask & (1 << i):
                    n = i + 1
                    # win or opponent not win
                    if n >= left or not dp(mask ^ (1 << i), left-n): return True
            return False

        return dp((1<<c)-1, t)