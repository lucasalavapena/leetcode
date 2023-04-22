from sortedcontainers import SortedList


class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.binary_index_tree(nums)
        
    def sorted_list(self, nums):
        s = SortedList()
        N = len(nums)
        res = [0] * N
        
        for i in range(N-1, -1, -1):
            idx = SortedList.bisect_left(s, nums[i])
            res[i] = idx
            s.add(nums[i])
        return res
    
    def binary_index_tree(self, nums):
        val_to_idx = {v: i for i, v in enumerate(sorted(set(nums)))}
        b = BIT(len(val_to_idx))
        
        indexes = [val_to_idx[n] for n in nums]
        
        N = len(indexes)
        res = [0] * N
        
        for i in range(N-1, -1, -1):
            number = b.query(indexes[i])
            res[i] = number
            b.update(indexes[i] + 1,1)
        return res
        
