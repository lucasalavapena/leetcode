
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        accum 2d array
        [0, 0, 1, 2, 3]

        a = [0, 1, 4]

        """       
        # count only using same letters
        # total = sum([1 for c, v in Counter(s) if v >= 3]) 
        total = 0
        counter = [(None, None)] * 26
        for i, c in enumerate(s):
            counter_idx = ord(c) - ord("a")
            min_idx, max_idx = counter[counter_idx]
            if min_idx is None:
                counter[counter_idx] = (i, i)
            else:
                counter[counter_idx] = (min_idx, max(max_idx, i))
        
        for min_idx, max_idx in counter:
            if min_idx is not None and min_idx != max_idx:
                seen = set()
                for idx in range(min_idx + 1, max_idx):
                    if s[idx] not in seen:
                        total += 1
                        seen.add(s[idx])
                    
                    
        return total