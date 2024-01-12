class Solution:
    def minimumSteps(self, s: str) -> int:
        """

        00001111
        00011011


        111000
        110101
        """
        # no_white = len([1 for c in s if c == "0"])
        total, white_idx = 0, 0
        for i, c in enumerate(s):
            if c == "0":
                total += i-white_idx
                white_idx += 1
        return total




        
        