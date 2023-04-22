class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        
        # print(sum_gas, sum_cost)
        if sum_gas < sum_cost:
            return -1
        
        N = len(gas)
        
        # if N > 100:
        #     return -1
        greedy_idx = [i for i, x in enumerate(gas) if x > 0]
        # other_idx = [i for i, x in enumerate(gas) if x <= 0]
        
        for i in greedy_idx:
            tank = gas[i]
            paid = 0
            for j in range(i, i + N):
                idx = j % N
                next_idx = (j + 1) % N
                paid += cost[idx]
                tank -= cost[idx]
                
                if tank < 0:
                    break
                
                if paid == sum_cost:
                    return i
                    
                tank += gas[next_idx]
                
                if tank > 0 and next_idx == i:
                    return i
        return -1
                    