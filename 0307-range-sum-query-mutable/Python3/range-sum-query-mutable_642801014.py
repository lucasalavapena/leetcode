class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.t = [0] * (4 * self.N)
        self.build(1, 0, self.N-1)
        
        
    def build(self, curr, beg, end):
        if beg == end:
            self.t[curr] = self.nums[beg] 
        else:
            mid = (beg + end) // 2
            self.build(curr * 2, beg, mid)
            self.build(curr * 2 + 1, mid + 1, end)
            self.t[curr] = self.t[curr * 2] + self.t[curr * 2 + 1] 
        

    def update(self, index: int, val: int) -> None:
        self.update_helper(index, 1, 0, self.N-1, val)
        
    def update_helper(self, index, curr, beg, end, new_value):
        if beg == end:
            self.t[curr] = new_value
        else:
            mid = (beg + end) // 2
            if index <= mid:
                self.update_helper(index, curr * 2, beg, mid, new_value)
            else:
                self.update_helper(index, curr * 2 + 1, mid + 1, end, new_value)
            self.t[curr] = self.t[curr * 2] + self.t[curr * 2 + 1] 

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRange_helper(1, 0, self.N-1, left, right)
        
    def sumRange_helper(self, curr, beg, end, l, r):
        if l > r:
            return 0
        elif l == beg and r == end:
            return self.t[curr]
        mid = (beg + end) // 2
        
        return self.sumRange_helper(curr * 2, beg, mid, l, min(r, mid)) +  self.sumRange_helper(curr * 2 + 1, mid + 1, end , max(l, mid + 1), r)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)