class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        Graph = [[] for i in range(N)]
        for x, y in paths:
            Graph[x - 1].append(y - 1)
            Graph[y - 1].append(x - 1)
            
        for i in range(N):
            connections = {res[j] for j in Graph[i]}
            res[i] = ({1, 2, 3, 4} - connections).pop()
        return res