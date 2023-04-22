class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        if not nums: return
        nums = list(map(int, nums))
        
        pivot = random.choice(nums)
        
        larger = [n for n in nums if n > pivot]
        equal = [n for n in nums if n == pivot]
        smaller = [n for n in nums if n < pivot]
        
        L, E = len(larger), len(equal)
        
        
        if k <= L:
            return self.kthLargestNumber(larger, k)
        elif k > L + E:
            return self.kthLargestNumber(smaller, k-L-E)
        else:
            return str(pivot)