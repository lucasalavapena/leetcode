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
        return map(''.join, product(*[set([i.lower(), i.upper()]) for i in s]))