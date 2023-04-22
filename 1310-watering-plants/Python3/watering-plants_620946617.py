class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        n = len(plants)
        steps = 0
        for i in range(n):
            steps += 1
            curr -= plants[i]
            
            if i + 1 < n and plants[i+1] > curr:
                steps += 2 * (i+1)
                curr = capacity
        return steps