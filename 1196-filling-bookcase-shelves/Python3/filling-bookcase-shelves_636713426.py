class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:        
        N = len(books)
        dp = [float("inf")] * (N + 1)
        dp[0] = 0
        for i in range(1, N + 1):
            w = books[i-1][0]
            h = books[i-1][1]
            
            # place on new level
            dp[i] = dp[i-1] + h
            
            j = i-2
            curr_height = h
            remainind_width = shelfWidth - w
            
            while j >= 0 and remainind_width >= books[j][0]:
                remainind_width -= books[j][0]
                curr_height = max(curr_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + curr_height)
                j -= 1
        return dp[-1]