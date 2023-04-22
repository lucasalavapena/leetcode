class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        res = [-1] * len(cars)
        
        for i in range(len(cars)-1, -1, -1):
            
            ccP, ccS = cars[i]
            
            while stack:
                top = cars[stack[-1]]
                
                # removing cars that dont collide
                if top[1] >= ccS or (top[0] - ccP) / (ccS-top[1]) >= res[stack[-1]] > 0:
                    stack.pop()
                else:
                    break
                    
            if stack:
                top = cars[stack[-1]]
                collisonT = (top[0] - ccP) / (ccS-top[1])
                res[i] = collisonT
            
            stack.append(i)
        return res