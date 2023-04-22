from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.sorted_list(nums)
        
    def sorted_list(self, nums):
        s = SortedList()
        N = len(nums)
        res = [0] * N
        
        for i in range(N-1, -1, -1):
            idx = SortedList.bisect_left(s, nums[i])
            res[i] = idx
            s.add(nums[i])
        return res