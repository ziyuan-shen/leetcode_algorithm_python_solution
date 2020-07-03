class Solution:
    def swapNumString(self, num):
        if len(num) <= 1:
            return num
        num_list = [int(char) for char in num]
        max_val = max(num_list)
        max_indices = []
        for idx, value in enumerate(num_list):
            if value == max_val:
                max_indices.append(idx)
        if num_list[0] == max_val:
            return str(max_val) + self.swapNumString(num[1:])
        else:
            return str(max_val) + num[1:max_indices[-1]] + num[0] + num[max_indices[-1]+1:]
        
    def maximumSwap(self, num: int) -> int:
        return self.swapNumString(str(num))