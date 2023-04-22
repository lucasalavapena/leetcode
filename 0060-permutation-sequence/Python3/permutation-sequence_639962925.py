from math import factorial

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1,n+1))
        answer = ""
        
        for n_it in range(n,0,-1):
            idx = (k-1) // factorial(n_it-1)
            k -= idx * factorial(n_it-1)
            answer += str(numbers[idx])
            numbers.remove(numbers[idx])
                   
        return answer
        
        
        
        
        
        