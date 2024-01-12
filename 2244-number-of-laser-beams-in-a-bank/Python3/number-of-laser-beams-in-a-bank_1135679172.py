class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            cand = row.count("1")
            # if either is greater than zero
            if cand:
                res += cand * prev
                prev = cand
        return res