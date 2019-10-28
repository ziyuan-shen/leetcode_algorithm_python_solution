class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return intersection
        