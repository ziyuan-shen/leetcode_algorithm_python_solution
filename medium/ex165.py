class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(reversion) for reversion in version1.split(".")]
        version2 = [int(reversion) for reversion in version2.split(".")]
        idx = 0
        while idx < len(version1) and idx < len(version2):
            if version1[idx] < version2[idx]:
                return -1
            if version1[idx] > version2[idx]:
                return 1
            idx += 1
        if idx == len(version1) and idx == len(version2):
            return 0
        if idx < len(version1):
            while idx < len(version1):
                if version1[idx] != 0:
                    return 1
                idx += 1
            return 0
        while idx < len(version2):
            if version2[idx] != 0:
                return -1
            idx += 1
        return 0