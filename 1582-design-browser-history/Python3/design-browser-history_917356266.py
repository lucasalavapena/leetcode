class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_index = 0
        self.urls = [homepage]

    def visit(self, url: str) -> None:
        self.curr_index += 1
        if len(self.urls) > self.curr_index: 
            del self.urls[self.curr_index:]  
        self.urls.append(url)

    def back(self, steps: int) -> str:
        self.curr_index = max(self.curr_index - steps, 0)
        return self.urls[self.curr_index]

    def forward(self, steps: int) -> str:
        self.curr_index = min(self.curr_index + steps, len(self.urls)-1)
        return self.urls[self.curr_index]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)