class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        curr_time = customers[0][0]
        N = len(customers)
        wait_time = 0
        
        for arrival_time, prep_time in customers:
            curr_time = max(curr_time, arrival_time)
            wait_time += curr_time - arrival_time + prep_time
            
            curr_time += prep_time
            
        return wait_time/N 