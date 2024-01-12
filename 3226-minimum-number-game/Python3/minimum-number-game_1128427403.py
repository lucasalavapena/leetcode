class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)//2):
            res.append(nums[2 * i + 1])
            res.append(nums[2 * i ])
        return res