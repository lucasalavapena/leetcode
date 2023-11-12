class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = s.count("1")
        length = len(s)
        zeros = length-cnt

        return "1" * (cnt-1) + "0" * zeros + "1"