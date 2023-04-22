from math import pi, sin, cos, sqrt
from random import random, uniform
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.center = (x_center, y_center)

    def randPoint(self) -> List[float]:
        inner_radius = self.radius * sqrt(uniform(0,1))
        angle = uniform(0, 2 * pi)
        
        return [self.center[0] + inner_radius * cos(angle), self.center[1] + inner_radius * sin(angle)]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()