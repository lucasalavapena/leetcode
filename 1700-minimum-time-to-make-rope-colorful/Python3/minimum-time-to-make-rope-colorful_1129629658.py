class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr_idx = 0
        res = 0
        acc_sum = [0] + list(accumulate(neededTime)) 
        for c, g in groupby(colors):
            group_size = len(list(g))
            if group_size > 1:
                total = acc_sum[curr_idx + group_size] - acc_sum[curr_idx]
                excluded = max(neededTime[curr_idx:curr_idx+ group_size])
                res +=  total - excluded
            curr_idx += group_size
        return res