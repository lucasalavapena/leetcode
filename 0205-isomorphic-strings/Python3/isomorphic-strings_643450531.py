class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def mask(st):
            reference = {}
            cnt = 65
            res = ""
            for i in st:
                if i not in reference:
                    reference[i] = chr(cnt)
                    cnt += 1
                res += reference[i]
            return res
        
        return mask(s) == mask(t)