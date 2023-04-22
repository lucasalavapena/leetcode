class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        N = len(nums)
        sols = set()
        
        for i in range(N):
            res_len = len(res)
            for j in range(res_len):
                curr = res[j][:]
                curr.append(nums[i])
                if (keys := tuple(curr)) in sols:
                    continue
                sols.add(keys)
                res.append(curr)
        return res
        