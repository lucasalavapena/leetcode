class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        N = len(time)

        lo = min(time) * math.ceil(totalTrips / N)
        hi = max(time) * math.ceil(totalTrips / N)

        def is_possible(guess_time):
            res = sum(guess_time//t for t in time)
            return res >= totalTrips


        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo



