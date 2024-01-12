class BIT:
    def __init__(self, n):
        self.sums = [0]*(n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] = max(self.sums[i], val)
            i += i & (-i)

    def query(self, i):
        res = 0
        while i > 0 :
            res = max(res, self.sums[i])
            i -= i & (-i)
        return res


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # this is just LIS with relaxation
        mapping = {}
        ordering = sorted(set(obstacles))
        for i, v in enumerate(ordering, start=1):
            mapping[v] = i
        N = len(ordering)

        bit = BIT(N)
        res = []
        for o in obstacles:
            idx = mapping[o]
            curr = bit.query(idx)
            bit.update(idx, curr+1)
            res.append(curr+1)
        return res