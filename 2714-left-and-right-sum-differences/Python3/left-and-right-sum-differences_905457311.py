class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        l = []
        cur = 0
        for i in nums:
            s -= i
            l.append(abs(s-cur))
            cur += i
        return l