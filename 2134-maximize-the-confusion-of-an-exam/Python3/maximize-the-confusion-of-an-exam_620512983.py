class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        max_cons = 0
        k_t, k_f = k, k
        start_t, start_f = -1, -1
        for i, ans in enumerate(answerKey):
            if ans == "T":
                k_f -= 1
            else:
                k_t -= 1
                
            while k_f < 0 :
                start_f += 1
                k_f += 1 if answerKey[start_f] == "T" else 0
            
            while k_t < 0 :
                start_t += 1
                k_t += 1 if answerKey[start_t] == "F" else 0
                
            
            max_cons = max(i - start_t, i - start_f, max_cons)
        return max_cons