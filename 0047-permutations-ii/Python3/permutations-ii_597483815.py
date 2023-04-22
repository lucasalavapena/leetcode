from itertools import permutations

class Solution:
    def permuteUnique(self, nums):
        # sort first
        nums.sort() # O(nlogn)
        
        stack = [(nums, [])] # (nums, path)
        res = []
        while stack: # -- O(E+V)
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            # children
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:  # --- Skip the sibling node if its the same as current node
                    continue
                newNums = nums[:i] + nums[i+1:]
                newPath = path + [nums[i]]
                stack.append((newNums, newPath))
        return res


        
        