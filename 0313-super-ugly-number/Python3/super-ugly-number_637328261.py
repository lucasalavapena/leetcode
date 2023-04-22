import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        res = [0] * n
        modified_primes = [1] + primes
        seen = set(modified_primes)
        h = modified_primes[:]
        heapq.heapify(h)
        count = n
        i = 0
        while count:
            num = heapq.heappop(h)
            res[i] = num
            
            for p in primes:
                if num * p <= 2147483647 and num * p not in seen:
                    heapq.heappush(h, num * p)
                    seen.add(num * p)
                    if num % p == 0:
                        break
                
            count -= 1
            i += 1              
        return res[-1]
        
        