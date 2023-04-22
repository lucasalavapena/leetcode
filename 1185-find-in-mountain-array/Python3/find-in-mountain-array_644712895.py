# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        beg, end = 0, N-1
        
        cache = {}
        
        while beg + 1 < end:
            mid = (beg + end)//2
            
            if mid-1 not in cache:
                cache[mid-1] = mountain_arr.get(mid-1)
                
            if mid not in cache:
                cache[mid] = mountain_arr.get(mid)
                
            if cache[mid-1] < cache[mid]:
                beg = mid
            else:
                end = mid -1
        
        if end-1 not in cache:
            cache[end-1] = mountain_arr.get(end-1)
                
        if end not in cache:
            cache[end] = mountain_arr.get(end)
                                          
        mountain_idx = end if cache[end-1] < cache[end] else beg
        mountain_value = mountain_arr.get(mountain_idx)
        
        if target > mountain_value:
            return -1
        elif target == mountain_value:
            return mountain_idx
        
        beg, end = 0, mountain_idx-1
        
        while beg <= end:
            mid = (beg + end)//2
                
            if mid not in cache:
                cache[mid] = mountain_arr.get(mid)
                                                                                    
            if cache[mid] == target:
                return mid
                                          
            elif cache[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
                
                
        beg, end = mountain_idx + 1, N-1
                
        while beg <= end:
            mid = (beg + end)//2
                
            if mid not in cache:
                cache[mid] = mountain_arr.get(mid)
                                                                                    
            if cache[mid] == target:
                return mid
                                          
            elif cache[mid] < target:
                end = mid - 1
            else:
                beg = mid + 1
                                          
        return -1



        
        