class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def generate_palindromes():
            for i in [1,2,3,4,5,6,7,8,9]:
                yield i
            for i in range(1,10000):
                yield int(str(i) + str(i)[::-1])
                for j in range(10):
                    yield int(str(i) + str(j) + str(i)[::-1])     
        
        def is_palindrome(n):
            n = str(n)
            l, r = 0, len(n)-1
            
            while l < r:
                if n[l] != n[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        left = int(left)
        right = int(right)
        count = 0
        for n in generate_palindromes():
            squared = n * n
            if left <= squared <= right and is_palindrome(squared):
                count += 1
        
        return count