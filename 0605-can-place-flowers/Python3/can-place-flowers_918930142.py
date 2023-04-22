class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        no_f = len(flowerbed)
        count = 0
        for i in range(no_f):
            if flowerbed[i] == 0:
                if 0< i < no_f-1 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i == 0 and i + 1 < no_f and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i == no_f-1 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    count += 1
        return count >= n