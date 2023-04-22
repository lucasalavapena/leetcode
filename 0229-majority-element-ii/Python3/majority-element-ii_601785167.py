class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        min_required = len(nums)//3
        items_set = set()
        counter = {}
        
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            
            if counter[n] > min_required and n not in items_set:
                items_set.add(n)
        
        
        return list(items_set)