class Solution:
    
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            stack.append(i)
            while len(stack) > 1:
                top = stack[-1]
                second_top = stack[-2]
                if (second_top > 0 and top < 0):
                    if -top > second_top:
                        stack.pop(-2)
                    elif -top == second_top:
                        stack.pop()
                        stack.pop()
                    else:
                        stack.pop()
                else:
                    break

        return stack