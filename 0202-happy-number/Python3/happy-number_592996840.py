class Solution:
    def isHappy(self, n: int) -> bool:
        
        def compute_sum_of_digits(n: int) -> int:
            return sum([l**2 for l in list(map(int, list(str(n))))])
        
        total = compute_sum_of_digits(n)
        count = 1
        
        while total != 1 and count < 200:
            total = compute_sum_of_digits(total)
            count += 1            
            # print(total, count)
            
        if total != 1:
            return False
        return True