class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            
            while True:
                if  k == 0 or not stack:
                    break
                
                if stack[-1] > num[i]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])
        while k != 0:
            stack.pop()
            k -= 1
        for i in range(len(stack)):
            if stack[i] != "0":
                break
        stack = stack[i:]

        if not stack:
            return "0"
        return "".join(stack)