class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N # dp[i] = largest LIS you can get using nums[i]
        for i in range(1, N):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
        # dp = defaultdict(int)
        # current_max = 1
        # sorted_list = SortedList()
        # for n in nums:
        #     dp[n] = max(dp[n], 1)
        #     idx = sorted_list.bisect_left(n-1)
        #     if sorted_list and idx < len(sorted_list):
        #         idx = idx if sorted_list[idx] < n else max(0, idx-1)
        #         if sorted_list[idx] < n:
        #             dp[n] = max(dp[sorted_list[idx]] + 1, dp[n])

        #     sorted_list.add(n) # log n
        #     current_max = max(dp[n], current_max)
        # return current_max















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

