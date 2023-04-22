class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cnt = 0
        lhs = []
        rhs = []
        
        for n in nums:
            if n < pivot:
                lhs.append(n)
            elif n == pivot:
                cnt += 1
            else:
                rhs.append(n)
        return lhs + [pivot] * cnt + rhs