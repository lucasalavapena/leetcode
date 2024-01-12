class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        non_zero = [cnt for row in bank if (cnt := row.count("1"))]
        return sum(a*b for a, b in pairwise(non_zero))