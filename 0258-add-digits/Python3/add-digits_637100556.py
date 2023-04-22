from math import log10

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        divisor = int(log10(num))
        
        if divisor < 1:
            return num
        
        total = 0
        for i in range(divisor, -1, -1):
            total += num // 10**i
            num -= (10**i) * (num // 10**i)
            
        # print(total, num)
        return self.addDigits(total)