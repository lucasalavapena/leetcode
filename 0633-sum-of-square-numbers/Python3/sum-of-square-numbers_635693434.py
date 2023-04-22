from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return self.brute_force(c)
        
    def brute_force(self, c):
        for b in range(int(sqrt(c)) + 1):
            a_squared = c - b * b
            # check if a_squared is an int
            if int(math.sqrt(a_squared))**2 == a_squared: return True
        return False
        
        
    def binary_search(self, c):
        first = 0
        last = int(sqrt(c))
        if c <= 2:
            return True
        
        while first <= last:
            k = (first * first) + (last * last) 
            if k == c:
                return True
            elif k < c:
                first=first+1
            else:
                last=last-1
        return False