class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        white_count = floor.count("1")
        if numCarpets * carpetLen >= len(floor):
            return 0
        

        floor = list(map(int, list(floor)))
        # print(floor)
        
        while numCarpets:
            heap = []
            white_l = [0] + list(accumulate(floor))
            for i, f in enumerate(floor):
                if i + 1 >= carpetLen:
                    heap.append([-(white_l[i + 1] - white_l[i + 1 - carpetLen]), i- carpetLen + 1])
                    
            # print(heap)
            no_white, idx = min(heap)
            # print(no_white, idx)
            floor = floor[:idx] + [0] * carpetLen + floor[idx + carpetLen:]
            white_count += no_white
            numCarpets -= 1
            if white_count < 0:
                return 0
            
        return white_count