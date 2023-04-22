class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candy = [0] * N
        sorted_ratings = sorted([(r, i) for i, r in enumerate(ratings)]) 
        
        def neighbour_dont_have_candy(i):
            if i == 0:
                return candy[i + 1] == 0 if i + 1 < N else True
            elif i == N - 1:
                return candy[i - 1] == 0
            else:
                return candy[i - 1] == 0 and candy[i + 1] == 0
        
        
        for r, i in sorted_ratings:
            # if neighbours dont have candy
            if neighbour_dont_have_candy(i):
                candy[i] = 1 
            else:
                if i == 0:
                    if r > ratings[i + 1]:
                        candy[i] = candy[i + 1] + 1
                    else:
                        candy[i] = 1 
                elif i == N - 1:                    
                    if r > ratings[i - 1]:
                        candy[i] = candy[i - 1] + 1
                    else:
                        candy[i] = 1 
                else:
                    max_rating = max(ratings[i - 1] if candy[i - 1] else 0, ratings[i + 1] if candy[i + 1] else 0)
                    max_value = max(candy[i - 1], candy[i + 1])
                    # min_value = min(ratings[i - 1] if candy[i - 1] else 0, ratings[i + 1] if candy[i + 1] else 0)
                    min_value = min(ratings[i - 1], ratings[i + 1])
                    # print(r, i, candy, max_rating, max_value)
                    if max_rating < r:
                        candy[i] = max_value + 1
                    else:
                        if r == min_value:
                            candy[i] = 1
                        else:
                            if ratings[i - 1] < r:
                                candy[i] = max(candy[i], candy[i - 1] + 1)
                            if ratings[i + 1] < r:
                                candy[i] = max(candy[i], candy[i + 1] + 1)
                                
        # print(candy)                              
        return sum(candy)