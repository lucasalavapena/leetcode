class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for n in range(left, right + 1):
            if n % 10:
                cp = n
                p = int(log10(n))
                should_break = False

                while not should_break and p >= 0:
                    digit = cp // (10 ** p)
                    # print(digit, p)
                    if digit == 0 or n % digit:
                        should_break = True

                    cp -= digit * (10 ** p)
                    p -= 1
                # print(n, cp, p, should_break)
                if should_break:
                    continue
                else:
                    res.append(n)
                
            
        return res