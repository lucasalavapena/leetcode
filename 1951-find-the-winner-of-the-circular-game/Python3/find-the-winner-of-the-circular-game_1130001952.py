class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        curr = k-1
        for i in range(n-1):
            # print(arr, curr)
            arr.pop(curr)
            curr = (curr -1 + k) % len(arr)
        # print(arr)
        return arr[0]