class Solution:
    
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            stack.append(i)
            if len(stack) > 1:
                while len(stack) > 1:
                    if (stack[-2] > 0 and stack[-1] < 0):
                        if abs(stack[-1]) > abs(stack[-2]):
                            stack.pop(-2)
                        elif abs(stack[-1]) == abs(stack[-2]):
                            stack.pop()
                            stack.pop()
                        else:
                            stack.pop()
                    else:
                        break

        return stack