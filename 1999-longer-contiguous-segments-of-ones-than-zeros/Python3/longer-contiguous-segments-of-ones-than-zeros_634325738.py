class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        table = {"1": 0, "0": 0}
        max1, max0 = 0, 0
        for i, si in enumerate(s, 1):
            if si == "1":
                table["0"] = i
            else:
                table["1"] = i
            
            max0 = max(max0, i-table["0"])
            max1 = max(max1, i-table["1"])
              
        return max1 > max0
        
        