class Solution:
       def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        }
        array = letters[digits[0]]
        
        if len(digits) == 1:
            return array
        
        for d in digits[1:]:
            chars = letters[d]
            newArray = []
            for a in array:
                for c in chars:
                    newArray.append(a+c)
            array = newArray
        return array
        
        
        
        