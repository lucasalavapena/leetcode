from itertools import groupby

class Solution:
    def countHomogenous(self, s: str) -> int:
        """ 
        aa
        a = 2
        aa = 1

        aaa 
        a = 3
        aa = 2
        aaa = 1

        aaaa
        a = 4
        aa = 3
        aaa = 2
        aaaa = 1
        """
        PRIME = 10**9 + 7
        total = 0
        for c, gb in groupby(s):
            cnt = len(list(gb))
            total = (total + int(cnt/2 * (1 + cnt))) % PRIME


        return total % PRIME
        