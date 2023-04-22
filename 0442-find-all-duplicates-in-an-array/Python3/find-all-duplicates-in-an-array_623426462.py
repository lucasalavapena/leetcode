class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            if nums[abs(nums[i]) - 1] < 0:
                # print(i, nums[i], nums[abs(nums[i]) - 1], nums)
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] *= -1
        return res