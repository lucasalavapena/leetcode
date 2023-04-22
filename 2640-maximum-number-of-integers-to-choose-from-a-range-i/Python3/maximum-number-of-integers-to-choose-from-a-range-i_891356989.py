class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        no_items = 0
        min_remaining = 1
        
        while maxSum > 0:
            if min_remaining > n:
                return no_items
            while min_remaining in banned_set:
                min_remaining += 1
                if min_remaining > n:
                    return no_items
            if maxSum - min_remaining >= 0:
                maxSum -= min_remaining
                no_items += 1
                min_remaining += 1
            else:
                return no_items

        return no_items

        