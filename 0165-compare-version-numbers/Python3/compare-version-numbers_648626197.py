class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_l = list(map(int, version1.split(".")))
        version2_l = list(map(int, version2.split(".")))
        
        m, n = len(version1_l), len(version2_l)
        if m > n :
            version2_l += [0] * (m - n)
        elif m < n:
            version1_l += [0] * (n - m)
        # print(version1_l, version2_l)
        for v1, v2 in zip(version1_l, version2_l):
            if v1 < v2:
                return -1
            elif v2 < v1:
                return 1
        return 0
        
        
