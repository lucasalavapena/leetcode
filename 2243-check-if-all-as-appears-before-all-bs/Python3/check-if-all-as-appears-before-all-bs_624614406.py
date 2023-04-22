class Solution:
    def checkString(self, s: str) -> bool:
        b_has_occured = False
        for si in s:
            if si == "b":
                b_has_occured = True
            else:
                if b_has_occured:
                    return False
        return True