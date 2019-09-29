class RecentCounter:

    def __init__(self):
        self.ping_calls = []
        
    def ping(self, t: int) -> int:
        self.ping_calls.append(t)
        while self.ping_calls[0] < t-3000:
            self.ping_calls.pop(0)
        return len(self.ping_calls)