class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        reference = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
        }
        
        res = [""]
        
        for s in digits:
            possible = reference[s]
            old_res = res
            res = [i + p for i in old_res for p in possible]
                
            
        return res