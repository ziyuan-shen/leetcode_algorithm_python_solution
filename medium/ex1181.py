from collections import defaultdict
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        startdic = defaultdict(list)
        enddic = defaultdict(list)
        ans = set()
        for i in range(len(phrases)):
            words = phrases[i].split(" ")
            startword = words[0]
            endword = words[-1]
            startdic[startword].append((i, " ".join(words[1:])))
            enddic[endword].append((i, phrases[i]))
        for endword in enddic:
            if endword in startdic:
                for phrase1 in enddic[endword]:
                    for phrase2 in startdic[endword]:
                        if phrase1[0] != phrase2[0]:
                            ans.add(phrase1[1] + ("" if phrase1[1] == ""  or phrase2[1] == "" else " ") + phrase2[1])
        ans = list(ans)
        ans.sort()
        return ans