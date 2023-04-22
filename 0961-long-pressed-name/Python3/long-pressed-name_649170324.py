class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i, j = 0, 0
        while i < m or j < n:
            if i < m and j < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j < n and i-1 >= 0 and name[i-1] == typed[j]:
                j += 1
            else:
                return False
        
        return i == m and j == n
        
        