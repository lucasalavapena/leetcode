class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versions1 = map(int, version1.split("."))
        versions2 = map(int, version2.split("."))
        
        for v1, v2 in zip_longest(versions1, versions2, fillvalue=0):            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
        
