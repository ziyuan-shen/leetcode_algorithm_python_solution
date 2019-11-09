class Solution(object):
    def binarySearch(self, nums, value):
        '''return largest idx that nums[idx]<=value
           return -1 if all nums>value or nums=[]
        '''
        if nums==[]:
            return -1
        length = len(nums)
        if nums[-1] <= value:
            return length - 1
        low = 0
        high = length-1
        mid = (low+high) // 2
        while low <= high:
            if nums[mid] <= value:
                if mid == length - 1 or nums[mid+1] > value:
                    return mid
                else:
                    low = mid + 1
                    mid = (low+high) // 2
            else:
                high = mid - 1
                mid = (low+high) // 2
        return -1
                    
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        mid = (length1 + length2) // 2
        idx1 = 0
        idx2 = 0
        merged = []
        while (idx1<length1 or idx2<length2):
            if idx1>=length1:
                merged.extend(nums2[idx2:])
                break
            elif idx2>=length2:
                merged.extend(nums1[idx1:])
                break
            else:
                if nums1[idx1] <= nums2[idx2]:
                    merged.append(nums1[idx1])
                    idx1 += 1
                    idx = self.binarySearch(nums1[idx1:], nums2[idx2])
                    if idx != -1:
                        merged.extend(nums1[idx1:idx1+idx+1])
                        idx1 = idx1+idx+1
                    merged.append(nums2[idx2])
                    idx2 += 1
                else:
                    merged.append(nums2[idx2])
                    idx2 += 1
                    idx = self.binarySearch(nums2[idx2:], nums1[idx1])
                    if idx != -1:
                        merged.extend(nums2[idx2:idx2+idx+1])
                        idx2 = idx2+idx+1
                    merged.append(nums1[idx1])
                    idx1 += 1
        if (length1+length2) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid-1]) / 2