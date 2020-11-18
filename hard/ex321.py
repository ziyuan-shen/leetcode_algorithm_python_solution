class Solution:
    def getMax(self, p1, p2, nums1, nums2, k):
        if (p1, p2, k) in self.mem:
            return self.mem[(p1, p2, k)]
        ans = ""
        p1_copy, p2_copy = p1, p2
        for i in range(k):
            selection = -1
            p11, p22 = p1, p2
            next_p1, next_p2 = p1, p2
            tie = False
            while p11 < len(nums1) and len(nums1) - p11 + len(nums2) - p2 >= k - i:
                if nums1[p11] > selection:
                    selection = nums1[p11]
                    next_p1 = p11 + 1
                p11 += 1
            while p22 < len(nums2) and len(nums2) - p22 + len(nums1) - p1 >= k - i:
                if nums2[p22] > selection:
                    selection = nums2[p22]
                    p2 = p22 + 1
                    next_p1 = p1
                    if tie:
                        tie = False
                elif nums2[p22] == selection:
                    if not tie and next_p1 != p1:
                        tie = True
                        next_p2 = p22 + 1
                p22 += 1
            if tie and i != k - 1:
                a = self.getMax(p1, next_p2, nums1, nums2, k - i - 1)
                b = self.getMax(next_p1, p2, nums1, nums2, k - i - 1)
                self.mem[(p1, p2, k)] = ans + str(selection) + max(a, b)
                return self.mem[(p1, p2, k)]
            else:
                ans += str(selection)
                p1 = next_p1
        self.mem[(p1_copy, p2_copy, k)] = ans
        return ans
            
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        self.mem = dict()
        ans = self.getMax(0, 0, nums1, nums2, k)
        return [int(num) for num in ans]