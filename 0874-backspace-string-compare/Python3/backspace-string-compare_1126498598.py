class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(val):
            res = ""
            cons = 0
            for i in range(len(val)-1,-1,-1):
                if val[i] != "#":
                    if cons == 0:
                        res += val[i]
                    cons = max(0, cons-1)
                else:
                    cons += 1
            return res
        return compare(s) == compare(t) 