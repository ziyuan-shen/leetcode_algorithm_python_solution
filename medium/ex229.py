class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        ans = []
        num1 = None
        num2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif num1 == None:
                num1 = num
                count1 = 1
            elif num2 == None:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                if count1 <= 0:
                    num1 = None
                    count1 = 0
                if count2 <= 0:
                    num2 = None
                    count2 = 0
        count1 , count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            if num == num2:
                count2 += 1
        if count1 > target:
            ans.append(num1)
        if count2 > target:
            ans.append(num2)
        return ans
        