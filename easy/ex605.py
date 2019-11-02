class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        idx = 0
        slot = 0
        while idx < len(flowerbed):
            zero_count = 0
            start_flag = False
            while idx<len(flowerbed) and flowerbed[idx] == 1:
                idx += 1
            if idx == 0:
                start_flag = True
            while idx<len(flowerbed) and flowerbed[idx] == 0:
                zero_count += 1
                idx += 1
            if zero_count > 0:
                if start_flag and idx==len(flowerbed):
                    slot += (zero_count+1) // 2
                elif start_flag or idx==len(flowerbed):
                    slot += zero_count // 2
                else:
                    slot += (zero_count+1) // 2 - 1
        return slot >= n