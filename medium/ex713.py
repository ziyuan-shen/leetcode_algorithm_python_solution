class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        p1, p2 = 0, 1
        product = nums[0]
        while product >= k and p1 < len(nums) - 1:
            p1 += 1
            p2 += 1
            product = nums[p1]
        if product < k:
            while p2 < len(nums) and product * nums[p2] < k:
                product *= nums[p2]
                p2 += 1
            length = p2 - p1
            ans += length * (length + 1) // 2
            while p2 < len(nums):
                product *= nums[p2]
                p2 += 1
                while product >= k and p1 < p2:
                    product //= nums[p1]
                    p1 += 1
                if p1 == p2:
                    p2 += 1
                    if p1 < len(nums):
                        product = nums[p1]
                        while p1 < len(nums) - 1 and product >= k:
                            p1 += 1
                            p2 += 1
                            product = nums[p1]
                        if product >= k:
                            break
                    else:
                        break
                ans += (p2 - p1)
        return ans