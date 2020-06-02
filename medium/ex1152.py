from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_list = defaultdict(list)
        user_set = defaultdict(set)
        website_count = defaultdict(int)
        visits = [[username[i], timestamp[i], website[i]] for i in range(len(username))]
        visits.sort(key=lambda x: (x[0], x[1]))
        for visit in visits:
            user_list[visit[0]].append(visit[2])
        for key, value in user_list.items():
            length = len(value)
            for i in range(length-2):
                for j in range(i+1, length-1):
                    for k in range(j+1, length):
                        user_set[key].add((value[i], value[j], value[k]))
        for value in user_set.values():
            for website in value:
                website_count[website] += 1
        ans = [[count, website] for website, count in website_count.items()]
        ans.sort(key=lambda x: (-x[0], x[1]))
        return list(ans[0][1])