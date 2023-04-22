class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}        
        count = 0
        
        for num in nums:            
            if num in hashmap:
                count += hashmap[num]
                hashmap[num] += 1
            
            else:
                hashmap[num] = 1
        return count