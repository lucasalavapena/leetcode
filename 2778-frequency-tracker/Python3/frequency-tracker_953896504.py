class FrequencyTracker:

    def __init__(self):
        self.c = Counter()
        self.freq = defaultdict(set)

    def add(self, number: int) -> None:
        self.c[number] += 1
        new_freq = self.c[number]

        self.freq[new_freq].add(number)
        old_feq = new_freq - 1

        if old_feq:
            self.freq[old_feq].remove(number)
            if len(self.freq[old_feq]) == 0:
                self.freq.pop(old_feq)
            
    def deleteOne(self, number: int) -> None:
        if number in self.c:
            old_freq = self.c[number]

            # print(f"Adding: {self.freq=} {self.c=} {old_freq=}")

            self.freq[old_freq].remove(number)

            if len(self.freq[old_freq]) == 0:
                self.freq.pop(old_freq)

            self.c[number] = old_freq - 1

            if old_freq > 1:
                self.freq[old_freq - 1].add(number)
            else:
                self.c.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)