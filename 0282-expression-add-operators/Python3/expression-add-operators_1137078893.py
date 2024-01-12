class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        end = len(num) - 1
        def dfs(i, path):
            if i == end:
                cand_path = path + num[i]
                if eval(cand_path) == target:
                    res.append(cand_path)
                return 

            # note "" is no op :)) which allows you to 
            for op in ['+', '-', '*', '']:
                if not(op == '' and num[i] == "0" and (not path or not path[-1].isdigit())):
                    dfs(i + 1, f"{path}{num[i]}{op}")

        dfs(0, "")
        return res

        
            