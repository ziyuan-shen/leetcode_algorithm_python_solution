from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {num: -1 for num in nums2}
        q = deque([0])
        for i in range(1, len(nums2)):
            if nums2[i] > nums2[i-1]:
                q.append(i)
        for i in range(len(nums2)):
            if q and q[0] == i:
                q.popleft()
            for idx in q:
                if nums2[idx] > nums2[i]:
                    dic[nums2[i]] = nums2[idx]
                    break
        return [dic[num] for num in nums1]