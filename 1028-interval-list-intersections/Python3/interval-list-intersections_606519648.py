from itertools import chain

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res, i, j = [], 0, 0
        
        while i < len(firstList) and j < len(secondList):

            if (firstList[i][1] >= secondList[j][0] >= firstList[i][0]) or (secondList[j][0] <= firstList[i][0] <= secondList[j][1]):
                inter_start = max(secondList[j][0], firstList[i][0])
                inter_end = min(secondList[j][1], firstList[i][1])
                res.append([inter_start, inter_end])
            
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1

        return res
        
        