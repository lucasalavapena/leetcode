from math import log10

# 12 123
# 23 234
# 34 345
# 45 456
# 56 
# 67
# 78
# 89


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        const = [1, 2, 3, 4, 5, 6, 7, 8]
        
        l_len = len(str(low))
        h_len = len(str(high))
        
        # print(l_len, h_len)
        
        for i in range(l_len, h_len + 1):
            for j_idx, j in enumerate(const):
                if j + i <= 10:
                    candidate = int("".join([str(el) for el in range(j, i + j)]))
                    if low > candidate:
                        continue
                    if high < candidate:
                        return res                 
                    res.append(candidate)
    
        return res
        