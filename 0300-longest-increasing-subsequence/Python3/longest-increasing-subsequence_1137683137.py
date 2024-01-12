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
    def lengthOfLIS(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        bit = BIT(max_num - min_num + 1)
        for n in nums:
            # transform
            t = n - min_num + 1
            curr = bit.query(t-1)
            bit.update(t, curr + 1)
        return bit.query(max_num - min_num + 1)















        # current_max = 1
        # for n in nums:
        #     if not dp: dp.append((n, 1))
        #     else:
        #         idx = bisect_left(dp, n-1, key=lambda x:x[0])
        #         if idx < len(dp):
        #             idx = idx if dp[idx][0] < n else max(0, idx-1)
        #             print(f"{dp=} {idx=} {dp[idx][0]=} {n=}")
        #             if dp[idx][0] < n:
        #                 bisect.insort(dp, (n, dp[idx][1] + 1), key=lambda x:x[0])
        #                 current_max = max(dp[idx][1] + 1, current_max)
        #             bisect.insort(dp, (n, 1), key=lambda x:x[0])
        # print(f"{dp=}")
        # return current_max

