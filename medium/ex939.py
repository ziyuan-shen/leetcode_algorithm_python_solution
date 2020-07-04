from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        ans = float("inf")
        dic = defaultdict(list)
        pair_dic = defaultdict(set)
        for point in points:
            dic[point[0]].append(point[1])
        x_list = list(dic.keys())
        for x in x_list:
            y_list = dic[x]
            for i in range(len(y_list) - 1):
                for j in range(i+1, len(y_list)):
                    pair_dic[x].add((y_list[i], y_list[j]))
        for i in range(len(x_list) - 1):
            for j in range(i+1, len(x_list)):
                u = pair_dic[x_list[i]].intersection(pair_dic[x_list[j]])
                for y1, y2 in u:
                    ans = min(ans, (x_list[j] - x_list[i]) * (y2 - y1))
        return ans if ans != float("inf") else 0