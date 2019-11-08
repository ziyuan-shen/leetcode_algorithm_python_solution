class Solution(object):
    def get_traps(self, height):
        traps = []
        idx = 0
        while True:
            while (idx<len(height)-1) and height[idx+1]>=height[idx]:
                idx += 1
            if idx > len(height)-3:
                break
            left_boundary = idx
            while (idx<len(height)-1) and height[idx+1]<=height[idx]:
                idx += 1
            if idx == len(height)-1:
                break
            local_minimum = idx
            while (idx<len(height)-1) and height[idx+1]>=height[idx]:
                idx += 1
            right_boundary = idx
            traps.append([left_boundary, local_minimum, right_boundary])
        return traps
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        all_water = 0
        while True:
            water = 0
            traps = self.get_traps(height)
            for trap in traps:
                upper_boundary = min(height[trap[0]], height[trap[2]])
                for idx in range(trap[0]+1, trap[2]):
                    if height[idx]<upper_boundary:
                        water += upper_boundary-height[idx]
                        height[idx] = upper_boundary
            if water==0:
                break
            all_water += water
        return all_water
            