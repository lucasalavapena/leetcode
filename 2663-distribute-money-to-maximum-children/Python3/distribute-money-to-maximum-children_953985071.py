class Solution:
    def distMoney(self, money: int, children: int) -> int:
        exactly = money // 8 
        remainder = money % 8

        if exactly > children:
            return children - 1
        elif exactly == children:
            return children -1 if remainder else children
        else:
            remaining_money = money - children
            children_fully_paid = remaining_money // 7

            rem = remaining_money % 7
            rem_children = children - children_fully_paid
            if (rem == 3 and rem_children == 1) or (rem and rem_children == 0): 
                return max(children_fully_paid-1, -1)

            return max(children_fully_paid, -1)