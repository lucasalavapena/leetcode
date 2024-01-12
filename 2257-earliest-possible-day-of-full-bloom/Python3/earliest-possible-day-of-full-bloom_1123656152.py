class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curr_time = 0
        max_time = 0
        for grow_time, plant_time in sorted(zip(growTime, plantTime), reverse=True):
            curr_time += plant_time
            max_time = max(curr_time + grow_time, max_time)
        return max_time


        