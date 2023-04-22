from itertools import groupby

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # print([(c, lst) for c, lst in groupby(s)])
        gp = [(c, len(list(lst))) for c, lst in groupby(s)]
        stack = []
        
        for c, count in gp:
            # print(c, count)
            # print(stack)
            remainder = count % k
            if remainder:
                if stack and stack[-1][0] == c:
                    remainder2 = (remainder + stack[-1][1]) % k
                    if remainder2:
                        stack[-1] = (c, remainder2)
                    else:
                        stack.pop()
                else:
                    stack.append((c, remainder))
                    if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                        remainder = (stack[-1][1] + stack[-2][1]) % k
                        if remainder:
                            stack.pop()
                            stack[-1] = (stack[-1][0], remainder)
                        else:
                            stack.pop()
                            stack.pop()
                    

        return "".join([c * count for c, count in stack])
            
                