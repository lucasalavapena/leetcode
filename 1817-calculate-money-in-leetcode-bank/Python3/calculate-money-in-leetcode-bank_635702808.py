class Solution:
    def totalMoney(self, n: int) -> int:
        single_week = [1, 3, 6, 10, 15, 21, 28]
        
        if n <= 7:
            return single_week[n-1]
        
        day = n % 7
        multiple = n // 7
        return multiple * 28 + sum(7 * i for i in range(0, multiple)) + single_week[day-1] * (day > 0) + day * multiple
        