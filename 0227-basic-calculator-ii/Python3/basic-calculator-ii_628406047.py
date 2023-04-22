class Solution:
    
    
    def calculate(self, s: str) -> int:
        
        
        def operation(op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            elif op == "/":
                stack.append(int(stack.pop()/ num) )
                
        s = s.strip()
        stack = []
        op = "+"
        total, num = 0, 0
        
        for si in s:
            if si.isdigit():
                num = int(si) + 10 * num                
            elif si in "*/+-":
                operation(op, num)
                op = si
                num = 0
        # print(stack, num)
        operation(op, num) 
        # print(stack)
        return sum(stack)