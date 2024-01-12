class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.id_to_price = {id_: price for id_, price in zip(products, prices)}
        self.customer_no = 0
        self.n = n
        self.discount = discount

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = sum(self.id_to_price[id_] * quantity for id_, quantity in zip(product, amount))
        self.customer_no += 1

        # discount branch
        if self.customer_no % self.n == 0:
            return bill * ((100 - self.discount) / 100)

        return bill



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)