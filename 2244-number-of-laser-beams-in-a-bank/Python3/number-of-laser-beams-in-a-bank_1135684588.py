class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        non_zero = [cnt for row in bank if (cnt := row.count("1"))]
        return sum(non_zero[i] * non_zero[i+1] for i in range(len(non_zero)-1))