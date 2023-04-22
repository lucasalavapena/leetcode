class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increment_set = {"++X", "X++"}
        return sum([1 if item in increment_set else -1 for item in operations])