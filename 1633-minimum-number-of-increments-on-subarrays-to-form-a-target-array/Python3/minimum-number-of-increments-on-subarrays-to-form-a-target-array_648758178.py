class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return self.one_line(target)
    
    def monontoic_stack(self, target):
        pass
    
    def one_line(self, target):
        return sum(max(b - a, 0) for b, a in zip(target, [0] + target))