class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        max_val = 11 * ceil(x/11)
        if x == y:
            return 0
        elif abs(x-y) <= 2:
            return abs(x-y)
        elif x < y:
            return y-x 
        seen = set()
        q = deque([x])
        level = -1
        while q:
            q_len = len(q)
            level += 1
            for _ in range(q_len):
                v = q.popleft()
                seen.add(v)
                if v == y:
                    return level
                if v % 11 == 0 and v//11 not in seen:
                    q.append(v//11) 
                if v % 5 == 0 and v//5 not in seen:      
                    q.append(v//5) 
                if v -1 not in seen:
                    q.append(v-1) 
                if v <= max_val and v +1 not in seen:
                    q.append(v+1)
                
        return level

        # max_val = 11 * ceil(x/11)
        # print(f"{x=}{y=} {max_val=}")
        # ans = False
        # def dfs(v):
        #     nonlocal ans, max_val
        #     if ans:
        #         return float("inf")
            # if v == y:
            #     ans = True
            #     return 0
            # elif abs(v-y) <= 2:
            #     ans = True
            #     return abs(v-y)
            # elif v < y:
            #     ans = True
            #     return y-v
        #     min_moves = float("inf")
            # if v % 11 == 0:  
            #     min_moves = min(dfs(v//11), min_moves)
            # if v % 5 == 0:  
            #     min_moves = min(dfs(v//5), min_moves)
            # min_moves = min(dfs(v-1), min_moves)
            #     min_moves = min(dfs(v+1), min_moves)
        #     return 1 + min_moves
        # return dfs(x)
        