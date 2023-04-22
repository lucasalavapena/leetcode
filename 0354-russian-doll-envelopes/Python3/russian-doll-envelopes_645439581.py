class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        heights = [e[1] for e in envelopes]
        
        dp = [float('inf')] * len(heights)
        res = 0
        for h in heights:
            i = bisect.bisect_left(dp, h)
            i = max(0, i)
            dp[i] = h
            if i == res:
                res += 1
        return res