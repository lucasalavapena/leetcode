class Solution:
    def convert(self, s: str, numRows: int) -> str:
        con = []
        if numRows < 2: return s
        parity = 0
        i = 0
        while i < len(s):
            if parity % 2 == 0:
                con.append(s[i:i+numRows])
                i += numRows
            else:
                con.append(s[i:i+numRows-2][::-1])
                i += numRows-2
            parity += 1
        
        res = ""
        # print(con)
        for n in range(numRows):
            for i, l in enumerate(con):    
                if len(l) == numRows:
                    res += l[n]
                else:
                    if i % 2 == 0:
                        if n < len(l):
                            res += l[n]
                        else:
                            continue
                    else:
                        if len(l) != numRows-2:
                            l_start = numRows-1-len(l)
                            if l_start <= n < numRows-1:
                                res += l[n-l_start]
                        else:
                            if 1 <= n < numRows-1:
                                res += l[n-1]
        return res