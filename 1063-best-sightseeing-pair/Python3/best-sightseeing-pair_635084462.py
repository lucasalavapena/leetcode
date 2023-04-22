class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_so_far,result = values[0], 0
        
        for i in range(1,len(values)):
            result = max(result, max_so_far + values[i] - i)
            max_so_far = max(max_so_far, values[i] + i)
			
        return result