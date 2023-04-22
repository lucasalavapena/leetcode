class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_total = 0
        
        for i in range(k):
            front_total += cardPoints[i] 
            
        back_total = front_total
        max_back = front_total
        
        for i in range(k):
            back_total +=  cardPoints[-1 -i]- cardPoints[k-i - 1]
            max_back = max(max_back, back_total)
            
        return max_back
        