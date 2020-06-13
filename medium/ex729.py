class MyCalendar:

    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        if not self.data:
            self.data.append((start, end))
            return True
        idx = 0
        while idx < len(self.data) and self.data[idx][0] < start:
            idx += 1
        if idx < len(self.data) and self.data[idx][0] < end:
            return False
        elif idx > 0 and self.data[idx-1][1] > start:
            return False
        else:
            self.data.insert(idx, (start, end))
            return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)