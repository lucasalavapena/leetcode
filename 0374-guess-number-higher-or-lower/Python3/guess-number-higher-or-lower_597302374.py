# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 1, n
        
        while lower <= upper:
            mid = (lower + upper)//2
            status = guess(mid)
            if status == 1:
                lower = mid+1
            elif status == -1:
                upper = mid-1
            else:
                return mid