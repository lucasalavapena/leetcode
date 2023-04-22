class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        def candidates(in_text, patt):
            a, b = patt
            yield a + in_text
            yield in_text + b
        
        def get_sub_sequences(c, patt):
            a, b = patt
            total = 0
            char_to_idx = defaultdict(list)
            
            for i, elem in enumerate(c):
                char_to_idx[elem].append(i)
            
            
            for idx in char_to_idx[a]:
                total += len(char_to_idx[b]) - bisect.bisect_right(char_to_idx[b], idx)
                
            return total
            
        
        max_sub = 0
        
        for cand in candidates(text, pattern):
            n = get_sub_sequences(cand, pattern)
            max_sub = max(n, max_sub)

        return max_sub