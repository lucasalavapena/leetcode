from collections import defaultdict, deque


class Solution:
    def _shortest_alternate_paths_helper(self, goal_node: int):
        q = deque([(0, "NoColor")])
        seen = set()

        level = 0
        while q:
            q_len = len(q)
            print(f"{level=} {q}")
            for _ in range(q_len):
                curr_node, curr_color = q.popleft()
                seen.add(f"{curr_node}{curr_color}")

                if curr_node == goal_node:
                    return level

                # could use pattern matching for this?
                if curr_color == "B" or curr_color == "NoColor":
                    for child in self.G[f"{curr_node}R"]:
                        if f"{child}R" not in seen:
                            q.append((child, "R"))

                if curr_color == "R" or curr_color == "NoColor":
                    for child in self.G[f"{curr_node}B"]:
                        if f"{child}B" not in seen:
                            q.append((child, "B"))
            level += 1

        return -1


    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        res[0] = 0

        self.G = defaultdict(list)
        """
        G = {node: [(edge_node_to, color)]}
        
        """
        for src_red_edge, dest_red_edge in redEdges:
            self.G[f"{src_red_edge}R"].append(dest_red_edge)

        for src_blue_edge, dest_blue_edge in blueEdges:
            self.G[f"{src_blue_edge}B"].append(dest_blue_edge)
        # return [ i for i in range(n)]
        return [self._shortest_alternate_paths_helper(i) for i in range(n)]




        
