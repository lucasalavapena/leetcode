import heapq
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N = len(dist)
        time_to_reach = [dist[i]/speed[i] for i in range(N)]
        heapq.heapify(time_to_reach)

        time = 0
        while time_to_reach and time_to_reach[0] > time:
            heapq.heappop(time_to_reach)
            time += 1

        return time