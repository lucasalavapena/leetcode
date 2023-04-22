class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        res = []
        
        for i in range(1, len(s) + 1):
            curr = s[:i]
            if curr == curr[::-1]:
                for remaining in self.partition(s[i:]):
                    res.append([curr] + remaining)
            
        return res