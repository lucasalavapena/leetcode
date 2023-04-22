class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        increment_set = {"++X", "X++"}
        for item in operations:
            if item in increment_set:
                res += 1
            else:
                res -= 1
        return res