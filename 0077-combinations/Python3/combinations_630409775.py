class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return self.cheating(n, k)
        return self.combine_iterative(n, k)
        # return self.combine_recursive2(n, k)
        # self.res = []
        # for i in range(1, n + 1):
        #     self.combine_recursive(n, k, [i])
        # return self.res
    
    def cheating(self, n, k):
        return combinations(range(1, n + 1), k)
    
    def combine_iterative(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs
    
    def combine_recursive(self, n, k, curr):
        if len(curr) == k:
            self.res.append(curr)
            return

        for i in range(curr[-1] + 1, n + 1):
            self.combine_recursive(n, k, curr + [i])
            
    def combine_recursive2(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
            
            
            
            
        
        