class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        a, b, c = None, None, None
        
        for i, word in enumerate(text.split()):
            a, b, c = b, c, word
            if a is not None and b is not None and c is not None:
                if a == first and b == second:
                    res.append(c)
            
 
        return res