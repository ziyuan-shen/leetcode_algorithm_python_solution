class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.arr = nums
        self.arr.sort()
        while len(self.arr)>self.k:
            self.arr.pop(0)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.arr.append(val)
        self.arr.sort()
        if len(self.arr) > self.k:
            self.arr.pop(0)
        return self.arr[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)