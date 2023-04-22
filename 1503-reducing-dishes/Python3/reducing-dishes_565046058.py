class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sorted_list = sorted(satisfaction, reverse=False)
        max_score = 0
        original_length = len(satisfaction)
        if sorted_list[-1] <= 0:
            return 0
        for  i in range(original_length):
            score = sum([(j + 1) * item for j, item in enumerate(sorted_list[i:])])
            if max_score < score:
                max_score = score
        return max_score
            