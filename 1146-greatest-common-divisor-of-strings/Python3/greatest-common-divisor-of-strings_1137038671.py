class Solution:
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def get_factors(inp: str):
            repeated = set([inp])
            N = len(inp)
            for i in range(1, (N//2) +1):
                cand = inp[:i]
                if N % i == 0:
                    if all(inp[j * i: (j+1) * i]== cand for j in range(N//i)):
                        repeated.add(cand)
            
            return repeated
        
        
        str1_factors = get_factors(str1)
        str2_factors = get_factors(str2)
        # print(str1_factors)
        # print(str2_factors)
        inter = str1_factors & str2_factors
        return max(inter) if inter else ""