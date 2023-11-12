class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        times = [0] * n
        curr_loc = 0
        for i in range(n):
            curr_loc = (curr_loc + i * k) % n
            times[curr_loc] += 1
            if times[curr_loc] > 1:
                break

        return [i + 1 for i, v in enumerate(times) if v == 0]