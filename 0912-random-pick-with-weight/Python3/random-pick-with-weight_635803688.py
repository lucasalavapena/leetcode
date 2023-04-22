class Solution:
    def __init__(self, w: List[int]):
        self.w_cumsum = list(accumulate(w))
        self.total = sum(w)
        
    def pickIndex(self) -> int:
        value = self.total * random.random()
        
        return bisect.bisect(self.w_cumsum, value)
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()