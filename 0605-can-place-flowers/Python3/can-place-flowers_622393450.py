class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        """
        [1, 0, 0, 1, 1]
        
        """        
        t = [len(list(j)) for i, j in groupby([0] + flowerbed + [0])]
        # print(t)
        return sum((i-1)//2 for i in t[0::2]) >= n