class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def BackTr(target, curr_sol, no_numbers, max_num):  
            if target == 0:
                if no_numbers == 0:
                    self.sol.append(curr_sol)
                else:
                    return

            if target < 0 or 0 > no_numbers:
                return

            for i in range(max_num, 10):
                BackTr(target - i, curr_sol + [i], no_numbers-1, i + 1)
        
        self.sol = []
        BackTr(n, [], k, 1)   
        return self.sol