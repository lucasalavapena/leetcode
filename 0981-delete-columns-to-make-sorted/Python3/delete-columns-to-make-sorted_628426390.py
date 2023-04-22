class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        to_delete = 0
        
        columns = len(strs[0])
        columns_strs = [""] * len(strs[0])
        
        for col in strs:
            for i, s in enumerate(col):
                columns_strs[i] += s
                
        for i in range(columns):
            if columns_strs[i] != "".join(sorted(columns_strs[i])):
                to_delete += 1
            
        return to_delete