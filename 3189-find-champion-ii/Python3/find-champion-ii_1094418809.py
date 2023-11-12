class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weak = set([v for u, v in edges])
        strong = set(list(range(n)))
        only_strong = strong - weak
        res = only_strong.pop()
        return -1 if only_strong else res

