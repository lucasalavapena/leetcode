class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        prev_perf = 0
        for p in pref:
            val = p ^ prev_perf
            res.append(val)
            prev_perf = p

        return res