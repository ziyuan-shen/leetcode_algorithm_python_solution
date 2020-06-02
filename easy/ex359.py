from collections import defaultdict
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        ans = 0
        if message in self.data and (timestamp - self.data[message][-1]) < 10:
            ans = False
        else:
            ans = True
        if ans:
            self.data[message].append(timestamp)
        return ans


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)