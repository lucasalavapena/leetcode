class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = collections.Counter(nums), 0, 0
        for value in range(10001):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr
