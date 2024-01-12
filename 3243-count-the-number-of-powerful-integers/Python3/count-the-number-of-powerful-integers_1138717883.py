class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        s_int = int(s)
        # not possible cases
        if s_int > finish: return 0
        if int(max(s)) > limit: return 0

        limitstr = str(limit)

        start_exp = floor(log10(s_int))

        def count(end):
            if end < s_int:
                return 0
            if len(s) == len(str(end)):
                if end >= s_int:
                    return 1
                else:
                    return 0

            before_exp = floor(log10(end))

            cnt_before = (limit + 1) ** (before_exp-start_exp-1)
            first = int(str(end)[0])
            if first > limit:
                return cnt_before * (limit + 1)
            else:
                current = cnt_before * first
                # print(f"{current=} {end=}")
                return current + (count(int(str(end)[1:])) if end > 9 else 0)

        return count(finish) - count(start-1) if start > 1 else count(finish)
    
