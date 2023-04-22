from math import sqrt, floor, ceil

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = 1
        
        not_prime = set([2])
        
        for i in range(3, n, 2):
            if i not in not_prime: 
                primes += 1
                for j in range(i**2, n, i): not_prime.add(j)
        return primes