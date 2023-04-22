class Solution:
    def generator(self, s):
        for i, c in enumerate(s):
            if c.isalpha():
                yield i, c
    
    def change_case(self, c):
        if c.isupper():
            return c.lower()
        else:
            return c.upper()
            
    
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [s]
        
        for i, elem in self.generator(s):
            res_len = len(res)
            for j in range(res_len):
                curr = list(res[j])
                curr[i] = self.change_case(elem)
                res.append("".join(curr))
        return res