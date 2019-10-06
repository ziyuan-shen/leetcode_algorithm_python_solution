class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        degree = max(freq_dict.values())
        max_elem = []
        for num, freq in freq_dict.items():
            if freq==degree:
                max_elem.append(num)
        length_list = [len(nums) - nums.index(elem) - nums[::-1].index(elem) for elem in max_elem]
        return min(length_list)
        