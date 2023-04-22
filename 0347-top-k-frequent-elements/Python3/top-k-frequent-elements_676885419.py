class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[-k:]

        
        
        