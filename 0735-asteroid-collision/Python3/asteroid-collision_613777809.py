class Solution:
    
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and -a > stack[-1]:
                    stack.pop()
                if not stack or -a > stack[-1]:
                    stack.append(a)
                elif -a == stack[-1]:
                    stack.pop()
                
            else:
                stack.append(a)
                
        return stack