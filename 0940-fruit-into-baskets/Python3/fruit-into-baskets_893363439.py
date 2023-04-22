class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits: return 0
        previous_type_idx, current_type_idx = None, 0

        curr_streak = 0
        max_streak = 0
        i = 0
        while i < len(fruits):
            fruit = fruits[i]
            if fruit != fruits[current_type_idx] and previous_type_idx is not None and fruit != fruits[previous_type_idx]:
                curr_streak = i - current_type_idx + 1
            else:
                curr_streak += 1
            max_streak = max(max_streak, curr_streak)

            if fruits[current_type_idx] != fruit:
                previous_type_idx = current_type_idx
                current_type_idx = i
            i += 1


        return max_streak
