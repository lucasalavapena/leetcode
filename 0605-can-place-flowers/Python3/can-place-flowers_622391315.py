class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        """
        [1, 0, 0, 1, 1]
        
        """        
        m = len(flowerbed)
        count = 0
        
        for i in range(m):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == m-1 or flowerbed[i+1]== 0) :
                flowerbed[i] = 1
                count += 1
        # print(f"{flowerbed=} {n=}")
        return count >= n