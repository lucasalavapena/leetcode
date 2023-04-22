class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = collections.defaultdict(list)
        
        for fro, to, cost in flights:
            d[fro].append((to, cost))
            
        visited_cost_dict = {}
        visited_cost_dict[src] = (0, 0)
        
        hp = [(0, 0,  src)]
        
        while hp:
            
            price, stops, pit = heapq.heappop(hp)
            
            if pit == dst:
                return price
            
            if stops > k:
                continue
                
            else:
                for otherDst, otherCost in d[pit]:
                    if otherDst not in visited_cost_dict or (otherCost + price < visited_cost_dict[otherDst][0]) or (stops+1 < visited_cost_dict[otherDst][1]):
                        visited_cost_dict[otherDst] = (otherCost + price, stops+1)
                        heapq.heappush(hp, (otherCost + price, stops+1, otherDst))
                
        return -1
