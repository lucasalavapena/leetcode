from heapq import heappush, heappop, heapify

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.food_to_cuis = {}
        self.rat_by_cuis = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.ratings[f] = -r
            self.food_to_cuis[f] = c
            self.rat_by_cuis[c].append((-r, f))

        for c in self.rat_by_cuis:
            heapify(self.rat_by_cuis[c])

    def changeRating(self, f: str, r: int) -> None:
        self.ratings[f] = -r
        c = self.food_to_cuis[f]
        heappush(self.rat_by_cuis[c], (-r, f))

    def highestRated(self, c: str) -> str:
        while self.ratings[self.rat_by_cuis[c][0][1]] != self.rat_by_cuis[c][0][0]:
            heappop(self.rat_by_cuis[c])
        return self.rat_by_cuis[c][0][1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)