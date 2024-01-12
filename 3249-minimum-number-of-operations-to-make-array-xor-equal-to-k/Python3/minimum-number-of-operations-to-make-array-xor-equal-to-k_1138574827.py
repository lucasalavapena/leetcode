class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = [0] * 32
        
        for n in nums:
            for i, v in enumerate(bin(n)[2:][::-1]):
                v = int(v)
                count[~i] ^= v

        flips = 0
        for i, v in enumerate(bin(k)[2:][::-1]):
            v = int(v)
            if count[~i] != v:
                flips += 1
        return flips + sum(count[:~i])