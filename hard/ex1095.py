# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findPeek(self, mountain_arr):
        length = mountain_arr.length()
        low = 0
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low += 1
                continue
            if mid == length - 1:
                high -= 1
                continue
            midvalue = mountain_arr.get(mid)
            left = mountain_arr.get(mid - 1)
            right = mountain_arr.get(mid + 1)
            if midvalue > left and midvalue > right:
                return mid
            elif midvalue < right:
                low = mid + 1
            else:
                high = mid - 1
                
    def binarySearch(self, mountain_arr, start, end, target, reverse=False):
        low = start
        high = end
        while low <= high:
            mid = (low + high) // 2
            midvalue = mountain_arr.get(mid)
            if midvalue == target:
                return mid
            elif midvalue > target:
                if reverse:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if reverse:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peek = self.findPeek(mountain_arr)
        idx = self.binarySearch(mountain_arr, 0, peek, target)
        if idx != -1:
            return idx
        return self.binarySearch(mountain_arr, peek + 1, mountain_arr.length()-1, target, True)