class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        grad_d = {}
        max_grad = 0
        
        if len(points) == 1:
            return 1
        
        for i in range(0, len(points)-1):
            for j in range(i + 1, len(points)):
                p_1 = points[i]
                p_2 = points[j]

                if p_2[0] != p_1[0]:
                    grad = (p_2[1] - p_1[1])/(p_2[0] - p_1[0])
                    y_intercept = p_2[1]  - grad * p_2[0]                    

                else:
                    grad = "special"
                    y_intercept = str(p_1[0])
                    
                key = f"{grad}_{y_intercept}"
                if grad == 0.0:
                    key = f"0.0_{p_2[1]}_{y_intercept}"
                    
                if key in grad_d:
                    grad_d[key].add(i)
                    grad_d[key].add(j)
                else:
                    grad_d[key] = {i, j}
                
                if max_grad < len(grad_d[key]):
                    max_grad = len(grad_d[key])
        
        # print("--"*20)
        # print(grad_d)
                    
        return max_grad
        
        