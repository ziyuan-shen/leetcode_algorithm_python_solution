class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        groupnum = 2 * numRows - 2
        group, rem = len(s) // groupnum, len(s) % groupnum
        rows = ["" for _ in range(numRows)]
        for i in range(0, group * groupnum, groupnum):
            for idx, j in enumerate(range(i, i+numRows)):
                rows[idx] += s[j]
            for idx, j in enumerate(range(i+numRows, i+groupnum)):
                rows[numRows-2-idx] += s[j]
        for idx, i in enumerate(range(group * groupnum, group * groupnum + min(numRows, rem))):
            rows[idx] += s[i]
        if rem > numRows:
            for idx, i in enumerate(range(group * groupnum + numRows, len(s))):
                rows[numRows-2-idx] += s[i]
        return "".join(rows)