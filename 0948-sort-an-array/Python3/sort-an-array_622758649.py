import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.mergeSort(nums)
        # return nums
        return self.quicksort(nums)
    def mergeSort(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l > 1:
            m = l // 2
            L = nums[:m]
            R = nums[m:]
            self.mergeSort(L)
            self.mergeSort(R)
            
            # merge two sorted list
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            nums[k:] = L[i:] + R[j:]
            print(m, nums)
            
    def quicksort(self, arr):
        n = len(arr)
        
        if n < 2:
            return arr
        
        pivot_loc = random.randint(0, n-1)
        
        arr[0], arr[pivot_loc] = arr[pivot_loc], arr[0] 
        pivot_loc = 0
        
        for i in range(1, n):
            if arr[i] <= arr[0] :
                pivot_loc += 1
                arr[i], arr[pivot_loc] = arr[pivot_loc], arr[i] 
                
        arr[0], arr[pivot_loc] = arr[pivot_loc], arr[0] 
                
            
        left = self.quicksort(arr[0:pivot_loc])
        right = self.quicksort(arr[pivot_loc+1:])

        return left + [arr[pivot_loc]] + right
        
        
