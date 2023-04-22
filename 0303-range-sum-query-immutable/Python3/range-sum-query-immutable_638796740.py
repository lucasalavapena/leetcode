class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.t = [0] * (4 * self.N)
        self.build(1, 0, self.N - 1)
        
    def build(self, curr, beg, end):
        if beg == end:
            self.t[curr] = self.nums[beg] 
        else:
            mid = (beg + end) // 2
            self.build(2 * curr, beg, mid)
            self.build(2 * curr + 1, mid + 1, end)
            self.t[curr] = self.t[2 * curr] + self.t[2 * curr + 1]
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sumRange_helper(1, 0, self.N - 1, left, right)
        
    def sumRange_helper(self, curr, beg, end, left, right) -> int:
        if left > right:
            return 0
        elif beg == left and end == right:
            return self.t[curr]

        mid = (beg + end)//2
        
        return self.sumRange_helper(2 * curr, beg, mid, left, min(right, mid)) + self.sumRange_helper(2 * curr + 1, mid + 1, end , max(left, mid + 1), right) 
                # return self.sumRange_helper(curr * 2, beg, mid, l, min(r, mid)) +  self.sumRange_helper(curr * 2 + 1, mid + 1, end , max(l, mid + 1), r)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)