class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        n = len(nums)
        formatted = f"0{n}b"
        all_possible = {f"{i:{formatted}}" for i in range(1<<n)}
        return (all_possible-num_set).pop()
  