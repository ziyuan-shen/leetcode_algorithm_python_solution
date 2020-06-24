class Solution:
    def insert(self, queue, people):
        if not people:
            for height, threshold, current in queue:
                if threshold != current:
                    return False
            return queue
        person = people[0]
        height, threshold = person[0], person[1]
        for i in range(len(queue) + 1):
            current = 0
            flag = False
            for pre in queue[:i]:
                if pre[0] >= height:
                    current += 1
                    if current > threshold:
                        flag = True
                        break
            if flag:
                continue
            for suf_height, suf_threshold, suf_current in queue[i:]:
                if height >= suf_height and suf_threshold == suf_current:
                    flag = True
                    break
            if flag:
                continue
            ans = self.insert(queue[:i] + [(height, threshold, current)] + [(suf_height, suf_threshold, suf_current+1 if height >= suf_height else suf_current) for suf_height, suf_threshold, suf_current in queue[i:]], people[1:])
            if ans:
                return ans
        return False
        
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        queue = [(people[0][0], people[0][1], 0)]
        queue = self.insert(queue, people[1:])
        return [[q[0], q[1]] for q in queue]