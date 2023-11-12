class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(val):
            res = []
            for c in val:
                if c == "#":
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return res

        return compare(s) == compare(t) 