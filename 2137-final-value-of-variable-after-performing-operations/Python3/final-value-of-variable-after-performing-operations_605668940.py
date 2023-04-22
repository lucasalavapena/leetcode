class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        increment_set = {"++X", "X++"}
        decrement_Set = {"--X", "X--"}
        for item in operations:
            if item in increment_set:
                res += 1
            elif item in decrement_Set:
                res -= 1
        return res