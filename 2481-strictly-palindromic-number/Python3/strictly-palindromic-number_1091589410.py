from math import log
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_pali(res):
            i, j = 0, len(res)-1
            while i < j:
                if res[i] != res[j]:
                    return False
                i += 1
                j -= 1

            return True

        def get_num(num, base):
            ret = []
            remaining = num
            max_exp = math.ceil(math.log(num, base))

            # note we are appending it in reverse order but since it is a palidromic it does not matter :))

            while remaining != 0:
                val = remaining//(base**max_exp)
                if remaining - val >= 0:
                    ret.append(val)
                    remaining -= val
                max_exp -= 1
            return ret


        for i in range(2, n-1):
            n_list = get_num(n, i)
            if not is_pali(n_list):
                return False

        return True