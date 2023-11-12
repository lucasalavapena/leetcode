from collections import deque

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy: return False 
        return max(abs(fx - sx), abs(fy - sy)) <= t 

        #         x_diff, y_diff = fx - sx, fy - sy
        # if abs(x_diff) > abs(y_diff):
        #     # diag_len = abs(y_diff) + 1
        #     # diag_len+ fx - (sx + diag_len)
        #     total = fx - sx
        # else:
        #     # diag_len = abs(x_diff) + 1
        #     total = fy - sy


