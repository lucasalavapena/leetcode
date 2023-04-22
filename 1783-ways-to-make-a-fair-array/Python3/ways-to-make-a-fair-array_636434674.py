class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        s1, s2 = [0, 0], [sum(nums[0::2]), sum(nums[1::2])]
        res = 0
        for i, n in enumerate(nums):
            parity = i % 2
            s2[parity] -= n
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[parity] += n
            
        return res
        