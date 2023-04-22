class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        to_delete = 0
        
        columns = len(strs[0])
        columns_strs = [""] * len(strs[0])
        columns_removed = set()
        
        for col in strs:
            for i, s in enumerate(col):
                if i not in columns_removed:
                    columns_strs[i] += s
                    if columns_strs[i] != "".join(sorted(columns_strs[i])):
                        columns_removed.add(i)
                        to_delete += 1
            
        return to_delete