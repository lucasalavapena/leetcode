class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        diff = defaultdict(int)
        res = 0
        for t in time:
            remainder = t % 60
            res += diff.get((60 - remainder) % 60, 0)
            diff[remainder] += 1
        return res