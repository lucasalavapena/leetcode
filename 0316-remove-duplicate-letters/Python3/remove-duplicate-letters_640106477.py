class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        stack = []
        used = set()
        
        for i, symbol in enumerate(s):
            if symbol in used: continue
            
            while stack and (symbol < stack[-1] and last_occ[stack[-1]] > i):
                used.remove(stack.pop())
           
            stack.append(symbol)
            used.add(symbol)        
            
        return "".join(stack)