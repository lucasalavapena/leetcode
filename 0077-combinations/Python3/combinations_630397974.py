class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.cheating(n, k)
    
    def cheating(self, n, k):
        return combinations(range(1, n + 1), k)