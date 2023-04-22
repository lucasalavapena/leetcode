class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def simplify(s):
            res = []
            
            for i, c in enumerate(s):
                if c == "#":
                    if res:
                        res.pop()
                else:
                    res.append(c)
                
            return "".join(res)
            
        return simplify(s) == simplify(t)
        