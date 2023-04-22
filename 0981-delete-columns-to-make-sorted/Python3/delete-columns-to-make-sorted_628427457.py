class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        
        for c in zip(*strs): 
            if list(c) != sorted(c): 
                ret += 1
                
        return ret 