from collections import deque

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xyCnt, yxCnt = 0,0
        for a, b in zip(s1, s2):
            if a+b=="xy":
                xyCnt+=1
            elif a+b=="yx":
                yxCnt+=1
        if (xyCnt%2+yxCnt%2)%2==0:
            return xyCnt//2 + yxCnt//2 + (xyCnt%2+yxCnt%2)
        else:
            return -1

        
        