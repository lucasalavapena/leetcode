from math import ceil
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend//divisor
        if res < 0 :
            res = ceil(dividend/divisor)
        return res if res < 2**31 - 1 else 2**31 - 1