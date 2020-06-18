class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        i = 0
        inblock = False
        while i < len(source):
            if not inblock:
                ans.append("")
            idx = 0
            effective_idx = 0
            line = source[i]
            line_end = False
            while idx < len(line) - 1:
                if inblock:
                    if line[idx] == "*" and line[idx+1] == "/":
                        inblock = False
                        effective_idx = idx + 2
                        idx += 1
                else:
                    if line[idx] == "/" and line[idx+1] == "/":
                        ans[-1] += line[effective_idx:idx]
                        line_end = True
                        break
                    elif line[idx] == "/" and line[idx+1] == "*":
                        inblock = True
                        ans[-1] += line[effective_idx:idx]
                        idx += 1
                idx += 1
            if not inblock and not line_end:
                ans[-1] += line[effective_idx:]
            i += 1
        return list(filter(lambda x: x != "", ans))