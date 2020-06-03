class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        slots = []
        while slots1 and slots2:
            if slots2[0][1] <= slots1[0][0]:
                slots2.pop(0)
            elif slots2[0][0] >= slots1[0][1]:
                slots1.pop(0)
            else:
                slots.append([max(slots1[0][0], slots2[0][0]), min(slots1[0][1], slots2[0][1])])
                if slots1[0][1] <= slots2[0][1]:
                    slots1.pop(0)
                else:
                    slots2.pop(0)
        for slot in slots:
            if (slot[1] - slot[0]) >= duration:
                return [slot[0], slot[0] + duration]
        return []