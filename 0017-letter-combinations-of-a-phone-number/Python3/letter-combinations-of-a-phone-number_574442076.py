class Solution:
     def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "":
            return []
        
        def getChars(d):
            if d == '2':
                return ['a', 'b', 'c']
            elif d == '3':
                return ['d', 'e', 'f']
            elif d == '4':
                return ['g', 'h', 'i']
            elif d == '5':
                return ['j', 'k', 'l']
            elif d == '6':
                return ['m', 'n', 'o']
            elif d == '7':
                return ['p', 'q', 'r', 's']
            elif d == '8':
                return ['t', 'u', 'v']
            elif d == '9':
                return ['w', 'x', 'y', 'z']
                
        array = getChars(digits[0])
        
        if len(digits) == 1:
            return array
        
        for d in digits[1:]:
            chars = getChars(d)
            newArray = []
            for a in array:
                for c in chars:
                    newArray.append(a+c)
            array = newArray
        return array