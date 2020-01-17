class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        ans = []
        while dirs:
            d = dirs.pop(0)
            if d == "." or d == "":
                continue
            elif d == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(d)
        return "/" + "/".join(ans) 