class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        s_int = int(s)

        # not possible cases
        if s_int > finish: return 0
        if int(max(s)) > limit: return 0

        # the exp of the required ending which would be our start of our solutions
        start_exp = floor(log10(s_int))

        def count(end):
            # base cases
            if end < s_int:
                return 0
            if len(s) == len(str(end)):
                if end >= s_int:
                    return 1
                else:
                    return 0

            before_exp = floor(log10(end))
            largest_exp10 = 10**before_exp

            first = end//largest_exp10 # first digit, digit of largest 

            # excluding the current base, how many solutions exist
            # (0, 1..,limit)[end]
            #  ^ this can occur as many times before the biggest exp hence the power
            cnt_before = (limit + 1) ** (before_exp-start_exp-1)

            if first > limit:
                return cnt_before * (limit + 1)
            else:
                current = cnt_before * first # this includes everything up to first digit and all zeros
                return current + count(end % largest_exp10)

        return count(finish) - count(start-1) if start > 1 else count(finish)
    
