class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        target = total/2
        N = len(nums)
        s = set([0])
        
        for i in range(N-1, -1, -1):
            entry = nums[i]
            for item in list(s):
                s.add(item + entry)
            s.add(entry)
            if target in s:
                return True
        return False
        
        