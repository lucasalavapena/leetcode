class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        remaining = income
        tax = 0
        idx = 0

        while remaining > 0:
            tax_range = brackets[idx][0]-brackets[idx-1][0] if idx != 0 else brackets[idx][0]
            taxed_at_bracket = min(tax_range, remaining)
            tax += taxed_at_bracket * brackets[idx][1] / 100
            remaining -= taxed_at_bracket
            idx += 1
        return tax