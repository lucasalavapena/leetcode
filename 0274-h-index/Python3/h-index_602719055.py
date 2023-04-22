class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n + 1)
        for c in citations:
            key = min(c, n)
            counter[key] += 1
        
        h_index = 0
        
        i = n
        while i >= 0:
            h_index += counter[i]
            
            if h_index >= i:
                return i
            i -= 1
        return 0
        