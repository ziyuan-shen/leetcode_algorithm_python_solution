class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare, tortoise = nums[0], nums[0]
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        while hare != tortoise:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare