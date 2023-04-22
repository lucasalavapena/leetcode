class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        reference = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
        }
        no_digits = len(digits)
        if no_digits == 0:
            return []
        
        if no_digits == 1:
            return list(reference[digits])
        
        core = self.letterCombinations(digits[:-1])
        current = reference[digits[-1]]
        return [s + c for c in current for s in core]
    
    
#         res
#         max_no = 4 if "7" in digits or "9" in digits else 3
#         digits_int = list(map(int, digits))
#         for i, digit in enumerate(digits_int):
#             res[i] =  
            
        
        
        
        