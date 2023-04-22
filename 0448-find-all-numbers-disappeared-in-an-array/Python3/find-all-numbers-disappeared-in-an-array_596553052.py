class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        A = set(range(1, n + 1))
        B = set()
        for n in nums:
            B.add(n)
        
        return list(A.symmetric_difference(B))