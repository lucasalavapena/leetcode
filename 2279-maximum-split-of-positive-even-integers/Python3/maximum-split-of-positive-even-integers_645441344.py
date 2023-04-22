class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        else:
            # greedy
            res = []
            curr_sum = 0
            
            for i in range(1, finalSum//2 + 1):
                val = 2 * i
                if curr_sum + val == finalSum:
                    res.append(val)
                    return res
                elif curr_sum + val + 2 * (i + 1) <= finalSum:
                    res.append(val)
                    curr_sum += val
            return res         