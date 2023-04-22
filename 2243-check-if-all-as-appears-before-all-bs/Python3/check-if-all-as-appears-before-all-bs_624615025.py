from itertools import groupby

class Solution:
    def checkString(self, s: str) -> bool:
        if s[0] == "b":
            n = 1
        else:
            n = 2
        return len(list(groupby(s))) <= n