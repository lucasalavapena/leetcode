# ((sum, min, max))
# def magic_func(funcs, iterable):
#     return (f(iterable) for f in (sum, min, max))

class Solution:
    def average(self, salary: List[int]) -> float:
        return functools.reduce(lambda a, b: [b + a[0], min(b, a[1]), max(b, a[2]), (b + a[0] - min(b, a[1]) - max(b, a[2])) / (len(salary) - 2)], salary, [0, 10_000_000, 0, 0])[-1]
    