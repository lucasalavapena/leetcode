
from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        max_ans = 46341
        min_ans = 0
        if x == 0: return 0
        # bisection search
        # binary search
        middle = (max_ans + min_ans) // 2
        while min_ans != max_ans - 1 and max_ans != min_ans:
            # print(min_ans, middle, max_ans)
            if min_ans * min_ans < x <= middle * middle:
                max_ans = middle
                middle = (middle + min_ans) // 2
            elif middle * middle < x <= max_ans * max_ans:
                min_ans = middle
                middle = (middle + max_ans) // 2

        if max_ans * max_ans == x:
            return max_ans
        else:
            return min_ans
