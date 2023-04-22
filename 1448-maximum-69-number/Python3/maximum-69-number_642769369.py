class Solution:
    def maximum69Number (self, num: int) -> int:
        a = int(log10(num))
        og_num = num
        
        for i in range(a, -1, -1):
            val = num // 10**i
            if val != 9:
                return og_num + 3 * 10**i
            num -= val * (10**i)
        return og_num