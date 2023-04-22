import string

class Solution:
    def numDecodings(self, s: str) -> int:
        
        return self.numDecodingsHelper(s)
      
    @cache
    def numDecodingsHelper(self, remaining_strings):
        
        encoded = [str(x) for x in range(1, 27)]  
        
        if remaining_strings == "" or (len(remaining_strings) == 1 and remaining_strings != "0"):
            return 1
        
        left, right = 0, 0
        if remaining_strings[0] in encoded:
            left = self.numDecodingsHelper(remaining_strings[1:])

        
        if len(remaining_strings) >= 2 and remaining_strings[:2] in encoded:
            right = self.numDecodingsHelper(remaining_strings[2:])
        
        
        return left + right
        