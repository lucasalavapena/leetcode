class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        N = len(nums)
        """
        [], [1], [2], [1, 2]
        
        
        
        """
        for i in range(N):
            curr_size = len(res)
            for j in range(curr_size):
                curr = res[j][:]
                curr.append(nums[i])
                res.append(curr)
        return res