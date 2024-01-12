class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(["1" if c[i] == "0" else "0" for i, c in enumerate(nums)])
  