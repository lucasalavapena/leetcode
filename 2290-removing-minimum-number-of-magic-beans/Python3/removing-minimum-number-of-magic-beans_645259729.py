class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        min_beans = float("inf")
        N = len(beans)
        prefix_sum = [0] + list(accumulate(beans))
        
        for i, b in enumerate(beans):
            before_removed = prefix_sum[i]
            after_removed = 0
            if i + 1 <= N :
                after_removed = prefix_sum[-1] - prefix_sum[i ] - b * (N-i)
            min_beans = min(min_beans, before_removed + after_removed)
        
        
        return min_beans