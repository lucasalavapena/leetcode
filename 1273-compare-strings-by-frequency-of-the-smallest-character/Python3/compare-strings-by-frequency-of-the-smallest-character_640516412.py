class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        Q = len(queries)
        res = [0] * Q
        
        @cache
        def f(s):
            d = defaultdict(int)
            min_char = "z"
            for c in s:
                d[c] += 1
                
                if c < min_char:
                    min_char = c
                
            return d[min_char]
        
        for i, q in enumerate(queries):
            q_count = f(q)
            
            for w in words:
                w_count = f(w)
                
                if q_count < w_count:
                    res[i] += 1
        return res