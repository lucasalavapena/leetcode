class Solution:
    def smallestSubsequence(self, s, k, l, r):
        n, stack = len(s), ["!"]
        suff = list(accumulate([c == l for c in s][::-1]))[::-1]

        for i, c in enumerate(s): 
            while stack[-1] > c and len(stack) + n - i > k + 1 and (stack[-1] != l or r < suff[i]):
                r += stack.pop() == l
                
            if len(stack) < min(k, k - r + (c==l)) + 1:
                stack += [c]
                r -= (c == l)
            
            # print(f"{i} {stack=}")
            
        return "".join(stack[1:])
