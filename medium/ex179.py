class Solution:
    def gt(self, x, y):
        x = str(x)
        y = str(y)
        return int(x + y) > int(y + x)
        
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            for j in range(len(nums)-1, i-1, -1):
                if self.gt(nums[j], nums[j-1]):
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
        if nums[0] == 0:
            return "0"
        numsstring = [str(num) for num in nums]
        return "".join(numsstring)