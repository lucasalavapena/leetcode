class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        for i, q in enumerate(queries):
            summation = 0
            for p in points:
                delta = (p[0] - q[0])**2 + (p[1] - q[1])**2 
                if q[0]-q[2] <= p[0] <= q[0] + q[2] and q[1]-q[2] <= p[1] <= q[1] + q[2] and delta <= q[2]**2:
                    summation += 1
            result[i] = summation
        return result