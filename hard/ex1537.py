class Solution:   
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1).intersection(set(nums2))
        dp1 = [0 for _ in range(len(nums1) + 1)]
        dp2 = [0 for _ in range(len(nums2) + 1)]
        p1 = len(nums1) - 1
        p2 = len(nums2) - 1
        while p1 >= 0 and p2 >= 0:
            while p1 >= 0 and nums1[p1] not in intersection:
                dp1[p1] = nums1[p1] + dp1[p1 + 1]
                p1 -= 1
            while p2 >= 0 and nums2[p2] not in intersection:
                dp2[p2] = nums2[p2] + dp2[p2 + 1]
                p2 -= 1
            if p1 >= 0:
                dp1[p1] = nums1[p1] + max(dp1[p1 + 1], dp2[p2 + 1])
                dp2[p2] = nums2[p2] + max(dp2[p2 + 1], dp1[p1 + 1])
                p1 -= 1
                p2 -= 1
        while p1 >= 0:
            dp1[p1] = nums1[p1] + dp1[p1 + 1]
            p1 -= 1
        while p2 >= 0:
            dp2[p2] = nums2[p2] + dp2[p2 + 1]
            p2 -= 1
        return max(dp1[0], dp2[0]) % (10 ** 9 + 7)
            