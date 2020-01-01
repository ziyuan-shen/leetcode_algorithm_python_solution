class Solution:
    def mctFromLeafValues(self, arr):
        if len(arr) <= 1:
            return 0
        elif len(arr) == 2:
            return arr[0] * arr[1]
        else:
            return min([max(arr[:i]) * max(arr[i:]) + self.mctFromLeafValues(arr[:i]) + self.mctFromLeafValues(arr[i:]) for i in range(1, len(arr))])
                
s = Solution()
print(s.mctFromLeafValues([10,14,7,10,6,14,4,14,4,4,4,15,7,4,9]))