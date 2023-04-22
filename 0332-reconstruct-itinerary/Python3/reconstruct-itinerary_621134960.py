class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"  
        graph = defaultdict(set)
        for src, des in tickets:
            graph[src].add(des)

        airports_vists = len(tickets) + 1
        # edges = {t[0]+t[1] for t in tickets}
        
        def dfs(node, path, graph_i, tickets_i):
            if len(path) > 1:
                tickets_i.remove(path[-2:])
            
            if len(path) == airports_vists:
                # print(f"{path=}")
                return path
            res = None            
            for neigh in sorted(graph_i[node]):
                # print(node+neigh, type(node+neigh), node, neigh, visited, path)
                # print(tickets_i)
                if [node, neigh] in tickets_i:
                    res = dfs(neigh, path+[neigh], graph_i, deepcopy(tickets_i))
                    # print(res)
                    if res is not None:
                        return res
        
            
        return dfs(start, [start], graph, tickets)