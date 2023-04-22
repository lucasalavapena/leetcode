class Solution:
    def uniqueLetterString(self, s: str) -> int:        
        N = len(s)
        dp = [0] * (N + 1)
        most_recent_idx = [[-1, -1]] * 26
        for i, c in enumerate(s):
            key = ord(c) - 65
            first, second = most_recent_idx[key]
            dp[i + 1] = (dp[i] + 1) + (i - 1 -second) - (second - first)
            most_recent_idx[key] = [second, i]

        return sum(dp)