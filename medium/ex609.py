class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for path in paths:
            direc = path.split(" ")[0]
            files = path.split(" ")[1:]
            for file in files:
                file_name = file.split("(")[0]
                content = file.split("(")[1][:-1]
                if content not in dic:
                    dic[content] = [direc + "/" + file_name]
                else:
                    dic[content].append(direc + "/" + file_name)
        ans = []
        for l in dic.values():
            if len(l) > 1:
                ans.append(l)
        return ans