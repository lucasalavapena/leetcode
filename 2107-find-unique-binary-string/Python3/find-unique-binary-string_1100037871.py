class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        n = len(nums)
        formatted = f"0{n}b"
        for i in range(1<<n):
            cand = f"{i:{formatted}}"
            if cand not in num_set:
                return cand