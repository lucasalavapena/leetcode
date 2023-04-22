class Solution:
    def calculate(self, s: str) -> int:
        def calc(it):
            def update(v, op):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
        
            num, stack, operator = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-":
                    update(num, operator)
                    operator = s[it]
                    num = 0
                elif s[it] == "(":
                    num, it = calc(it + 1)
                elif s[it] == ")":
                    update(num, operator)
                    return sum(stack), it
                it += 1
            update(num, operator)
            return sum(stack)
        return calc(0)
        
        
        
        
        