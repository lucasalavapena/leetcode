class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        res = [0] * len(A)

        for i, (x, y) in enumerate(zip(A, B)):
            a.add(x)
            b.add(y)
            res[i] = len(a & b)

        return res
