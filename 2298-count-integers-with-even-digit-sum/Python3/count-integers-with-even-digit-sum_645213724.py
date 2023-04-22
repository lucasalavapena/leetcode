class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        
        for i in range(1, num + 1):
            n = i
            digit_sums = 0
            while n:
                digit_sums += n % 10
                n //= 10
            if digit_sums % 2 == 0:
                res += 1
            
        return res