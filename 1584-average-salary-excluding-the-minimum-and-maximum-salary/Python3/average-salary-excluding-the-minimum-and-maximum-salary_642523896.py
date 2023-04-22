class Solution:
    def average(self, salary: List[int]) -> float:
        total, min_val, max_val = 0, float("inf"), float("-inf")
        for s in salary:
            total += s
            min_val = min(min_val, s)
            max_val = max(max_val, s)

        return (total -min_val - max_val)/(len(salary)-2)