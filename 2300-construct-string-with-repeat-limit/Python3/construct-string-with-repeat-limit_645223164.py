class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        heap = [[-(ord(k)-97), cnt[k]] for k in cnt]
        res = ""
        
        heapq.heapify(heap)
        
        while heap:
            character, count = heapq.heappop(heap)
            c = chr(-character + 97)
            if res and res[-1] == c:
                if repeat_count >= repeatLimit:
                    if not heap:
                        return res
                    repeat_count = 1
                    
                    char2, count2 = heapq.heappop(heap)
                    
                    res += chr(-char2+ 97)
                    
                    heapq.heappush(heap, [character, count])
                    if count2-1 > 0:
                        heapq.heappush(heap, [char2, count2-1])

                else:
                    repeat_count += 1
                    res += c
                    if count-1 > 0:
                        heapq.heappush(heap, [character, count-1])
                    
            else:
                repeat_count = 1
                res += c
                if count-1 > 0:
                    heapq.heappush(heap, [character, count-1])
                
        return res
