from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q = deque([source])

        seen_routes = set()
        bus_stop_route_idx = defaultdict(list)

        for i, route in enumerate(routes):
            for bus_stop in route:
                bus_stop_route_idx[bus_stop].append(i)


        steps = -1
        while q:
            q_len = len(q)
            steps += 1
            for _ in range(q_len):
                current_loc = q.popleft()

                if current_loc == target:
                    return steps

                for route_idx in bus_stop_route_idx[current_loc]:
                    if route_idx not in seen_routes:
                        for bus_stop in routes[route_idx]:
                            q.append(bus_stop)

                        seen_routes.add(route_idx)

        return -1

        