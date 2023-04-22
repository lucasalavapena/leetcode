class Solution:
    def flatten(self, t):
        return [item for sublist in t for item in sublist]
    def generate_possibilities(self, inpu: str):
        location_of_brackets = {
            "(": [],
            ")": [],
        }
        
        res = []
        
        for i, s in enumerate(inpu):
            location_of_brackets[s].append(i)
        
        res = [inpu[:open_idx] + "(" + inpu[open_idx:close_idx] + ")" + inpu[close_idx:] for open_idx in location_of_brackets["("] for close_idx in location_of_brackets[")"] if open_idx < close_idx]
        res.append(inpu + "()")
        return res
        
    
    def generateParenthesis(self, n: int) -> List[str]:
                
        res = ["()"]
        self.generate_possibilities(res[0])
        
        
        for i in range(1, n):
            old_res = res
            res = list(set(self.flatten([self.generate_possibilities(r) for r in old_res])))
                
            
        return res