class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people)-1
        
        boat_count = 0
        
        while start <= end:
            
            if start == end:
                boat_count += 1
                break
                
            curr_capacity = people[end]
            if people[end] + people[start] <= limit:
                start += 1
            end -= 1
            boat_count += 1
            
            
        return boat_count
            
            
        
        
        