class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        if self.idx == len(self.history) - 1:
            self.history.append(url)
        else:
            self.history[self.idx+1:] = [url]
        self.idx = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 0)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, len(self.history) - 1)
        return self.history[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)