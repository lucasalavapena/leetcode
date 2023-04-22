class Solution:
    def calculate(self, s):    
        it = 0
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(int(stack.pop() / v))

        num, stack, sign = 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = 10 * num + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            it += 1
        update(sign, num)
        return sum(stack)

