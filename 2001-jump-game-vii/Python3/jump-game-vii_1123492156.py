class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        dp = [c == "0" for c in s] 
        zeros_in_window = 0
        for i in range(1, N):
            if i >= minJump: zeros_in_window += dp[i-minJump]
            if i > maxJump: zeros_in_window -= dp[i-maxJump -1]
            # has to already be a zero hence and [&] (and the init of c == "0") have some zeros in the window, so that from that window it can jump to i :)
            dp[i] &= zeros_in_window > 0
        return dp[-1]