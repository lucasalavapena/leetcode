class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)

        lo = math.ceil(min(piles) * N / h)
        hi = max(piles) 

        def is_possible(guess_time):
            res = sum(math.ceil(p/guess_time) for p in piles)
            return res <= h

        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo