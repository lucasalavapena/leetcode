class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        cnt = Counter(nums) 
        for num, freq in cnt.items(): bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[-k:]

        
        
        