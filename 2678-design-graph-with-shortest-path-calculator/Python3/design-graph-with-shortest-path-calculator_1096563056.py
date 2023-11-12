from collections import defaultdict

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(set)
        self.n = n

        for src, dest, weight in edges:
            self.graph[src].add((dest, weight))

        self.dist = [[[float('inf') for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]   
        self.new_nodes = [[set() for k in range(self.n)] for j in range(self.n)]    

        self.dest_seen = [[False] * n for _ in range(n)]

        """
        n
        """

    def addEdge(self, edge: List[int]) -> None:
        if (edge[1], edge[2]) not in self.graph[edge[0]]:
            # print(f"{edge=}")
            src, dest, weight = edge
            self.graph[src].add((dest, weight))
            for i in range(self.n):
                for j in range(self.n):
                    # only add once it has been seen or tried the first time
                    if self.dest_seen[i][j]:
                        self.new_nodes[i][j].add(src)


    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2: return 0
        h = []

        # print("-" * 80)
        # print("finding h")
        if self.new_nodes[node2][node1]:
            # print(f"{self.new_nodes[node2][node1]=}")
            for item in self.new_nodes[node2][node1]:
                cand_dist = self.dist[node2][node1][item]
                if cand_dist < float('inf'):
                    h.append((cand_dist, item))
                
        # if not self.dest_seen[node2][node1]:# or not h:
        # h = [(0, node1)]
        h.append((0, node1))

        # print("-" * 80)
        # print(f"{self.dist[node2][node1]=}")
        # print(f"{h=}")
        # print(f"{self.dest_seen[node2][node1]=}")

        while h:
            d, loc = heappop(h)

            if loc == node2:
                self.dist[node2][node1][node2] = min(self.dist[node2][node1][node2], d)

            for (neigh, neigh_dist) in self.graph[loc]:
                cand = d + neigh_dist

                if cand < self.dist[node2][node1][neigh]:
                    self.dist[node2][node1][neigh] = cand
                    heappush(h, (cand, neigh))
        
        self.new_nodes[node2][node1] = set()
        self.dest_seen[node2][node1] = True
        # print(f"{self.new_nodes[node2][node1]=} {self.dist[node2][node1][node2]=} {self.dist[node2][node1]=}")
        # print(f"{self.graph}")
        # print(f"{node1=} {node2=}")

        if self.dist[node2][node1][node2] < float('inf'):
            return self.dist[node2][node1][node2]
        return -1




# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)