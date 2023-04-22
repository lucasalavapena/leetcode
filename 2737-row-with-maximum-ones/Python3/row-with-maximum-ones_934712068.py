class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cnt = ans = 0 
        for i, row in enumerate(mat): 
            for ii in range(len(mat)):
                if i == ii: 
                    cand = row.count(1)
                    if cand > cnt: 
                        ans = i
                        cnt = cand 
        return [ans, cnt]