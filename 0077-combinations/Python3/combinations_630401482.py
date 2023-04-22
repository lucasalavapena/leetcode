class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return self.cheating(n, k)
        self.res = []
        for i in range(1, n + 1):
            self.combine_recursive(n, k, [i])
        return self.res
    
    def cheating(self, n, k):
        return combinations(range(1, n + 1), k)
    
    def combine_iterative(self, n, k):
        pass
    
    def combine_recursive(self, n, k, curr):
        if len(curr) == k:
            self.res.append(curr)
            return

        for i in range(curr[-1] + 1, n + 1):
            self.combine_recursive(n, k, curr + [i])
            
            
            
            
        
        