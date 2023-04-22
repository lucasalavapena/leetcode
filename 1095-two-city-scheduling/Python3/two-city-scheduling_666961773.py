class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        [[1, 2], [2, 3], [5, 5], [6, 12]]
        
        A: 2 5
        B: 1 6
        """
        N = len(costs)
        city1 = 0
        # city2 = 0
        
        res = 0
        
        for _, a, b in sorted([[a - b, a, b] for a, b in costs]):
            if city1 < N//2:
                # print(f"city1 {a}")
                res += a
                city1 += 1
            else:
                # print(f"city2 {b}")
                res += b

            
        return res

        