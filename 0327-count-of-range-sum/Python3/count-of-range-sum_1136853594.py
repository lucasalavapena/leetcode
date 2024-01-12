class BIT:
    def __init__(self, n):
        self.sums = [0] * (n + 1) # is 1 indexed

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i) # add least signfcant bit

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i) # sub least signfcant bit
        return res

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        acc = [0] + list(accumulate(nums))
        acc_sorted = sorted(acc)

        bit = BIT(n + 1)
        res = 0

        for s in acc:
            # computes the total sum before and after legal states
            left = bit.query(bisect_left(acc_sorted, s - upper))
            right = bit.query(bisect_right(acc_sorted, s - lower))
            res += right - left

            # coordinate compression
            # also the occurances match up since you have a difference of +1 between consquetative repeated numbers if that makes sense
            idx = bisect_right(acc_sorted, s)
            # add 1 to the number of occurances, so we can later do the range sum calculations
            bit.update(idx, 1)
        return res