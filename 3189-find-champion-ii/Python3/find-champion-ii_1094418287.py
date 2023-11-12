class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        weak = set([v for u, v in edges])
        strong = set(list(range(n)))
        only_strong = strong - weak
        res = only_strong.pop() if only_strong else -1
        return -1 if only_strong else res

