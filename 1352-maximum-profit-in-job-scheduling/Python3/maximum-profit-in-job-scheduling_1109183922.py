class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        prev_end, curr_max = 0, 0
        end_seen = []
        dp = collections.defaultdict(int)
        for start, end, profit in sorted(zip(startTime, endTime, profit), key=lambda x: x[1]):
            if prev_end < end:
                end_seen.append(end)
            idx = bisect.bisect(end_seen, start)
            nearest_to_start = 0 if idx == 0 else end_seen[idx-1]

            dp[end] = max(dp[nearest_to_start] + profit, curr_max)
            prev_end, curr_max = end, dp[end]
        return dp[prev_end]
