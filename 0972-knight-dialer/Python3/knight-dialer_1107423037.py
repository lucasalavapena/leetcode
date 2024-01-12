class Solution:
    def knightDialer(self, n: int) -> int:
        PRIME = 10**9 + 7

        prev_state = [1] * 10
        current_state = [1] * 10

        for i in range(1, n):
            # how to get zeros in the ith step
            # either start from 4, 6
            current_state[0] = (prev_state[4] + prev_state[6] ) % PRIME
            current_state[1] = (prev_state[6] + prev_state[8] ) % PRIME
            current_state[2] = (prev_state[7] + prev_state[9] ) % PRIME
            current_state[3] = (prev_state[4] + prev_state[8] ) % PRIME
            current_state[4] = (prev_state[0] +  prev_state[3] + prev_state[9] ) % PRIME
            current_state[5] = 0
            current_state[6] = (prev_state[0] + prev_state[1] + prev_state[7] ) % PRIME
            current_state[7] = (prev_state[2] + prev_state[6] ) % PRIME
            current_state[8] = (prev_state[1] + prev_state[3] ) % PRIME
            current_state[9] = (prev_state[2] + prev_state[4] ) % PRIME
            prev_state = current_state[:]

        return sum(current_state) % PRIME