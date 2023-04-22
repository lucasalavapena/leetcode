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
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                res.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return res
        