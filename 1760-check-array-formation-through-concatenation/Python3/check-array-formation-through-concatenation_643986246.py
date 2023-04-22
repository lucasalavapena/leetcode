class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        strr =""
        for i in arr:
            strr += str(i)
        lenn=len(strr)
        count=0
        for i in pieces:
            s=""
            for j in i:
                if str(j) not in strr:
                    return 
                s+=str(j)
            if s not in strr:
                return 
            else:
                count+=len(s)
        if count==lenn:        
            return "true"    