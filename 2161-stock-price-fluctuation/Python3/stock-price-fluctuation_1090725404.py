from collections import defaultdict
from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.max_timestamp = None
        self.current_price = None
        self.timestamp_to_price = {}
        self.price_to_freq = defaultdict(int)
        self.prices_sorted = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        # timestamps are monotomically incrasing so no need for anything fancy here
        if self.max_timestamp is None or timestamp >= self.max_timestamp:
            self.max_timestamp = timestamp
            self.current_price = price

        if timestamp in self.timestamp_to_price:
            past_price = self.timestamp_to_price[timestamp]
            self.price_to_freq[past_price] -= 1 
            self.timestamp_to_price.pop(timestamp)

            if self.price_to_freq[past_price] == 0:# and price != past_price:
                self.prices_sorted.remove(past_price)

        self.timestamp_to_price[timestamp] = price
        if price not in self.price_to_freq or self.price_to_freq[price] == 0:
            self.prices_sorted.add(price)
        self.price_to_freq[price] += 1 

    def current(self) -> int:
        return self.current_price

    def maximum(self) -> int:
        # print(f"{self.prices_sorted[-1]=} {max([k for k, v in self.price_to_freq.items() if v])=} {max(self.timestamp_to_price.values())=}")
        return self.prices_sorted[-1]

    def minimum(self) -> int:
        # print(f"{self.prices_sorted[0]=} {min([k for k, v in self.price_to_freq.items() if v])=} {min(self.timestamp_to_price.values())=}")         
        
        return self.prices_sorted[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()